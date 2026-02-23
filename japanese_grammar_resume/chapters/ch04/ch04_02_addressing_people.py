from ...styles import *


def build():
    story = []

    story.append(PageBreak())
    story.append(Paragraph(jp("4.2  Addressing People"), title_s))
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
                    "名前",
                    "僕",
                    "俺",
                    "社長",
                    "課長",
                    "田中",
                    "彼女",
                    "母",
                    "お母さん",
                    "両親",
                    "父",
                    "お父さん",
                    "妻",
                    "奥さん",
                    "夫",
                    "主人",
                    "姉",
                    "お姉さん",
                    "兄",
                    "お兄さん",
                    "妹",
                    "弟",
                    "息子",
                    "娘",
                ]
            )
        )
    )
    story.append(Spacer(1, 3.5 * mm))

    # --- Table: Referring to Yourself ---
    self_data = [
        ["Word", "Usage"],
        ["私（わたくし）", "Formal — used by both males and females"],
        ["私（わたし）", "Normal polite — used by both males and females"],
        ["僕（ぼく）", "Males — from fairly polite to fairly casual"],
        ["俺（おれ）", "Males — very casual, rough"],
        ["あたし", "Feminine — casual, cutesy"],
        ["Own name", "Feminine/childish — casual way to refer to oneself"],
        ["わし", "Males — older men, middle-aged+"],
    ]
    self_rows = [
        [cell(c, bold=(ri == 0), center=(ri == 0 or ci == 0), sz=8) for ci, c in enumerate(row)]
        for ri, row in enumerate(self_data)
    ]
    cw_self = [38 * mm, W - 38 * mm]
    self_t = Table(self_rows, colWidths=cw_self)
    self_t.setStyle(
        TableStyle(
            TABLE_STYLE
            + [
                ("BACKGROUND", (0, 1), (0, -1), CR1),
                ("FONTNAME", (0, 1), (0, -1), "DV-B"),
            ]
        )
    )
    story.append(section("Referring to Yourself", self_t))
    story.append(Spacer(1, 3.5 * mm))

    # --- Table: Name Suffixes and Titles ---
    suffix_data = [
        ["Suffix / Title", "Usage"],
        ["さん", "General polite — attached to last name (e.g. 田中さん)"],
        ["くん", "Males of equal or lower social position"],
        ["ちゃん", "Endearing — usually females of equal or lower position"],
        ["先生（せんせい）", "Teacher, doctor, or expert in a field"],
        ["社長（しゃちょう）", "Company president — can combine: 田中社長"],
        ["課長（かちょう）", "Section manager — used the same way as 社長"],
    ]
    suffix_rows = [
        [cell(c, bold=(ri == 0), center=(ri == 0 or ci == 0), sz=8) for ci, c in enumerate(row)]
        for ri, row in enumerate(suffix_data)
    ]
    cw_suffix = [38 * mm, W - 38 * mm]
    suffix_t = Table(suffix_rows, colWidths=cw_suffix)
    suffix_t.setStyle(
        TableStyle(
            TABLE_STYLE
            + [
                ("BACKGROUND", (0, 1), (0, -1), CR1),
                ("FONTNAME", (0, 1), (0, -1), "DV-B"),
            ]
        )
    )
    story.append(section("Name Suffixes and Titles", suffix_t))
    story.append(Spacer(1, 3.5 * mm))

    # --- Table: Referring to Others with "You" ---
    you_data = [
        ["Word", "Usage"],
        ["あなた", "General — only when you can't use the person's name"],
        ["君（きみ）", "Close/assuming — mostly by guys, can be rude"],
        ["お前（おまえ）", "Rough and coarse — usually used by guys"],
        ["あんた", "Assuming and familiar — can sound miffed"],
        ["手前（てめえ）", "Very rude — seen mostly in fiction / comic books"],
        ["貴様（きさま）", "Very rude — seen mostly in fiction / comic books"],
    ]
    you_rows = [
        [cell(c, bold=(ri == 0), center=(ri == 0 or ci == 0), sz=8) for ci, c in enumerate(row)]
        for ri, row in enumerate(you_data)
    ]
    cw_you = [38 * mm, W - 38 * mm]
    you_t = Table(you_rows, colWidths=cw_you)
    you_t.setStyle(
        TableStyle(
            TABLE_STYLE
            + [
                ("BACKGROUND", (0, 1), (0, -1), CR1),
                ("FONTNAME", (0, 1), (0, -1), "DV-B"),
            ]
        )
    )
    story.append(section(jp('Referring to Others with "You"'), you_t))
    story.append(Spacer(1, 3.5 * mm))

    # --- Table: Third Person ---
    third_data = [
        ["Word", "Meaning"],
        ["彼（かれ）", "He; boyfriend"],
        ["彼女（かのじょ）", "She; girlfriend"],
        ["ガールフレンド", "Girlfriend (unambiguous)"],
        ["ボーイフレンド", "Boyfriend (unambiguous)"],
    ]
    third_rows = [
        [cell(c, bold=(ri == 0), center=(ri == 0 or ci == 0), sz=8) for ci, c in enumerate(row)]
        for ri, row in enumerate(third_data)
    ]
    cw_third = [38 * mm, W - 38 * mm]
    third_t = Table(third_rows, colWidths=cw_third)
    third_t.setStyle(
        TableStyle(
            TABLE_STYLE
            + [
                ("BACKGROUND", (0, 1), (0, -1), CR1),
                ("FONTNAME", (0, 1), (0, -1), "DV-B"),
            ]
        )
    )
    story.append(section("Third Person", third_t))
    story.append(Spacer(1, 3.5 * mm))

    # --- Table: Family Members ---
    fam_data = [
        ["Relation", "One's own family", "Someone else's family"],
        ["Parents", "両親", "ご両親"],
        ["Mother", "母", "お母さん"],
        ["Father", "父", "お父さん"],
        ["Wife", "妻", "奥さん"],
        ["Husband", "夫", "ご主人"],
        ["Older Sister", "姉", "お姉さん"],
        ["Older Brother", "兄", "お兄さん"],
        ["Younger Sister", "妹", "妹さん"],
        ["Younger Brother", "弟", "弟さん"],
        ["Son", "息子", "息子さん"],
        ["Daughter", "娘", "娘さん"],
    ]
    fam_rows = [
        [cell(c, bold=(ri == 0), center=True, sz=8) for ci, c in enumerate(row)]
        for ri, row in enumerate(fam_data)
    ]
    cw_fam = [35 * mm, (W - 35 * mm) / 2, (W - 35 * mm) / 2]
    fam_t = Table(fam_rows, colWidths=cw_fam)
    fam_t.setStyle(
        TableStyle(
            TABLE_STYLE
            + [
                ("BACKGROUND", (0, 1), (0, -1), CR1),
                ("FONTNAME", (0, 1), (0, -1), "DV-B"),
            ]
        )
    )
    story.append(section("Family Members", fam_t))
    story.append(Spacer(1, 3.5 * mm))

    # --- Notes ---
    story.append(section("Notes"))
    story.append(Spacer(1, 1 * mm))
    for n in [
        jp('私（わたし） is the safest default for "I". 僕 and 俺 are masculine-only.'),
        jp("Attach さん to last names for politeness. くん for males, ちゃん for endearing."),
        jp("Titles like 先生、社長、課長 can replace さん or combine with a name (田中先生)."),
        jp('Avoid あなた — use the person\'s name + suffix instead. Direct "you" sounds accusatory.'),
        jp("彼 and 彼女 can mean both he/she and boyfriend/girlfriend — context decides."),
        jp(
            "Family: use humble forms (母、父) for your own family, polite forms (お母さん、お父さん) for others'."
        ),
    ]:
        story.append(Paragraph(f"- {n}", note_s))

    return story
