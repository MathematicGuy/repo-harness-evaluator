# Context Budget Protocol

Both configured models have a 1,050,000-token window. The audit intentionally operates far below it.

## Budgets

| Thread | Target | Stop broad loading | Emergency ceiling | Forbidden |
|---|---:|---:|---:|---:|
| Sol coordinator | 367,500 (35%) | 472,500 (45%) | 577,500 (55%) | 630,000 (60%) |
| Terra specialist | 262,500 (25%) | 367,500 (35%) | 472,500 (45%) | 630,000 (60%) |

The emergency ceiling includes uncertainty from system instructions, tool schemas, conversation history, and token estimation.

## Working-set rules

1. Inventory before reading.
2. Read targeted ranges, not whole large files.
3. Search before opening.
4. Send noisy exploration to specialists.
5. Return summaries under 1,500 tokens.
6. Persist full evidence to files.
7. Keep the coordinator on decisions, scores, conflicts, and final synthesis.
8. Run Detailed specialists in waves of 3–4.
9. Close finished threads before the next wave.
10. Never paste full build logs or repository trees into the main thread.

## Checkpoints

Check budget:

- after inventory;
- after each subagent wave;
- after dynamic tests;
- before scoring;
- before final synthesis.

When estimated context reaches 35%:

- stop speculative exploration;
- fill the evidence matrix;
- list unknowns;
- finish the current lane.

At 45%:

- stop loading new broad evidence;
- summarize;
- create a fresh continuation thread when available;
- continue through pointers and ledgers.

At 55%:

- halt the phase;
- save state;
- compact or restart before continuing.

## Estimation

Prefer a runtime context meter. When unavailable, use `scripts/context_budget.py` for selected text evidence. Its estimate is conservative but cannot measure hidden platform instructions or tool schemas; therefore the skill uses a 55% emergency ceiling rather than planning to 60%.

## Evidence ledger format

Each entry should fit this shape:

```text
ID:
Claim:
Evidence level:
Path or command:
Relevant range:
Observed result:
Implication:
Unknown:
```

Do not duplicate the evidence body in the coordinator context.
