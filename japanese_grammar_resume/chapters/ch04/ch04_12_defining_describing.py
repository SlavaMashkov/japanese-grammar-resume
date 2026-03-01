from ...styles import *


def build():
    story = []

    story.append(PageBreak())
    story.append(
        Paragraph(
            jp("4.12  Defining and Describing  （という）"),
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
                        "英語",
                        "意味",
                        "鯛",
                        "主人公",
                        "日本人",
                        "お酒",
                        "弱い",
                        "独身",
                        "嘘",
                        "パソコン",
                        "再起動",
                        "困る",
                        "結婚",
                        "幸せ",
                        "多分",
                        "別れる",
                        "彼氏",
                        "留学",
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
            jp("[X]という[Y]"),
            jp("[Y] called [X]"),
            jp("鯛という魚"),
        ],
        [
            jp("[clause]というの"),
            jp("the thing that [clause]"),
            jp("犯人だったというのが面白い"),
        ],
        [
            jp("こういう / そういう\nああいう / どういう"),
            jp("this kind / that kind\nthat kind (far) / what kind"),
            jp("こういう時"),
        ],
        [
            jp("というか"),
            jp("or rather"),
            jp("好きというか"),
        ],
        [
            jp("ということ"),
            jp("means that..."),
            jp("彼氏がいないということ？"),
        ],
        [
            jp("って / て (casual)"),
            jp("= という"),
            jp("留学するって智子のこと？"),
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

    # --- という to Define ---
    def_notes: list = [Spacer(1, 1 * mm)]
    def_notes += [
        Paragraph(
            jp(
                "Xという[noun] = [noun] called/known as X. Uses hiragana いう (not 言う) since nothing is literally said."
            ),
            note_s,
        ),
        Paragraph(jp("これは、なんという魚ですか。 — What is this fish referred to as?"), ex_s),
        Paragraph(jp('この魚は、鯛といいます。 — This fish is known as "Tai".'), ex_s),
        Paragraph(
            jp(
                'ルミネというデパートはどこにあるか、知っていますか？ — Do you know where the department store called "Lumine" is?'
            ),
            ex_s,
        ),
        Paragraph(
            jp(
                '「友達」は、英語で「friend」という意味です。 — The meaning of "tomodachi" in English is "friend".'
            ),
            ex_s,
        ),
    ]
    story.append(section(jp("という — to Define"), *def_notes))
    story.append(Spacer(1, 3.5 * mm))

    # --- という to Describe ---
    desc_notes: list = [Spacer(1, 1 * mm)]
    desc_notes += [
        Paragraph(
            jp(
                "[clause]という is so abstract that いう is just a generic verb enabling us to talk about any relative clause."
            ),
            note_s,
        ),
        Paragraph(
            jp(
                "主人公が犯人だったというのが一番面白かった。 — The most interesting thing was that the main character was the criminal."
            ),
            ex_s,
        ),
        Paragraph(
            jp("日本人はお酒に弱いというのは本当？ — Is it true that Japanese people are weak to alcohol?"),
            ex_s,
        ),
        Paragraph(
            jp("独身だというのは、嘘だったの？ — It was a lie that you were single?"),
            ex_s,
        ),
        Paragraph(
            jp(
                "リブートというのは、パソコンを再起動するということです。 — Reboot means to restart your computer."
            ),
            ex_s,
        ),
        Paragraph(
            jp("With こう/そう/ああ/どう + いう = this/that/what kind of:"),
            note_s,
        ),
        Paragraph(
            jp(
                "いつもこういう時に来るんだから、困るんだよ。 — You always come at times like these, so it's troubling."
            ),
            ex_s,
        ),
        Paragraph(
            jp(
                "ああいう人と結婚できたら、幸せになれると思います。 — I think you can become happy if you could marry that type of person."
            ),
            ex_s,
        ),
        Paragraph(
            jp('大学に行かないって、どういう意味なの？ — What do you mean, "You\'re not going to college?"'),
            ex_s,
        ),
    ]
    story.append(section(jp("という — to Describe"), *desc_notes))
    story.append(Spacer(1, 3.5 * mm))

    # --- Rephrasing with というか / ということ ---
    reph_notes: list = [Spacer(1, 1 * mm)]
    reph_notes += [
        Paragraph(
            jp('というか = "or rather". Used to correct, rephrase, or come to a different conclusion.'),
            note_s,
        ),
        Paragraph(
            jp(
                "お酒は好きというか、ないと生きていけない。 — I like alcohol or rather, can't live without it."
            ),
            ex_s,
        ),
        Paragraph(
            jp(
                "多分行かないと思う。というか、お金がないから、行けない。 — Don't think I'll go. Or rather, can't because no money."
            ),
            ex_s,
        ),
        Paragraph(
            jp('ということ = "means that...". Attach か for a questioning element.'),
            note_s,
        ),
        Paragraph(
            jp(
                "みきちゃんが洋介と別れたんだって。ということは、今彼氏がいないということ？ — Does that mean she has no boyfriend now?"
            ),
            ex_s,
        ),
    ]
    story.append(section(jp("Rephrasing — というか / ということ"), *reph_notes))
    story.append(Spacer(1, 3.5 * mm))

    # --- って/て for という ---
    tte_notes: list = [Spacer(1, 1 * mm)]
    tte_notes += [
        Paragraph(
            jp("って can replace という (casual). Can leave out いう and accompanying particles."),
            note_s,
        ),
        Paragraph(
            jp("来年留学するというのは、智子のこと？ → 来年留学するって智子のこと？"),
            ex_s,
        ),
        Paragraph(
            jp(
                'だって = "but (even so)" — expresses disagreement or dissatisfaction (abbr. of とはいっても).'
            ),
            note_s,
        ),
        Paragraph(
            jp("だって、時間がないからできないよ。 — But (even so), can't do it because there's no time."),
            ex_s,
        ),
        Paragraph(
            jp(
                "だって、みんな行くって。私も行かないと。 — But, everybody said they're going. I have to go too."
            ),
            ex_s,
        ),
        Paragraph(
            jp("て can also replace って (more slangy). て is not used for something actually said."),
            note_s,
        ),
        Paragraph(
            jp("ゆう is often used instead of いう in casual speech (easier to say)."),
            note_s,
        ),
    ]
    story.append(section(jp("って / て for という"), *tte_notes))
    story.append(Spacer(1, 3.5 * mm))

    # --- Notes ---
    final_notes: list = [Spacer(1, 1 * mm)]
    for n in [
        jp("Xという[noun] = [noun] called X. Uses いう in hiragana, not 言う."),
        jp("[clause]というの describes any clause as a noun. という is a generic verb for this."),
        jp("こういう/そういう/ああいう/どういう = this/that/that(far)/what kind of."),
        jp("というか = or rather. ということ = means that... Can attach か for questions."),
        jp("って/て replace という in casual speech. だって = but (even so). ゆう = casual いう."),
    ]:
        final_notes.append(Paragraph(f"- {n}", note_s))
    story.append(section("Notes", *final_notes))

    return story
