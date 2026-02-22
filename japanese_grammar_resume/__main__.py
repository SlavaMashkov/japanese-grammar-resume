import argparse
import importlib
import re
from pathlib import Path

from .styles import *

CHAPTERS_DIR = Path(__file__).resolve().parent / "chapters"


def _discover_chapters() -> list:
    """Import all ch*/*.py modules under chapters/ and call build() in sorted order."""
    modules = []
    for part_dir in sorted(CHAPTERS_DIR.iterdir()):
        if not part_dir.is_dir() or not re.match(r"ch\d+", part_dir.name):
            continue
        for py_file in sorted(part_dir.glob("ch*.py")):
            module_name = f".chapters.{part_dir.name}.{py_file.stem}"
            modules.append(importlib.import_module(module_name, package="japanese_grammar_resume"))
    return modules


def main():
    parser = argparse.ArgumentParser(description="Generate Japanese grammar summary PDF")
    parser.add_argument(
        "-o",
        "--output-dir",
        default=os.path.join(BASE_DIR, "output"),
        help="Output directory (default: output/)",
    )
    args = parser.parse_args()

    output_path = os.path.join(args.output_dir, "japanese_summary.pdf")
    os.makedirs(args.output_dir, exist_ok=True)
    doc = SimpleDocTemplate(
        output_path,
        pagesize=A4,
        leftMargin=15 * mm,
        rightMargin=15 * mm,
        topMargin=12 * mm,
        bottomMargin=12 * mm,
        title="Japanese Grammar Guide — Chapter Summaries",
        subject="Japanese grammar notes: state-of-being, particles, adjectives",
        author="Claude (Anthropic)",
    )

    story = []
    for module in _discover_chapters():
        story += module.build()

    doc.build(story)
    print("Done:", output_path)


if __name__ == "__main__":
    main()
