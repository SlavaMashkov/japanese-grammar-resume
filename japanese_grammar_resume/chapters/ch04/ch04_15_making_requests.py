from ...styles import *


def build():
    story = []

    story.append(PageBreak())
    story.append(
        Paragraph(
            jp("4.15  Making Requests  （〜ください、〜ちょうだい、〜なさい、command form）"),
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
                        "消しゴム",
                        "遠い",
                        "壊れる",
                        "頂戴",
                        "致す",
                        "スプーン",
                        "座る",
                        "あっち",
                        "酒",
                        "変",
                    ]
                )
            ),
        )
    )
    story.append(Spacer(1, 3.5 * mm))

    # --- Patterns Overview ---
    sum_data = [
        ["Pattern", "Meaning", "Politeness"],
        [jp("te-form + ください"), jp("please do"), jp("polite request")],
        [jp("te-form + ちょうだい"), jp("please do"), jp("casual (feminine)")],
        [jp("verb stem + なさい"), jp("do it (firm)"), jp("firm but polite")],
        [jp("command form"), jp("do it! (order)"), jp("rough / manga")],
        [jp("verb + な"), jp("don't do it!"), jp("negative command")],
    ]
    sum_rows = [
        [cell(c, bold=(ri == 0), center=(ri == 0 or ci == 0), sz=8) for ci, c in enumerate(row)]
        for ri, row in enumerate(sum_data)
    ]
    sw = (W - 40 * mm) / 2
    sum_t = Table(sum_rows, colWidths=[40 * mm, sw, sw])
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

    # --- ください ---
    kuda_notes: list = [Spacer(1, 1 * mm)]
    kuda_notes += [
        Paragraph(
            jp("ください is the honorific form of くれる (くださる). Te-form + ください = please do."),
            note_s,
        ),
        Paragraph(jp("それをください。 — Please give me that."), ex_s),
        Paragraph(jp("漢字で書いてください。 — Please write it in kanji."), ex_s),
        Paragraph(jp("ゆっくり話してください。 — Please speak slowly."), ex_s),
        Paragraph(
            jp("Negative: ないで + ください."),
            note_s,
        ),
        Paragraph(jp("落書きを書かないでください。 — Please don't write graffiti."), ex_s),
        Paragraph(jp("ここに来ないでください。 — Please don't come here."), ex_s),
        Paragraph(
            jp("Casual: drop ください and just use te-form."),
            note_s,
        ),
        Paragraph(jp("日本語で話して。 — Please speak in Japanese."), ex_s),
        Paragraph(jp("消しゴムを貸して。 — Please lend me the eraser."), ex_s),
        Paragraph(jp("遠い所に行かないで。 — Please don't go to a far place."), ex_s),
        Paragraph(
            jp("Even more commanding: くれ (くれる with る removed)."),
            note_s,
        ),
        Paragraph(jp("日本語で話してくれ。 — Speak in Japanese."), ex_s),
        Paragraph(
            jp("ください must come at end of sentence — cannot directly modify a noun."),
            note_s,
        ),
    ]
    story.append(section(jp("ください — Polite Request"), *kuda_notes))
    story.append(Spacer(1, 3.5 * mm))

    # --- ちょうだい ---
    chou_notes: list = [Spacer(1, 1 * mm)]
    chou_notes += [
        Paragraph(
            jp(
                "ちょうだい = casual alternative of ください. Slightly feminine/childish. Always in hiragana."
            ),
            note_s,
        ),
        Paragraph(jp("スプーンをちょうだい。 — Please give me the spoon."), ex_s),
        Paragraph(jp("ここに名前を書いてちょうだい。 — Please write your name here."), ex_s),
    ]
    story.append(section(jp("ちょうだい — Casual Request"), *chou_notes))
    story.append(Spacer(1, 3.5 * mm))

    # --- なさい ---
    nasa_notes: list = [Spacer(1, 1 * mm)]
    nasa_notes += [
        Paragraph(
            jp("なさい = special honorific conjugation of する. Verb stem + なさい = firm but soft command."),
            note_s,
        ),
        Paragraph(jp("食べる → 食べなさい / 飲む → 飲みなさい / する → しなさい"), ex_s),
        Paragraph(jp("よく聞きなさい！ — Listen well!"), ex_s),
        Paragraph(jp("ここに座りなさい。 — Sit here."), ex_s),
        Paragraph(
            jp("Casual: drop さい → stem + な."),
            note_s,
        ),
        Paragraph(
            jp("まだいっぱいあるから、たくさん食べな。 — There's still a lot, so eat a lot."),
            ex_s,
        ),
        Paragraph(
            jp("それでいいと思うなら、そうしなよ。 — If you think that's fine, then go ahead and do it."),
            ex_s,
        ),
    ]
    story.append(section(jp("なさい — Firm but Polite"), *nasa_notes))
    story.append(Spacer(1, 3.5 * mm))

    # --- Command Form ---
    def conj_tbl(data, cw):
        rows = [[cell(c, bold=(ri == 0), center=True, sz=8) for c in row] for ri, row in enumerate(data)]
        t = Table(rows, colWidths=cw)
        t.setStyle(TableStyle(TABLE_STYLE))
        return t

    ru_data = [
        ["Plain", "Command"],
        [jp("食べる"), jp("食べろ")],
        [jp("着る"), jp("着ろ")],
        [jp("信じる"), jp("信じろ")],
        [jp("寝る"), jp("寝ろ")],
        [jp("起きる"), jp("起きろ")],
        [jp("出る"), jp("出ろ")],
        [jp("掛ける"), jp("掛けろ")],
        [jp("捨てる"), jp("捨てろ")],
    ]
    u_data = [
        ["Plain", "Command"],
        [jp("話す"), jp("話せ")],
        [jp("聞く"), jp("聞け")],
        [jp("遊ぶ"), jp("遊べ")],
        [jp("待つ"), jp("待て")],
        [jp("飲む"), jp("飲め")],
        [jp("直る"), jp("直れ")],
        [jp("死ぬ"), jp("死ね")],
        [jp("買う"), jp("買え")],
    ]
    exc_data = [
        ["Plain", "Command"],
        [jp("する"), jp("しろ")],
        [jp("くる"), jp("こい")],
        [jp("くれる"), jp("くれ")],
    ]

    GAP = 2 * mm
    tw3 = (W - 2 * GAP) / 3
    cw2 = [tw3 / 2, tw3 / 2]
    ru_t = conj_tbl(ru_data, cw2)
    u_t = conj_tbl(u_data, cw2)
    exc_t = conj_tbl(exc_data, cw2)

    outer = Table(
        [[ru_t, "", u_t, "", exc_t]],
        colWidths=[tw3, GAP, tw3, GAP, tw3],
        style=TableStyle(
            [
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 0),
                ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                ("TOPPADDING", (0, 0), (-1, -1), 0),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
            ]
        ),
    )

    cmd_notes: list = [Spacer(1, 1 * mm)]
    cmd_notes += [
        Paragraph(
            jp("ru-verbs: る→ろ. u-verbs: /u/→/e/ vowel. Rarely used — mostly in fiction/manga."),
            note_s,
        ),
        Paragraph(jp("好きにしろ。 — Do as you please."), ex_s),
        Paragraph(jp("あっち行け！ — Go away!"), ex_s),
        Paragraph(jp("早く酒を持ってきてくれ。 — Hurry up and bring me some alcohol."), ex_s),
    ]
    story.append(section(jp("Command Form"), outer, *cmd_notes))
    story.append(Spacer(1, 3.5 * mm))

    # --- Negative Command ---
    neg_notes: list = [Spacer(1, 1 * mm)]
    neg_notes += [
        Paragraph(
            jp(
                "Attach な to the dictionary form of the verb. Don't confuse with shortened なさい (uses stem)."
            ),
            note_s,
        ),
        Paragraph(jp("それを食べるな！ — Don't eat that!"), ex_s),
        Paragraph(jp("変なことを言うな！ — Don't say such weird things!"), ex_s),
        Paragraph(
            jp("Compare: しな = casual なさい (do it). するな = negative command (don't do it)."),
            note_s,
        ),
    ]
    story.append(section(jp("Negative Command — verb + な"), *neg_notes))
    story.append(Spacer(1, 3.5 * mm))

    # --- Notes ---
    final_notes: list = [Spacer(1, 1 * mm)]
    for n in [
        jp("ください: te-form + ください. Negative: ないで + ください. Casual: just te-form."),
        jp("ちょうだい: casual ください, slightly feminine. Always written in hiragana."),
        jp("なさい: verb stem + なさい. Firm but soft (parent/teacher). Casual: stem + な."),
        jp("Command form: ru→ろ, u→e vowel. する→しろ, くる→こい, くれる→くれ. Mostly fiction."),
        jp("Negative command: dictionary form + な. Don't confuse with shortened なさい."),
    ]:
        final_notes.append(Paragraph(f"- {n}", note_s))
    story.append(section("Notes", *final_notes))

    return story
