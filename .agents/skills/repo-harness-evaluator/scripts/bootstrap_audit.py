#!/usr/bin/env python3
"""Create deterministic purpose-aware repository-harness audit artifacts."""

from __future__ import annotations
import argparse
import json
from pathlib import Path

DIMENSIONS = [
    ("task_contracts", "Task contracts and definition of done", 10),
    ("context", "Context and repository knowledge", 12),
    ("architecture", "Architecture and change locality", 12),
    ("runtime", "Runtime, tools, and reproducibility", 10),
    ("verification", "Verification and agent evaluations", 16),
    ("observability", "Observability and failure attribution", 10),
    ("state", "State and long-horizon continuity", 8),
    ("safety", "Permissions, safety, and recovery", 8),
    ("subagents", "Subagent coordination and integration", 6),
    ("evolution", "Entropy control and harness evolution", 8),
]

TARGETS = {
    "hackathon": {
        "task_contracts": 2.0, "context": 1.5, "architecture": 1.0,
        "runtime": 2.5, "verification": 2.0, "observability": 1.0,
        "state": 1.0, "safety": 1.0, "subagents": 1.0, "evolution": 0.5,
    },
    "mvp": {
        "task_contracts": 2.5, "context": 2.0, "architecture": 2.0,
        "runtime": 3.0, "verification": 2.5, "observability": 2.0,
        "state": 2.0, "safety": 2.0, "subagents": 1.5, "evolution": 1.5,
    },
    "short_product": {
        "task_contracts": 3.0, "context": 2.5, "architecture": 2.5,
        "runtime": 3.0, "verification": 3.0, "observability": 2.5,
        "state": 2.5, "safety": 2.5, "subagents": 2.0, "evolution": 2.0,
    },
    "long_lived": {
        "task_contracts": 3.5, "context": 3.0, "architecture": 3.5,
        "runtime": 3.5, "verification": 3.5, "observability": 3.0,
        "state": 3.5, "safety": 3.5, "subagents": 2.5, "evolution": 3.5,
    },
}

FRICTION = [
    ("fixed_process_cost", "Fixed process cost", 5),
    ("context_load", "Context load", 4),
    ("feedback_latency", "Feedback latency", 4),
    ("coordination_burden", "Coordination burden", 3),
    ("maintenance_surface", "Maintenance surface", 4),
]

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True)
    parser.add_argument("--depth", choices=["low", "medium", "detailed"], required=True)
    parser.add_argument(
        "--profile",
        choices=["hackathon", "mvp", "short_product", "long_lived"],
        required=True,
    )
    args = parser.parse_args()

    out = Path(args.output).resolve()
    out.mkdir(parents=True, exist_ok=True)
    (out / "logs").mkdir(exist_ok=True)
    (out / "evidence").mkdir(exist_ok=True)

    payload = {
        "metadata": {
            "repository": "",
            "version": "",
            "depth": args.depth,
            "supported_harnesses": [],
            "permissions": {},
            "exclusions": [],
        },
        "purpose": {
            "profile": args.profile,
            "horizon_days": None,
            "expected_lifetime": "",
            "primary_optimization": [],
            "team_size": None,
            "autonomy": "",
            "failure_cost": "",
            "data_sensitivity": "",
            "reuse": "",
            "overlays": [],
            "targets": TARGETS[args.profile],
            "rationale": "",
            "assumptions": [],
        },
        "dimensions": [
            {
                "id": key,
                "name": name,
                "weight": weight,
                "score": None,
                "highest_evidence": "E0",
                "evidence": [],
                "requirements": [],
                "notes": "",
            }
            for key, name, weight in DIMENSIONS
        ],
        "friction": [
            {
                "id": key,
                "name": name,
                "weight": weight,
                "level": 0,
                "highest_evidence": "E0",
                "evidence": [],
                "justification": "",
            }
            for key, name, weight in FRICTION
        ],
        "purpose_gates": [
            {
                "id": "critical_path",
                "name": "Critical user or demo path works",
                "applicable": True,
                "passed": None,
                "max_fit_if_failed": 49,
                "evidence": [],
            },
            {
                "id": "fresh_setup",
                "name": "Fresh setup succeeds within the delivery budget",
                "applicable": True,
                "passed": None,
                "max_fit_if_failed": 64,
                "evidence": [],
            },
            {
                "id": "feedback_budget",
                "name": "Feedback loop fits the delivery cadence",
                "applicable": True,
                "passed": None,
                "max_fit_if_failed": 69,
                "evidence": [],
            },
            {
                "id": "risk_overlay",
                "name": "Risk and autonomy overlay controls are satisfied",
                "applicable": False,
                "passed": None,
                "max_fit_if_failed": 49,
                "evidence": [],
            },
        ],
        "context_file_evaluation": {
            "present": False,
            "score": None,
            "evidence": [],
        },
        "tests": [],
        "findings": [],
        "gates": {
            "dynamic_validation": False,
            "executable_architecture_or_safety": False,
            "representative_agent_eval": False,
            "recovery_evidence": False,
            "critical_uncontrolled_risk": False,
        },
        "subagents": [],
        "unknowns": [],
    }

    (out / "audit.json").write_text(json.dumps(payload, indent=2), encoding="utf-8")
    (out / "REPORT.md").write_text("# Repository Harness Evaluation\n\nDraft.\n", encoding="utf-8")
    (out / "EVIDENCE_LEDGER.md").write_text("# Evidence Ledger\n\n", encoding="utf-8")
    (out / "TEST_LEDGER.md").write_text("# Test Ledger\n\n", encoding="utf-8")
    (out / "FRICTION_LEDGER.md").write_text("# Friction Ledger\n\n", encoding="utf-8")
    print(out)

if __name__ == "__main__":
    main()
