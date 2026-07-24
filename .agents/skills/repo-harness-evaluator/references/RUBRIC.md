# Harness Capability and Purpose-Fit Rubric

## Capability score

Score each dimension 0–4.

- 0: absent.
- 1: informal or prompt-only.
- 2: documented and repeatable.
- 3: automated or structurally enforced.
- 4: measured on representative tasks and deliberately evolved.

`capability points = weight × score / 4`

| Dimension | Weight |
|---|---:|
| Task contracts and definition of done | 10 |
| Context and repository knowledge | 12 |
| Architecture and change locality | 12 |
| Runtime, tools, and reproducibility | 10 |
| Verification and agent evaluations | 16 |
| Observability and failure attribution | 10 |
| State and long-horizon continuity | 8 |
| Permissions, safety, and recovery | 8 |
| Subagent coordination and integration | 6 |
| Entropy control and harness evolution | 8 |

## Evidence ladder

- E4: direct dynamic proof.
- E3: executable static proof.
- E2: repository documentation.
- E1: naming or implied convention.
- E0: assumption.

Restrictions:

- 4 requires E4;
- 3 requires E3 or E4;
- 2 requires E2 or stronger.

## Capability ranks

| Points | Rank |
|---:|---|
| 90–100 | S — Evidence-Driven Harness |
| 80–89 | A — Agent-Ready Repository |
| 65–79 | B — Verified Harness Foundation |
| 45–64 | C — Guided Repository |
| 25–44 | D — Prompt-Centered Harness |
| 0–24 | E — Unharnessed or Unsafe |

Capability is descriptive. Do not treat S as the goal for every repository.

## Purpose-fit adequacy

Use targets from `PURPOSE_PROFILES.md`.

```text
dimension adequacy = min(actual capability / target, 1)
weighted adequacy = weighted mean × 100
```

When target is zero, exclude the dimension from the adequacy denominator unless a risk overlay makes it applicable.

Extra capability receives no fit bonus.

## Unjustified overhead

Each category has a 0–4 level and weight.

| Category | Weight |
|---|---:|
| Fixed process cost | 5 |
| Context load | 4 |
| Feedback latency | 4 |
| Coordination burden | 3 |
| Maintenance surface | 4 |

```text
base friction = Σ(weight × level / 4)
overhead penalty = 2 × base friction
fitness = max(0, weighted adequacy - overhead penalty)
```

Assign a penalty only with E2 or stronger evidence. A level 3 or 4 should normally have E4 timing or task evidence.

## Fit ranks

| Fitness | Rank |
|---:|---|
| 90–100 | Excellent Fit |
| 80–89 | Strong Fit |
| 65–79 | Adequate Fit |
| 45–64 | Misaligned |
| 0–44 | Poor Fit |

## Capability rank gates

- no dynamic validation: maximum C;
- no executable architecture or safety controls: maximum B;
- no representative agent-task evaluation: maximum A;
- no recovery evidence: maximum A;
- critical uncontrolled secret, production, or destructive risk: force D or E as justified.

These gates affect capability, not purpose-fit adequacy directly.

## Purpose fit gates

Apply only relevant gates from the selected profile.

A failed gate caps fitness at its configured maximum. Unknown gates remain limitations and reduce confidence.

Safety and critical-risk gates override deadline or prototype status.

## Context-file score

Evaluate `AGENTS.md`, `CLAUDE.md`, nested rules, and skills:

| Criterion | Weight |
|---|---:|
| Universal relevance | 12 |
| Repository specificity | 10 |
| Actionability and verifiability | 10 |
| Brevity and active payload | 10 |
| Scope and precedence correctness | 10 |
| True progressive disclosure | 10 |
| Freshness and source authority | 10 |
| Separation from deterministic enforcement | 10 |
| Cross-agent portability | 8 |
| Measured task impact | 10 |

Do not add this score to capability or fitness. It informs the Context dimension and Context Load friction.

## Coverage

- verified = 1;
- partial = 0.5;
- unverified = 0;
- not applicable = excluded.

`coverage = (verified + 0.5 × partial) / applicable`

## Confidence

- Low depth: Preliminary.
- Medium: Validated when required dynamic evidence exists.
- Detailed: High only with >90% coverage, purpose-critical dynamic evidence, recovery evidence, and adversarial challenge.
