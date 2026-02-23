from ...styles import *


def build():
    story = []

    story.append(PageBreak())
    story.append(Paragraph(jp("3.6  Negative Verbs  （否定形）"), title_s))
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

    neg_rules = [
        ["Type", "Rule", "Example"],
        ["ru-verb", "Drop る, add ない", "食べる → 食べない"],
        ["u-verb (う)", "Replace う with わ, add ない", "買う → 買わない"],
        ["u-verb (other)", "Replace ending with a-vowel, add ない", "待つ → 待たない\n聞く → 聞かない"],
        ["する", "Exception → しない", "する → しない"],
        ["くる", "Exception → こない", "来る → こない"],
        ["ある", "Special exception → ない", "ある → ない"],
    ]
    nrrows = [
        [cell(c, bold=(ri == 0), center=(ri == 0 or ci == 0), sz=8) for ci, c in enumerate(row)]
        for ri, row in enumerate(neg_rules)
    ]
    col_nr = [28 * mm, 62 * mm, W - 90 * mm]
    nrt = Table(nrrows, colWidths=col_nr)
    nrt.setStyle(
        TableStyle(
            TABLE_STYLE
            + [
                ("BACKGROUND", (0, 1), (0, -1), CR1),
                ("FONTNAME", (0, 1), (0, -1), "DV-B"),
            ]
        )
    )
    story.append(section("Grammar: Negative Conjugation Rules", nrt))
    story.append(Spacer(1, 3.5 * mm))

    neg_ex = [
        ["ru-verb", "u-verb", "exception"],
        ["見る → 見ない", "話す → 話さない", "する → しない"],
        ["食べる → 食べない", "聞く → 聞かない", "来る → こない"],
        ["寝る → 寝ない", "泳ぐ → 泳がない", "ある → ない"],
        ["起きる → 起きない", "遊ぶ → 遊ばない", ""],
        ["考える → 考えない", "待つ → 待たない", ""],
        ["教える → 教えない", "飲む → 飲まない", ""],
        ["出る → 出ない", "買う → 買わない", ""],
        ["着る → 着ない", "帰る → 帰らない", ""],
        ["いる → いない", "死ぬ → 死なない", ""],
    ]
    nerows = [
        [cell(c, bold=(ri == 0), center=(ri == 0), sz=8) for ci, c in enumerate(row)]
        for ri, row in enumerate(neg_ex)
    ]
    hw6 = W / 3
    net = Table(nerows, colWidths=[hw6, hw6, hw6])
    net.setStyle(TableStyle(TABLE_STYLE))
    story.append(section("Negative Conjugation Examples", net))

    return story
