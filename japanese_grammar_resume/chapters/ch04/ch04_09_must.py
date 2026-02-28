from ...styles import *


def build():
    story = []

    story.append(PageBreak())
    story.append(
        Paragraph(
            jp('4.9  Expressing "Must" / "Have To"  （〜だめ、〜いけない、〜ならない、〜ても）'),
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
                    "駄目",
                    "夜",
                    "遅い",
                    "電話",
                    "構う",
                ]
            )
        )
    )
    story.append(Spacer(1, 3.5 * mm))

    # --- Summary Table ---
    sum_data = [
        ["Pattern", "Meaning", "Example"],
        [
            jp("te-form + はだめ\n/ いけない / ならない"),
            jp("must not do"),
            jp("入ってはいけない"),
        ],
        [
            jp("neg te-form + は\n+ だめ / いけない / ならない"),
            jp("must do"),
            jp("行かなくてはならない"),
        ],
        [
            jp("neg verb + と\n+ だめ / いけない / ならない"),
            jp("must do"),
            jp("行かないとだめ"),
        ],
        [
            jp("neg verb + ば\n+ だめ / いけない / ならない"),
            jp("must do"),
            jp("行かなければいけない"),
        ],
        [
            jp("te-form + もいい\n/ 大丈夫 / 構わない"),
            jp("ok to do /\ndon't have to"),
            jp("食べてもいい\n食べなくてもいい"),
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

    # --- Must Not ---
    not_notes: list = [Spacer(1, 1 * mm)]
    not_notes += [
        Paragraph(
            jp("Te-form + は + だめ / いけない / ならない. だめ is casual, ならない is for rules/policies."),
            note_s,
        ),
        Paragraph(jp("ここに入ってはいけません。 — You must not enter here."), ex_s),
        Paragraph(jp("それを食べてはだめ！ — You can't (must not) eat that!"), ex_s),
        Paragraph(
            jp("夜、遅くまで電話してはならない。 — You must not use the phone until late at night."), ex_s
        ),
    ]
    story.append(section(jp("Must Not — てはだめ / いけない / ならない"), *not_notes))
    story.append(Spacer(1, 3.5 * mm))

    # --- Must Do ---
    must_notes: list = [Spacer(1, 1 * mm)]
    must_notes += [
        Paragraph(
            jp("Double negative: negate the verb, then add だめ / いけない / ならない. Three methods:"),
            note_s,
        ),
        Paragraph(
            jp("1. Neg te-form + は: 毎日学校に行かなくてはなりません。 — Must go to school everyday."),
            note_s,
        ),
        Paragraph(
            jp("2. Neg verb + と: 毎日学校に行かないとだめです。 — Must go to school everyday."),
            note_s,
        ),
        Paragraph(
            jp("3. Neg verb + ば: 毎日学校に行かなければいけません。 — Must go to school everyday."),
            note_s,
        ),
        Paragraph(
            jp("宿題をしなくてはいけなかった。 — Had to do homework. (method 1)"),
            ex_s,
        ),
        Paragraph(jp("宿題をしないといけない。 — Have to do homework. (method 2)"), ex_s),
        Paragraph(jp("宿題をしなければだめだった。 — Had to do homework. (method 3)"), ex_s),
        Paragraph(
            jp(
                "In practice, ～なければ and ～なくては are long. Casual speech prefers ～ないと or shortcuts."
            ),
            note_s,
        ),
    ]
    story.append(section(jp("Must Do — Double Negative"), *must_notes))
    story.append(Spacer(1, 3.5 * mm))

    # --- Casual Shortcuts ---
    short_data = [
        ["Full Form", "Shortcut", "Usage"],
        [jp("なくては"), jp("なくちゃ"), jp("must do (casual)")],
        [jp("なければ"), jp("なきゃ"), jp("must do (casual)")],
        [jp("ては"), jp("ちゃ"), jp("must not do (casual)")],
        [jp("では"), jp("じゃ"), jp("must not do (casual)")],
    ]
    short_rows = [
        [cell(c, bold=(ri == 0), center=(ri == 0), sz=8) for ci, c in enumerate(row)]
        for ri, row in enumerate(short_data)
    ]
    shw = (W - 30 * mm) / 2
    short_t = Table(short_rows, colWidths=[30 * mm, shw, shw])
    short_t.setStyle(TableStyle(TABLE_STYLE))

    short_notes: list = [Spacer(1, 1 * mm)]
    short_notes += [
        Paragraph(
            jp("With なくちゃ / なきゃ, you can drop だめ / いけない / ならない entirely."),
            note_s,
        ),
        Paragraph(jp("勉強しなくちゃ。 — Gotta study."), ex_s),
        Paragraph(jp("ご飯を食べなきゃ。 — Gotta eat."), ex_s),
        Paragraph(jp("学校に行かないと。 — Gotta go to school. (と by itself implies the rest)"), ex_s),
        Paragraph(
            jp("For must not: ちゃ/じゃ require だめ. Verbs with む/ぶ/ぬ (past ～んだ) use じゃ."),
            note_s,
        ),
        Paragraph(jp("ここに入っちゃだめだよ。 — You can't enter here."), ex_s),
        Paragraph(jp("死んじゃだめだよ！ — You can't die!"), ex_s),
    ]
    story.append(section(jp("Casual Shortcuts"), short_t, *short_notes))
    story.append(Spacer(1, 3.5 * mm))

    # --- OK to Do / Don't Have To ---
    ok_notes: list = [Spacer(1, 1 * mm)]
    ok_notes += [
        Paragraph(
            jp(
                "Te-form + も + いい / 大丈夫 / 構わない = \"even if you do X, it's ok\" = you may / don't have to."
            ),
            note_s,
        ),
        Paragraph(jp("全部食べてもいいよ。 — You can go ahead and eat it all."), ex_s),
        Paragraph(jp("全部食べなくてもいいよ。 — You don't have to eat it all."), ex_s),
        Paragraph(jp("全部飲んでも大丈夫だよ。 — It's ok if you drink it all."), ex_s),
        Paragraph(jp("全部飲んでも構わないよ。 — I don't mind if you drink it all."), ex_s),
        Paragraph(jp("Casual: ～てもいい shortens to ～ていい."), note_s),
        Paragraph(jp("もう帰っていい？ — Can I go home already?"), ex_s),
        Paragraph(jp("これ、ちょっと見ていい？ — Can I take a quick look at this?"), ex_s),
    ]
    story.append(section(jp("OK to Do / Don't Have To — ても"), *ok_notes))
    story.append(Spacer(1, 3.5 * mm))

    # --- Notes ---
    final_notes: list = [Spacer(1, 1 * mm)]
    for n in [
        jp("Must not: te-form + はだめ/いけない/ならない. だめ = casual, ならない = rules/policies."),
        jp(
            "Must do: double negative. Three methods: ～なくては, ～ないと, ～なければ + だめ/いけない/ならない."
        ),
        jp("Casual shortcuts: なくちゃ / なきゃ (can drop ending). ～ないと alone also works."),
        jp("Must not (casual): ちゃだめ / じゃだめ. Use じゃ for verbs with past ～んだ (む/ぶ/ぬ)."),
        jp("OK / don't have to: te-form + もいい / 大丈夫 / 構わない. Casual: ～ていい."),
    ]:
        final_notes.append(Paragraph(f"- {n}", note_s))
    story.append(section("Notes", *final_notes))

    return story
