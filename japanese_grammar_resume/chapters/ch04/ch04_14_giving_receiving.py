from ...styles import *


def build():
    story = []

    story.append(PageBreak())
    story.append(
        Paragraph(
            jp("4.14  Giving and Receiving  （あげる、やる、くれる、もらう）"),
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
                        "お歳暮",
                        "お中元",
                        "もらう",
                        "車",
                        "代わり",
                        "餌",
                        "チェック",
                        "無理",
                        "時計",
                        "千円",
                        "あなた",
                    ]
                )
            ),
        )
    )
    story.append(Spacer(1, 3.5 * mm))

    # --- Patterns Overview ---
    sum_data = [
        ["Verb", "Meaning", "Point of View", "Example"],
        [
            jp("あげる"),
            jp("to give"),
            jp("giver's POV"),
            jp("プレゼントをあげた"),
        ],
        [
            jp("やる"),
            jp("to give (casual)"),
            jp("giver's (for pets)"),
            jp("犬に餌をやった"),
        ],
        [
            jp("くれる"),
            jp("to give"),
            jp("receiver's POV"),
            jp("プレゼントをくれた"),
        ],
        [
            jp("もらう"),
            jp("to receive"),
            jp("receiver's POV"),
            jp("プレゼントをもらった"),
        ],
    ]
    sum_rows = [
        [cell(c, bold=(ri == 0), center=(ri == 0 or ci == 0), sz=8) for ci, c in enumerate(row)]
        for ri, row in enumerate(sum_data)
    ]
    cw0 = 22 * mm
    cw3 = 42 * mm
    cw_mid = (W - cw0 - cw3) / 2
    sum_t = Table(sum_rows, colWidths=[cw0, cw_mid, cw_mid, cw3])
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

    # --- あげる — To Give (Giver's POV) ---
    ageru_notes: list = [Spacer(1, 1 * mm)]
    ageru_notes += [
        Paragraph(
            jp("あげる = to give from the speaker's point of view. Use when YOU are the giver."),
            note_s,
        ),
        Paragraph(jp("私が友達にプレゼントをあげた。 — I gave present to friend."), ex_s),
        Paragraph(jp("これは先生にあげる。 — I'll give this to teacher."), ex_s),
        Paragraph(
            jp("Te-form + あげる = give the favor of doing. Applies to くれる/もらう too."),
            note_s,
        ),
        Paragraph(jp("車を買ってあげるよ。 — I'll give you the favor of buying a car."), ex_s),
        Paragraph(jp("代わりに行ってあげる。 — I'll give you the favor of going in your place."), ex_s),
        Paragraph(
            jp("For third-person, speaker looks from the giver's POV:"),
            note_s,
        ),
        Paragraph(
            jp("学生がこれを先生にあげる。 — The student gives this to teacher. (giver's POV)"),
            ex_s,
        ),
        Paragraph(
            jp("友達が父にいいことを教えてあげた。 — Friend taught something good to my dad. (friend's POV)"),
            ex_s,
        ),
        Paragraph(
            jp("やる can replace あげる for pets/animals (casual):"),
            note_s,
        ),
        Paragraph(jp("犬に餌をやった？ — Did you give the dog food?"), ex_s),
    ]
    story.append(section(jp("あげる — To Give (Giver's POV)"), *ageru_notes))
    story.append(Spacer(1, 3.5 * mm))

    # --- くれる — To Give (Receiver's POV) ---
    kureru_notes: list = [Spacer(1, 1 * mm)]
    kureru_notes += [
        Paragraph(
            jp("くれる = to give from the receiver's POV. Use when someone ELSE gives to you."),
            note_s,
        ),
        Paragraph(jp("友達が私にプレゼントをくれた。 — Friend gave present to me."), ex_s),
        Paragraph(jp("これは、先生がくれた。 — Teacher gave this to me."), ex_s),
        Paragraph(jp("車を買ってくれるの？ — Will you give me the favor of buying a car?"), ex_s),
        Paragraph(jp("代わりに行ってくれる？ — Will you go in my place?"), ex_s),
        Paragraph(
            jp("Direction: あげる goes UP (away from speaker), くれる comes DOWN (toward speaker)."),
            note_s,
        ),
        Paragraph(
            jp("先生が教えてあげるんですか。 — Teacher will teach... [someone else, not speaker]"),
            ex_s,
        ),
        Paragraph(
            jp("先生が教えてくれるんですか。 — Teacher will teach... [speaker or speaker's group]"),
            ex_s,
        ),
    ]
    story.append(section(jp("くれる — To Give (Receiver's POV)"), *kureru_notes))
    story.append(Spacer(1, 3.5 * mm))

    # --- もらう — To Receive ---
    morau_notes: list = [Spacer(1, 1 * mm)]
    morau_notes += [
        Paragraph(
            jp("もらう = to receive. Since you receive FROM someone, から is also appropriate besides に."),
            note_s,
        ),
        Paragraph(jp("私が友達にプレゼントをもらった。 — I received present from friend."), ex_s),
        Paragraph(jp("友達からプレゼントをもらった。 — I received present from friend."), ex_s),
        Paragraph(
            jp("これは友達に買ってもらった。 — About this, received the favor of buying it from friend."),
            ex_s,
        ),
        Paragraph(
            jp(
                "宿題をチェックしてもらいたかったけど、時間がなくて無理だった。 — Wanted the favor of checking homework but no time."
            ),
            ex_s,
        ),
    ]
    story.append(section(jp("もらう — To Receive"), *morau_notes))
    story.append(Spacer(1, 3.5 * mm))

    # --- Asking Favors ---
    favor_notes: list = [Spacer(1, 1 * mm)]
    favor_notes += [
        Paragraph(
            jp(
                "Use くれる or potential of もらう (もらえる) to make requests. Cannot use あげる for requests."
            ),
            note_s,
        ),
        Paragraph(jp("千円を貸してくれる？ — Will you lend me 1000 yen?"), ex_s),
        Paragraph(jp("千円を貸してもらえる？ — Can I receive the favor of you lending 1000 yen?"), ex_s),
        Paragraph(
            jp("Use negative for softer requests:"),
            note_s,
        ),
        Paragraph(jp("ちょっと静かにしてくれない？ — Won't you be a little quieter?"), ex_s),
        Paragraph(jp("漢字で書いてもらえませんか。 — Can you write this in kanji for me?"), ex_s),
        Paragraph(
            jp("Negative requests: attach で to negative form of verb:"),
            note_s,
        ),
        Paragraph(jp("全部食べないでくれますか。 — Can you not eat it all?"), ex_s),
        Paragraph(jp("高い物を買わないでくれる？ — Can you not buy expensive things?"), ex_s),
    ]
    story.append(section(jp("Asking Favors — くれる / もらえる"), *favor_notes))
    story.append(Spacer(1, 3.5 * mm))

    # --- Notes ---
    final_notes: list = [Spacer(1, 1 * mm)]
    for n in [
        jp("あげる = give (giver's POV). くれる = give (receiver's POV). もらう = receive."),
        jp("Te-form + あげる/くれる/もらう = give/receive the favor of doing something."),
        jp("あげる goes UP (away from speaker). くれる comes DOWN (toward speaker)."),
        jp("やる replaces あげる for pets/animals (casual)."),
        jp("Requests: てくれる / てもらえる. Softer with negative: てくれない / てもらえませんか."),
        jp("Negative requests: ないで + くれる (attach で to negative form)."),
    ]:
        final_notes.append(Paragraph(f"- {n}", note_s))
    story.append(section("Notes", *final_notes))

    return story
