# Japanese Grammar Resume

A compact PDF summary of [Tae Kim's Guide to Learning Japanese](https://guidetojapanese.org/learn/grammar) — grammar tables, examples, and a vocabulary section with furigana readings.

Each book chapter is a separate Python module; they are all assembled into a single PDF.

## Example

Here's what a page with adjective conjugation looks like:

<!-- TODO: add screenshot output/screenshot.png -->

## Getting Started

```bash
# Clone
git clone https://github.com/<user>/japanese-grammar-resume.git
cd japanese-grammar-resume

# Create a virtual environment and install dependencies
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt

# Generate the PDF
bash generate-pdf.sh
# or directly:
.venv/bin/python3 -m japanese_grammar_resume
```

Output: `output/japanese_summary.pdf`

You can specify a different output directory:

```bash
bash generate-pdf.sh -o ~/Desktop
```

## Requirements

- Python 3.12+
- [reportlab](https://docs.reportlab.com/) >= 4.0
- [ruff](https://docs.astral.sh/ruff/) >= 0.15 (linting & formatting)
- DejaVuSans font (usually pre-installed on Linux)

The NotoSansJP-Light font for Japanese text is included in the repository (`fonts/`).

## Code Quality

`generate-pdf.sh` automatically formats and lints the code before building the PDF. If the linter finds errors, the build stops.

To run manually:

```bash
.venv/bin/ruff format japanese_grammar_resume/ scripts/   # format
.venv/bin/ruff check japanese_grammar_resume/ scripts/    # lint
```

## Project Structure

```txt
japanese_grammar_resume/        Python package
  __main__.py                   entry point: auto-discovers chapters, builds PDF
  styles.py                     fonts, styles, helpers
  vocab_registry.json           vocabulary (single source of truth)
  chapters/                     one subdir per part, auto-discovered
    ch03/                       Part 3: Basic Grammar
      ch03_02_state_of_being.py
      ch03_03_particles.py
      ch03_04_adjectives.py
      ...
scripts/
  sync_vocab_registry.py        vocabulary validation
fonts/                          NotoSansJP-Light.ttf
output/                         generated PDF (in .gitignore)
```

## Vocabulary (`vocab_registry.json`)

All words are stored in a single JSON file. Each entry contains furigana/kanji pairs for rendering, a translation, and the chapter of first appearance:

```json
{
  "学生": {
    "pairs": [["がく", "学"], ["せい", "生"]],
    "meaning": "student",
    "chapter": "ch03_02"
  }
}
```

Chapters reference words by key:

```python
story.append(vocab_two_col(vocab_from_registry([
    "人", "学生", "元気", "友達",
])))
```

## Adding a New Chapter

1. Add new words to `vocab_registry.json`
2. Create `japanese_grammar_resume/chapters/chXX/chXX_YY_name.py` with a `build()` function (start with `PageBreak()`). Create the part subdir with an empty `__init__.py` if needed.
3. Chapters are auto-discovered — no manual imports needed
4. Validate: `.venv/bin/python3 scripts/sync_vocab_registry.py`
5. Generate PDF: `bash generate-pdf.sh`

## License

Content is based on [Tae Kim's Guide to Learning Japanese](https://guidetojapanese.org/learn/grammar), distributed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).
