#!/usr/bin/env bash
set -e
DIR="$(cd "$(dirname "$0")" && pwd)"

echo "Formatting..."
"$DIR/.venv/bin/ruff" format japanese_grammar_resume/ scripts/
echo "Linting..."
"$DIR/.venv/bin/ruff" check japanese_grammar_resume/ scripts/

"$DIR/.venv/bin/python3" -m japanese_grammar_resume "$@"
