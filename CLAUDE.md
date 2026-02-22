# Japanese Grammar Resume

PDF-резюме книги по японской грамматике (Tae Kim's Guide). Каждая глава добавляется к общему PDF.

## Структура проекта

```
pyproject.toml                     — метаданные проекта, зависимости
requirements.txt                   — зависимости для pip install -r
generate-pdf.sh                    — обёртка для запуска через bash
fonts/                             — шрифты (NotoSansJP-Light.ttf для японского текста)
output/                            — сгенерированные PDF файлы
.venv/                             — виртуальное окружение Python
scripts/
  sync_vocab_registry.py           — валидация vocab_registry.json (проверка ключей из глав)
japanese_grammar_resume/           — Python-пакет
  __init__.py
  __main__.py                      — точка входа: импорт глав, сборка PDF
  styles.py                        — шрифты, цвета, стили, хелперы (jp, cell, section_header, kanji_cell, vocab_two_col, vocab_from_registry, TABLE_STYLE)
  vocab_registry.json              — реестр уникальных слов по главам
  chapters/                        — по одному файлу на главу, каждый экспортирует build() → list
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

## Запуск

```bash
bash generate-pdf.sh
# или напрямую:
.venv/bin/python3 -m japanese_grammar_resume
```

Результат: `output/japanese_summary.pdf`

## Зависимости

- Python 3.12+ с venv
- reportlab>=4.0 (установлен в .venv, описан в `pyproject.toml` и `requirements.txt`)

## Шрифты

- **DV / DV-B** — DejaVuSans (системный, `/usr/share/fonts/truetype/dejavu/`)
- **JP** — NotoSansJP-Light (`fonts/NotoSansJP-Light.ttf`, вес 300) — японский текст

Функция `jp()` автоматически определяет CJK-символы и переключает шрифт.

## Добавление новой главы

1. Создать файл `japanese_grammar_resume/chapters/ch03_XX_name.py` с функцией `build()`, возвращающей `list` элементов story.
2. Импортировать `from ..styles import *` — все хелперы и стили доступны.
3. Первая глава (3.2) не начинается с `PageBreak()`, все остальные — начинаются.
4. Добавить импорт и вызов `build()` в `japanese_grammar_resume/__main__.py`.

## Vocab Registry

Файл `japanese_grammar_resume/vocab_registry.json` — единственный источник данных о словах. Ключ — написание слова (кандзи или кана), значение — `{ pairs, meaning, chapter }`:

```json
{
  "学生": {
    "pairs": [["がく", "学"], ["せい", "生"]],
    "meaning": "student",
    "chapter": "ch03_02"
  }
}
```

- `pairs` — матрица `[[furigana, char], ...]` для рендеринга через `kanji_cell()`
- `meaning` — перевод слова
- `chapter` — глава первого появления

Главы ссылаются на слова по ключу через хелпер `vocab_from_registry()`:

```python
story.append(vocab_two_col(vocab_from_registry([
    "人", "学生", "元気", "友達",
])))
```

Скрипт `scripts/sync_vocab_registry.py` валидирует реестр — проверяет, что все ключи из глав существуют в JSON.

```bash
.venv/bin/python3 scripts/sync_vocab_registry.py
```

### Workflow при добавлении новой главы

1. Добавить новые слова в `vocab_registry.json` (проверить по реестру, какие слова уже были)
2. Создать главу (см. «Добавление новой главы»), использовать `vocab_from_registry([...ключи...])`
3. Запустить `sync_vocab_registry.py` — валидация ключей

## Когда обновлять CLAUDE.md

Обновляй этот файл при:
- Добавлении новых глав — обнови список глав и описание контента
- Изменении структуры проекта — новые папки, файлы, скрипты
- Изменении зависимостей — новые пакеты, смена версий
- Рефакторинге — если меняется API хелперов (jp(), cell(), section_header() и т.д.)
- Изменении шрифтов или стилей оформления
- Изменении процесса сборки или деплоя
