# Purpose Profiles

Purpose determines the target harness. Select one base profile, then apply overlays.

The target levels use the same 0–4 capability scale as the main rubric. They are sufficiency targets, not mandatory implementation counts.

## Classification questions

Determine:

1. delivery horizon;
2. expected repository lifetime;
3. primary optimization;
4. team size and parallelism;
5. agent autonomy;
6. failure cost;
7. data sensitivity or regulation;
8. expected reuse.

When purpose is unclear, ask one purpose question before scoring. Avoid designing the profile from repository size alone.

## Base targets

| Dimension | Hackathon ≤7 days | MVP 2–6 weeks | Short Product 1–3 months | Long-Lived Production |
|---|---:|---:|---:|---:|
| Task contracts | 2.0 | 2.5 | 3.0 | 3.5 |
| Context and knowledge | 1.5 | 2.0 | 2.5 | 3.0 |
| Architecture and locality | 1.0 | 2.0 | 2.5 | 3.5 |
| Runtime and reproducibility | 2.5 | 3.0 | 3.0 | 3.5 |
| Verification and evals | 2.0 | 2.5 | 3.0 | 3.5 |
| Observability | 1.0 | 2.0 | 2.5 | 3.0 |
| State and continuity | 1.0 | 2.0 | 2.5 | 3.5 |
| Safety and recovery | 1.0 | 2.0 | 2.5 | 3.5 |
| Subagent coordination | 1.0 | 1.5 | 2.0 | 2.5 |
| Entropy and evolution | 0.5 | 1.5 | 2.0 | 3.5 |

These targets assume ordinary low-to-medium risk. Overlays can raise them.

## Profile intent

### Hackathon

Optimize for:

- time to first working path;
- fast local feedback;
- reliable demo;
- simple deployment;
- recoverable experimentation;
- minimal coordination overhead.

Expected controls:

- tiny decision map;
- one-command setup;
- targeted smoke tests;
- demo/deploy checklist;
- basic secrets discipline;
- simple Git checkpoints;
- one visible source of truth for scope.

Usually defer:

- broad architecture governance;
- extensive agent eval suites;
- elaborate memory systems;
- complex multi-agent orchestration;
- comprehensive observability platforms;
- maintenance automation for a repository that may be discarded.

A heavy harness is acceptable only when already reusable, automated, and nearly free on the critical path.

### MVP

Optimize for:

- validated user workflow;
- repeatable builds and deployment;
- team handoff;
- targeted regression protection;
- ability to change direction;
- preserving pilot data and decisions.

Expected controls:

- concise task and acceptance criteria;
- reproducible environment;
- critical-path integration tests;
- basic architecture boundaries;
- progress and decision state;
- deployment and rollback procedure;
- bounded agent instructions;
- lightweight observability.

Defer enterprise-grade controls unless risk overlays require them.

### Short Product

Optimize for:

- steady multi-week delivery;
- safe cross-module changes;
- team parallelism;
- CI reliability;
- maintainable architecture;
- predictable releases.

Expected controls:

- clearer ownership and boundaries;
- stronger integration testing;
- resumable state;
- actionable logs;
- controlled subagent work;
- regular debt and documentation maintenance.

### Long-Lived Production

Optimize for:

- sustained change;
- reliability;
- recoverability;
- security;
- institutional memory;
- model and harness evolution;
- low long-term entropy.

Expected controls:

- executable architecture boundaries;
- broad verification and agent evals;
- mature observability;
- durable state;
- permission isolation;
- rollback evidence;
- entropy and stale-control removal;
- measured harness changes.

## Overlays

Apply the smallest increase that covers the actual risk. Cap all targets at 4.0.

### High or critical failure cost

Raise by `+0.5`:

- task contracts;
- verification;
- observability;
- safety and recovery;
- state.

For critical failure cost, set safety and verification to at least `3.5`.

### Unattended autonomy

Raise by `+0.5`:

- task contracts;
- verification;
- observability;
- state;
- safety.

Set recovery evidence as a mandatory fit gate.

### Sensitive or regulated data

Set:

- safety to at least `3.5`;
- observability to at least `3.0`;
- verification to at least `3.0`;
- state to at least `3.0`.

For regulated systems, raise each to at least `3.5` and require intervention records.

### Team size and concurrency

For 5 or more contributors or parallel agents, raise by `+0.5`:

- context;
- architecture;
- state;
- subagent coordination.

For multiple teams, set architecture and state to at least `3.0`.

### Reusable template or platform

Raise by `+0.5`:

- runtime;
- verification;
- context;
- evolution.

A reusable hackathon scaffold may therefore need more harness than one disposable hackathon repository.

### High change velocity

Raise runtime and verification by `+0.5`, but prefer fast targeted checks over slow broad gates.

## Purpose fit formula

The score script calculates:

```text
adequacy per dimension = min(actual capability / target, 1)
weighted adequacy = weighted mean of adequacy × 100
fitness = weighted adequacy - unjustified overhead penalty
```

Capability above target receives no extra fitness credit.

This prevents a mature production harness from automatically outranking a lean hackathon harness.

## Fit gates

Add purpose gates to `audit.json`.

Common gates:

| Gate | Suggested maximum fit when failed |
|---|---:|
| Critical user/demo path works | 49 |
| Fresh setup succeeds within deadline budget | 64 |
| Feedback loop fits delivery cadence | 69 |
| Deployment or handoff path works when required | 69 |
| Risk-overlay controls satisfied | 49 |
| Recovery works for unattended agents | 49 |
| Required sensitive-data boundary works | 39 |

Use a gate only when applicable to the selected purpose.

## Friction categories

Score only **unjustified** overhead from 0–4.

| Category | Weight | Examples |
|---|---:|---|
| Fixed process cost | 5 | mandatory plans, gates, or ceremonies on every small change |
| Context load | 4 | large always-loaded instructions or duplicated references |
| Feedback latency | 4 | slow full suites blocking tiny changes without risk justification |
| Coordination burden | 3 | excessive agent roles, handoffs, or approvals |
| Maintenance surface | 4 | generators, hooks, or docs whose upkeep exceeds current value |

Do not penalize a large harness merely for having many files. Penalize measured or strongly evidenced delay, cognitive load, failure surface, or maintenance burden.

The doubled penalty makes severe fixed costs material:

| Penalty | Overhead |
|---:|---|
| 0–5 | Low |
| >5–12 | Moderate |
| >12–24 | High |
| >24–40 | Severe |

A failed feedback-budget or critical-path gate can cap fitness further.

## Fit interpretation

| Score | Fit rank |
|---:|---|
| 90–100 | Excellent Fit |
| 80–89 | Strong Fit |
| 65–79 | Adequate Fit |
| 45–64 | Misaligned |
| 0–44 | Poor Fit |

## Lifecycle recommendation

A good audit distinguishes:

- **needed now**;
- **useful after the next milestone**;
- **useful only if risk or autonomy increases**;
- **remove or simplify**.

The target profile should be revisited when deadline, users, data, autonomy, or repository lifetime changes.
