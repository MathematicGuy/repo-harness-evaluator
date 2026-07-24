---
name: repo-harness-evaluator
description: Evaluate whether a repository's coding-agent harness is fit for its delivery purpose, at Low, Medium, or Detailed depth, using evidence, bounded subagents, dynamic tests, and friction-aware scoring.
---

# Repository Harness Evaluator

Run a **fitness loop**:

> purpose → target → evidence → test → score → friction → challenge → report

A harness is not good because it is large. It is good when it supplies enough control for the repository's horizon, risk, autonomy, team, and reuse goals without slowing delivery unnecessarily.

A three-day hackathon, a four-week MVP, and a long-lived production system should not target the same harness maturity.

## Invocation contract

Inputs may include:

- repository or folder;
- evaluation depth: `Low`, `Medium`, or `Detailed`;
- purpose profile or delivery horizon;
- team size and parallelism;
- agent autonomy;
- failure cost and data sensitivity;
- supported coding-agent harnesses;
- permission to run commands;
- permission to create an isolated worktree or disposable copy;
- desired report location.

When depth is absent in an interactive run, ask exactly:

> How deeply should I evaluate the repository: Low, Medium, or Detailed?

Treat `Detail` as `Detailed`.

After depth is known, determine the purpose profile from the user's request and repository evidence. When still materially ambiguous, ask exactly:

> Which target best matches this repository: 3-day Hackathon, 4-week MVP, Short Product, or Long-Lived Production?

Do not ask when the target is already clear. When interaction is unavailable, default depth to `Medium`, infer the closest purpose profile, and record assumptions.

## Primary outputs

Report these separately:

1. **Purpose profile** and risk/autonomy/team overlays.
2. **Fitness-for-purpose score:** `0–100`.
3. **Fit rank:** Excellent / Strong / Adequate / Misaligned / Poor.
4. **Harness capability score:** `0–100`.
5. **Capability rank:** `S–E`.
6. **Unjustified overhead penalty:** `0–40`.
7. Evaluation depth.
8. Audit confidence.
9. Requirement coverage.
10. Critical findings, fit gates, and remediation roadmap.

The fitness score is the primary verdict. Capability is descriptive, not the universal target.

A high-capability harness can be a poor fit for a short project. A small harness can be an excellent fit when it protects the critical path, feedback loop, and actual risks.

## Context budget

The configured parent and subagent models each have a 1,050,000-token context window. Never plan to use 60%.

Use these conservative limits:

- Parent target: at most 35% (`367,500` tokens).
- Parent stop-loading threshold: 45% (`472,500` tokens).
- Per-subagent target: at most 25% (`262,500` tokens).
- Universal emergency ceiling: 55% (`577,500` tokens).
- Absolute forbidden boundary: 60% (`630,000` tokens).

At each phase boundary, estimate context. Prefer a runtime context meter. Otherwise run:

```bash
python <skill-dir>/scripts/context_budget.py <selected evidence paths>
```

At the stop-loading threshold:

1. stop broad reading;
2. save evidence to audit artifacts;
3. compress findings into an evidence ledger;
4. close completed subagents;
5. continue from summaries and file pointers.

Read [`references/CONTEXT_BUDGET.md`](references/CONTEXT_BUDGET.md) before a Medium or Detailed audit, or whenever the repository is large.

## Step 1 — Establish audit depth and purpose

Record:

- absolute repository or folder path;
- commit, branch, or snapshot;
- evaluation depth;
- delivery horizon and deadline;
- expected repository lifetime;
- primary optimization: speed, learning, demo reliability, pilot validation, steady delivery, safety, compliance, or reuse;
- team size and expected parallel work;
- agent autonomy: interactive, supervised, or unattended;
- failure cost: low, medium, high, or critical;
- data sensitivity and compliance;
- supported coding agents;
- allowed commands and network access;
- whether isolated writes are allowed;
- inaccessible systems;
- output location.

Read [`references/PURPOSE_PROFILES.md`](references/PURPOSE_PROFILES.md). Select one base profile and apply only justified overlays.

Prefer read-only inspection. Run mutating tests only with explicit permission and only in a worktree, sandbox, disposable copy, or throwaway branch.

**Complete when:** depth, base profile, overlays, optimization target, permissions, version, and exclusions are explicit.

## Step 2 — Initialize evidence artifacts

Create an audit workspace outside the target repository unless requested otherwise.

Run:

```bash
python <skill-dir>/scripts/bootstrap_audit.py \
  --output <audit-dir> \
  --depth <low|medium|detailed> \
  --profile <hackathon|mvp|short_product|long_lived>
```

Use `audit.json` as the source of truth. Store large logs separately and reference them by path.

**Complete when:** purpose targets, evidence matrix, test ledger, friction ledger, findings ledger, and report draft exist.

## Step 3 — Load only the selected evaluation branch

Read [`references/DEPTHS.md`](references/DEPTHS.md), then load only the selected depth section.

Evaluation depth controls confidence and testing thoroughness. Purpose profile controls what “enough harness” means. Never substitute one for the other.

**Complete when:** required activities, subagent count, tests, coverage target, and confidence ceiling are recorded.

## Step 4 — Inventory before interpretation

Locate without reading everything:

