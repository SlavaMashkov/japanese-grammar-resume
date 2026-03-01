from ...styles import *


def build():
    story = []

    story.append(PageBreak())
    story.append(
        Paragraph(
            jp("4.18  More Sentence-Ending Particles  （文末助詞）"),
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
                        "込む",
                        "一体",
                        "何時",
                        "つもり",
                        "土曜日",
                        "終わり",
                        "覚える",
                        "間違える",
                        "表現",
                        "来週",
                    ]
                )
            ),
        )
    )
    story.append(Spacer(1, 3.5 * mm))

    # --- Patterns Overview ---
    sum_data = [
        ["Particle", "Usage", "Gender"],
        [jp("さ"), jp("filler (like よ, very casual)"), jp("neutral")],
        [jp("な"), jp("seeking explanation / wondering"), jp("rough (male)")],
        [jp("かな"), jp("I wonder if…"), jp("neutral")],
        [jp("かい"), jp("yes/no question (masculine)"), jp("male")],
        [jp("だい"), jp("open-ended question (masculine)"), jp("male")],
        [jp("わ"), jp("emphasis (feminine)"), jp("female")],
        [jp("かしら"), jp("I wonder (= かな, feminine)"), jp("female")],
        [jp("ぞ"), jp('emphasis ("cool" / manly)'), jp("male")],
        [jp("ぜ"), jp('emphasis ("cool" / manly)'), jp("male")],
    ]
    sum_rows = [
        [cell(c, bold=(ri == 0), center=(ri == 0 or ci == 0), sz=7) for ci, c in enumerate(row)]
        for ri, row in enumerate(sum_data)
    ]
    sw = (W - 22 * mm) / 2
    sum_t = Table(sum_rows, colWidths=[22 * mm, sw, sw])
    sum_t.setStyle(
        TableStyle(
            TABLE_STYLE
            + [
                ("BACKGROUND", (0, 1), (0, -1), CR1),
                ("FONTNAME", (0, 1), (0, -1), "DV-B"),
            ]
        )
    )
    story.append(section(jp("Particles Overview"), sum_t))
    story.append(Spacer(1, 3.5 * mm))

    # --- さ and な ---
    sa_notes: list = [Spacer(1, 1 * mm)]
    sa_notes += [
        Paragraph(
            jp(
                'さ = very casual よ. Used as filler at end of phrases. Like English "like" — almost meaningless from overuse.'
            ),
            note_s,
        ),
        Paragraph(
            jp(
                "ディズニーランドに行ったんだけどさ、なんかさ、すごい込んでて… — I went to Disney Land, and like, it was really crowded…"
            ),
            ex_s,
        ),
        Paragraph(
            jp("な = rougher ね. Seeks explanation or expresses wondering. Male-leaning but not restricted."),
            note_s,
        ),
        Paragraph(
            jp("今、図書館に行くんだよな。 — You are going to the library now huh? (seeking explanation)"),
            ex_s,
        ),
        Paragraph(
            jp(
                "日本語は、たくさん勉強したけどな。まだ全然わからない。 — I studied Japanese a lot, right? But I still don't get it at all."
            ),
            ex_s,
        ),
        Paragraph(
            jp('かな = か + な. "I wonder if…" Speaker considering something.'),
            note_s,
        ),
        Paragraph(jp("今日は雨が降るかな？ — I wonder if it'll rain today."), ex_s),
        Paragraph(jp("いい大学に行けるかな？ — I wonder if I can go to a good college."), ex_s),
    ]
    story.append(section(jp("さ and な — Casual Particles"), *sa_notes))
    story.append(Spacer(1, 3.5 * mm))

    # --- かい and だい ---
    kai_notes: list = [Spacer(1, 1 * mm)]
    kai_notes += [
        Paragraph(
            jp("かい = masculine yes/no question. だい = masculine open-ended question. Strongly male."),
            note_s,
        ),
        Paragraph(jp("おい、どこに行くんだい？ — Hey, where are (you) going?"), ex_s),
        Paragraph(
            jp("さきちゃんって呼んでもいいかい？ — Can (I) call you Saki-chan?"),
            ex_s,
        ),
        Paragraph(
            jp(
                "一体何時に帰ってくるつもりだったんだい？ — What time were (you) planning on coming home exactly?"
            ),
            ex_s,
        ),
        Paragraph(
            jp(
                "俺は土曜日、映画を見に行くけど、一緒に行くかい？ — I'm going to see a movie Saturday, go together?"
            ),
            ex_s,
        ),
    ]
    story.append(section(jp("かい / だい — Masculine Questions"), *kai_notes))
    story.append(Spacer(1, 3.5 * mm))

    # --- Gender-Specific ---
    gen_notes: list = [Spacer(1, 1 * mm)]
    gen_notes += [
        Paragraph(
            jp("わ = emphasis (feminine). Different from Kansai わ. かしら = feminine かな (I wonder)."),
            note_s,
        ),
        Paragraph(jp("もう時間がないわ。 — There is no more time."), ex_s),
        Paragraph(jp("いい大学に入れるかしら？ — I wonder if I can enter a good college."), ex_s),
        Paragraph(
            jp('ぞ / ぜ = emphasis (masculine, "cool" / manly). Identical to よ but rougher.'),
            note_s,
        ),
        Paragraph(jp("おい、行くぞ！ — Hey, we're going!"), ex_s),
        Paragraph(jp("これで、もう終わりだぜ。 — With this, it's over already."), ex_s),
    ]
    story.append(section(jp("Gender-Specific Particles"), *gen_notes))
    story.append(Spacer(1, 3.5 * mm))

    # --- Combining Everything ---
    combo_notes: list = [Spacer(1, 1 * mm)]
    combo_notes += [
        Paragraph(
            jp(
                "At this point we can mix conjugations in various combinations to create complex expressions."
            ),
            note_s,
        ),
        Paragraph(
            jp(
                '「Hello」を日本語で何と言えばいいですか。 — If you say what for "Hello" in Japanese, is it ok?'
            ),
            ex_s,
        ),
        Paragraph(
            jp("何と言えば = quoted sub-clause + conditional of 言う."),
            note_s,
        ),
        Paragraph(
            jp(
                "英語を教えてもらいたいんだけどさ、もし時間があれば、教えてくれない？ — I want to receive the favor of being taught English; if you have time, won't you teach me?"
            ),
            ex_s,
        ),
        Paragraph(
            jp("教えてもらいたい = receiving favor + want (たい). 教えてくれない = negative request."),
            note_s,
        ),
        Paragraph(
            jp(
                "勉強を怠けたり来なかったりしないでね。 — Don't do things like shirk studies or not come, ok?"
            ),
            ex_s,
        ),
        Paragraph(
            jp("怠けたり来なかったりしないで = list of actions (～たりする) + negative request (ないで)."),
            note_s,
        ),
    ]
    story.append(section(jp("Combining Everything"), *combo_notes))
    story.append(Spacer(1, 3.5 * mm))

    # --- Notes ---
    final_notes: list = [Spacer(1, 1 * mm)]
    for n in [
        jp("さ = casual filler (like よ). な = rough ね (seeks explanation). かな = I wonder if."),
        jp("かい = masculine yes/no question. だい = masculine open-ended question."),
        jp("わ = feminine emphasis. かしら = feminine かな. ぞ/ぜ = masculine emphasis (rough よ)."),
        jp(
            "Mix conjugations freely: quoted clauses + conditionals, て-form + favors + たい, たり + requests."
        ),
    ]:
        final_notes.append(Paragraph(f"- {n}", note_s))
    story.append(section("Notes", *final_notes))

    return story
