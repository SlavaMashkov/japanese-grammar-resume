from ...styles import *


def build():
    story = []

    story.append(PageBreak())
    story.append(Paragraph(jp("3.2  Expressing State-of-Being  (状態の表現)"), title_s))
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

    # --- Vocabulary ---
    story.append(
        section(
            "Vocabulary",
            vocab_two_col(
                vocab_from_registry(
                    [
                        "人",
                        "学生",
                        "元気",
                        "友達",
                        "明日",
                        "今日",
                        "試験",
                        "うん",
                        "ううん",
                    ]
                )
            ),
        )
    )
    story.append(Spacer(1, 3.5 * mm))

    # --- Conjugation Table ---
    gram = [
        ["", "Affirmative (+)", "Negative (-)"],
        [
            "Non-Past",
            "Noun / na-adj. + だ\n  \u300c学生だ\u300d  Is a student\n  \u300c元気（だ）\u300d  Is well",
            "Noun / na-adj. + じゃない\n"
            "  \u300c学生じゃない\u300d  Is not a student\n"
            "  \u300c友達じゃない\u300d  Is not a friend",
        ],
        [
            "Past",
            "Noun / na-adj. + だった\n"
            "  \u300c学生だった\u300d  Was a student\n"
            "  \u300c友達だった\u300d  Was a friend",
            "じゃない  ->  じゃなかった\n"
            "(drop い, add かった)\n"
            "  \u300c学生じゃなかった\u300d  Was not a student\n"
            "  \u300c友達じゃなかった\u300d  Was not a friend",
        ],
    ]

    grows = []
    for ri, row in enumerate(gram):
        grows.append([cell(c, bold=(ri == 0), center=(ri == 0 or ci == 0), sz=8) for ci, c in enumerate(row)])

    hw = (W - 22 * mm) / 2
    gt = Table(grows, colWidths=[22 * mm, hw, hw], repeatRows=1)
    gt.setStyle(
        TableStyle(
            TABLE_STYLE
            + [
                ("BACKGROUND", (0, 1), (0, -1), CR1),
                ("FONTNAME", (0, 1), (0, -1), "DV-B"),
            ]
        )
    )
    story.append(section("Grammar: State-of-Being Conjugation", gt))
    story.append(Spacer(1, 3.5 * mm))

    # --- Notes ---
    final_notes: list = [Spacer(1, 1 * mm)]
    for n in [
        jp("「だ」 makes the statement emphatic and declarative. More commonly used by men."),
        jp("Without 「だ」, state-of-being is still implied from context (very common in casual speech)."),
        jp("Negative and past forms are NOT declarative on their own — 「だ」 can be added separately."),
        jp("Casual greeting:  元気？ — 元気。  (Are you well? — I'm well.)"),
    ]:
        final_notes.append(Paragraph(f"- {n}", note_s))
    story.append(section("Notes", *final_notes))

    return story
