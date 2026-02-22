from ...styles import *


def build():
    story = []

    story.append(PageBreak())
    story.append(Paragraph(jp("3.12  Adverbs and Sentence-ending Particles"), title_s))
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

    story.append(section_header("Vocabulary"))
    story.append(Spacer(1, 1 * mm))
    story.append(
        vocab_two_col(
            vocab_from_registry(
                [
                    "早い",
                    "自分",
                    "たくさん",
                    "最近",
                    "全然",
                    "声",
                    "結構",
                    "大きい",
                    "この",
                    "町",
                    "変わる",
                    "中",
                    "天気",
                    "そう",
                    "時間",
                    "大丈夫",
                    "雨",
                    "降る",
                ]
            )
        )
    )
    story.append(Spacer(1, 3.5 * mm))

    # --- Grammar: Adjective → Adverb ---
    story.append(section_header("Grammar: Adjective → Adverb"))
    story.append(Spacer(1, 1 * mm))

    adv = [
        ["Type", "Rule", "Example"],
        [
            "i-adjective",
            "Replace い with く",
            "早い → 早く  (fast → quickly/early)",
        ],
        [
            "na-adjective",
            "Attach target particle に",
            "きれい → きれいに  (pretty → cleanly)",
        ],
    ]
    arows = [
        [cell(c, bold=(ri == 0), center=(ri == 0 or ci == 0), sz=8) for ci, c in enumerate(row)]
        for ri, row in enumerate(adv)
    ]
    hw = (W - 28 * mm) / 2
    at = Table(arows, colWidths=[28 * mm, hw, hw])
    at.setStyle(
        TableStyle(
            TABLE_STYLE
            + [
                ("BACKGROUND", (0, 1), (0, -1), CR1),
                ("FONTNAME", (0, 1), (0, -1), "DV-B"),
            ]
        )
    )
    story.append(at)
    story.append(Spacer(1, 3.5 * mm))

    # --- Grammar: Sentence-ending Particles ---
    story.append(section_header(jp("Grammar: Sentence-ending Particles  （ね、よ、よね）")))
    story.append(Spacer(1, 1 * mm))

    particles = [
        ["Particle", "Function", "Example"],
        [
            "ね",
            'Seeks agreement from listener.\nLike "right?", "isn\'t it?", "huh?".',
            "いい天気だね。\nGood weather, huh?\nおもしろい映画だったね。\nThat was an interesting movie, wasn't it?",
        ],
        [
            "よ",
            'Informs listener of something new.\nLike "you know", "I tell you".',
            "時間がないよ。\nYou know, there is no time.\n大丈夫だよ。\nIt's ok, you know.",
        ],
        [
            "よね",
            "Combines both: informs + seeks agreement.\nOrder is always よね (never ねよ).",
            "魚が好きなんだよね。\nYou like fish, dontcha?\n今日はいい天気だよね。\nToday is good weather, you know?",
        ],
    ]
    prows = [
        [cell(c, bold=(ri == 0), center=(ri == 0 or ci == 0), sz=8) for ci, c in enumerate(row)]
        for ri, row in enumerate(particles)
    ]
    col_p = [19 * mm, 55 * mm, W - 74 * mm]
    pt = Table(prows, colWidths=col_p, repeatRows=1)
    pt.setStyle(
        TableStyle(
            TABLE_STYLE
            + [
                ("BACKGROUND", (0, 1), (0, -1), CR1),
                ("FONTNAME", (0, 1), (0, -1), "DV-B"),
            ]
        )
    )
    story.append(pt)
    story.append(Spacer(1, 3.5 * mm))

    # --- Notes ---
    story.append(section_header("Notes"))
    story.append(Spacer(1, 1 * mm))
    for n in [
        jp(
            "早く can mean 'quickly' or 'early' depending on context: 早く走った (ran quickly) vs 早く食べた (ate early)."
        ),
        jp(
            "Not all adverbs come from adjectives. 全然 and たくさん are adverbs on their own — no conjugation needed."
        ),
        jp("Adverbs must come before the verb they modify, but otherwise word order is flexible."),
        jp("ね seeks agreement; よ informs. When combined, order must be よね — never ねよ."),
        jp("Males tend to say そうだね instead of そうね."),
    ]:
        story.append(Paragraph(f"- {n}", note_s))

    return story
