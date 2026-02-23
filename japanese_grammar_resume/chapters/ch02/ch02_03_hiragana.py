from ...styles import *


def build():
    story = []

    story.append(PageBreak())
    story.append(Paragraph(jp("2.3  Hiragana  （ひらがな）"), title_s))
    story.append(
        Table(
            [[""]],
            colWidths=[W],
            rowHeights=[1.5],
            style=TableStyle(
                [
                    ("BACKGROUND", (0, 0), (0, 0), CD),
                    ("TOPPADDING", (0, 0), (-1, -1), 0),
                    ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
                ]
            ),
        )
    )
    story.append(Spacer(1, 3 * mm))

    # --- Basic Kana ---
    lw = 14 * mm
    kw = (W - lw) / 5

    hira = [
        ["", "a", "i", "u", "e", "o"],
        ["", "あ", "い", "う", "え", "お"],
        ["k", "か", "き", "く", "け", "こ"],
        ["s", "さ", "し", "す", "せ", "そ"],
        ["t", "た", "ち", "つ", "て", "と"],
        ["n", "な", "に", "ぬ", "ね", "の"],
        ["h", "は", "ひ", "ふ", "へ", "ほ"],
        ["m", "ま", "み", "む", "め", "も"],
        ["y", "や", "", "ゆ", "", "よ"],
        ["r", "ら", "り", "る", "れ", "ろ"],
        ["w", "わ", "", "", "", "を"],
        ["", "ん", "", "", "", ""],
    ]
    hira_rows = [
        [
            cell(c, bold=(ri == 0), center=True, sz=(8 if ri == 0 or ci == 0 else 8))
            for ci, c in enumerate(row)
        ]
        for ri, row in enumerate(hira)
    ]
    hira_t = Table(hira_rows, colWidths=[lw, kw, kw, kw, kw, kw])
    hira_t.setStyle(
        TableStyle(
            TABLE_STYLE
            + [
                ("BACKGROUND", (0, 1), (0, -1), CR1),
                ("FONTNAME", (0, 1), (0, -1), "DV-B"),
            ]
        )
    )
    story.append(section("Basic Kana", hira_t))
    story.append(Spacer(1, 3.5 * mm))

    # --- Voiced Sounds (Dakuten / Handakuten) ---
    voiced = [
        ["", "a", "i", "u", "e", "o"],
        ["g", "が", "ぎ", "ぐ", "げ", "ご"],
        ["z", "ざ", "じ", "ず", "ぜ", "ぞ"],
        ["d", "だ", "ぢ", "づ", "で", "ど"],
        ["b", "ば", "び", "ぶ", "べ", "ぼ"],
        ["p", "ぱ", "ぴ", "ぷ", "ぺ", "ぽ"],
    ]
    voiced_rows = [
        [
            cell(c, bold=(ri == 0), center=True, sz=(8 if ri == 0 or ci == 0 else 8))
            for ci, c in enumerate(row)
        ]
        for ri, row in enumerate(voiced)
    ]
    voiced_t = Table(voiced_rows, colWidths=[lw, kw, kw, kw, kw, kw])
    voiced_t.setStyle(
        TableStyle(
            TABLE_STYLE
            + [
                ("BACKGROUND", (0, 1), (0, -1), CR1),
                ("FONTNAME", (0, 1), (0, -1), "DV-B"),
            ]
        )
    )
    story.append(section(jp("Voiced Sounds  （濁点 ゛・半濁点 ゜）"), voiced_t))
    story.append(Spacer(1, 3.5 * mm))

    # --- Combinations (Small や、ゆ、よ) ---
    clw = 14 * mm
    ckw = (W - clw) / 3

    combo = [
        ["", "ya", "yu", "yo"],
        ["k", "きゃ", "きゅ", "きょ"],
        ["s", "しゃ", "しゅ", "しょ"],
        ["c", "ちゃ", "ちゅ", "ちょ"],
        ["n", "にゃ", "にゅ", "にょ"],
        ["h", "ひゃ", "ひゅ", "ひょ"],
        ["m", "みゃ", "みゅ", "みょ"],
        ["r", "りゃ", "りゅ", "りょ"],
        ["g", "ぎゃ", "ぎゅ", "ぎょ"],
        ["j", "じゃ", "じゅ", "じょ"],
        ["b", "びゃ", "びゅ", "びょ"],
        ["p", "ぴゃ", "ぴゅ", "ぴょ"],
    ]
    combo_rows = [
        [
            cell(c, bold=(ri == 0), center=True, sz=(8 if ri == 0 or ci == 0 else 8))
            for ci, c in enumerate(row)
        ]
        for ri, row in enumerate(combo)
    ]
    combo_t = Table(combo_rows, colWidths=[clw, ckw, ckw, ckw])
    combo_t.setStyle(
        TableStyle(
            TABLE_STYLE
            + [
                ("BACKGROUND", (0, 1), (0, -1), CR1),
                ("FONTNAME", (0, 1), (0, -1), "DV-B"),
            ]
        )
    )
    story.append(section(jp("Combinations  （拗音 — 小さい や・ゆ・よ）"), combo_t))
    story.append(Spacer(1, 3.5 * mm))

    # --- Notes ---
    final_notes: list = [Spacer(1, 1 * mm)]
    for n in [
        jp("Pronunciation exceptions: し = shi, ち = chi, つ = tsu, ふ = fu, を = o (as particle)."),
        jp("Dakuten (゛) voices the consonant: k→g, s→z, t→d, h→b. Handakuten (゜): h→p."),
        jp("ぢ = じ (both /ji/). づ is pronounced /dzu/."),
        jp("Small っ (double consonant): doubles the next consonant sound. がっき = gakki, はっぱ = happa."),
        jp(
            "Long vowels: /a/ → +あ, /i/ & /e/ → +い, /u/ & /o/ → +う."
            " Rare exceptions use え or お: おねえさん, おおきい."
        ),
        jp("The /r/ sound is a tap — tongue flicks the roof of the mouth. Not English r or l."),
        "Stroke order and direction matter — learn them correctly from the start.",
    ]:
        final_notes.append(Paragraph(f"- {n}", note_s))
    story.append(section("Notes", *final_notes))

    return story
