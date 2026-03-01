from ...styles import *


def build():
    story = []

    story.append(PageBreak())
    story.append(
        Paragraph(
            jp("4.13  Trying / Attempting to Do Something  （〜てみる、volitional+とする）"),
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
                        "切る",
                        "お好み焼き",
                        "初めて",
                        "眠い",
                        "広島",
                        "避ける",
                        "無理矢理",
                        "徹夜",
                        "止める",
                        "なるべく",
                        "ジム",
                        "決める",
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
            jp("te-form + みる"),
            jp("try doing (try out)"),
            jp("食べてみる"),
        ],
        [
            jp("volitional + とする"),
            jp("attempt to do"),
            jp("入ろうとする"),
        ],
        [
            jp("volitional + と思う"),
            jp("thought to attempt"),
            jp("避けようと思った"),
        ],
        [
            jp("volitional + と決める"),
            jp("decided to attempt"),
            jp("行こうと決めた"),
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

    # --- てみる — To Try Something Out ---
    try_notes: list = [Spacer(1, 1 * mm)]
    try_notes += [
        Paragraph(
            jp(
                "Te-form + みる = try doing something to see the result. Written in hiragana. Conjugates like 見る."
            ),
            note_s,
        ),
        Paragraph(jp("切る → 切って → 切ってみる / 切ってみた / 切ってみない / 切ってみなかった"), ex_s),
        Paragraph(
            jp(
                "お好み焼きを初めて食べてみたけど、とてもおいしかった！ — I tried eating okonomiyaki for the first time and it was very tasty!"
            ),
            ex_s,
        ),
        Paragraph(
            jp(
                "お酒を飲んでみましたが、すごく眠くなりました。 — I tried drinking alcohol and I became extremely sleepy."
            ),
            ex_s,
        ),
        Paragraph(
            jp("新しいデパートに行ってみる。 — I'm going to check out the new department store."), ex_s
        ),
        Paragraph(
            jp("広島のお好み焼きを食べてみたい！ — I want to try eating Hiroshima okonomiyaki!"),
            ex_s,
        ),
    ]
    story.append(section(jp("てみる — To Try Something Out"), *try_notes))
    story.append(Spacer(1, 3.5 * mm))

    # --- volitional + とする — To Attempt ---
    att_notes: list = [Spacer(1, 1 * mm)]
    att_notes += [
        Paragraph(
            jp("Volitional form + とする = attempt to do. An extension of quoted clause + する."),
            note_s,
        ),
        Paragraph(
            jp("毎日、勉強を避けようとする。 — Everyday, she attempts to avoid study."),
            ex_s,
        ),
        Paragraph(
            jp("無理矢理に部屋に入ろうとしている。 — He is attempting to force his way into the room."),
            ex_s,
        ),
        Paragraph(
            jp(
                "早く寝ようとしたけど、結局は徹夜した。 — I attempted to sleep early but ended up staying up all night."
            ),
            ex_s,
        ),
        Paragraph(
            jp(
                "お酒を飲もうとしたが、奥さんが止めた。 — He tried to drink alcohol but his wife stopped him."
            ),
            ex_s,
        ),
        Paragraph(
            jp(
                "Can use other verbs instead of する: 思う (thought to attempt), 決める (decided to attempt)."
            ),
            note_s,
        ),
        Paragraph(
            jp(
                "勉強をなるべく避けようと思った。 — I thought I would attempt to avoid studying as much as possible."
            ),
            ex_s,
        ),
        Paragraph(jp("毎日ジムに行こうと決めた。 — Decided to attempt to go to gym everyday."), ex_s),
    ]
    story.append(section(jp("volitional + とする — To Attempt"), *att_notes))
    story.append(Spacer(1, 3.5 * mm))

    # --- Notes ---
    final_notes: list = [Spacer(1, 1 * mm)]
    for n in [
        jp("てみる = try doing (to see result). Te-form + みる in hiragana. Conjugates like 見る."),
        jp("volitional + とする = attempt to do. Extension of quoted clause + する."),
        jp("Can replace する with 思う (thought to attempt) or 決める (decided to attempt)."),
        jp(
            'てみる: "I tried the cherry flavor." とする: "I tried to do homework." Different meanings of "try".'
        ),
    ]:
        final_notes.append(Paragraph(f"- {n}", note_s))
    story.append(section("Notes", *final_notes))

    return story
