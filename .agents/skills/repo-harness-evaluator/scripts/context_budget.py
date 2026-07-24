#!/usr/bin/env python3
"""Estimate text evidence tokens without external dependencies.

This cannot measure hidden instructions or tool schemas. It intentionally uses
a conservative characters-per-token estimate.
"""

from __future__ import annotations
import argparse
import math
from pathlib import Path

TEXT_SUFFIXES = {
    ".md", ".txt", ".py", ".js", ".ts", ".tsx", ".jsx", ".json", ".toml",
    ".yaml", ".yml", ".xml", ".html", ".css", ".scss", ".rs", ".go", ".java",
    ".kt", ".cs", ".cpp", ".c", ".h", ".sh", ".ps1", ".sql", ".ini", ".cfg",
}
SKIP_DIRS = {".git", "node_modules", "vendor", "dist", "build", ".venv", "venv", "target"}

def files_for(path: Path):
    if path.is_file():
        yield path
        return
    for item in path.rglob("*"):
        if any(part in SKIP_DIRS for part in item.parts):
            continue
        if item.is_file() and (item.suffix.lower() in TEXT_SUFFIXES or item.name in {"Dockerfile", "Makefile"}):
            yield item

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("paths", nargs="+")
    parser.add_argument("--window", type=int, default=1_050_000)
    parser.add_argument("--chars-per-token", type=float, default=3.2)
    args = parser.parse_args()

    chars = 0
    count = 0
    failures = []
    for raw in args.paths:
        path = Path(raw)
        if not path.exists():
            failures.append(str(path))
            continue
        for file in files_for(path):
            try:
                chars += len(file.read_text(encoding="utf-8", errors="ignore"))
                count += 1
            except OSError:
                failures.append(str(file))

    tokens = math.ceil(chars / args.chars_per_token)
    pct = tokens / args.window * 100
    print(f"files={count}")
    print(f"characters={chars}")
    print(f"estimated_tokens={tokens}")
    print(f"window_percent={pct:.2f}%")
    print("status=" + (
        "FORBIDDEN" if pct >= 60 else
        "EMERGENCY" if pct >= 55 else
        "STOP_LOADING" if pct >= 45 else
        "CAUTION" if pct >= 35 else
        "OK"
    ))
    if failures:
        print("unreadable_or_missing=" + ",".join(failures))

if __name__ == "__main__":
    main()
