from ...styles import *


def build():
    story = []

    story.append(PageBreak())
    story.append(Paragraph(jp("2.4  Katakana  （カタカナ）"), title_s))
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

    # --- Basic Kana ---
    story.append(section_header("Basic Kana"))
    story.append(Spacer(1, 1 * mm))

    lw = 14 * mm
    kw = (W - lw) / 5

    kata = [
        ["", "a", "i", "u", "e", "o"],
        ["", "ア", "イ", "ウ", "エ", "オ"],
        ["k", "カ", "キ", "ク", "ケ", "コ"],
        ["s", "サ", "シ", "ス", "セ", "ソ"],
        ["t", "タ", "チ", "ツ", "テ", "ト"],
        ["n", "ナ", "ニ", "ヌ", "ネ", "ノ"],
        ["h", "ハ", "ヒ", "フ", "ヘ", "ホ"],
        ["m", "マ", "ミ", "ム", "メ", "モ"],
        ["y", "ヤ", "", "ユ", "", "ヨ"],
        ["r", "ラ", "リ", "ル", "レ", "ロ"],
        ["w", "ワ", "", "", "", "ヲ"],
        ["", "ン", "", "", "", ""],
    ]
    kata_rows = [
        [
            cell(c, bold=(ri == 0), center=True, sz=(8 if ri == 0 or ci == 0 else 8))
            for ci, c in enumerate(row)
        ]
        for ri, row in enumerate(kata)
    ]
    kata_t = Table(kata_rows, colWidths=[lw, kw, kw, kw, kw, kw])
    kata_t.setStyle(
        TableStyle(
            TABLE_STYLE
            + [
                ("BACKGROUND", (0, 1), (0, -1), CR1),
                ("FONTNAME", (0, 1), (0, -1), "DV-B"),
            ]
        )
    )
    story.append(kata_t)
    story.append(Spacer(1, 3.5 * mm))

    # --- Additional Sounds (Small ア、イ、ウ、エ、オ) ---
    story.append(section_header(jp("Additional Sounds  （小さい ア・イ・ウ・エ・オ）")))
    story.append(Spacer(1, 1 * mm))

    add = [
        ["", "sh", "j", "t", "d", "ch", "f", "w", "v"],
        ["a", "シャ", "ジャ", "タ", "ダ", "チャ", "ファ", "ワ", "ヴァ"],
        ["i", "シ", "ジ", "ティ", "ディ", "チ", "フィ", "ウィ", "ヴィ"],
        ["u", "シュ", "ジュ", "トゥ", "ドゥ", "チュ", "フ", "ウ", "ヴ"],
        ["e", "シェ", "ジェ", "テ", "デ", "チェ", "フェ", "ウェ", "ヴェ"],
        ["o", "ショ", "ジョ", "ト", "ド", "チョ", "フォ", "ウォ", "ヴォ"],
    ]
    add_rows = [
        [
            cell(c, bold=(ri == 0), center=True, sz=(8 if ri == 0 or ci == 0 else 8))
            for ci, c in enumerate(row)
        ]
        for ri, row in enumerate(add)
    ]
    alw = 14 * mm
    akw = (W - alw) / 8
    add_t = Table(add_rows, colWidths=[alw] + [akw] * 8)
    add_t.setStyle(
        TableStyle(
            TABLE_STYLE
            + [
                ("BACKGROUND", (0, 1), (0, -1), CR1),
                ("FONTNAME", (0, 1), (0, -1), "DV-B"),
            ]
        )
    )
    story.append(add_t)
    story.append(Spacer(1, 3.5 * mm))

    # --- Sample Katakana Words ---
    story.append(section_header("Sample Katakana Words"))
    story.append(Spacer(1, 1 * mm))

    samples = [
        ["English", "Japanese"],
        ["America", "アメリカ"],
        ["Russia", "ロシア"],
        ["cheating", "カンニング (cunning)"],
        ["tour", "ツアー"],
        ["company employee", "サラリーマン (salary man)"],
        ["Mozart", "モーツァルト"],
        ["car horn", "クラクション (klaxon)"],
        ["sofa", "ソファ or ソファー"],
        ["Halloween", "ハロウィーン"],
        ["French fries", "フライドポテト (fried potato)"],
    ]
    sample_rows = [
        [cell(c, bold=(ri == 0), center=(ri == 0), sz=8) for ci, c in enumerate(row)]
        for ri, row in enumerate(samples)
    ]
    sw = W / 2
    sample_t = Table(sample_rows, colWidths=[sw, sw])
    sample_t.setStyle(TableStyle(TABLE_STYLE))
    story.append(sample_t)
    story.append(Spacer(1, 3.5 * mm))

    # --- Notes ---
    story.append(section_header("Notes"))
    story.append(Spacer(1, 1 * mm))
    for n in [
        "Same sounds as Hiragana — only the characters are different.",
        jp(
            "Long vowels use a dash ー instead of adding a kana."
            " キュート = cute, メール = email, ケーキ = cake."
        ),
        jp("ヲ is almost never used — を is only a particle and particles are written in Hiragana."),
        jp("Tricky look-alikes: シ/ン/ツ/ソ (horizontal vs vertical strokes), ノ/メ/ヌ, フ/ワ/ウ."),
        jp("・(middle dot) optionally separates words: ロック・アンド・ロール (rock and roll)."),
        "Forget the original English pronunciation — treat Katakana words as entirely Japanese.",
    ]:
        story.append(Paragraph(f"- {n}", note_s))

    return story
