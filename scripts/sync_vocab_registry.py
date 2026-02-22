#!/usr/bin/env python3
"""Validate vocab_registry.json against chapter files.

Parses each ch03_*.py via the ast module (no reportlab import needed),
finds vocab_from_registry([...]) calls, extracts keys, and checks that
every key exists in the registry.

Usage:
    .venv/bin/python3 scripts/sync_vocab_registry.py
"""

import ast
import json
import re
from pathlib import Path

CHAPTERS_DIR = Path(__file__).resolve().parent.parent / "japanese_grammar_resume" / "chapters"
REGISTRY_PATH = Path(__file__).resolve().parent.parent / "japanese_grammar_resume" / "vocab_registry.json"


def chapter_sort_key(path: Path) -> tuple[int, int]:
    """Extract (major, minor) chapter numbers for sorting, e.g. ch03_11 → (3, 11)."""
    m = re.search(r"ch(\d+)_(\d+)", path.stem)
    if not m:
        return (999, 999)
    return (int(m.group(1)), int(m.group(2)))


def chapter_id(path: Path) -> str:
    """Extract chapter id like 'ch03_02' from filename."""
    m = re.search(r"(ch\d+_\d+)", path.stem)
    return m.group(1) if m else path.stem


def extract_keys_from_file(path: Path) -> list[str]:
    """Parse a chapter file with ast and return vocab keys from vocab_from_registry() calls."""
    tree = ast.parse(path.read_text())
    keys: list[str] = []

    for node in ast.walk(tree):
        if (
            isinstance(node, ast.Call)
            and isinstance(node.func, ast.Name)
            and node.func.id == "vocab_from_registry"
            and node.args
            and isinstance(node.args[0], ast.List)
        ):
            for elt in node.args[0].elts:
                if isinstance(elt, ast.Constant) and isinstance(elt.value, str):
                    keys.append(elt.value)

    return keys


def main() -> None:
    registry = json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))

    chapter_files = sorted(CHAPTERS_DIR.glob("ch03_*.py"), key=chapter_sort_key)

    all_ok = True
    total_keys = 0

    for path in chapter_files:
        chap = chapter_id(path)
        keys = extract_keys_from_file(path)
        if not keys:
            continue

        total_keys += len(keys)
        missing = [k for k in keys if k not in registry]
        print(f"  {chap}: {len(keys)} words", end="")
        if missing:
            all_ok = False
            print(f"  ⚠ missing: {missing}")
        else:
            print()

    print(f"\nRegistry: {len(registry)} words, chapters reference {total_keys} keys")
    unused = set(registry) - {k for p in chapter_files for k in extract_keys_from_file(p)}
    if unused:
        print(f"Unused registry keys: {sorted(unused)}")
    if all_ok:
        print("All keys valid ✓")
    else:
        print("Some keys are missing from the registry!")
        raise SystemExit(1)


if __name__ == "__main__":
    main()
