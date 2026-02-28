from ...styles import *


def build():
    story = []

    story.append(PageBreak())
    story.append(Paragraph(jp("3.7  Past Tense  （過去形）"), title_s))
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

    story.append(
        section(
            "Vocabulary",
            vocab_two_col(
                vocab_from_registry(
                    [
                        "捨てる",
                        "ご飯",
                        "映画",
                        "全ぶ",
                        "書く",
                        "持つ",
                        "行く",
                        "走る",
                        "勉強",
                    ]
                )
            ),
        )
    )
    story.append(Spacer(1, 3.5 * mm))

    past_rules = [
        ["Type", "Rule", "Example"],
        ["ru-verb", "Drop る, add た", "食べる → 食べた"],
        ["u-verb  す", "す → した", "話す → 話した"],
        ["u-verb  く", "く → いた", "書く → 書いた"],
        ["u-verb  ぐ", "ぐ → いだ", "泳ぐ → 泳いだ"],
        ["u-verb  む ぬ ぶ", "む/ぬ/ぶ → んだ", "飲む→飲んだ、死ぬ→死んだ、遊ぶ→遊んだ"],
        ["u-verb  る つ う", "る/つ/う → った", "切る→切った、持つ→持った、買う→買った"],
        ["する", "Exception → した", "する → した"],
        ["くる", "Exception → きた", "来る → きた"],
        ["行く", "Exception → 行った  (not 行いた)", "行く → 行った"],
    ]
    prrows = [
        [cell(c, bold=(ri == 0), center=(ri == 0 or ci == 0), sz=8) for ci, c in enumerate(row)]
        for ri, row in enumerate(past_rules)
    ]
    col_pr = [30 * mm, 42 * mm, W - 72 * mm]
    prt = Table(prrows, colWidths=col_pr)
    prt.setStyle(
        TableStyle(
            TABLE_STYLE
            + [
                ("BACKGROUND", (0, 1), (0, -1), CR1),
                ("FONTNAME", (0, 1), (0, -1), "DV-B"),
            ]
        )
    )
    story.append(section("Grammar: Past Tense Conjugation Rules", prt))
    story.append(Spacer(1, 3.5 * mm))

    pastneg = [
        ["Rule", "Examples"],
        [
            "Take the negative form, drop い from ない, add かった",
            "食べない → 食べなかった\n行かない → 行かなかった\nしない → しなかった\nない → なかった",
        ],
    ]
    pnrows = [
        [cell(c, bold=(ri == 0), center=(ri == 0 and ci == 0), sz=8) for ci, c in enumerate(row)]
        for ri, row in enumerate(pastneg)
    ]
    col_pn = [65 * mm, W - 65 * mm]
    pnt = Table(pnrows, colWidths=col_pn)
    pnt.setStyle(TableStyle(TABLE_STYLE))
    story.append(section("Past-Negative Tense  (all verb types)", pnt))
    story.append(Spacer(1, 3.5 * mm))

    final_notes: list = [Spacer(1, 1 * mm)]
    for n in [
        jp("Past-negative works the same for ALL verbs: negative form → drop い → add かった."),
        jp("行く is a regular u-verb in all conjugations except past tense (行った, not 行いた)."),
        jp("ある in past-negative: ない → なかった (there was no...)."),
    ]:
        final_notes.append(Paragraph(f"- {n}", note_s))
    story.append(section("Notes", *final_notes))

    return story
