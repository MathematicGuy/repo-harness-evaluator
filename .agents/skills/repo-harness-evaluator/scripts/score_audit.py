#!/usr/bin/env python3
"""Validate and score a purpose-aware repository-harness audit."""

from __future__ import annotations
import argparse
import json
from pathlib import Path

EVIDENCE_VALUE = {"E0": 0, "E1": 1, "E2": 2, "E3": 3, "E4": 4}
RANK_ORDER = ["E", "D", "C", "B", "A", "S"]

def raw_rank(points: float) -> str:
    if points >= 90: return "S"
    if points >= 80: return "A"
    if points >= 65: return "B"
    if points >= 45: return "C"
    if points >= 25: return "D"
    return "E"

def fit_rank(points: float) -> str:
    if points >= 90: return "Excellent Fit"
    if points >= 80: return "Strong Fit"
    if points >= 65: return "Adequate Fit"
    if points >= 45: return "Misaligned"
    return "Poor Fit"

def overhead_label(points: float) -> str:
    if points <= 5: return "Low"
    if points <= 12: return "Moderate"
    if points <= 24: return "High"
    return "Severe"

def cap_rank(rank: str, maximum: str) -> str:
    return RANK_ORDER[min(RANK_ORDER.index(rank), RANK_ORDER.index(maximum))]

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("audit_json")
    args = parser.parse_args()

    path = Path(args.audit_json)
    data = json.loads(path.read_text(encoding="utf-8"))

    capability_total = 0.0
    errors = []
    warnings = []
    verified = partial = applicable = 0
    scores = {}

    for dimension in data["dimensions"]:
        score = dimension.get("score")
        level = dimension.get("highest_evidence", "E0")
        if score is None:
            errors.append(f"{dimension['id']}: missing score")
            continue
        if not isinstance(score, (int, float)) or score < 0 or score > 4:
            errors.append(f"{dimension['id']}: score must be 0..4")
            continue
        if level not in EVIDENCE_VALUE:
            errors.append(f"{dimension['id']}: invalid evidence level {level}")
            continue
        if score >= 4 and EVIDENCE_VALUE[level] < 4:
            errors.append(f"{dimension['id']}: score 4 requires E4")
        elif score >= 3 and EVIDENCE_VALUE[level] < 3:
            errors.append(f"{dimension['id']}: score 3 requires E3")
        elif score >= 2 and EVIDENCE_VALUE[level] < 2:
            errors.append(f"{dimension['id']}: score 2 requires E2")
        capability_total += dimension["weight"] * score / 4
        scores[dimension["id"]] = score

        for req in dimension.get("requirements", []):
            status = req.get("status", "unverified")
            if status == "not_applicable":
                continue
            applicable += 1
            if status == "verified":
                verified += 1
            elif status == "partial":
                partial += 1

    targets = data.get("purpose", {}).get("targets", {})
    adequacy_numerator = 0.0
    adequacy_denominator = 0.0
    adequacy_by_dimension = {}
    for dimension in data["dimensions"]:
        key = dimension["id"]
        target = targets.get(key)
        score = scores.get(key)
        if target is None:
            errors.append(f"purpose target missing for {key}")
            continue
        if not isinstance(target, (int, float)) or target < 0 or target > 4:
            errors.append(f"invalid target for {key}: {target}")
            continue
        if score is None:
            continue
        if target == 0:
            adequacy_by_dimension[key] = None
            continue
        adequacy = min(score / target, 1.0)
        adequacy_by_dimension[key] = round(adequacy * 100, 2)
        adequacy_numerator += dimension["weight"] * adequacy
        adequacy_denominator += dimension["weight"]

    weighted_adequacy = (
        adequacy_numerator / adequacy_denominator * 100
        if adequacy_denominator else 0.0
    )

    overhead_penalty = 0.0
    for item in data.get("friction", []):
        level = item.get("level", 0)
        evidence = item.get("highest_evidence", "E0")
        if not isinstance(level, (int, float)) or level < 0 or level > 4:
            errors.append(f"friction {item.get('id')}: level must be 0..4")
            continue
        if evidence not in EVIDENCE_VALUE:
            errors.append(f"friction {item.get('id')}: invalid evidence {evidence}")
            continue
        if level > 0 and EVIDENCE_VALUE[evidence] < 2:
            errors.append(
                f"friction {item.get('id')}: nonzero penalty requires E2 or stronger"
            )
        if level >= 3 and EVIDENCE_VALUE[evidence] < 4:
            warnings.append(
                f"friction {item.get('id')}: level 3–4 should normally have E4 timing or task evidence"
            )
        overhead_penalty += 2 * item["weight"] * level / 4

    fitness = max(0.0, weighted_adequacy - overhead_penalty)
    applied_fit_gates = []
    unknown_fit_gates = []
    for gate in data.get("purpose_gates", []):
        if not gate.get("applicable", False):
            continue
        passed = gate.get("passed")
        if passed is False:
            cap = float(gate.get("max_fit_if_failed", 100))
            fitness = min(fitness, cap)
            applied_fit_gates.append(f"{gate.get('name')}: maximum fit {cap:g}")
        elif passed is None:
            unknown_fit_gates.append(gate.get("name", gate.get("id", "unknown")))

    coverage = ((verified + 0.5 * partial) / applicable * 100) if applicable else 0.0
    capability_rank = raw_rank(capability_total)
    capability_gates = []
    gates = data.get("gates", {})

    if not gates.get("dynamic_validation", False):
        capability_rank = cap_rank(capability_rank, "C")
        capability_gates.append("No dynamic validation: maximum capability rank C")
    if not gates.get("executable_architecture_or_safety", False):
        capability_rank = cap_rank(capability_rank, "B")
        capability_gates.append("No executable architecture or safety controls: maximum capability rank B")
    if not gates.get("representative_agent_eval", False):
        capability_rank = cap_rank(capability_rank, "A")
        capability_gates.append("No representative agent evaluation: maximum capability rank A")
    if not gates.get("recovery_evidence", False):
        capability_rank = cap_rank(capability_rank, "A")
        capability_gates.append("No recovery evidence: maximum capability rank A")
    if gates.get("critical_uncontrolled_risk", False):
        capability_rank = cap_rank(capability_rank, "D")
        capability_gates.append("Critical uncontrolled risk: maximum capability rank D")
        fitness = min(fitness, 39)
        applied_fit_gates.append("Critical uncontrolled risk: maximum fit 39")

    depth = data.get("metadata", {}).get("depth", "medium")
    confidence = {
        "low": "Preliminary",
        "medium": "Validated" if gates.get("dynamic_validation") else "Preliminary",
        "detailed": (
            "High"
            if coverage > 90
            and gates.get("dynamic_validation")
            and gates.get("recovery_evidence")
            and not unknown_fit_gates
            else "Validated"
        ),
    }.get(depth, "Preliminary")

    result = {
        "purpose_profile": data.get("purpose", {}).get("profile"),
        "fitness_for_purpose": round(fitness, 2),
        "fit_rank": fit_rank(fitness),
        "weighted_target_adequacy": round(weighted_adequacy, 2),
        "adequacy_by_dimension": adequacy_by_dimension,
        "unjustified_overhead_penalty": round(overhead_penalty, 2),
        "overhead_label": overhead_label(overhead_penalty),
        "capability_points": round(capability_total, 2),
        "capability_rank": capability_rank,
        "coverage_percent": round(coverage, 2),
        "confidence": confidence,
        "applied_fit_gates": applied_fit_gates,
        "unknown_fit_gates": unknown_fit_gates,
        "capability_rank_gates": capability_gates,
        "warnings": warnings,
        "validation_errors": errors,
    }
    print(json.dumps(result, indent=2))
    if errors:
        raise SystemExit(2)

if __name__ == "__main__":
    main()
