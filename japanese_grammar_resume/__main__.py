import argparse
import importlib
import re
import sys
from pathlib import Path

from reportlab.platypus import Paragraph

from .styles import *

_RE_SUBCHAPTER = re.compile(r"^\d+\.\d+")

CHAPTERS_DIR = Path(__file__).resolve().parent / "chapters"


class BookmarkedDoc(SimpleDocTemplate):
    """SimpleDocTemplate subclass that auto-generates PDF bookmarks from chapter
    titles (level 0) and sub-chapter titles (level 1)."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._bm_seq = 0

    def afterFlowable(self, flowable):
        if not isinstance(flowable, Paragraph) or flowable.style.name != title_s.name:
            return
        key = f"bm{self._bm_seq}"
        self._bm_seq += 1
        text = re.sub(r"<[^>]+>", "", flowable.text)
        level = 1 if _RE_SUBCHAPTER.match(text) else 0
        self.canv.bookmarkPage(key)
        self.canv.addOutlineEntry(text, key, level=level, closed=False)


def _discover_chapters() -> list:
    """Import all ch*/*.py modules under chapters/ in sorted order and return them."""
    modules = []
    for part_dir in sorted(CHAPTERS_DIR.iterdir()):
        if not part_dir.is_dir():
            continue
        if not re.match(r"ch\d+", part_dir.name):
            if part_dir.name != "__pycache__":
                print(f"Warning: skipping non-chapter directory: {part_dir.name}", file=sys.stderr)
            continue
        for py_file in sorted(part_dir.glob("ch*.py")):
            module_name = f".chapters.{part_dir.name}.{py_file.stem}"
            try:
                mod = importlib.import_module(module_name, package="japanese_grammar_resume")
            except Exception as exc:
                raise ImportError(
                    f"Failed to import '{module_name}': {exc}\nCheck {py_file} for errors."
                ) from exc
            if not hasattr(mod, "build"):
                raise AttributeError(f"Module '{module_name}' has no build() function.")
            modules.append(mod)
    return modules


def main():
    parser = argparse.ArgumentParser(description="Generate Japanese grammar summary PDF")
    default_output = os.path.join(BASE_DIR, "output")
    parser.add_argument(
        "-o",
        "--output",
        default=default_output,
        help="Output file (.pdf) or directory (default: output/)",
    )
    parser.add_argument(
        "-w",
        "--overwrite",
        action="store_true",
        help="Overwrite output file if it already exists",
    )
    args = parser.parse_args()

    custom_output = args.output != default_output
    if args.output.endswith(".pdf"):
        output_path = args.output
    else:
        output_path = os.path.join(args.output, "japanese_summary.pdf")

    if custom_output and os.path.exists(output_path) and not args.overwrite:
        parser.error(f"file already exists: {output_path}\nUse -w to overwrite.")

    os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
    doc = BookmarkedDoc(
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
        try:
            story += module.build()
        except Exception as exc:
            raise RuntimeError(f"Error building '{module.__name__}': {exc}") from exc

    doc.build(story)
    print("Done:", output_path)


if __name__ == "__main__":
    main()
