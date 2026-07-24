#!/usr/bin/env sh
set -eu

ROOT=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
STAMP=$(date +%Y%m%d-%H%M%S)

copy_with_backup() {
  src=$1
  dst=$2
  mkdir -p "$(dirname "$dst")"
  if [ -e "$dst" ]; then
    cp -R "$dst" "$dst.bak-$STAMP"
  fi
  rm -rf "$dst"
  cp -R "$src" "$dst"
}

copy_with_backup \
  "$ROOT/.agents/skills/repo-harness-evaluator" \
  "$HOME/.agents/skills/repo-harness-evaluator"

mkdir -p "$HOME/.codex/agents"
for src in "$ROOT"/.codex/agents/*.toml; do
  copy_with_backup "$src" "$HOME/.codex/agents/$(basename "$src")"
done

copy_with_backup \
  "$ROOT/profile/repo-harness-eval.config.toml" \
  "$HOME/.codex/repo-harness-eval.config.toml"

printf '%s\n' "Installed repo-harness-evaluator."
printf '%s\n' "Run: codex --profile repo-harness-eval"
printf '%s\n' 'Invoke: $repo-harness-evaluator evaluate the current repository'
