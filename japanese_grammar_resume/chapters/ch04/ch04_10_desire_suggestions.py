from ...styles import *


def build():
    story = []

    story.append(PageBreak())
    story.append(
        Paragraph(
            jp("4.10  Desire and Suggestions  （たい、欲しい、volitional、〜たらどう）"),
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
                        "温泉",
                        "ケーキ",
                        "一緒",
                        "縫いぐるみ",
                        "全部",
                        "テーマパーク",
                        "カレー",
                        "たまに",
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
            jp("verb stem + たい"),
            jp("want to do"),
            jp("行きたい"),
        ],
        [
            jp("noun + が + 欲しい"),
            jp("want (something)"),
            jp("縫いぐるみが欲しい"),
        ],
        [
            jp("te-form + ほしい"),
            jp("want done"),
            jp("食べてほしい"),
        ],
        [
            jp("ru: る→よう\nu: /u/→/o/+う"),
            jp("let's (casual)"),
            jp("食べよう / 行こう"),
        ],
        [
            jp("verb stem + ましょう"),
            jp("let's (polite)"),
            jp("食べましょう"),
        ],
        [
            jp("たら/ば + どう"),
            jp("how about...?"),
            jp("行ったらどう"),
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

    # --- たい — Want to Do ---
    tai_data = [
        ["", "Positive", "Negative"],
        ["Non-Past", jp("行きたい"), jp("行きたくない")],
        ["Past", jp("行きたかった"), jp("行きたくなかった")],
    ]
    tai_rows = [
        [cell(c, bold=(ri == 0 or ci == 0), center=True, sz=8) for ci, c in enumerate(row)]
        for ri, row in enumerate(tai_data)
    ]
    tw = (W - 24 * mm) / 2
    tai_t = Table(tai_rows, colWidths=[24 * mm, tw, tw])
    tai_t.setStyle(
        TableStyle(
            TABLE_STYLE
            + [
                ("BACKGROUND", (0, 1), (0, -1), CR1),
            ]
        )
    )
    tai_notes: list = [Spacer(1, 1 * mm)]
    tai_notes += [
        Paragraph(
            jp("Add たい to verb stem. Becomes an i-adjective but retains verb particles (を, に, へ, で)."),
            note_s,
        ),
        Paragraph(jp("何をしたいですか。 — What do you want to do?"), ex_s),
        Paragraph(jp("温泉に行きたい。 — I want to go to hot spring."), ex_s),
        Paragraph(jp("ケーキ、食べたくないの？ — You don't want to eat cake?"), ex_s),
        Paragraph(
            jp("食べたくなかったけど食べたくなった。 — I didn't want to eat it but I became wanting to eat."),
            ex_s,
        ),
        Paragraph(
            jp('Only for first person. For others, use "I think he wants to..." OK in questions.'),
            note_s,
        ),
        Paragraph(jp("ずっと一緒にいたい。 — I want to be together forever."), ex_s),
        Paragraph(jp("犬と遊びたいですか。 — Do you want to play with dog?"), ex_s),
    ]
    story.append(section(jp("たい — Want to Do"), tai_t, *tai_notes))
    story.append(Spacer(1, 3.5 * mm))

    # --- 欲しい — Want Something / Want Done ---
    hoshii_notes: list = [Spacer(1, 1 * mm)]
    hoshii_notes += [
        Paragraph(
            jp("欲しい is an i-adjective (like 好き). Noun + が + 欲しい = want something."),
            note_s,
        ),
        Paragraph(jp("大きい縫いぐるみが欲しい！ — I want a big stuffed doll!"), ex_s),
        Paragraph(
            jp("Te-form + ほしい = want something done. Written in hiragana after te-form."),
            note_s,
        ),
        Paragraph(jp("全部食べてほしいんだけど・・・。 — I want it all eaten but..."), ex_s),
        Paragraph(jp("部屋をきれいにしてほしいのよ。 — I want the room cleaned up, you know."), ex_s),
    ]
    story.append(section(jp("欲しい — Want Something / Want Done"), *hoshii_notes))
    story.append(Spacer(1, 3.5 * mm))

    # --- Conjugation table helper ---
    def conj_tbl(data, cw):
        rows = [
            [cell(c, bold=(ri == 0), center=True, sz=8) for ci, c in enumerate(row)]
            for ri, row in enumerate(data)
        ]
        t = Table(rows, colWidths=cw)
        t.setStyle(TableStyle(TABLE_STYLE))
        return t

    # --- Volitional Form — Casual ---
    ru_data = [
        ["Plain", "Volitional"],
        [jp("食べる"), jp("食べよう")],
        [jp("着る"), jp("着よう")],
        [jp("信じる"), jp("信じよう")],
        [jp("寝る"), jp("寝よう")],
        [jp("起きる"), jp("起きよう")],
        [jp("出る"), jp("出よう")],
        [jp("掛ける"), jp("掛けよう")],
        [jp("捨てる"), jp("捨てよう")],
        [jp("調べる"), jp("調べよう")],
    ]
    u_data = [
        ["Plain", "Volitional"],
        [jp("話す"), jp("話そう")],
        [jp("聞く"), jp("聞こう")],
        [jp("泳ぐ"), jp("泳ごう")],
        [jp("遊ぶ"), jp("遊ぼう")],
        [jp("待つ"), jp("待とう")],
        [jp("飲む"), jp("飲もう")],
        [jp("直る"), jp("直ろう")],
        [jp("死ぬ"), jp("死のう")],
        [jp("買う"), jp("買おう")],
    ]
    exc_data = [
        ["Plain", "Volitional"],
        [jp("する"), jp("しよう")],
        [jp("くる"), jp("こよう")],
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

    vol_notes: list = [Spacer(1, 1 * mm)]
    vol_notes += [
        Paragraph(
            jp("ru-verbs: remove る, add よう. u-verbs: replace /u/ with /o/, add う."),
            note_s,
        ),
        Paragraph(jp("今日は何をしようか？ — What shall (we) do today?"), ex_s),
        Paragraph(jp("テーマパークに行こう！ — Let's go to theme park!"), ex_s),
        Paragraph(jp("明日は何を食べようか？ — What shall (we) eat tomorrow?"), ex_s),
        Paragraph(jp("カレーを食べよう！ — Let's eat curry!"), ex_s),
    ]
    story.append(section(jp("Volitional Form — Casual"), outer, *vol_notes))
    story.append(Spacer(1, 3.5 * mm))

    # --- Volitional Form — Polite ---
    pol_data = [
        ["Plain", "Volitional"],
        [jp("する"), jp("しましょう")],
        [jp("くる"), jp("きましょう")],
        [jp("寝る"), jp("寝ましょう")],
        [jp("行く"), jp("行きましょう")],
        [jp("遊ぶ"), jp("遊びましょう")],
    ]
    pol_t = conj_tbl(pol_data, [30 * mm, 36 * mm])

    pol_notes: list = [Spacer(1, 1 * mm)]
    pol_notes += [
        Paragraph(jp("Add ましょう to verb stem. Must come at end of sentence."), note_s),
        Paragraph(jp("今日は何をしましょうか？ — What shall (we) do today?"), ex_s),
        Paragraph(jp("テーマパークに行きましょう！ — Let's go to theme park!"), ex_s),
        Paragraph(jp("カレーを食べましょう！ — Let's eat curry!"), ex_s),
    ]
    story.append(section(jp("Volitional Form — Polite"), pol_t, *pol_notes))
    story.append(Spacer(1, 3.5 * mm))

    # --- Making Suggestions — ば/たら + どう ---
    sug_notes: list = [Spacer(1, 1 * mm)]
    sug_notes += [
        Paragraph(
            jp('ば/たら conditional + どう = "How about doing X?" A commonly used set phrase.'),
            note_s,
        ),
        Paragraph(jp("銀行に行ったらどうですか。 — How about going to bank?"), ex_s),
        Paragraph(
            jp("たまにご両親と話せばどう？ — How about talking with your parents once in a while?"), ex_s
        ),
    ]
    story.append(section(jp("Making Suggestions — ば/たら + どう"), *sug_notes))
    story.append(Spacer(1, 3.5 * mm))

    # --- Notes ---
    final_notes: list = [Spacer(1, 1 * mm)]
    for n in [
        jp("たい: add to verb stem → i-adj. Verb particles still work. First person only (or questions)."),
        jp("欲しい: i-adj. Noun+が+欲しい = want thing. Te-form+ほしい = want done."),
        jp("Volitional casual: ru-verbs る→よう. u-verbs /u/→/o/+う. する→しよう, くる→こよう."),
        jp("Volitional polite: verb stem + ましょう. Must end the sentence."),
        jp('Suggestions: ば/たら + どう = "How about doing X?"'),
    ]:
        final_notes.append(Paragraph(f"- {n}", note_s))
    story.append(section("Notes", *final_notes))

    return story
