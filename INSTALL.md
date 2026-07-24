# Manual Installation

## User-scoped installation

Copy:

```text
.agents/skills/repo-harness-evaluator
```

to:

```text
~/.agents/skills/repo-harness-evaluator
```

Copy every file from:

```text
.codex/agents
```

to:

```text
~/.codex/agents
```

Copy:

```text
profile/repo-harness-eval.config.toml
```

to:

```text
~/.codex/repo-harness-eval.config.toml
```

Restart Codex when the new skill or agents do not appear.

Launch:

```bash
codex --profile repo-harness-eval
```

Invoke:

```text
$repo-harness-evaluator evaluate this repository for its delivery purpose
```

## Repository-scoped installation

To version the skill with one repository, copy the `.agents` and `.codex` folders into its root. Merge the profile's `[agents]` settings into the repository's `.codex/config.toml` rather than overwriting existing configuration.
