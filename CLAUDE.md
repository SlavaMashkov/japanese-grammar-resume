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
  __main__.py                      — entry point: auto-discovers chapters, builds PDF
  styles.py                        — fonts, colors, styles, helpers (jp, cell, section, kanji_cell, vocab_two_col, vocab_from_registry, TABLE_STYLE)
  vocab_registry.json              — registry of unique words by chapter
  chapters/                        — one subdir per part, auto-discovered
    __init__.py
    ch01/                          — Part 1: Introduction
      __init__.py
      ch01_00_introduction.py
      ch01_01_problem.py
      ch01_02_japanese_guide.py
      ch01_03_suggestions.py
    ch02/                          — Part 2: The Writing System
      __init__.py
      ch02_00_writing_system.py
      ch02_01_scripts.py
      ch02_02_intonation.py
      ch02_03_hiragana.py
      ch02_04_katakana.py
      ch02_05_kanji.py
    ch03/                          — Part 3: Basic Grammar
      __init__.py
      ch03_00_basic_grammar.py
      ch03_01_basic_grammatical_structures.py
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
      ch03_12_adverbs.py
    ch04/                          — Part 4: Essential Grammar
      __init__.py
      ch04_00_essential_grammar.py
      ch04_01_polite_form.py
      ch04_02_addressing_people.py
      ch04_03_question_marker.py
      ch04_04_compound_sentences.py
      ch04_05_other_te_form.py
      ch04_06_potential_form.py
      ch04_07_ni_naru_suru.py
      ch04_08_conditionals.py
      ch04_09_must.py
      ch04_10_desire_suggestions.py
```

## Running

```bash
bash generate-pdf.sh
# or directly:
.venv/bin/python3 -m japanese_grammar_resume
# custom output directory:
bash generate-pdf.sh -o ~/Desktop
# custom output file:
bash generate-pdf.sh -o ~/Desktop/grammar.pdf
# overwrite existing file:
bash generate-pdf.sh -o ~/Desktop/grammar.pdf -w
```

Output: `output/japanese_summary.pdf` (default)

## Dependencies

- Python 3.12+ with venv
- reportlab>=4.0 (installed in .venv, declared in `pyproject.toml` and `requirements.txt`)
- ruff>=0.15 (dev dependency for linting/formatting)

## Code Quality

[ruff](https://docs.astral.sh/ruff/) is used for both linting and formatting. It runs automatically as part of `generate-pdf.sh` — code is formatted and checked before every PDF build. If the linter finds errors, the build stops.

To run manually:

```bash
.venv/bin/ruff format japanese_grammar_resume/ scripts/   # format
.venv/bin/ruff check japanese_grammar_resume/ scripts/    # lint
```

Configuration is in `pyproject.toml` under `[tool.ruff]`.

## Fonts

- **DV / DV-B** — DejaVuSans (system font, `/usr/share/fonts/truetype/dejavu/`)
- **JP** — NotoSansJP-Light (`fonts/NotoSansJP-Light.ttf`, weight 300) — Japanese text

The `jp()` function auto-detects CJK characters and switches the font accordingly.

## Adding a New Chapter

1. Create `japanese_grammar_resume/chapters/chXX/chXX_YY_name.py` with a `build()` function returning a `list` of story elements. If the part subdirectory doesn't exist yet, create it with an empty `__init__.py`.
2. Import `from ...styles import *` — all helpers and styles are available.
3. The first file (`ch01_00`) does not start with `PageBreak()`; all others do.
4. Chapters are auto-discovered — no manual imports needed in `__main__.py`.
5. **Always use `section()` with content** to prevent page breaks between a section header and its body. Pass tables and/or bullet lists as arguments:

```python
# Tables — pass directly:
story.append(section("Title", my_table))

# Content sections — rules as plain text, examples indented:
notes: list = [Spacer(1, 1 * mm)]
notes += [
    Paragraph(jp("Rule or explanation text."), note_s),
    Paragraph(jp("Example sentence. — Translation."), ex_s),
]
story.append(section("Title", *notes))

# Notes section (end of chapter) — keep bullet prefix:
notes: list = [Spacer(1, 1 * mm)]
for n in [jp("First point."), jp("Second point.")]:
    notes.append(Paragraph(f"- {n}", note_s))
story.append(section("Notes", *notes))

# Table + content together:
extra: list = [Spacer(1, 1 * mm)]
extra += [
    Paragraph(jp("Rule text."), note_s),
    Paragraph(jp("Example sentence. — Translation."), ex_s),
]
story.append(section("Title", my_table, *extra))
```

Never append `section()` without content and then append bullets separately — this causes the header and body to split across pages.

**Content section formatting:**
- **Rules/explanations** → `Paragraph(text, note_s)` — plain text, no bullet prefix
- **Example sentences** (Japanese + translation) → `Paragraph(text, ex_s)` — indented (8mm), no bullet
- **Notes section** (final section of each chapter) → `Paragraph(f"- {text}", note_s)` — keeps bullet prefix

**Important:** annotate mixed-flowable lists with `: list` (e.g. `notes: list = [Spacer(...)]`). Without the annotation, Pylance infers the type from the first element (`list[Spacer]`) and reports errors when appending `Paragraph`.

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

Each chapter's vocabulary section must contain only **new unique words** — words whose `chapter` field matches the current chapter. Do not include words that first appeared in earlier chapters.

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
- Refactoring — if the helper API changes (jp(), cell(), section(), etc.)
- Changing fonts or styling
- Changing the build or deploy process
