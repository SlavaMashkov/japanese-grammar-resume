#!/usr/bin/env bash
set -e
DIR="$(cd "$(dirname "$0")" && pwd)"
"$DIR/.venv/bin/python3" -m japanese_grammar_resume
echo "PDF generated: $DIR/output/japanese_summary.pdf"
