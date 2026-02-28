from ...styles import *


def build():
    story = []

    story.append(PageBreak())
    story.append(
        Paragraph(
            jp("4.4  Compound Sentences  （て-form、から、ので、のに、が、けど、し、～たりする）"),
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
                        "一般的",
                        "狭い",
                        "お金持ち",
                        "魅力的",
                        "食堂",
                        "昼寝",
                        "パーティー",
                        "プレゼント",
                        "どうして",
                        "山田",
                        "一郎",
                        "直子",
                        "そろそろ",
                        "失礼",
                        "穏やか",
                        "運動",
                        "痩せる",
                        "デパート",
                        "欲しい",
                        "まだ",
                        "年上",
                        "優しい",
                        "簡単",
                        "難しい",
                        "読む",
                    ]
                )
            ),
        )
    )
    story.append(Spacer(1, 3.5 * mm))

    # --- 4.4.1 Chaining States ---
    chain_data = [
        ["Type", "Rule", "Example"],
        [
            "Nouns / na-adj",
            jp("Attach で"),
            jp("一般的 → 一般的で\n静か → 静かで"),
        ],
        [
            "i-adj",
            jp("Replace い with くて"),
            jp("狭い → 狭くて"),
        ],
        [
            "Negative",
            jp("Same くて rule"),
            jp("彼女じゃない → 彼女じゃなくて"),
        ],
        [
            jp("いい / かっこいい"),
            jp("い → よ exception"),
            jp("いい → よくて"),
        ],
    ]
    chain_rows = [
        [cell(c, bold=(ri == 0), center=(ri == 0 or ci == 0), sz=8) for ci, c in enumerate(row)]
        for ri, row in enumerate(chain_data)
    ]
    hw = (W - 35 * mm) / 2
    chain_t = Table(chain_rows, colWidths=[35 * mm, hw, hw])
    chain_t.setStyle(
        TableStyle(
            TABLE_STYLE
            + [
                ("BACKGROUND", (0, 1), (0, -1), CR1),
                ("FONTNAME", (0, 1), (0, -1), "DV-B"),
            ]
        )
    )
    story.append(section("Chaining States", chain_t))
    story.append(Spacer(1, 3.5 * mm))

    # --- 4.4.2 Te-form Conjugation ---
    te_data = [
        ["Past Tense", "Te-form", "Negative", "Neg Te-form"],
        [jp("食べた"), jp("食べて"), jp("食べない"), jp("食べなくて")],
        [jp("行った"), jp("行って"), jp("行かない"), jp("行かなくて")],
        [jp("した"), jp("して"), jp("しない"), jp("しなくて")],
        [jp("遊んだ"), jp("遊んで"), jp("遊ばない"), jp("遊ばなくて")],
        [jp("飲んだ"), jp("飲んで"), jp("飲まない"), jp("飲まなくて")],
    ]
    te_rows = [
        [cell(c, bold=(ri == 0), center=True, sz=8) for ci, c in enumerate(row)]
        for ri, row in enumerate(te_data)
    ]
    cw_te = [W / 4] * 4
    te_t = Table(te_rows, colWidths=cw_te)
    te_t.setStyle(TableStyle(TABLE_STYLE))
    te_notes: list = [Spacer(1, 1 * mm)]
    te_notes += [
        Paragraph(jp("Positive: conjugate to past tense, replace た with て (だ with で)."), note_s),
        Paragraph(jp("Negative: same as i-adjectives — replace い with くて."), note_s),
        Paragraph(jp("Polite forms also work: です → でして, ます → まして."), note_s),
    ]
    story.append(section("Te-form Conjugation", te_t, *te_notes))
    story.append(Spacer(1, 3.5 * mm))

    # --- 4.4.3 から and ので ---
    kara_notes: list = [Spacer(1, 1 * mm)]
    kara_notes += [
        Paragraph(jp("[reason]から[result] = 'because [reason], [result]'."), note_s),
        Paragraph(
            jp("時間がなかったからパーティーに行きませんでした。 — No time so didn't go to party."), ex_s
        ),
        Paragraph(jp("For nouns / na-adj: add だ before から (友達だからプレゼントが来た)."), note_s),
        Paragraph(
            jp("ので is softer and more polite than から. For nouns / na-adj: add な before ので."), note_s
        ),
        Paragraph(jp("私は学生なので、お金がないんです。 — Because I'm a student, I have no money."), ex_s),
        Paragraph(
            jp("ちょっと忙しいので、そろそろ失礼します。 — A little busy, so I'll be leaving soon."), ex_s
        ),
        Paragraph(
            jp("ので can shorten to んで in speech (時間がなかったんでパーティーに行かなかった)."), note_s
        ),
        Paragraph(jp("Either the reason or the result can be omitted if clear from context."), note_s),
    ]
    story.append(section(jp("から and ので — Reason"), *kara_notes))
    story.append(Spacer(1, 3.5 * mm))

    # --- 4.4.4 のに — "despite" ---
    noni_notes: list = [Spacer(1, 1 * mm)]
    noni_notes += [
        Paragraph(jp("[Sentence 2]のに[Sentence 1] = 'despite [S2], [S1]'."), note_s),
        Paragraph(jp("Grammatically identical to ので but with reversed meaning."), note_s),
        Paragraph(
            jp("毎日運動したのに、全然痩せなかった。 — Despite exercising every day, didn't get thinner."),
            ex_s,
        ),
        Paragraph(jp("学生なのに、彼女は勉強しない。 — Despite being a student, she does not study."), ex_s),
        Paragraph(jp("For nouns / na-adj: add な before のに (same as ので)."), note_s),
    ]
    story.append(section(jp("のに — Despite"), *noni_notes))
    story.append(Spacer(1, 3.5 * mm))

    # --- 4.4.5 が and けど — contradiction ---
    ga_notes: list = [Spacer(1, 1 * mm)]
    ga_notes += [
        Paragraph(
            jp("が (softer) and けど (casual) connect two sentences — contradiction or just topic shift."),
            note_s,
        ),
        Paragraph(jp("が is commonly seen with ～ます / ～です; けど with plain form."), note_s),
        Paragraph(
            jp("デパートに行きましたが、何も欲しくなかったです。 — Went to dept store but wanted nothing."),
            ex_s,
        ),
        Paragraph(jp("友達に聞いたけど、知らなかった。 — Asked a friend but (he) didn't know."), ex_s),
        Paragraph(jp("For nouns / na-adj: add だ before けど (今日は暇だけど、明日は忙しい)."), note_s),
        Paragraph(jp("More formal: けど → けれど → けれども."), note_s),
        Paragraph(jp("Can also just connect two topics (no contradiction):"), note_s),
        Paragraph(
            jp(
                "デパートに行きましたが、いい物がたくさんありました。 — Went to dept store and there was a lot of good stuff."
            ),
            ex_s,
        ),
    ]
    story.append(section(jp("が and けど — Contradiction"), *ga_notes))
    story.append(Spacer(1, 3.5 * mm))

    # --- 4.4.6 し — multiple reasons ---
    shi_notes: list = [Spacer(1, 1 * mm)]
    shi_notes += [
        Paragraph(
            jp(
                "Attach し to the end of each clause to list multiple reasons (like や but for verbs / states)."
            ),
            note_s,
        ),
        Paragraph(jp("A：どうして彼が好きなの？ — Why do you like him?"), ex_s),
        Paragraph(
            jp("B：優しいし、かっこいいし、面白いから。 — Because he's kind, handsome, and interesting."),
            ex_s,
        ),
        Paragraph(jp("先生だし、年上だし… — He's the teacher, and older..."), ex_s),
        Paragraph(
            jp("だ required for non-conjugated nouns / na-adj before し (先生だし, 好きだし)."), note_s
        ),
        Paragraph(jp("し implies there may be other reasons beyond those listed."), note_s),
    ]
    story.append(section(jp("し — Multiple Reasons"), *shi_notes))
    story.append(Spacer(1, 3.5 * mm))

    # --- 4.4.7 ～たりする ---
    tari_data = [
        ["Type", "Rule", "Example"],
        [
            "Verbs",
            jp("Past tense + り.\nAdd する at very end."),
            jp("食べる、飲む →\n食べたり、飲んだりする"),
        ],
        [
            "State-of-being",
            jp("Past state + り.\nAdd する at very end."),
            jp("簡単、難しい →\n簡単だったり、難しかったりする"),
        ],
    ]
    tari_rows = [
        [cell(c, bold=(ri == 0), center=(ri == 0 or ci == 0), sz=8) for ci, c in enumerate(row)]
        for ri, row in enumerate(tari_data)
    ]
    hw2 = (W - 30 * mm) / 2
    tari_t = Table(tari_rows, colWidths=[30 * mm, hw2, hw2])
    tari_t.setStyle(
        TableStyle(
            TABLE_STYLE
            + [
                ("BACKGROUND", (0, 1), (0, -1), CR1),
                ("FONTNAME", (0, 1), (0, -1), "DV-B"),
            ]
        )
    )
    tari_notes: list = [Spacer(1, 1 * mm)]
    tari_notes += [
        Paragraph(jp("Tense / polarity is controlled by the final する (した, しない, しなかった)."), note_s),
        Paragraph(
            jp(
                "映画を見たり、本を読んだり、昼寝したりする。 — Watch movies, read books, take naps (among other things)."
            ),
            ex_s,
        ),
        Paragraph(
            jp(
                "この大学の授業は簡単だったり、難しかったりする。 — Classes are sometimes easy, sometimes difficult."
            ),
            ex_s,
        ),
    ]
    story.append(section(jp("～たりする — Among Other Things"), tari_t, *tari_notes))
    story.append(Spacer(1, 3.5 * mm))

    # --- Notes ---
    final_notes: list = [Spacer(1, 1 * mm)]
    for n in [
        jp("Chain nouns/na-adj with で, i-adj with くて. Last item keeps its original form."),
        jp("Te-form chains verbs: replace た→て (だ→で). Tense set by the final verb."),
        jp("から = explicit 'because'; ので = softer/politer 'because'. Both need だ/な for nouns/na-adj."),
        jp("のに = 'despite' — same grammar as ので but opposite meaning."),
        jp("が/けど = contradiction or topic connector. が is softer; けど is casual."),
        jp("し lists multiple reasons (like や for verbs). Implies more reasons may exist."),
        jp("～たりする lists actions among a larger set. Tense controlled by final する."),
    ]:
        final_notes.append(Paragraph(f"- {n}", note_s))
    story.append(section("Notes", *final_notes))

    return story
