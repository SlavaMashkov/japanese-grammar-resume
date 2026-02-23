from ...styles import *


def build():
    story = []

    story.append(PageBreak())
    story.append(Paragraph(jp("2.5  Kanji  （漢字）"), title_s))
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

    # --- 2.5.1 What is Kanji? ---
    story.append(section_header("What is Kanji?"))
    story.append(Spacer(1, 1 * mm))
    for n in [
        "Nouns, verb stems, adjective stems, and many adverbs are written in Kanji.",
        jp('Not all words use Kanji — some are always written in Hiragana (e.g. する, the verb "to do").'),
        "Learn Kanji alongside vocabulary from the start — spreading the load over time is far easier"
        " than cramming at an advanced level.",
    ]:
        story.append(Paragraph(f"- {n}", note_s))
    story.append(Spacer(1, 3.5 * mm))

    # --- 2.5.3 Reading Kanji ---
    readings = [
        ["Reading", "Origin", "When used", "Example"],
        [
            "音読み\n(on'yomi)",
            "Chinese reading",
            "In compound words (熟語)",
            "力 in 能力 → りょく",
        ],
        [
            "訓読み\n(kun'yomi)",
            "Japanese reading",
            "Standalone kanji,\nadjectives, verbs",
            "力 alone → ちから",
        ],
    ]
    read_rows = [
        [cell(c, bold=(ri == 0), center=(ri == 0 or ci == 0), sz=8) for ci, c in enumerate(row)]
        for ri, row in enumerate(readings)
    ]
    rw0 = 28 * mm
    rw1 = 30 * mm
    rw2 = (W - rw0 - rw1) / 2
    read_t = Table(read_rows, colWidths=[rw0, rw1, rw2, rw2])
    read_t.setStyle(
        TableStyle(
            TABLE_STYLE
            + [
                ("BACKGROUND", (0, 1), (0, -1), CR1),
                ("FONTNAME", (0, 1), (0, -1), "DV-B"),
            ]
        )
    )
    story.append(section_header(jp("Reading Kanji  （音読み・訓読み）"), read_t))
    story.append(Spacer(1, 3.5 * mm))

    # --- Sound Changes in Compounds ---
    changes = [
        ["Pattern", "Example"],
        ["/h/ → /b/ or /p/", "一本 (いっぽん)"],
        ["つ → っ (gemination)", "徹底 (てってい)"],
        ["Irregular reading", "格好 (かっこう)"],
    ]
    ch_rows = [
        [cell(c, bold=(ri == 0), center=(ri == 0), sz=8) for ci, c in enumerate(row)]
        for ri, row in enumerate(changes)
    ]
    chw = W / 2
    ch_t = Table(ch_rows, colWidths=[chw, chw])
    ch_t.setStyle(TableStyle(TABLE_STYLE))
    story.append(section_header("Sound Changes in Compounds", ch_t))
    story.append(Spacer(1, 3.5 * mm))

    # --- Notes ---
    story.append(section_header("Notes"))
    story.append(Spacer(1, 1 * mm))
    for n in [
        jp(
            "Okurigana (送り仮名): kana suffix attached to a kanji so the reading stays stable across"
            " conjugations. 食べる → 食べた (食 always reads た)."
        ),
        jp(
            "Some compounds have special readings unrelated to individual characters — memorize them."
            " 今日 = きょう, not こんにち."
        ),
        jp(
            "Different kanji, same reading, slight nuance: 聞く (to hear/listen) vs 聴く"
            " (to listen attentively) vs 訊く (to ask)."
        ),
        jp("々 repeats the previous kanji: 時々 (sometimes), 色々 (various), 人々 (people)."),
        jp(
            "Why Kanji? Japanese has too many homophones for kana alone — Kanji provides"
            " visual cues and removes ambiguity without needing spaces."
        ),
    ]:
        story.append(Paragraph(f"- {n}", note_s))

    return story
