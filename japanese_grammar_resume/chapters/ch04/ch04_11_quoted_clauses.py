from ...styles import *


def build():
    story = []

    story.append(PageBreak())
    story.append(
        Paragraph(
            jp("4.11  Performing an Action on a Relative Clause  （と、って）"),
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
    story.append(
        section(
            "Vocabulary",
            vocab_two_col(
                vocab_from_registry(
                    [
                        "叫ぶ",
                        "呼ぶ",
                        "呟く",
                        "寒い",
                        "高校生",
                        "智子",
                        "すごい",
                    ]
                )
            ),
        )
    )
    story.append(Spacer(1, 3.5 * mm))

    # --- Patterns Overview ---
    sum_data = [
        ["Pattern", "Meaning", "Example"],
        [
            jp("「quote」と + verb"),
            jp("direct quotation"),
            jp("「寒い」と言った"),
        ],
        [
            jp("[clause] と + verb"),
            jp("interpreted quote"),
            jp("授業がないと聞いた"),
        ],
        [
            jp("[clause] と思う"),
            jp("I think [clause]"),
            jp("食べようと思った"),
        ],
        [
            jp("noun/na-adj だと"),
            jp("state-of-being in quote"),
            jp("高校生だと聞いた"),
        ],
        [
            jp("って"),
            jp("casual と"),
            jp("時間がないって"),
        ],
    ]
    sum_rows = [
        [cell(c, bold=(ri == 0), center=(ri == 0 or ci == 0), sz=8) for ci, c in enumerate(row)]
        for ri, row in enumerate(sum_data)
    ]
    sw = (W - 42 * mm) / 2
    sum_t = Table(sum_rows, colWidths=[42 * mm, sw, sw])
    sum_t.setStyle(
        TableStyle(
            TABLE_STYLE
            + [
                ("BACKGROUND", (0, 1), (0, -1), CR1),
                ("FONTNAME", (0, 1), (0, -1), "DV-B"),
            ]
        )
    )
    story.append(section(jp("Patterns Overview"), sum_t))
    story.append(Spacer(1, 3.5 * mm))

    # --- Direct Quote ---
    dq_notes: list = [Spacer(1, 1 * mm)]
    dq_notes += [
        Paragraph(
            jp("Enclose statement in 「」, add と, then verb (言う, 聞く, 叫ぶ, 呼ぶ, 呟く)."),
            note_s,
        ),
        Paragraph(jp('アリスが、「寒い」と言った。 — Alice said, "Cold".'), ex_s),
        Paragraph(
            jp(
                '「今日は授業がない」と先生から聞いたんだけど。 — I heard from the teacher, "There is no class today."'
            ),
            ex_s,
        ),
        Paragraph(
            jp("Verb doesn't need to be directly connected to the clause:"),
            note_s,
        ),
        Paragraph(jp('「寒い」とアリスが田中に言った。 — "Cold," Alice said to Tanaka.'), ex_s),
    ]
    story.append(section(jp("Direct Quote — 「」と"), *dq_notes))
    story.append(Spacer(1, 3.5 * mm))

    # --- Interpreted Quote ---
    iq_notes: list = [Spacer(1, 1 * mm)]
    iq_notes += [
        Paragraph(
            jp("Not word-for-word. No quotation marks. Can express thoughts with 思う / 考える."),
            note_s,
        ),
        Paragraph(
            jp(
                "先生から今日は授業がないと聞いたんだけど。 — I heard from the teacher that there is no class today."
            ),
            ex_s,
        ),
        Paragraph(jp("これは、日本語で何と言いますか。 — What do you call this in Japanese?"), ex_s),
        Paragraph(jp("私は、アリスと言います。 — I am called Alice."), ex_s),
        Paragraph(
            jp(
                "カレーを食べようと思ったけど、食べる時間がなかった。 — I thought about eating curry but didn't have time."
            ),
            ex_s,
        ),
        Paragraph(
            jp("今、どこに行こうかと考えている。 — Now, I'm considering where to go."),
            ex_s,
        ),
        Paragraph(
            jp("For noun/na-adj state-of-being, include declarative だ:"),
            note_s,
        ),
        Paragraph(
            jp("彼は、これは何だと言いましたか。 — What did he say this is?"),
            ex_s,
        ),
        Paragraph(
            jp(
                "彼は高校生だと聞いたけど、信じられない。 — I heard he is a high school student but I can't believe it."
            ),
            ex_s,
        ),
        Paragraph(
            jp(
                "Compare: これは何だと言いましたか (What did he say this is?) vs 何と言いましたか (What did he say?)"
            ),
            note_s,
        ),
    ]
    story.append(section(jp("Interpreted Quote — [clause]と"), *iq_notes))
    story.append(Spacer(1, 3.5 * mm))

    # --- って — Casual と ---
    tte_notes: list = [Spacer(1, 1 * mm)]
    tte_notes += [
        Paragraph(
            jp("って is a shorter casual version of と. You can drop the rest of the sentence."),
            note_s,
        ),
        Paragraph(
            jp("智子は来年、海外に行くんだって。 — Tomoko said that she's going overseas next year."),
            ex_s,
        ),
        Paragraph(jp("もうお金がないって。 — I already told you I have no money."), ex_s),
        Paragraph(jp("え？何だって？ — Huh? What did you say?"), ex_s),
        Paragraph(
            jp("今、時間がないって聞いたんだけど、本当？ — I heard you don't have time now, is that true?"),
            ex_s,
        ),
        Paragraph(
            jp("って can also replace は to bring up a topic in casual speech:"),
            note_s,
        ),
        Paragraph(
            jp("明日って、雨が降るんだって。 — About tomorrow, I hear it's going to rain."),
            ex_s,
        ),
        Paragraph(
            jp("アリスって、すごくいい人でしょ？ — About Alice, she's a very good person, right?"),
            ex_s,
        ),
    ]
    story.append(section(jp("って — Casual と"), *tte_notes))
    story.append(Spacer(1, 3.5 * mm))

    # --- Notes ---
    final_notes: list = [Spacer(1, 1 * mm)]
    for n in [
        jp("Direct quote: 「quote」と + verb. Common verbs: 言う, 聞く, 叫ぶ, 呼ぶ, 呟く."),
        jp("Interpreted quote: [clause] + と + verb. No quotation marks, not word-for-word."),
        jp("と思う = I think..., と考える = I'm considering.... Use volitional + と思う for intentions."),
        jp("Noun/na-adj in quoted clause needs だ: 高校生だと聞いた (heard he IS a student)."),
        jp("って = casual と. Can drop the rest of sentence. Also replaces は to introduce topics."),
    ]:
        final_notes.append(Paragraph(f"- {n}", note_s))
    story.append(section("Notes", *final_notes))

    return story
