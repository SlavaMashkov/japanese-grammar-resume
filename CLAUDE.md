# Japanese Grammar Resume

PDF-резюме книги по японской грамматике (Tae Kim's Guide). Каждая глава добавляется к общему PDF.

## Структура проекта

```
create_summary.py   — основной скрипт генерации PDF (ReportLab)
generate-pdf.sh     — обёртка для запуска через bash
fonts/              — шрифты (NotoSansJP.ttf для японского текста)
output/             — сгенерированные PDF файлы
.venv/              — виртуальное окружение Python
```

## Запуск

```bash
bash generate-pdf.sh
# или напрямую:
.venv/bin/python3 create_summary.py
```

Результат: `output/japanese_summary.pdf`

## Зависимости

- Python 3.12+ с venv
- reportlab (установлен в .venv)

## Шрифты

- **DV / DV-B** — DejaVuSans (системный, `/usr/share/fonts/truetype/dejavu/`)
- **JP** — NotoSansJP-Light (`fonts/NotoSansJP-Light.ttf`, вес 300) — японский текст

Функция `jp()` автоматически определяет CJK-символы и переключает шрифт.

## Добавление новой главы

Новый контент добавляется в конец массива `story` в `create_summary.py` перед вызовом `doc.build(story)`. Каждая глава начинается с `PageBreak()` и заголовка через `title_s` стиль.

## Когда обновлять CLAUDE.md

Обновляй этот файл при:
- Добавлении новых глав — обнови список глав и описание контента
- Изменении структуры проекта — новые папки, файлы, скрипты
- Изменении зависимостей — новые пакеты, смена версий
- Рефакторинге — если меняется API хелперов (jp(), cell(), section_header() и т.д.)
- Изменении шрифтов или стилей оформления
- Изменении процесса сборки или деплоя
