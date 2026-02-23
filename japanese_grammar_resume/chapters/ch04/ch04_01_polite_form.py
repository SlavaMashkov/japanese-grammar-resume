from ...styles import *


def build():
    story = []

    story.append(PageBreak())
    story.append(Paragraph(jp("4.1  Polite Form and Verb Stems  （〜です、〜ます）"), title_s))
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
                    "丁寧語",
                    "尊敬語",
                    "謙譲語",
                    "はい",
                    "いいえ",
                    "怒る",
                    "鉄拳",
                    "休み",
                    "楽しむ",
                    "走り出す",
                    "替える",
                    "着替える",
                    "加える",
                    "付け加える",
                    "言う",
                    "言い出す",
                    "子犬",
                    "とても",
                    "昨日",
                    "その",
                    "思う",
                    "答える",
                ]
            )
        )
    )
    story.append(Spacer(1, 3.5 * mm))

    # --- Grammar: Verb Stem Rules ---
    stem_data = [
        ["Type", "Rule", "Example"],
        ["ru-verb", "Remove る", "食べる → 食べ"],
        ["u-verb", "Change /u/ vowel to /i/ vowel", "泳ぐ → 泳ぎ"],
        ["する", "Exception → し", "する → し"],
        ["くる", "Exception → き", "来る → き"],
    ]
    stem_rows = [
        [cell(c, bold=(ri == 0), center=(ri == 0 or ci == 0), sz=8) for ci, c in enumerate(row)]
        for ri, row in enumerate(stem_data)
    ]
    hw = (W - 28 * mm) / 2
    stem_t = Table(stem_rows, colWidths=[28 * mm, hw, hw])
    stem_t.setStyle(
        TableStyle(
            TABLE_STYLE
            + [
                ("BACKGROUND", (0, 1), (0, -1), CR1),
                ("FONTNAME", (0, 1), (0, -1), "DV-B"),
            ]
        )
    )
    story.append(section("Grammar: Verb Stem Rules", stem_t))
    story.append(Spacer(1, 3.5 * mm))

    # --- Grammar: ます Conjugation ---
    masu_data = [
        ["Tense", "ます conjugation", "Stem + ます"],
        ["Plain", "ます", "遊びます"],
        ["Negative", "ません", "遊びません"],
        ["Past", "ました", "遊びました"],
        ["Past-Neg", "ませんでした", "遊びませんでした"],
    ]
    masu_rows = [
        [cell(c, bold=(ri == 0), center=(ri == 0 or ci == 0), sz=8) for ci, c in enumerate(row)]
        for ri, row in enumerate(masu_data)
    ]
    cw_masu = [28 * mm, (W - 28 * mm) / 2, (W - 28 * mm) / 2]
    masu_t = Table(masu_rows, colWidths=cw_masu)
    masu_t.setStyle(
        TableStyle(
            TABLE_STYLE
            + [
                ("BACKGROUND", (0, 1), (0, -1), CR1),
                ("FONTNAME", (0, 1), (0, -1), "DV-B"),
            ]
        )
    )
    story.append(section(jp("Grammar: ます Conjugation"), masu_t))
    story.append(Spacer(1, 3.5 * mm))

    # --- Grammar: です Conjugation — i-adjective ---
    desu_i_data = [
        ["Tense", "Casual", "Polite"],
        ["Plain", "かわいい", "かわいいです"],
        ["Negative", "かわいくない", "かわいくないです"],
        ["Past", "かわいかった", "かわいかったです"],
        ["Past-Neg", "かわいくなかった", "かわいくなかったです"],
    ]
    desu_i_rows = [
        [cell(c, bold=(ri == 0), center=(ri == 0 or ci == 0), sz=8) for ci, c in enumerate(row)]
        for ri, row in enumerate(desu_i_data)
    ]
    cw_desu = [28 * mm, (W - 28 * mm) / 2, (W - 28 * mm) / 2]
    desu_i_t = Table(desu_i_rows, colWidths=cw_desu)
    desu_i_t.setStyle(
        TableStyle(
            TABLE_STYLE
            + [
                ("BACKGROUND", (0, 1), (0, -1), CR1),
                ("FONTNAME", (0, 1), (0, -1), "DV-B"),
            ]
        )
    )
    story.append(section(jp("Grammar: です Conjugation — i-adjective"), desu_i_t))
    story.append(Spacer(1, 3.5 * mm))

    # --- Grammar: です Conjugation — na-adj / noun ---
    desu_na_data = [
        ["Tense", "Casual", "Polite"],
        ["Plain", "静か（だ）", "静かです"],
        ["Negative", "静かじゃない", "静かじゃないです"],
        ["Past", "静かだった", "静かでした"],
        ["Past-Neg", "静かじゃなかった", "静かじゃなかったです"],
    ]
    desu_na_rows = [
        [cell(c, bold=(ri == 0), center=(ri == 0 or ci == 0), sz=8) for ci, c in enumerate(row)]
        for ri, row in enumerate(desu_na_data)
    ]
    desu_na_t = Table(desu_na_rows, colWidths=cw_desu)
    desu_na_t.setStyle(
        TableStyle(
            TABLE_STYLE
            + [
                ("BACKGROUND", (0, 1), (0, -1), CR1),
                ("FONTNAME", (0, 1), (0, -1), "DV-B"),
            ]
        )
    )
    story.append(section(jp("Grammar: です Conjugation — na-adj / noun"), desu_na_t))
    story.append(Spacer(1, 3.5 * mm))

    # --- Grammar: Formal Negative (ありません alternative) ---
    formal_data = [
        ["Tense", "Casual", "Polite"],
        ["i-adj Neg", "かわいくない", "かわいくありません"],
        ["i-adj Past-Neg", "かわいくなかった", "かわいくありませんでした"],
        ["na-adj Neg", "静かじゃない", "静かじゃありません"],
        ["na-adj Past-Neg", "静かじゃなかった", "静かじゃありませんでした"],
    ]
    formal_rows = [
        [cell(c, bold=(ri == 0), center=(ri == 0 or ci == 0), sz=8) for ci, c in enumerate(row)]
        for ri, row in enumerate(formal_data)
    ]
    cw_formal = [35 * mm, (W - 35 * mm) / 2, (W - 35 * mm) / 2]
    formal_t = Table(formal_rows, colWidths=cw_formal)
    formal_t.setStyle(
        TableStyle(
            TABLE_STYLE
            + [
                ("BACKGROUND", (0, 1), (0, -1), CR1),
                ("FONTNAME", (0, 1), (0, -1), "DV-B"),
            ]
        )
    )
    story.append(section(jp("Grammar: Formal Negative （ありません alternative）"), formal_t))
    story.append(Spacer(1, 3.5 * mm))

    # --- Notes ---
    final_notes = [Spacer(1, 1 * mm)]
    for n in [
        jp("Polite speech (丁寧語) is used with strangers and social superiors."),
        jp("Verb stem = drop る for ru-verbs, change /u/→/i/ for u-verbs."),
        jp("Stem + ます for polite verbs; です for polite nouns/adjectives."),
        jp("For i-adjectives, だ cannot be used; for na-adj/noun, remove だ before adding です."),
        jp('Formal negative replaces ないです with ありません (stiff but grammatically "correct").'),
        jp(
            "です ≠ だ: だ is declarative and used inside relative clauses; です shows politeness at sentence end only."
        ),
    ]:
        final_notes.append(Paragraph(f"- {n}", note_s))
    story.append(section("Notes", *final_notes))

    return story
