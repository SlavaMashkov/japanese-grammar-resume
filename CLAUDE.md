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
japanese_grammar_resume/           — Python-пакет
  __init__.py
  __main__.py                      — точка входа: импорт глав, сборка PDF
  styles.py                        — шрифты, цвета, стили, хелперы (jp, cell, section_header, kanji_cell, vocab_two_col, TABLE_STYLE)
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

## Когда обновлять CLAUDE.md

Обновляй этот файл при:
- Добавлении новых глав — обнови список глав и описание контента
- Изменении структуры проекта — новые папки, файлы, скрипты
- Изменении зависимостей — новые пакеты, смена версий
- Рефакторинге — если меняется API хелперов (jp(), cell(), section_header() и т.д.)
- Изменении шрифтов или стилей оформления
- Изменении процесса сборки или деплоя
