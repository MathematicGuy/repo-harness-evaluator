# Purpose-Aware Repo Harness Evaluator for Codex

Reusable Codex skill for evaluating whether a repository's coding-agent harness is appropriate for its actual purpose.

## Key distinction

The package reports:

- **Fitness for purpose:** Is this the right amount and type of harness for the project?
- **Harness capability:** How mature and evidence-backed is the harness?
- **Unjustified overhead:** Which controls slow delivery without current risk-reduction value?

A three-day hackathon can receive an Excellent Fit with a small harness. A large production harness can receive high capability but poor fit for the same hackathon.

## Supported purpose profiles

- Hackathon: up to about 7 days.
- MVP: about 2–6 weeks.
- Short Product: about 1–3 months.
- Long-Lived Production.

Risk, autonomy, team concurrency, sensitive data, and reuse overlays raise specific targets without forcing every repository toward maximum maturity.

## Model topology

This skill is model-agnostic: it works with any coordinator and specialist models your harness supports. The values below are an example configuration (using the `gpt-5.6` family) — substitute your own models and reasoning settings.

- Coordinator (example): `gpt-5.6-sol`, reasoning `high`.
- Specialists (example): `gpt-5.6-terra`, reasoning `high`.
- Specialist sandboxes: read-only.
- Maximum concurrent specialist threads: 6.
- Detailed audits run in waves.

## Install

Windows PowerShell:

```powershell
Set-ExecutionPolicy -Scope Process Bypass
.\install-user.ps1
```

macOS/Linux:

```bash
chmod +x install-user.sh
./install-user.sh
```

## Run

```bash
codex --profile repo-harness-eval
```

Invoke explicitly:

```text
$repo-harness-evaluator evaluate the current repository
```

Or:

```text
$repo-harness-evaluator perform a Detailed evaluation for a 3-day hackathon repository
```

When depth or purpose is missing, the skill asks for them or records an explicit fallback assumption.

## Primary report

```text
Purpose profile: MVP + 5-person team overlay
Fitness for purpose: 86/100 — Strong Fit
Harness capability: 64/100 — Rank C
Unjustified overhead: 4/40 — Low
Evaluation depth: Medium
Audit confidence: Validated
Requirement coverage: 78%
```

## Safety

The skill is read-only by default. Controlled write tests require explicit permission and isolation.

## Validate package

```bash
python .agents/skills/repo-harness-evaluator/scripts/validate_skill.py
```
