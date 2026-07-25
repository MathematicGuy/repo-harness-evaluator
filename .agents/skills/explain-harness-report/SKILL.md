---
name: explain-harness-report
description: Render a repo-harness-evaluator REPORT.md as a two-audience HTML explainer (decision makers + engineers) saved next to the report.
disable-model-invocation: true
---

# Explain Harness Report

Turn a repo-harness-evaluator `REPORT.md` into a single self-contained HTML explainer with two stacked audiences: **decision makers** (BA / PM / boss — plain language, scores, actions) first, **engineers** (flow diagrams, dimension bars, findings, evidence) second, and a stable **method appendix** last so it can be skipped by anyone who has read it once. The file lands next to the report and is regenerated on every audit cycle.

## Process

### 1. Locate input

Use the `REPORT.md` path given in the invocation argument. If no argument was given, find the most recently modified `REPORT.md` under `.audit/` in the workspace and confirm that path with the user before proceeding.

**Complete when:** exactly one absolute `REPORT.md` path is fixed.

### 2. Extract

Parse the report into the data the template needs. The repo-harness-evaluator template uses these headings — read all of them:

- **Executive verdict** (fenced text block): repository, purpose profile, depth, fitness score + rank, capability score + rank, overhead score + level, audit confidence, requirement coverage, overall recommendation.
- **Purpose profile** — delivery horizon, team, autonomy, failure cost.
- The three scorecards: **Purpose-fit scorecard** (weight, target, actual, adequacy, gap type per dimension), **Capability scorecard** (score, points, evidence level), **Overhead scorecard** (category, penalty, justification).
- **Findings** — each `F-xx` block: ID, title, dimension, severity, evidence level, observed evidence, recommendation, action timing.
- **Fit gates**, **Tests** table, **Coverage matrix**, **Lifecycle roadmap** (Add now / Keep now / Simplify now / Defer), **Limitations**, and **Scope inspected**.

**Complete when:** every HTML section in HTML-TEMPLATE.md has its data, or an explicit "not in report" marker where the report omits it.

### 3. Reconstruct the harness flow (for section B1)

Derive the audited repo's current working flow — session start → context files → edit → verify → CI → deploy → handoff — from the report's Scope inspected section, scorecard evidence columns, and findings. Map each finding onto the step of the flow where it bites (e.g. stale doc paths bite at the context-reading step; missing boundary lint bites at the edit step; missing logs bite after deploy). Then derive the improved flow by applying each finding's recommendation at that same step.

Only if the report is too thin to draw the flow, read the audited repo's `AGENTS.md` and CI workflow directly — the paths are listed in the report's Scope inspected section.

**Complete when:** both the current-flow and improved-flow diagrams have every node placed and every finding attached to a specific step.

### 4. Render

Write a single self-contained HTML file following [HTML-TEMPLATE.md](HTML-TEMPLATE.md) exactly. Output path: **same folder as the input**, named `REPORT.html`, overwriting any previous version so the HTML always matches its sibling markdown.

**Complete when:** the file exists and every anchor resolves — `#verdict`, `#engineers`, `#method`, and every finding-card anchor referenced from a red flowchart edge in B1.

### 5. Deliver

Open the file for the user — `start <path>` on Windows, `open <path>` on macOS, `xdg-open <path>` on Linux — and state the absolute path.

**Complete when:** the open command has run and the path has been reported.

## Layout

See [HTML-TEMPLATE.md](HTML-TEMPLATE.md) for the full scaffold, section layout, palette, flowchart conventions, and tone rules — follow it verbatim; do not redesign the layout.