- `AGENTS.md`, `AGENTS.override.md`, `CLAUDE.md`, nested rules, skills, hooks;
- architecture, product, plans, progress, decisions, and debt documents;
- task runners, setup scripts, manifests, lockfiles, CI;
- tests, linters, types, schemas, boundary checks;
- observability, traces, logs, permissions, sandbox, recovery;
- custom-agent and subagent configuration.

Also locate likely fixed costs:

- mandatory startup steps;
- always-loaded context;
- blocking approval gates;
- required full-suite checks;
- duplicated documentation;
- maintenance-heavy generators;
- multi-agent coordination rituals.

Use filenames, sizes, indexes, search, and manifests to select evidence. Avoid recursive full-file reads.

**Complete when:** all ten capability dimensions and five friction dimensions have candidate evidence or are marked missing.

## Step 5 — Delegate bounded evidence lanes

For Medium and Detailed audits, read [`references/SUBAGENT_PROTOCOL.md`](references/SUBAGENT_PROTOCOL.md).

Use the supplied `harness_*` Terra specialists.

- Medium: 3–5 relevant specialists.
- Detailed: all specialist lanes, normally in waves of 3–4.
- Low: zero or one explorer when necessary.

Always include `harness_purpose_fit_auditor` in a Detailed audit. Include it in Medium when the repository appears overbuilt, underbuilt, or its purpose is disputed.

Give every specialist a non-overlapping question, purpose profile, repository scope, evidence format, and stop condition. Require summaries no longer than 1,500 tokens.

**Complete when:** required lanes have evidence summaries, unknowns, preliminary capability scores, fit mismatches, and confidence labels.

## Step 6 — Test the purpose-critical loop

Read [`references/TEST_CATALOG.md`](references/TEST_CATALOG.md).

Choose tests from both:

1. the selected evaluation depth;
2. the selected purpose profile.

Examples:

- Hackathon: fresh setup, fast feedback, demo path, deploy path, one recovery path.
- MVP: critical user workflow, data/state continuity, deployment, targeted regression, handoff.
- Short Product: cross-module change, architecture boundary, CI recovery, team coordination.
- Long-Lived Production: regression breadth, rollback, observability, permission boundaries, resume, entropy controls.

Record expected result before execution. Measure elapsed time where possible.

**Complete when:** depth minimums and purpose-critical tests are satisfied, or skips have explicit constraints.

## Step 7 — Score capability and purpose fit

Read [`references/RUBRIC.md`](references/RUBRIC.md).

Evidence strength:

- `E4`: direct dynamic proof;
- `E3`: executable static proof;
- `E2`: repository documentation;
- `E1`: naming or implied convention;
- `E0`: assumption.

Restrictions:

- capability score 4 requires E4;
- score 3 requires E3 or E4;
- score 2 requires E2 or stronger.

Then evaluate purpose fit:

1. compare each capability score with its purpose target;
2. give no extra fitness credit above the target;
3. record deficits as under-harnessing;
4. record costly, unsupported surplus as over-harnessing;
5. score the five unjustified-friction categories;
6. apply purpose-specific fit gates.

Update `audit.json`, then run:

```bash
python <skill-dir>/scripts/score_audit.py <audit-dir>/audit.json
```

**Complete when:** capability, target adequacy, friction penalty, fitness score, coverage, and gates are explicit.

## Step 8 — Challenge both directions

Before finalizing, ask:

1. Which missing control creates unacceptable risk for this purpose?
2. Which existing control costs more than the risk it reduces?
3. Which high capability score has weak evidence?
4. Which apparently lean mechanism would fail under the expected autonomy or team size?
5. Which heavy mechanism could be deferred until after the current horizon?
6. Which documented claim differs from runtime behavior?

Detailed audits must use the adversarial tester. Medium audits should have one specialist challenge the preliminary purpose fit.

**Complete when:** under-harnessing and over-harnessing have both been tested.

## Step 9 — Produce the report

Read [`references/REPORT_TEMPLATE.md`](references/REPORT_TEMPLATE.md).

Lead with:

```text
Purpose profile: <profile + overlays>
Fitness for purpose: <score>/100 — <fit rank>
Harness capability: <score>/100 — Rank <S–E>
Unjustified overhead: <penalty>/40 — <Low|Moderate|High|Severe>
Evaluation depth: <Low|Medium|Detailed>
Audit confidence: <Preliminary|Validated|High>
Requirement coverage: <percent>
```

Separate:

- **Keep now:** controls that serve the current purpose.
- **Simplify now:** controls imposing unsupported delivery friction.
- **Add now:** missing controls required by current risks.
- **Defer:** useful controls whose value begins in a later lifecycle stage.

**Complete when:** another engineer can reproduce the scores and understand why the same harness could be good for one purpose and poor for another.

## Final guardrails

- More harness is not automatically better.
- Less harness is not automatically faster when failures and handoffs dominate.
- Capability is descriptive; fitness is contextual.
- Extra capability earns no fit bonus above the target.
- Penalize only observed or strongly evidenced friction, not file count.
- Safety and critical-risk overlays override deadline pressure.
- Loading is not compliance; compliance is not task success.
- Put navigation in documents, invariants in code, and judgment in review.
- Parallelize independent discovery, isolate writes, and centralize integration.
- Do not claim Detailed completion below 90% applicable-requirement coverage.
- Never hide skipped tests, inaccessible systems, assumptions, or context-budget breaches.
