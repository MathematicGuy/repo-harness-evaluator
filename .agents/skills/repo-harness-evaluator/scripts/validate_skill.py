#!/usr/bin/env python3
"""Validate the packaged skill and Codex custom-agent TOML files."""

from __future__ import annotations
import re
import sys
from pathlib import Path
import tomllib

def main() -> None:
    package = Path(__file__).resolve().parents[4]
    skill = Path(__file__).resolve().parents[1]
    skill_md = skill / "SKILL.md"
    text = skill_md.read_text(encoding="utf-8")

    errors = []
    if not text.startswith("---\n"):
        errors.append("SKILL.md missing YAML frontmatter")
    if not re.search(r"^name:\s+repo-harness-evaluator\s*$", text, re.M):
        errors.append("SKILL.md missing expected name")
    if not re.search(r"^description:\s+\S", text, re.M):
        errors.append("SKILL.md missing description")
    if "PURPOSE_PROFILES.md" not in text:
        errors.append("SKILL.md must load purpose profiles")

    for target in re.findall(r"\]\((references/[^)]+)\)", text):
        if not (skill / target).exists():
            errors.append(f"Missing reference: {target}")

    yaml_path = skill / "agents" / "openai.yaml"
    yaml_text = yaml_path.read_text(encoding="utf-8")
    if "allow_implicit_invocation: false" not in yaml_text:
        errors.append("Skill must remain explicitly invoked")

    agent_paths = list((package / ".codex" / "agents").glob("*.toml"))
    if not any(p.name == "harness-purpose-fit-auditor.toml" for p in agent_paths):
        errors.append("Missing purpose-fit custom agent")
    for toml_path in agent_paths:
        try:
            data = tomllib.loads(toml_path.read_text(encoding="utf-8"))
        except Exception as exc:
            errors.append(f"{toml_path.name}: invalid TOML: {exc}")
            continue
        for field in ("name", "description", "developer_instructions"):
            if not data.get(field):
                errors.append(f"{toml_path.name}: missing {field}")
        if data.get("model") != "gpt-5.6-terra":
            errors.append(f"{toml_path.name}: expected gpt-5.6-terra")
        if data.get("model_reasoning_effort") != "high":
            errors.append(f"{toml_path.name}: expected high reasoning")
        if data.get("sandbox_mode") != "read-only":
            errors.append(f"{toml_path.name}: expected read-only sandbox")

    profile = package / "profile" / "repo-harness-eval.config.toml"
    try:
        profile_data = tomllib.loads(profile.read_text(encoding="utf-8"))
        if profile_data.get("model") != "gpt-5.6-sol":
            errors.append("Profile parent model must be gpt-5.6-sol")
        if profile_data.get("model_reasoning_effort") != "high":
            errors.append("Profile parent reasoning must be high")
    except Exception as exc:
        errors.append(f"Invalid profile TOML: {exc}")

    if errors:
        print("\n".join(f"ERROR: {e}" for e in errors))
        raise SystemExit(1)
    print("Skill package validation passed.")

if __name__ == "__main__":
    main()
