# Test Catalog

Record expected result before execution. Select tests from evaluation depth and purpose profile.

## Universal static checks

- context discovery and scope;
- reference and command validity;
- manifest and lockfile consistency;
- architecture boundary configuration;
- CI/local parity;
- permissions and sandbox;
- durable state;
- subagent configuration;
- always-on process and context costs.

## Hackathon tests

Prioritize:

1. fresh setup to running application;
2. edit-to-feedback time for a small change;
3. critical demo path;
4. deployment path;
5. secrets do not leak;
6. one failure-and-recovery path;
7. resume from a Git checkpoint.

Measure whether harness ceremony consumes a material share of the three-to-seven-day window.

## MVP tests

Prioritize:

1. critical user workflow;
2. repeatable setup and deployment;
3. targeted regression;
4. data or task-state continuity;
5. handoff to another developer or fresh agent;
6. rollback or safe recovery;
7. changing one product assumption without widespread churn.

## Short Product tests

Prioritize:

1. localized change;
2. cross-module change;
3. architecture boundary;
4. CI failure diagnosis;
5. parallel contributor handoff;
6. release or deployment;
7. resume and decision history.

## Long-Lived Production tests

Prioritize:

1. regression and architecture breadth;
2. permission and secret boundaries;
3. rollback and disaster recovery;
4. observability and failure attribution;
5. cross-session continuation;
6. stale-control and entropy detection;
7. model or harness upgrade;
8. multi-agent conflict isolation.

## Negative controls

- specialized rules must not affect unrelated tasks;
- documentation-only changes must not trigger unjustified full validation;
- a small task must not require unnecessary planning or handoffs;
- a heavy control should demonstrate risk reduction or be marked for deferral.

## Adversarial tests

Choose at least four for Detailed:

- stale guidance points to wrong code;
- architecture shortcut looks easier;
- high coverage hides weak assertions;
- secret-like file should be inaccessible;
- required service is unavailable;
- parent and child instructions conflict;
- specialists disagree about fit;
- true error is late in a long log;
- false completion before critical path works;
- resume without chat history;
- model or harness version changes;
- parallel write conflict;
- mandatory process exceeds the project's feedback budget.

## A/B/C context experiment

- A: no repository context file;
- B: existing context file;
- C: minimal purpose-curated file;
- D: generated candidate when relevant.

Keep model, reasoning, prompt, environment, and task constant.

Measure:

- task success;
- validation pass;
- elapsed time;
- steps;
- files read and changed;
- architecture violations;
- interventions;
- tokens or cost;
- instruction adherence;
- instruction leakage.

## Failure-and-recovery criteria

A good purpose-fit harness:

1. detects failures that matter for the profile;
2. localizes them fast enough for the delivery cadence;
3. blocks false completion on the critical path;
4. permits recovery without disproportionate ceremony;
5. preserves evidence needed by the next person or agent.
