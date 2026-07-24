# Subagent Protocol

The Sol parent is the Audit Coordinator. Terra specialists gather bounded evidence.

Every assignment must include the selected purpose profile and overlays.

## Required assignment

```text
Role:
Capability dimension:
Purpose profile:
Repository scope:
Questions:
Required evidence:
Allowed tools:
Write permission:
Context target:
Output limit:
Stop conditions:
```

## Required result

Every specialist returns:

1. direct conclusion;
2. evidence paths, symbols, commands, or outputs;
3. confirmed facts;
4. inferences;
5. unknowns;
6. severity-ranked findings;
7. preliminary capability score;
8. purpose-fit deficit or surplus;
9. observed friction;
10. next verification;
11. confidence.

Maximum summary: 1,500 tokens.

## Lanes

- `harness_purpose_fit_auditor`
- `harness_context_auditor`
- `harness_architecture_auditor`
- `harness_verification_auditor`
- `harness_runtime_auditor`
- `harness_state_observability_auditor`
- `harness_safety_recovery_auditor`
- `harness_adversarial_tester`

## Orchestration

Medium:

- Wave 1: context, architecture, verification.
- Add purpose-fit, runtime, or state/safety based on profile and preliminary gaps.

Detailed:

- Wave 1: purpose fit, context, architecture, runtime.
- Reconcile targets and evidence matrix.
- Wave 2: verification, state/observability, safety/recovery.
- Wave 3: adversarial tester after preliminary scoring.

## Write policy

Specialists are read-only. Controlled writes require an isolated environment and coordinator authorization. One integration authority owns shared-state decisions.

## Conflict resolution

1. isolate the disputed claim;
2. compare evidence levels;
3. distinguish capability disagreement from purpose disagreement;
4. prefer runtime evidence to documentation;
5. run a focused test;
6. preserve unresolved disagreement;
7. choose the less optimistic fit when evidence remains equal.
