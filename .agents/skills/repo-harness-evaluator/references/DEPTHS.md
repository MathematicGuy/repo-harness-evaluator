# Evaluation Depths

Load only the selected section.

Depth controls audit thoroughness. Purpose controls the target harness.

## Low

Purpose: preliminary screening.

Coverage target: 35–50% of applicable requirements.

Required work:

- classify the purpose profile and obvious overlays;
- root and major-folder inventory;
- main context files;
- README, architecture, scripts, CI, tests, plans, permissions;
- reference and command existence checks;
- obvious contradiction, duplication, staleness, under-harnessing, and over-harnessing checks;
- capability and preliminary purpose fit;
- top five risks and improvements.

Subagents: optional; at most one read-only explorer.

Dynamic tests: lightweight non-destructive checks.

Confidence ceiling: Preliminary.

## Medium

Purpose: verify the most important harness practices for the selected profile.

Coverage target: 65–85%.

Required work:

- all Low work;
- active instruction scope;
- standard setup or validation where safe;
- profile-critical dynamic tests;
- guide-versus-sensor analysis;
- mechanical enforcement checks;
- one controlled failure and recovery;
- one resumability or handoff test when profile-relevant;
- subagent boundaries;
- elapsed-time or friction evidence for major fixed costs;
- evidence for every score of 3 or 4;
- under-harnessing and over-harnessing findings.

Subagents: 3–5 specialists. Include purpose-fit auditor when fit is disputed.

Tests: at least 3 representative tests, chosen from depth and purpose requirements.

Confidence ceiling: Validated.

## Detailed

Purpose: high-confidence capability and purpose-fit assessment.

Coverage target: greater than 90%. Below 90%, report “Detailed evaluation attempted — coverage incomplete.”

Required work:

- all Medium work;
- requirement-to-evidence matrix;
- all specialist lanes, including purpose fit;
- at least 6 representative task types;
- outcome and trajectory evaluation;
- A/B/C context experiment when practical;
- negative controls;
- contradiction and precedence tests;
- at least 4 adversarial tests;
- test-quality analysis;
- isolation, permissions, rollback, and recovery;
- cross-session continuation;
- context cost and instruction leakage;
- entropy and model-upgrade revalidation;
- fixed-cost and feedback-latency measurement;
- evidence attached to every score and friction penalty.

Confidence ceiling: High only when coverage exceeds 90%, dynamic and adversarial evidence exists, and no major fit assumption remains unexplained.
