from ...styles import *


def build():
    story = []

    story.append(PageBreak())
    story.append(
        Paragraph(
            jp("4.17  Casual Patterns and Slang  （カジュアルなパターンとスラング）"),
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
                        "つまらない",
                        "まったく",
                        "サラリーマン",
                        "残業",
                        "風呂",
                        "超",
                        "奴",
                        "負ける",
                        "近い",
                        "隣",
                    ]
                )
            ),
        )
    )
    story.append(Spacer(1, 3.5 * mm))

    # --- Patterns Overview ---
    sum_data = [
        ["Pattern", "Meaning", "Example"],
        [jp("Sound slurring"), jp("reduce mouth movement"), jp("つまんない = つまらない")],
        [jp("Particle dropping"), jp("casual omission"), jp("何それ？ = 何？それ？")],
        [jp("じゃん"), jp("confirmation (= じゃない)"), jp("いるじゃん！")],
        [jp("つ for という"), jp("rough という (male)"), jp("つうか = というか")],
        [jp("ってば / ったら"), jp("exasperation"), jp("もう行くってば！")],
        [jp("なんか"), jp("filler word (like)"), jp("なんか忙しいみたい")],
        [jp("～やがる"), jp("contempt for action"), jp("負けやがって")],
    ]
    sum_rows = [
        [cell(c, bold=(ri == 0), center=(ri == 0 or ci == 0), sz=7) for ci, c in enumerate(row)]
        for ri, row in enumerate(sum_data)
    ]
    sw = (W - 36 * mm) / 2
    sum_t = Table(sum_rows, colWidths=[36 * mm, sw, sw])
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

    # --- Basic Principles ---
    bp_notes: list = [Spacer(1, 1 * mm)]
    bp_notes += [
        Paragraph(
            jp(
                "Goal of slang: reduce mouth movement. Two methods: 1) shorten words, 2) slur sounds together."
            ),
            note_s,
        ),
        Paragraph(
            jp("ここはつまらないから私の家に行こう。 → ここつまんないから、私んち行こう。"),
            ex_s,
        ),
        Paragraph(
            jp(
                "まったく、いつまでこんなところで、ぐずぐずするんだよ。 → ったく、いつまでこんなとこで、ぐずぐずすんだよ。"
            ),
            ex_s,
        ),
    ]
    story.append(section(jp("Basic Principles of Slang"), *bp_notes))
    story.append(Spacer(1, 3.5 * mm))

    # --- Sentence Ordering & Particles ---
    so_notes: list = [Spacer(1, 1 * mm)]
    so_notes += [
        Paragraph(
            jp("Casual speech drops particles freely and reorders sentences — verb-first is OK."),
            note_s,
        ),
        Paragraph(jp("それは何？ → 何それ？ — What? That. (two fragments lumped as one)"), ex_s),
        Paragraph(jp("見た？あの人？ — Did you see? That guy?"), ex_s),
        Paragraph(
            jp("もう食べた？昨日買ったアイス。 — Ate it already? The ice cream I bought yesterday."), ex_s
        ),
    ]
    story.append(section(jp("Sentence Ordering & Particles"), *so_notes))
    story.append(Spacer(1, 3.5 * mm))

    # --- じゃん ---
    jan_notes: list = [Spacer(1, 1 * mm)]
    jan_notes += [
        Paragraph(
            jp('じゃん = abbreviated じゃない. Always confirms the positive (≈ "See, I\'m right?").'),
            note_s,
        ),
        Paragraph(
            jp(
                "Attaches to end of any sentence — noun, adjective, verb, adverb. Unlike じゃない (mature/feminine), じゃん is gender-neutral."
            ),
            note_s,
        ),
        Paragraph(
            jp(
                "ほら、やっぱりレポートを書かないとだめじゃん。 — See, as I thought, you have to write the report."
            ),
            ex_s,
        ),
        Paragraph(
            jp(
                "誰もいないからここで着替えてもいいじゃん。 — Since there's nobody, it's fine to change here."
            ),
            ex_s,
        ),
        Paragraph(jp("あっ！やっぱ、いるじゃん！ — Ah! See, he is here!"), ex_s),
        Paragraph(
            jp("じゃんか adds a questioning, confirming tone."),
            note_s,
        ),
        Paragraph(
            jp("駅の近くにカラオケがあるじゃんか。 — There's a karaoke near the station, right?"),
            ex_s,
        ),
    ]
    story.append(section(jp("じゃん — Confirmation"), *jan_notes))
    story.append(Spacer(1, 3.5 * mm))

    # --- つ for という ---
    tsu_notes: list = [Spacer(1, 1 * mm)]
    tsu_notes += [
        Paragraph(
            jp(
                "つ replaces という in rough/male speech. つう = という, つうか = というか. Sounds rougher than って."
            ),
            note_s,
        ),
        Paragraph(
            jp("つうか、なんでお前がここにいるんのよ！ — Or rather, why are you here?!"),
            ex_s,
        ),
        Paragraph(
            jp(
                "宿題で時間がないつってんのに、みきちゃんとデートしにいったらしい。 — Although he's saying he has no time due to homework, I hear he went on a date."
            ),
            ex_s,
        ),
        Paragraph(
            jp("だから、違うだつうの！ — Like I said, you're wrong!"),
            ex_s,
        ),
        Paragraph(
            jp("Extra small つ (っつう) adds even more emphasis."),
            note_s,
        ),
    ]
    story.append(section(jp("つ for という — Rough Speech"), *tsu_notes))
    story.append(Spacer(1, 3.5 * mm))

    # --- ってば / ったら ---
    tteba_notes: list = [Spacer(1, 1 * mm)]
    tteba_notes += [
        Paragraph(
            jp(
                'ってば = abbreviated といえば. ったら = abbreviated といったら. Expresses exasperation — "I told you already!"'
            ),
            note_s,
        ),
        Paragraph(jp("もう行くってば！ — I told you I'm going already!"), ex_s),
        Paragraph(jp("あなたったら、いつも忘れるんだから。 — You're always forgetting."), ex_s),
    ]
    story.append(section(jp("ってば / ったら — Exasperation"), *tteba_notes))
    story.append(Spacer(1, 3.5 * mm))

    # --- なんか ---
    nanka_notes: list = [Spacer(1, 1 * mm)]
    nanka_notes += [
        Paragraph(
            jp(
                'なんか = contracted なにか (something). Also used as a meaningless filler word like English "like".'
            ),
            note_s,
        ),
        Paragraph(
            jp("今日は、なんか忙しいみたいよ。 — I guess he's like busy today. (filler)"),
            ex_s,
        ),
        Paragraph(
            jp("なんかね。お風呂って超気持ちいいよね！ — Like, baths feel really good, huh?"),
            ex_s,
        ),
        Paragraph(
            jp(
                "お母さんが、なんか明日まで戻らないんだってよ。 — Mom said she's like not coming back until tomorrow."
            ),
            ex_s,
        ),
        Paragraph(
            jp("Only なんか (not なにか) can be used as a filler."),
            note_s,
        ),
    ]
    story.append(section(jp("なんか — Filler Word"), *nanka_notes))
    story.append(Spacer(1, 3.5 * mm))

    # --- ～やがる ---
    yagaru_notes: list = [Spacer(1, 1 * mm)]
    yagaru_notes += [
        Paragraph(
            jp(
                "～やがる = verb suffix showing hatred/contempt. Attach to verb stem. Conjugates as u-verb. Mostly fiction/manga."
            ),
            note_s,
        ),
        Paragraph(
            jp(
                "あんなやつに負けやがって。じゃ、どうすんだよ？ — Losing to a guy like that. What are you going to do?"
            ),
            ex_s,
        ),
        Paragraph(
            jp("やる気か？だったらさっさと来やがれ！ — You want to fight? Then hurry up and come on!"),
            ex_s,
        ),
    ]
    story.append(section(jp("～やがる — Contempt"), *yagaru_notes))
    story.append(Spacer(1, 3.5 * mm))

    # --- Notes ---
    final_notes: list = [Spacer(1, 1 * mm)]
    for n in [
        jp("Slang goal: reduce mouth movement. Shorten words or slur sounds together."),
        jp("Casual speech: drop particles, reorder sentences (verb-first OK), break into fragments."),
        jp("じゃん = じゃない (confirms positive). Gender-neutral. じゃんか adds questioning tone."),
        jp("つ/つう = という (rough, male). つうか = というか. っつう = extra emphasis."),
        jp("ってば (= といえば) / ったら (= といったら) express exasperation."),
        jp("なんか = なにか (something) or filler word (like). Only なんか works as filler."),
        jp("～やがる = contempt verb suffix. Attach to stem. Mostly fiction. Conjugates as u-verb."),
    ]:
        final_notes.append(Paragraph(f"- {n}", note_s))
    story.append(section("Notes", *final_notes))

    return story
