from ...styles import *


def build():
    story = []

    story.append(PageBreak())
    story.append(
        Paragraph(
            jp("4.6  Potential Form  （可能形）"),
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
                        "出来る",
                        "信じる",
                        "掛ける",
                        "調べる",
                        "取る",
                        "漢字",
                        "残念",
                        "富士山",
                        "登る",
                        "重い",
                        "荷物",
                        "見える",
                        "聞こえる",
                        "晴れる",
                        "おかげ",
                        "ただ",
                        "久しぶり",
                        "周り",
                        "うるさい",
                        "有り得る",
                        "寝坊",
                        "それ",
                    ]
                )
            ),
        )
    )
    story.append(Spacer(1, 3.5 * mm))

    # --- Conjugation Rules ---
    rules_data = [
        ["Type", "Rule", "Example"],
        ["ru-verbs", jp("Replace る with られる"), jp("見る → 見られる")],
        ["u-verbs", jp("Change /u/ to /e/ vowel\nand add る"), jp("遊ぶ → 遊べ → 遊べる")],
        [jp("する (exception)"), jp("Becomes できる"), jp("する → できる")],
        [jp("くる (exception)"), jp("Becomes こられる"), jp("くる → こられる")],
    ]
    rules_rows = [
        [cell(c, bold=(ri == 0), center=(ri == 0 or ci == 0), sz=8) for ci, c in enumerate(row)]
        for ri, row in enumerate(rules_data)
    ]
    rw = (W - 30 * mm) / 2
    rules_t = Table(rules_rows, colWidths=[30 * mm, rw, rw])
    rules_t.setStyle(
        TableStyle(
            TABLE_STYLE
            + [
                ("BACKGROUND", (0, 1), (0, -1), CR1),
                ("FONTNAME", (0, 1), (0, -1), "DV-B"),
            ]
        )
    )
    rules_notes: list = [Spacer(1, 1 * mm)]
    rules_notes += [
        Paragraph(jp("All potential verbs become ru-verbs."), note_s),
        Paragraph(
            jp("Casual: ru-verbs can drop ら (食べられる → 食べれる). Common but considered slang."),
            note_s,
        ),
    ]
    story.append(section(jp("Conjugation Rules"), rules_t, *rules_notes))
    story.append(Spacer(1, 3.5 * mm))

    # --- Sample Conjugations (three tables side by side) ---
    GAP = 2 * mm
    tw = (W - 2 * GAP) / 3
    cw_half = tw / 2
    ts = TableStyle(TABLE_STYLE)

    def conj_sub(data):
        rows = [
            [cell(c, bold=(ri == 0), center=(ri == 0), sz=8) for ci, c in enumerate(row)]
            for ri, row in enumerate(data)
        ]
        t = Table(rows, colWidths=[cw_half, cw_half])
        t.setStyle(ts)
        return t

    ru_t = conj_sub(
        [
            ["Plain", "Potential"],
            [jp("食べる"), jp("食べられる")],
            [jp("着る"), jp("着られる")],
            [jp("信じる"), jp("信じられる")],
            [jp("寝る"), jp("寝られる")],
            [jp("起きる"), jp("起きられる")],
            [jp("出る"), jp("出られる")],
            [jp("掛ける"), jp("掛けられる")],
            [jp("調べる"), jp("調べられる")],
        ]
    )
    u_t = conj_sub(
        [
            ["Plain", "Potential"],
            [jp("話す"), jp("話せる")],
            [jp("書く"), jp("書ける")],
            [jp("遊ぶ"), jp("遊べる")],
            [jp("待つ"), jp("待てる")],
            [jp("飲む"), jp("飲める")],
            [jp("取る"), jp("取れる")],
            [jp("死ぬ"), jp("死ねる")],
            [jp("買う"), jp("買える")],
        ]
    )
    ex_t = conj_sub(
        [
            ["Plain", "Potential"],
            [jp("する"), jp("できる")],
            [jp("くる"), jp("こられる")],
        ]
    )
    outer = Table(
        [[ru_t, "", u_t, "", ex_t]],
        colWidths=[tw, GAP, tw, GAP, tw],
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
    story.append(section(jp("Sample Conjugations"), outer))
    story.append(Spacer(1, 3.5 * mm))

    # --- Examples ---
    ex_notes: list = [Spacer(1, 1 * mm)]
    ex_notes += [
        Paragraph(jp("漢字は書けますか？ — Can you write kanji?"), ex_s),
        Paragraph(jp("残念だが、今週末は行けない。 — It's unfortunate, but can't go this weekend."), ex_s),
        Paragraph(jp("もう信じられない。 — I can't believe it already."), ex_s),
    ]
    story.append(section(jp("Examples"), *ex_notes))
    story.append(Spacer(1, 3.5 * mm))

    # --- Potential Forms Do Not Have Direct Objects ---
    obj_notes: list = [Spacer(1, 1 * mm)]
    obj_notes += [
        Paragraph(
            jp("Potential form describes a state, not an action — do not use を for the direct object."),
            note_s,
        ),
        Paragraph(jp("富士山を登れた。 → 富士山が登れた。 — Was able to climb Fuji-san."), ex_s),
        Paragraph(jp("重い荷物を持てます。 → 重い荷物は持てます。 — Am able to hold heavy baggage."), ex_s),
    ]
    story.append(section(jp("No Direct Objects with Potential"), *obj_notes))
    story.append(Spacer(1, 3.5 * mm))

    # --- 見える and 聞こえる ---
    mieru_notes: list = [Spacer(1, 1 * mm)]
    mieru_notes += [
        Paragraph(
            jp(
                "見える = visible (naturally). 聞こえる = audible (naturally). These are not potential forms."
            ),
            note_s,
        ),
        Paragraph(
            jp("Use 見える / 聞こえる for natural ability; 見られる / 聞ける for given opportunity."), note_s
        ),
        Paragraph(jp("今日は晴れて、富士山が見える。 — Cleared up today and Fuji-san is visible."), ex_s),
        Paragraph(
            jp(
                "友達のおかげで、映画はただで見られた。 — Thanks to friend, was able to watch movie for free."
            ),
            ex_s,
        ),
        Paragraph(jp("Alternatively: 映画をただで見ることができた。 (using こと + できる)"), note_s),
        Paragraph(
            jp("久しぶりに彼の声が聞けた。 — Was able to hear his voice for the first time in a long time."),
            ex_s,
        ),
        Paragraph(jp("周りがうるさくて、彼が言っていることがあんまり聞こえなかった。"), ex_s),
        Paragraph(jp("— Surroundings were noisy and couldn't hear what he was saying very well."), ex_s),
    ]
    story.append(section(jp("見える and 聞こえる"), *mieru_notes))
    story.append(Spacer(1, 3.5 * mm))

    # --- ある Exception — 有り得る ---
    aru_notes: list = [Spacer(1, 1 * mm)]
    aru_notes += [
        Paragraph(
            jp("ある + 得る = 有り得る — something can possibly exist. Read as ありうる or ありえる."),
            note_s,
        ),
        Paragraph(jp("Other conjugations only use え: ありえない、ありえた、ありえなかった."), note_s),
        Paragraph(jp("そんなことはありえる。 — That kind of situation is possible."), ex_s),
        Paragraph(jp("そんなことはありえない。 — That kind of situation is not possible."), ex_s),
        Paragraph(jp("彼が寝坊したこともありうるね。 — It's also possible that he overslept."), ex_s),
        Paragraph(jp("それは、ありえない話だよ。 — That's an impossible story/scenario."), ex_s),
    ]
    story.append(section(jp("ある Exception — 有り得る"), *aru_notes))
    story.append(Spacer(1, 3.5 * mm))

    # --- Notes ---
    final_notes: list = [Spacer(1, 1 * mm)]
    for n in [
        jp("Potential form: ru-verbs る→られる, u-verbs /u/→/e/+る, する→できる, くる→こられる."),
        jp("All potential verbs become ru-verbs. Casual: ru-verbs drop ら (食べれる)."),
        jp("Potential form = state, not action. Use が/は instead of を for the object."),
        jp("見える = visible, 聞こえる = audible (natural). 見られる / 聞ける = given opportunity."),
        jp("有り得る (ありうる/ありえる) = can possibly exist. Conjugations use え only."),
    ]:
        final_notes.append(Paragraph(f"- {n}", note_s))
    story.append(section("Notes", *final_notes))

    return story
