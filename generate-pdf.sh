#!/usr/bin/env bash
set -e
DIR="$(cd "$(dirname "$0")" && pwd)"
"$DIR/.venv/bin/python3" -m japanese_grammar_resume "$@"
