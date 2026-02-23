from ...styles import *


def build():
    story = []

    story.append(PageBreak())
    story.append(Paragraph(jp("3.9  Transitive and Intransitive Verbs"), title_s))
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

    story.append(section("Vocabulary"))
    story.append(Spacer(1, 1 * mm))
    story.append(
        vocab_two_col(
            vocab_from_registry(
                [
                    "電気",
                    "窓",
                    "箱",
                    "落とす",
                    "落ちる",
                    "出す",
                    "入れる",
                    "入る",
                    "開ける",
                    "開く",
                    "閉める",
                    "閉まる",
                    "つける",
                    "つく",
                    "消す",
                    "消える",
                    "抜く",
                    "抜ける",
                ]
            )
        )
    )
    story.append(Spacer(1, 3.5 * mm))

    ti_intro = [
        ["", "Transitive", "Intransitive"],
        ["Agent", "Active agent performs action", "No direct agent — event just happens"],
        ["Particle", "を (direct object)", "が or は (subject of event)"],
        ["Example", "電気をつけた。\nTurned on the lights.", "電気がついた。\nThe lights turned on."],
    ]
    tirows = [
        [cell(c, bold=(ri == 0), center=(ri == 0 or ci == 0), sz=8) for ci, c in enumerate(row)]
        for ri, row in enumerate(ti_intro)
    ]
    hw_ti = (W - 28 * mm) / 2
    tit = Table(tirows, colWidths=[28 * mm, hw_ti, hw_ti])
    tit.setStyle(
        TableStyle(
            TABLE_STYLE
            + [
                ("BACKGROUND", (0, 1), (0, -1), CR1),
                ("FONTNAME", (0, 1), (0, -1), "DV-B"),
            ]
        )
    )
    story.append(section("Grammar: Transitive vs Intransitive", tit))
    story.append(Spacer(1, 3.5 * mm))

    pairs_data = [
        ["Transitive (を)", "Meaning", "Intransitive (が)", "Meaning"],
        ["落とす", "to drop", "落ちる", "to fall"],
        ["出す", "to take out", "出る", "to come out"],
        ["入れる", "to insert", "入る", "to enter"],
        ["開ける", "to open", "開く", "to be opened"],
        ["閉める", "to close", "閉まる", "to be closed"],
        ["つける", "to attach", "つく", "to be attached"],
        ["消す", "to erase", "消える", "to disappear"],
        ["抜く", "to extract", "抜ける", "to be extracted"],
    ]
    prows = [
        [cell(c, bold=(ri == 0), center=(ri == 0), sz=8) for ci, c in enumerate(row)]
        for ri, row in enumerate(pairs_data)
    ]
    hw_p = W / 4
    pt2 = Table(prows, colWidths=[hw_p] * 4)
    pt2.setStyle(TableStyle(TABLE_STYLE))
    story.append(section("Transitive / Intransitive Pairs", pt2))
    story.append(Spacer(1, 3.5 * mm))

    story.append(section("Notes"))
    story.append(Spacer(1, 1 * mm))
    for n in [
        jp("Intransitive verbs CANNOT take を. Use が or は instead: 電気がついた not 電気をついた."),
        jp("Exception: を can be used with intransitive motion verbs for traversed locations: 部屋を出た。"),
        "When unsure whether a verb is transitive or intransitive, check a dictionary (e.g. jisho.org).",
    ]:
        story.append(Paragraph(f"- {jp(n) if isinstance(n, str) else n}", note_s))

    return story
