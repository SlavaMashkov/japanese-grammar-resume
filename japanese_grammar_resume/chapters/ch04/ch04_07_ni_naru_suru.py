from ...styles import *


def build():
    story = []

    story.append(PageBreak())
    story.append(
        Paragraph(
            jp("4.7  Using する and なる with the に Particle  （〜[よう]になる／する）"),
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
                    "上手",
                    "有名",
                    "ハンバーガー",
                    "サラダ",
                    "他",
                    "やはり",
                    "これ",
                    "去年",
                    "背",
                    "強い",
                    "頭",
                    "海外",
                    "寿司",
                    "一年間",
                    "練習",
                    "ピアノ",
                    "弾く",
                    "地下",
                ]
            )
        )
    )
    story.append(Spacer(1, 3.5 * mm))

    # --- Summary Table ---
    sum_data = [
        ["Pattern", "Meaning", "Example"],
        [
            jp("Noun/Na-adj + になる"),
            jp("become X"),
            jp("医者になった (became a doctor)"),
        ],
        [
            jp("Noun + にする"),
            jp("decide on X"),
            jp("ハンバーガーにする (I'll have hamburger)"),
        ],
        [
            jp("i-adj く + なる"),
            jp("become [adj]"),
            jp("高くなった (became taller)"),
        ],
        [
            jp("Verb + ことになる"),
            jp("it's been decided"),
            jp("行くことになった"),
        ],
        [
            jp("Verb + ことにする"),
            jp("decide to"),
            jp("行くことにした"),
        ],
        [
            jp("Verb + ようになる"),
            jp("come to / become able"),
            jp("食べられるようになった"),
        ],
        [
            jp("Verb + ようにする"),
            jp("try to / make effort"),
            jp("食べるようにする"),
        ],
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
    story.append(section(jp("Patterns with になる and にする"), sum_t))
    story.append(Spacer(1, 3.5 * mm))

    # --- なる and する with Nouns / Na-adj ---
    noun_notes: list = [Spacer(1, 1 * mm)]
    noun_notes += [
        Paragraph(jp("Noun/na-adj + になる = become X. Works as expected."), note_s),
        Paragraph(jp("彼の日本語が上手になった。 — His Japanese has become skillful."), ex_s),
        Paragraph(jp("私は医者になった。 — I became a doctor."), ex_s),
        Paragraph(jp("私は有名な人になる。 — I will become a famous person."), ex_s),
        Paragraph(
            jp("Noun + にする = decide on X. Common when ordering from a menu."),
            note_s,
        ),
        Paragraph(
            jp("私は、ハンバーガーとサラダにします。 — I'll have the hamburger and salad."),
            ex_s,
        ),
        Paragraph(
            jp("他にいいものがたくさんあるけど、やっぱりこれにする。"),
            ex_s,
        ),
        Paragraph(
            jp("— There are a lot of other good things, but as I thought, I'll go with this one."), ex_s
        ),
    ]
    story.append(section(jp("なる and する with Nouns / Na-adj"), *noun_notes))
    story.append(Spacer(1, 3.5 * mm))

    # --- なる with i-adjectives ---
    iadj_notes: list = [Spacer(1, 1 * mm)]
    iadj_notes += [
        Paragraph(
            jp("に targets nouns/na-adj. For i-adj, use the adverb form (く) instead."),
            note_s,
        ),
        Paragraph(
            jp("去年から背が高くなったね。 — Your height has gotten taller from last year, huh?"), ex_s
        ),
        Paragraph(jp("運動しているから、強くなる。 — I will become stronger because I am exercising."), ex_s),
        Paragraph(
            jp("勉強をたくさんしたから、頭がよくなった。 — Since I studied a lot, I became smarter."),
            ex_s,
        ),
    ]
    story.append(section(jp("なる with i-adjectives"), *iadj_notes))
    story.append(Spacer(1, 3.5 * mm))

    # --- なる and する with Verbs ---
    verb_notes: list = [Spacer(1, 1 * mm)]
    verb_notes += [
        Paragraph(
            jp(
                "Can't directly modify a verb with なる/する. Use generic nouns: こと (event) or よう (manner)."
            ),
            note_s,
        ),
        Paragraph(
            jp("Verb + ことになる = it has been decided. Verb + ことにする = I decided."),
            note_s,
        ),
        Paragraph(jp("海外に行くことになった。 — It's been decided that I will go abroad."), ex_s),
        Paragraph(jp("海外に行くことにした。 — I decided I will go abroad."), ex_s),
        Paragraph(
            jp("Verb + ようになる = it came to be that... Verb + ようにする = make effort to..."),
            note_s,
        ),
        Paragraph(
            jp("毎日、肉を食べるようになった。 — It became so that I eat meat everyday."),
            ex_s,
        ),
        Paragraph(jp("毎日、肉を食べるようにする。 — I will try to eat meat everyday."), ex_s),
        Paragraph(
            jp("Potential + ようになる is common — describes becoming able to do something."),
            note_s,
        ),
        Paragraph(
            jp(
                "日本に来て、寿司が食べられるようになった。 — After coming to Japan, I became able to eat sushi."
            ),
            ex_s,
        ),
        Paragraph(
            jp("一年間練習したから、ピアノが弾けるようになった。"),
            ex_s,
        ),
        Paragraph(jp("— Because I practiced for one year, I became able to play the piano."), ex_s),
        Paragraph(
            jp(
                "地下に入って、富士山が見えなくなった。 — After going underground, Fuji-san became not visible."
            ),
            ex_s,
        ),
    ]
    story.append(section(jp("なる and する with Verbs"), *verb_notes))
    story.append(Spacer(1, 3.5 * mm))

    # --- Notes ---
    final_notes: list = [Spacer(1, 1 * mm)]
    for n in [
        jp("Noun/na-adj + になる = become. Noun + にする = decide on (e.g. ordering from menu)."),
        jp("i-adj: use adverb form (く) + なる. いい → よくなる."),
        jp("Verb + ことになる = it's been decided. Verb + ことにする = I decided."),
        jp("Verb + ようになる = come to (change of state). Verb + ようにする = try to / make effort."),
        jp("Potential + ようになる = became able to. 食べられるようになった = became able to eat."),
    ]:
        final_notes.append(Paragraph(f"- {n}", note_s))
    story.append(section("Notes", *final_notes))

    return story
