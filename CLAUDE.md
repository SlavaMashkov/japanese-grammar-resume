# Japanese Grammar Resume

PDF summary of a Japanese grammar book (Tae Kim's Guide). Each chapter is appended to a single PDF.

## Project Structure

```txt
pyproject.toml                     — project metadata, dependencies
requirements.txt                   — dependencies for pip install -r
generate-pdf.sh                    — bash wrapper for running the generator
fonts/                             — fonts (NotoSansJP-Light.ttf for Japanese text)
output/                            — generated PDF files
.venv/                             — Python virtual environment
scripts/
  sync_vocab_registry.py           — vocab_registry.json validation (checks keys from chapters)
japanese_grammar_resume/           — Python package
  __init__.py
  __main__.py                      — entry point: imports chapters, builds PDF
  styles.py                        — fonts, colors, styles, helpers (jp, cell, section_header, kanji_cell, vocab_two_col, vocab_from_registry, TABLE_STYLE)
  vocab_registry.json              — registry of unique words by chapter
  chapters/                        — one file per chapter, each exports build() → list
    __init__.py
    ch03_02_state_of_being.py
    ch03_03_particles.py
    ch03_04_adjectives.py
    ch03_05_verb_basics.py
    ch03_06_negative_verbs.py
    ch03_07_past_tense.py
    ch03_08_verb_particles.py
    ch03_09_transitive.py
    ch03_10_relative_clauses.py
    ch03_11_noun_particles.py
```

## Running

```bash
bash generate-pdf.sh
# or directly:
.venv/bin/python3 -m japanese_grammar_resume
# with custom output directory:
bash generate-pdf.sh -o ~/Desktop
```

Output: `output/japanese_summary.pdf` (default)

## Dependencies

- Python 3.12+ with venv
- reportlab>=4.0 (installed in .venv, declared in `pyproject.toml` and `requirements.txt`)

## Fonts

- **DV / DV-B** — DejaVuSans (system font, `/usr/share/fonts/truetype/dejavu/`)
- **JP** — NotoSansJP-Light (`fonts/NotoSansJP-Light.ttf`, weight 300) — Japanese text

The `jp()` function auto-detects CJK characters and switches the font accordingly.

## Adding a New Chapter

1. Create `japanese_grammar_resume/chapters/ch03_XX_name.py` with a `build()` function returning a `list` of story elements.
2. Import `from ..styles import *` — all helpers and styles are available.
3. The first chapter (3.2) does not start with `PageBreak()`; all others do.
4. Add the import and `build()` call in `japanese_grammar_resume/__main__.py`.

## Vocab Registry

`japanese_grammar_resume/vocab_registry.json` is the single source of truth for word data. Key is the word spelling (kanji or kana), value is `{ pairs, meaning, chapter }`:

```json
{
  "学生": {
    "pairs": [["がく", "学"], ["せい", "生"]],
    "meaning": "student",
    "chapter": "ch03_02"
  }
}
```

- `pairs` — matrix `[[furigana, char], ...]` for rendering via `kanji_cell()`
- `meaning` — word translation
- `chapter` — chapter of first appearance

Chapters reference words by key via the `vocab_from_registry()` helper:

```python
story.append(vocab_two_col(vocab_from_registry([
    "人", "学生", "元気", "友達",
])))
```

The script `scripts/sync_vocab_registry.py` validates the registry — checks that all keys referenced in chapters exist in the JSON.

```bash
.venv/bin/python3 scripts/sync_vocab_registry.py
```

### Workflow for Adding a New Chapter

1. Add new words to `vocab_registry.json` (check the registry for words that already exist)
2. Create the chapter (see "Adding a New Chapter"), use `vocab_from_registry([...keys...])`
3. Run `sync_vocab_registry.py` — key validation

## When to Update CLAUDE.md

Update this file when:

- Adding new chapters — update the chapter list and content description
- Changing project structure — new folders, files, scripts
- Changing dependencies — new packages, version changes
- Refactoring — if the helper API changes (jp(), cell(), section_header(), etc.)
- Changing fonts or styling
- Changing the build or deploy process
