from ...styles import *


def build():
    story = []

    story.append(PageBreak())
    story.append(Paragraph(jp("4.3  The Question Marker  （か）"), title_s))
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
                    "鈴木",
                    "買い物",
                    "料理",
                    "すみません",
                    "ちょっと",
                    "お腹",
                    "いっぱい",
                    "ごめんなさい",
                    "ごめん",
                    "こんな",
                    "本当",
                    "そんな",
                    "どう",
                    "知る",
                    "盗む",
                    "犯人",
                    "選ぶ",
                    "皆",
                    "皆さん",
                    "質問",
                    "答え",
                    "遅れる",
                    "ここ",
                    "レストラン",
                    "今週末",
                    "あの",
                    "イタリア",
                    "クッキー",
                ]
            )
        )
    )
    story.append(Spacer(1, 3.5 * mm))

    # --- Polite Form ---
    story.append(section(jp("Polite Form — か at Sentence End")))
    story.append(Spacer(1, 1 * mm))
    for n in [
        jp("か is attached to the end of a polite sentence to indicate a question."),
        jp("You don't need a question mark — か already signals it (though ? is sometimes added)."),
        jp("Do NOT use the declarative だ before か. Use です form directly."),
        jp("  田中さん：お母さんはどこですか。 — Where is (your) mother?"),
        jp("  鈴木さん：母は買い物に行きました。 — (My) mother went shopping."),
        jp("  キムさん：イタリア料理を食べに行きませんか。 — Go to eat Italian food?"),
        jp("  鈴木さん：すみません。ちょっと、お腹がいっぱいです。 — Sorry. (My) stomach is a little full."),
        jp("すみません is a polite apology. ごめんなさい is slightly less formal. ごめん is casual."),
    ]:
        story.append(Paragraph(f"- {n}", note_s))
    story.append(Spacer(1, 3.5 * mm))

    # --- Casual Speech ---
    story.append(section(jp("Casual Speech — か Is Not for Real Questions")))
    story.append(Spacer(1, 1 * mm))
    for n in [
        jp("In casual speech, か is NOT used for genuine questions — it sounds rough or sarcastic."),
        jp("Instead, か is used for rhetorical questions or internal wondering."),
        jp("  こんなのを本当に食べるか？ — Do you think [he] will really eat this type of thing?"),
        jp("  そんなのは、あるかよ！ — Do I look like I would have something like that?!"),
        jp("Real casual questions use the explanatory の particle or just rising intonation:"),
        jp("  こんなのを本当に食べる？ — Are you really going to eat something like this?"),
        jp("  そんなのは、あるの？ — Do you have something like that?"),
    ]:
        story.append(Paragraph(f"- {n}", note_s))
    story.append(Spacer(1, 3.5 * mm))

    # --- か in Relative Clauses ---
    story.append(section(jp("か in Relative Clauses — Embedded Questions")))
    story.append(Spacer(1, 1 * mm))
    for n in [
        jp("か at the end of a relative clause creates a mini-question inside a larger sentence."),
        jp("  昨日何を食べたか忘れた。 — Forgot what I ate yesterday."),
        jp("  彼は何を言ったか分からない。 — Don't understand what he said."),
        jp("  先生が学校に行ったか教えない？ — Won't you inform me whether teacher went to school?"),
        jp('どうか = "whether or not": 先生が学校に行ったかどうか知らない。'),
        jp("Alternative: include both options: 行ったか行かなかったか知らない。"),
    ]:
        story.append(Paragraph(f"- {n}", note_s))
    story.append(Spacer(1, 3.5 * mm))

    # --- Table: Question Words (word + か) ---
    q_data = [
        ["Word + か", "Meaning"],
        ["誰か", "Someone"],
        ["何か", "Something"],
        ["いつか", "Sometime"],
        ["どこか", "Somewhere"],
        ["どれか", "A certain one from many"],
    ]
    q_rows = [
        [cell(c, bold=(ri == 0), center=True, sz=8) for ci, c in enumerate(row)]
        for ri, row in enumerate(q_data)
    ]
    cw_q = [W / 2, W / 2]
    q_t = Table(q_rows, colWidths=cw_q)
    q_t.setStyle(
        TableStyle(
            TABLE_STYLE
            + [
                ("BACKGROUND", (0, 1), (0, -1), CR1),
                ("FONTNAME", (0, 1), (0, -1), "DV-B"),
            ]
        )
    )
    story.append(section(jp("Question Words （word + か）"), q_t))
    story.append(Spacer(1, 3.5 * mm))

    # --- Table: Inclusive Words (word + も) ---
    inc_data = [
        ["Word + も", "Meaning"],
        ["誰も", "Everybody / Nobody (with negative)"],
        ["何も", "Nothing (negative only)"],
        ["いつも", "Always"],
        ["どこも", "Everywhere"],
        ["どれも", "Any and all"],
    ]
    inc_rows = [
        [cell(c, bold=(ri == 0), center=True, sz=8) for ci, c in enumerate(row)]
        for ri, row in enumerate(inc_data)
    ]
    inc_t = Table(inc_rows, colWidths=cw_q)
    inc_t.setStyle(
        TableStyle(
            TABLE_STYLE
            + [
                ("BACKGROUND", (0, 1), (0, -1), CR1),
                ("FONTNAME", (0, 1), (0, -1), "DV-B"),
            ]
        )
    )
    story.append(section(jp("Inclusive Words （word + も）"), inc_t))
    story.append(Spacer(1, 3.5 * mm))

    # --- Table: "Any" Words (word + でも) ---
    any_data = [
        ["Word + でも", "Meaning"],
        ["誰でも", "Anybody"],
        ["何でも", "Anything"],
        ["いつでも", "Anytime"],
        ["どこでも", "Anywhere"],
        ["どれでも", "Whichever"],
    ]
    any_rows = [
        [cell(c, bold=(ri == 0), center=True, sz=8) for ci, c in enumerate(row)]
        for ri, row in enumerate(any_data)
    ]
    any_t = Table(any_rows, colWidths=cw_q)
    any_t.setStyle(
        TableStyle(
            TABLE_STYLE
            + [
                ("BACKGROUND", (0, 1), (0, -1), CR1),
                ("FONTNAME", (0, 1), (0, -1), "DV-B"),
            ]
        )
    )
    story.append(section(jp('"Any" Words （word + でも）'), any_t))
    story.append(Spacer(1, 3.5 * mm))

    # --- Notes ---
    story.append(section("Notes"))
    story.append(Spacer(1, 1 * mm))
    for n in [
        jp("In polite form, add か to the end to make a question. Never use だ before か."),
        jp("In casual speech, か is rhetorical/wondering — use の or intonation for real questions."),
        jp("か inside relative clauses creates embedded questions (昨日何を食べたか忘れた)."),
        jp('どうか = "whether or not". You can also list both alternatives (...か...か).'),
        jp('Question word + か = "some-" (誰か = someone). Treat them as regular nouns.'),
        jp("Question word + も = inclusive/negative (誰も = everybody/nobody). 何も is negative only."),
        jp('Question word + でも = "any" (誰でも = anybody). 何でも is read なんでも, not なにでも.'),
        jp('Use 皆 or 皆さん for "everybody" (not 誰も). Use 全部 for "everything" (not 何も).'),
    ]:
        story.append(Paragraph(f"- {n}", note_s))

    return story
