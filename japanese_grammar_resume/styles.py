import json
import os

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    KeepTogether,
    PageBreak,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

pdfmetrics.registerFont(TTFont("DV", "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"))
pdfmetrics.registerFont(TTFont("DV-B", "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"))
pdfmetrics.registerFont(TTFont("JP", os.path.join(BASE_DIR, "fonts", "NotoSansJP-Light.ttf")))


def jp(text):
    """Inline-switch to JP font for CJK characters, DV for everything else."""
    result, buf, in_jp = [], [], False
    for ch in text:
        is_jp = ("\u3000" <= ch <= "\u9fff") or ("\uff00" <= ch <= "\uffef")
        if is_jp != in_jp:
            if buf:
                chunk = "".join(buf)
                result.append(f'<font name="JP">{chunk}</font>' if in_jp else chunk)
            buf, in_jp = [ch], is_jp
        else:
            buf.append(ch)
    if buf:
        chunk = "".join(buf)
        result.append(f'<font name="JP">{chunk}</font>' if in_jp else chunk)
    return "".join(result)


# Greyscale palette
CK = colors.HexColor("#1A1A1A")  # near-black
CD = colors.HexColor("#6A6A6A")  # medium grey (header bg)
CM = colors.HexColor("#888888")  # mid grey
CL = colors.HexColor("#D8D8D8")  # light grey (grid)
CR1 = colors.HexColor("#F4F4F4")  # row alt 1
CR2 = colors.white
CW = colors.white

W = A4[0] - 30 * mm


def S(name, **kw):
    return ParagraphStyle(name, **kw)


title_s = S("title", fontSize=14, textColor=CK, spaceAfter=2 * mm, leading=18, fontName="DV-B")
section_s = S("sec", fontSize=8, textColor=CW, leading=10, fontName="DV-B")
note_s = S("note", fontSize=8, leading=11.5, leftIndent=3 * mm, textColor=CD)


def cell(text, bold=False, sz=8.5, col=CK, center=False):
    fn = "DV-B" if bold else "DV"
    aln = 1 if center else 0
    return Paragraph(
        jp(text.replace("\n", "<br/>")),
        S(f"x{abs(hash(text))}", fontName=fn, fontSize=sz, leading=sz * 1.4, textColor=col, alignment=aln),
    )


def section_header(text):
    t = Table(
        [[Paragraph(jp(text), section_s)]],
        colWidths=[W],
        style=TableStyle(
            [
                ("BACKGROUND", (0, 0), (0, 0), CD),
                ("TOPPADDING", (0, 0), (0, 0), 3),
                ("BOTTOMPADDING", (0, 0), (0, 0), 3),
                ("LEFTPADDING", (0, 0), (0, 0), 6),
            ]
        ),
    )
    return t


TABLE_STYLE = [
    ("BACKGROUND", (0, 0), (-1, 0), CD),
    ("TEXTCOLOR", (0, 0), (-1, 0), CW),
    ("ROWBACKGROUNDS", (0, 1), (-1, -1), [CR1, CR2]),
    ("GRID", (0, 0), (-1, -1), 0.4, CL),
    ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ("TOPPADDING", (0, 0), (-1, -1), 3),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
    ("LEFTPADDING", (0, 0), (-1, -1), 5),
    ("RIGHTPADDING", (0, 0), (-1, -1), 4),
]


def kanji_cell(pairs):
    """Render a word as a 2×N table from list of (furigana, char) pairs.
    furigana='' means no reading above that character."""
    FURI_SZ, FURI_LD = 6, 7
    CHAR_SZ, CHAR_LD = 11, 13

    # pure-kana: all furigana empty → single-row simple paragraph
    if all(f == "" for f, _ in pairs):
        word = "".join(ch for _, ch in pairs)
        return Paragraph(
            jp(word), S(f"kc{abs(hash(word))}", fontName="JP", fontSize=CHAR_SZ, leading=CHAR_LD)
        )

    top_row, bot_row, col_w = [], [], []
    for furi, ch in pairs:
        furi_w = pdfmetrics.stringWidth(furi, "JP", FURI_SZ) if furi else 0
        char_w = pdfmetrics.stringWidth(ch, "JP", CHAR_SZ)
        cw = max(furi_w, char_w)
        col_w.append(cw)
        top_row.append(
            Paragraph(
                jp(furi),
                S(f"ft{abs(hash(furi + ch))}", fontName="JP", fontSize=FURI_SZ, leading=FURI_LD, alignment=1),
            )
        )
        bot_row.append(
            Paragraph(
                jp(ch), S(f"fb{abs(hash(ch))}", fontName="JP", fontSize=CHAR_SZ, leading=CHAR_LD, alignment=1)
            )
        )

    return Table(
        [top_row, bot_row],
        colWidths=col_w,
        rowHeights=[FURI_LD, CHAR_LD],
        style=TableStyle(
            [
                ("ALIGN", (0, 0), (-1, -1), "CENTER"),
                ("VALIGN", (0, 0), (-1, -1), "BOTTOM"),
                ("TOPPADDING", (0, 0), (-1, -1), 0),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
                ("LEFTPADDING", (0, 0), (-1, -1), 0),
                ("RIGHTPADDING", (0, 0), (-1, -1), 0),
            ]
        ),
    )


def vocab_two_col(vocab_list):
    """Split vocab into two side-by-side tables of equal row count."""
    half = (len(vocab_list) + 1) // 2
    left = vocab_list[:half]
    right = vocab_list[half:]

    GAP = 2 * mm
    WC = (W - GAP) / 2  # width of each sub-table
    ww = 36 * mm  # word col width
    mw = WC - ww  # meaning col width

    ts = TableStyle(TABLE_STYLE + [("VALIGN", (0, 1), (-1, -1), "MIDDLE")])

    FURI_LD = 7  # furigana row leading
    CHAR_LD = 13  # character row leading
    CELL_PAD_V = 3  # top + bottom padding per side (pt)
    ROW_H = (FURI_LD + CHAR_LD + 2 * CELL_PAD_V) / 72 * 25.4 * mm
    HEADER_H = 6 * mm

    def build(items, pad_to):
        rows = [[cell("Word", bold=True, center=True), cell("Meaning", bold=True, center=True)]]
        for pairs, meaning in items:
            rows.append([kanji_cell(pairs), cell(meaning, sz=8)])
        while len(rows) - 1 < pad_to:
            rows.append([Paragraph("", note_s), Paragraph("", note_s)])
        heights = [HEADER_H] + [ROW_H] * (len(rows) - 1)
        t = Table(rows, colWidths=[ww, mw], rowHeights=heights, repeatRows=1)
        t.setStyle(ts)
        return t

    tl = build(left, half)
    tr = build(right, half)
    outer = Table(
        [[tl, "", tr]],
        colWidths=[WC, GAP, WC],
        style=TableStyle(
            [
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 0),
                ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                ("TOPPADDING", (0, 0), (-1, -1), 0),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
            ]
        ),
    )
    return outer


_registry_cache = None


def vocab_from_registry(keys):
    """Load words from vocab_registry.json by keys, return list for vocab_two_col()."""
    global _registry_cache
    if _registry_cache is None:
        reg_path = os.path.join(os.path.dirname(__file__), "vocab_registry.json")
        with open(reg_path, encoding="utf-8") as f:
            _registry_cache = json.load(f)
    result = []
    for key in keys:
        entry = _registry_cache[key]
        pairs = [tuple(p) for p in entry["pairs"]]
        result.append((pairs, entry["meaning"]))
    return result
