from ...styles import *


def build():
    story = []

    story.append(PageBreak())
    story.append(
        Paragraph(
            jp("4.5  Other Uses of the Te-form  （〜ている、〜てある、〜ておく、〜ていく、〜てくる）"),
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
                    "教科書",
                    "話",
                    "歌",
                    "道",
                    "もう",
                    "先",
                    "美恵",
                    "準備",
                    "旅行",
                    "計画",
                    "終わる",
                    "切符",
                    "ホテル",
                    "予約",
                    "作る",
                    "電池",
                    "えんぴつ",
                    "駅",
                    "方",
                    "冬",
                    "コート",
                    "増える",
                    "一生懸命",
                    "頑張る",
                    "色々",
                    "付き合う",
                    "見つかる",
                    "ずっと",
                    "前",
                    "結局",
                    "やめる",
                ]
            )
        )
    )
    story.append(Spacer(1, 3.5 * mm))

    # --- ～ている — Enduring States ---
    teiru_data = [
        ["Tense", "Positive", "Negative"],
        ["Non-Past", jp("読んでいる (reading)"), jp("読んでいない (not reading)")],
        ["Past", jp("読んでいた (was reading)"), jp("読んでいなかった (was not reading)")],
    ]
    teiru_rows = [
        [cell(c, bold=(ri == 0), center=(ri == 0 or ci == 0), sz=8) for ci, c in enumerate(row)]
        for ri, row in enumerate(teiru_data)
    ]
    cw_teiru = [28 * mm, (W - 28 * mm) / 2, (W - 28 * mm) / 2]
    teiru_t = Table(teiru_rows, colWidths=cw_teiru)
    teiru_t.setStyle(
        TableStyle(
            TABLE_STYLE
            + [
                ("BACKGROUND", (0, 1), (0, -1), CR1),
                ("FONTNAME", (0, 1), (0, -1), "DV-B"),
            ]
        )
    )
    teiru_notes: list = [Spacer(1, 1 * mm)]
    for n in [
        jp("Te-form + いる describes a continuing action or state. Result conjugates as a ru-verb."),
        jp("  食べる → 食べて → 食べている (is eating)"),
        jp("  読む → 読んで → 読んでいる (is reading)"),
        jp("  友達は何をしているの？ — What is friend doing?"),
        jp("  昼ご飯を食べている。 — (Friend) is eating lunch."),
        jp("  話を聞いていますか。 — Are you listening? (polite)"),
        jp("In casual speech, い is often dropped: 食べてる、読んでる、してる."),
        jp("  何をしているの？ → 何してるの？ → 何してんの？"),
    ]:
        teiru_notes.append(Paragraph(f"- {n}", note_s))
    story.append(section(jp("〜ている — Enduring States"), teiru_t, *teiru_notes))
    story.append(Spacer(1, 3.5 * mm))

    # --- State-of-Being vs State of Action ---
    state_notes: list = [Spacer(1, 1 * mm)]
    for n in [
        jp("Some verbs in ～ている describe a resultant state, not an ongoing action."),
        jp('知っている = "know" (state of having learned), not "am knowing".'),
        jp("  今日、知りました。 — I found out today. (action of knowing)"),
        jp("  この歌を知っていますか？ — Do you know this song? (state)"),
        jp('分かっている = "already understand / I get it" — can sound pompous if misused.'),
        jp("  道は分かりますか。 — Do you know the way? (use 分かる, not 分かっている)"),
        jp('Motion verbs: 行っている / 来ている = "has gone / has come" (and is there now).'),
        jp("  もう、家に帰っている。 — He is already at home. (went home and is there)"),
        jp("  先に行っているよ。 — I'll go on ahead. (I'll go and be there before you)"),
        jp("  美恵ちゃんは、もう来ているよ。 — Mie-chan is already here."),
    ]:
        state_notes.append(Paragraph(f"- {n}", note_s))
    story.append(section(jp("State-of-Being vs State of Action"), *state_notes))
    story.append(Spacer(1, 3.5 * mm))

    # --- ～てある — Resultant States ---
    tearu_notes: list = [Spacer(1, 1 * mm)]
    for n in [
        jp("Te-form + ある describes a resultant state — the action is already done."),
        jp("Carries a nuance of completion in preparation for something else."),
        jp("Common to see は or も instead of を (describes a state, not an action)."),
        jp("  準備はどうですか。 — How are the preparations?"),
        jp("  準備は、もうしてあるよ。 — The preparations are already done."),
        jp("  旅行の計画は終わった？ — Are the plans for the trip complete?"),
        jp("  うん、切符を買ったし、ホテルの予約もしてある。"),
        jp("  — Yeah, bought the ticket and also took care of hotel reservations."),
    ]:
        tearu_notes.append(Paragraph(f"- {n}", note_s))
    story.append(section(jp("〜てある — Resultant States"), *tearu_notes))
    story.append(Spacer(1, 3.5 * mm))

    # --- ～ておく — Preparation for the Future ---
    teoku_notes: list = [Spacer(1, 1 * mm)]
    for n in [
        jp("Te-form + おく（置く）= action done (or will be done) with the future in mind."),
        jp('おく means "to place" — think of placing something ready for later use.'),
        jp("  晩ご飯を作っておく。 — Make dinner (in advance for later)."),
        jp("  電池を買っておきます。 — I'll buy batteries (in advance)."),
        jp("Abbreviated to ～とく in casual speech:"),
        jp("  晩ご飯を作っとく。 電池を買っときます。"),
    ]:
        teoku_notes.append(Paragraph(f"- {n}", note_s))
    story.append(section(jp("〜ておく — Preparation for the Future"), *teoku_notes))
    story.append(Spacer(1, 3.5 * mm))

    # --- ～ていく / ～てくる — Motion with Te-form ---
    teiku_notes: list = [Spacer(1, 1 * mm)]
    for n in [
        jp("Te-form + 行く / 来る shows action oriented toward or from someplace."),
        jp("持っている (have) → 持っていく (take) / 持ってくる (bring)."),
        jp("  えんぴつを持っている？ — Do you have a pencil?"),
        jp("  えんぴつを学校へ持っていく？ — Taking pencil to school?"),
        jp("  えんぴつを家に持ってくる？ — Bringing pencil home?"),
        jp("  お父さんは、早く帰ってきました。 — Father came back home early."),
        jp("  駅の方へ走っていった。 — Went running toward the station."),
        jp("Can also express movement through time:"),
        jp("  ～ていく = toward the future; ～てくる = up to the present."),
        jp("  冬に入って、コートを着ている人が増えていきます。"),
        jp("  — Entering winter, people wearing coats will increase (toward the future)."),
        jp("  一生懸命、頑張っていく！ — Will try my hardest (going forward)!"),
        jp("  色々な人と付き合ってきたけど、いい人はまだ見つからない。"),
        jp("  — Went out with various people (up to now) but haven't found a good person yet."),
        jp("  日本語をずっと前から勉強してきて、結局はやめた。"),
        jp("  — Studied Japanese from way back (up to then) and eventually quit."),
    ]:
        teiku_notes.append(Paragraph(f"- {n}", note_s))
    story.append(section(jp("〜ていく / 〜てくる — Motion with Te-form"), *teiku_notes))
    story.append(Spacer(1, 3.5 * mm))

    # --- Notes ---
    final_notes: list = [Spacer(1, 1 * mm)]
    for n in [
        jp("Te-form + いる = continuing action/state. Conjugates as ru-verb. い often dropped casually."),
        jp("知っている = know (state). 分かっている = already understand (careful — can sound pompous)."),
        jp("Motion verbs + ている = resultant state: 行っている = has gone (is there now)."),
        jp("Te-form + ある = completed action with nuance of preparation. Uses は/も instead of を."),
        jp("Te-form + おく = action done for the future. Abbreviated to ～とく."),
        jp("Te-form + 行く = action moving away / toward future. Te-form + 来る = toward / up to present."),
        jp("持っていく = take (hold + go). 持ってくる = bring (hold + come)."),
    ]:
        final_notes.append(Paragraph(f"- {n}", note_s))
    story.append(section("Notes", *final_notes))

    return story
