from ...styles import *


def build():
    story = []

    story.append(PageBreak())
    story.append(
        Paragraph(
            jp("4.8  Conditionals  （と、なら、ば、たら）"),
            title_s,
        )
    )
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
    story.append(section("Vocabulary"))
    story.append(Spacer(1, 1 * mm))
    story.append(
        vocab_two_col(
            vocab_from_registry(
                [
                    "ボール",
                    "暗い",
                    "太る",
                    "きっと",
                    "問題",
                    "あそこ",
                    "おかしい",
                    "楽しい",
                    "病気",
                    "自動",
                    "割引",
                    "家",
                    "アメリカ",
                    "もし",
                    "観る",
                ]
            )
        )
    )
    story.append(Spacer(1, 3.5 * mm))

    # --- Summary of Four Conditionals ---
    sum_data = [
        ["Form", "Formation", "Usage"],
        [
            jp("と"),
            jp("[Condition] + と + [Result]\nState-of-being: だと"),
            jp("Natural consequence\n(always happens)"),
        ],
        [
            jp("なら"),
            jp("[Context] + なら + [Result]\nNo だ before なら"),
            jp("Contextual\n(if that's the case)"),
        ],
        [
            jp("ば"),
            jp("Verb: /u/→/e/ + ば\ni-adj: い→ければ\nNoun: であれば"),
            jp('General "if"\n(focuses on condition)'),
        ],
        [
            jp("たら"),
            jp("Past tense + ら\n(た→たら, だ→だら)"),
            jp('General "if"\n(focuses on result)'),
        ],
    ]
    sum_rows = [
        [cell(c, bold=(ri == 0), center=(ri == 0 or ci == 0), sz=8) for ci, c in enumerate(row)]
        for ri, row in enumerate(sum_data)
    ]
    sw = (W - 18 * mm) / 2
    sum_t = Table(sum_rows, colWidths=[18 * mm, sw, sw])
    sum_t.setStyle(
        TableStyle(
            TABLE_STYLE
            + [
                ("BACKGROUND", (0, 1), (0, -1), CR1),
                ("FONTNAME", (0, 1), (0, -1), "DV-B"),
            ]
        )
    )
    story.append(section(jp('Four Ways to Say "If"'), sum_t))
    story.append(Spacer(1, 3.5 * mm))

    # --- と — Natural Consequence ---
    to_notes: list = [Spacer(1, 1 * mm)]
    to_notes += [
        Paragraph(
            jp("If [X] happens, [Y] will happen as a natural consequence. No question about it."),
            note_s,
        ),
        Paragraph(jp("For state-of-being (nouns/na-adj), use だと explicitly."), note_s),
        Paragraph(jp("ボールを落すと落ちる。 — If you drop the ball, it will fall."), ex_s),
        Paragraph(jp("電気を消すと暗くなる。 — If you turn off the lights, it will get dark."), ex_s),
        Paragraph(
            jp(
                "学校に行かないと友達と会えないよ。 — If you don't go to school, you can't meet your friends."
            ),
            ex_s,
        ),
        Paragraph(jp("たくさん食べると太るよ。 — If you eat a lot, you will get fat."), ex_s),
        Paragraph(
            jp("先生だと、きっと年上なんじゃないですか？ — If he's a teacher, he must be older, right?"),
            ex_s,
        ),
    ]
    story.append(section(jp("と — Natural Consequence"), *to_notes))
    story.append(Spacer(1, 3.5 * mm))

    # --- なら — Contextual Conditional ---
    nara_notes: list = [Spacer(1, 1 * mm)]
    nara_notes += [
        Paragraph(
            jp('Expresses what will happen given a certain context. "If that\'s the case, then..."'),
            note_s,
        ),
        Paragraph(jp("Do not attach だ before なら. ならば is more formal."), note_s),
        Paragraph(
            jp("みんなが行くなら私も行く。 — If everybody is going, then I'll go too."),
            ex_s,
        ),
        Paragraph(
            jp("アリスさんが言うなら問題ないよ。 — If Alice-san says so, there's no problem."),
            ex_s,
        ),
        Paragraph(
            jp("A：図書館はどこですか。 — Where is the library?"),
            ex_s,
        ),
        Paragraph(
            jp("B：図書館なら、あそこです。 — If you're talking about the library, it's over there."),
            ex_s,
        ),
    ]
    story.append(section(jp("なら — Contextual Conditional"), *nara_notes))
    story.append(Spacer(1, 3.5 * mm))

    # --- ば — General Conditional ---
    ba_data = [
        ["Type", "Rule", "Example"],
        [
            "Verbs",
            jp("Change /u/ to /e/\nand attach ば"),
            jp("食べる → 食べれば\n待つ → 待てば"),
        ],
        [
            jp("i-adj / ない"),
            jp("Drop い,\nattach ければ"),
            jp("おかしい → おかしければ\nない → なければ"),
        ],
        [
            jp("Noun / na-adj"),
            jp("Attach であれば"),
            jp("学生 → 学生であれば\n暇 → 暇であれば"),
        ],
    ]
    ba_rows = [
        [cell(c, bold=(ri == 0), center=(ri == 0 or ci == 0), sz=8) for ci, c in enumerate(row)]
        for ri, row in enumerate(ba_data)
    ]
    bw = (W - 28 * mm) / 2
    ba_t = Table(ba_rows, colWidths=[28 * mm, bw, bw])
    ba_t.setStyle(
        TableStyle(
            TABLE_STYLE
            + [
                ("BACKGROUND", (0, 1), (0, -1), CR1),
                ("FONTNAME", (0, 1), (0, -1), "DV-B"),
            ]
        )
    )
    ba_notes: list = [Spacer(1, 1 * mm)]
    ba_notes += [
        Paragraph(jp('General "if" without assumptions. Focuses on the condition itself.'), note_s),
        Paragraph(
            jp("友達に会えれば、買い物に行きます。 — If I can meet with my friend, we will go shopping."),
            ex_s,
        ),
        Paragraph(jp("お金があればいいね。 — If I had money, it would be good, huh?"), ex_s),
        Paragraph(jp("楽しければ、私も行く。 — If it's fun, I'll go too."), ex_s),
        Paragraph(jp("楽しくなければ、私も行かない。 — If it's not fun, I'll also not go."), ex_s),
        Paragraph(jp("食べなければ病気になるよ。 — If you don't eat, you will become sick."), ex_s),
    ]
    story.append(section(jp("ば — General Conditional"), ba_t, *ba_notes))
    story.append(Spacer(1, 3.5 * mm))

    # --- たら — Past Conditional ---
    tara_notes: list = [Spacer(1, 1 * mm)]
    tara_notes += [
        Paragraph(
            jp(
                'Change to past tense and add ら. General "if" that focuses on the result, not the condition.'
            ),
            note_s,
        ),
        Paragraph(
            jp("自動 → 自動だったら, 待つ → 待ったら, 読む → 読んだら, 忙しい → 忙しかったら."),
            note_s,
        ),
        Paragraph(jp("暇だったら、遊びに行くよ。 — If I am free, I will go play."), ex_s),
        Paragraph(
            jp(
                "学生だったら、学生割引で買えます。 — If you're a student, you can buy with a student discount."
            ),
            ex_s,
        ),
        Paragraph(
            jp(
                "ば focuses on the condition; たら focuses on what happens after. たら often sounds more natural."
            ),
            note_s,
        ),
        Paragraph(
            jp("たら is the only conditional where the result can be in the past (expressing surprise)."),
            note_s,
        ),
        Paragraph(
            jp("家に帰ったら、誰もいなかった。 — When I went home, there was no one there."),
            ex_s,
        ),
        Paragraph(
            jp(
                "アメリカに行ったら、たくさん太りました。 — As a result of going to America, I got really fat."
            ),
            ex_s,
        ),
    ]
    story.append(section(jp("たら — Past Conditional"), *tara_notes))
    story.append(Spacer(1, 3.5 * mm))

    # --- もし — Adding Uncertainty ---
    moshi_notes: list = [Spacer(1, 1 * mm)]
    moshi_notes += [
        Paragraph(
            jp(
                "もし is a supplement that adds uncertainty. It must be paired with one of the four conditionals."
            ),
            note_s,
        ),
        Paragraph(
            jp("もしよかったら、映画を観に行きますか？ — If by any chance it's ok, go to watch a movie?"),
            ex_s,
        ),
        Paragraph(
            jp("もし時間がないなら、明日でもいいよ。 — If there's no time, tomorrow is fine as well."),
            ex_s,
        ),
    ]
    story.append(section(jp("もし — Adding Uncertainty"), *moshi_notes))
    story.append(Spacer(1, 3.5 * mm))

    # --- Notes ---
    final_notes: list = [Spacer(1, 1 * mm)]
    for n in [
        jp("と = natural consequence. State-of-being requires だと. Result is inevitable."),
        jp('なら = contextual ("if that\'s the case"). No だ before なら. ならば is more formal.'),
        jp('ば = general "if". Verbs: /u/→/e/+ば. i-adj: い→ければ. Noun: であれば. Focuses on condition.'),
        jp(
            'たら = past tense + ら. General "if" that focuses on result. Can express surprise at past outcome.'
        ),
        jp("もし adds uncertainty. Must be paired with a conditional (もし〜たら, もし〜なら, etc.)."),
    ]:
        final_notes.append(Paragraph(f"- {n}", note_s))
    story.append(section("Notes", *final_notes))

    return story
