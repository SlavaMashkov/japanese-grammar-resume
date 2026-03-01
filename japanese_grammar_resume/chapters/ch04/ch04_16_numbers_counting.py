from ...styles import *


def build():
    story = []

    story.append(PageBreak())
    story.append(
        Paragraph(
            jp("4.16  Numbers and Counting  （数と数え方）"),
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
                        "零",
                        "点",
                        "マイナス",
                        "平成",
                        "昭和",
                        "午前",
                        "午後",
                        "秒",
                        "枚",
                        "冊",
                    ]
                )
            ),
        )
    )
    story.append(Spacer(1, 3.5 * mm))

    # --- helper for compact tables ---
    def mini_tbl(data, cw, highlight_row0=True):
        rows = [[cell(c, bold=(ri == 0), center=True, sz=7) for c in row] for ri, row in enumerate(data)]
        t = Table(rows, colWidths=cw)
        sty = list(TABLE_STYLE)
        if highlight_row0:
            sty += [
                ("BACKGROUND", (0, 0), (-1, 0), CR1),
                ("FONTNAME", (0, 0), (-1, 0), "DV-B"),
            ]
        t.setStyle(TableStyle(sty))
        return t

    # --- Number System — 1 to 10 ---
    num10_data = [
        ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"],
        [jp("一"), jp("二"), jp("三"), jp("四"), jp("五"), jp("六"), jp("七"), jp("八"), jp("九"), jp("十")],
        [
            jp("いち"),
            jp("に"),
            jp("さん"),
            jp("し/よん"),
            jp("ご"),
            jp("ろく"),
            jp("しち/なな"),
            jp("はち"),
            jp("きゅう"),
            jp("じゅう"),
        ],
    ]
    cw10 = [W / 10] * 10
    num10_t = mini_tbl(num10_data, cw10, highlight_row0=False)

    num_notes: list = [Spacer(1, 1 * mm)]
    num_notes += [
        Paragraph(
            jp(
                "Japanese number system is in units of four. Past 10, reading is always よん and なな (not し/しち)."
            ),
            note_s,
        ),
        Paragraph(
            jp("三十一 (さんじゅういち) = 31 / 五十四 (ごじゅうよん) = 54 / 二十 (にじゅう) = 20"),
            ex_s,
        ),
    ]
    story.append(section(jp("Number System — 1 to 10"), num10_t, *num_notes))
    story.append(Spacer(1, 3.5 * mm))

    # --- Higher Numbers ---
    hi_data = [
        ["", "100", "1,000", jp("10⁴"), jp("10⁸"), jp("10¹²")],
        [jp("漢字"), jp("百"), jp("千"), jp("万"), jp("億"), jp("兆")],
        [jp("読み"), jp("ひゃく"), jp("せん"), jp("まん"), jp("おく"), jp("ちょう")],
    ]
    hw = W / 6
    hi_t = mini_tbl(hi_data, [hw] * 6, highlight_row0=False)

    # Sound changes table
    sc_data = [
        ["Numeral", jp("漢字"), jp("ひらがな")],
        ["300", jp("三百"), jp("さんびゃく")],
        ["600", jp("六百"), jp("ろっぴゃく")],
        ["800", jp("八百"), jp("はっぴゃく")],
        ["3,000", jp("三千"), jp("さんぜん")],
        ["8,000", jp("八千"), jp("はっせん")],
        [jp("10¹²"), jp("一兆"), jp("いっちょう")],
    ]
    scw = [22 * mm, 22 * mm, W - 44 * mm]
    sc_t = mini_tbl(sc_data, scw)

    hi_notes: list = [Spacer(1, 1 * mm)]
    hi_notes += [
        Paragraph(
            jp("Units jump by four digits: 一万 (10⁴), 一億 (10⁸), 一兆 (10¹²). Sound changes:"),
            note_s,
        ),
        sc_t,
    ]
    story.append(section(jp("Higher Numbers"), hi_t, *hi_notes))
    story.append(Spacer(1, 3.5 * mm))

    # --- Numbers < 1 ---
    lt1_notes: list = [Spacer(1, 1 * mm)]
    lt1_notes += [
        Paragraph(
            jp("Zero: 零 (れい), ゼロ, or マル. ゼロ/マル are more common in modern Japanese."),
            note_s,
        ),
        Paragraph(
            jp("Decimals: say 点 (てん) for the dot, then each digit individually."),
            note_s,
        ),
        Paragraph(jp("0.0021 = ゼロ、点、ゼロ、ゼロ、二、一。"), ex_s),
        Paragraph(
            jp("Negative: say マイナス before the number."),
            note_s,
        ),
        Paragraph(jp("マイナス二十九 = -29"), ex_s),
    ]
    story.append(section(jp("Numbers < 1"), *lt1_notes))
    story.append(Spacer(1, 3.5 * mm))

    # --- Dates ---
    # Year: number + 年 (ねん). Month: number + 月 (がつ). Watch 4月=しがつ, 7月=しちがつ, 9月=くがつ.
    # Days of month — special readings for 1st–10th, 14th, 20th, 24th, 29th
    day_data = [
        ["Day", jp("漢字"), jp("読み"), "Day", jp("漢字"), jp("読み")],
        [jp("何日"), jp("何日"), jp("なんにち"), "10th", jp("十日"), jp("とおか")],
        ["1st", jp("一日"), jp("ついたち"), "14th", jp("十四日"), jp("じゅうよっか")],
        ["2nd", jp("二日"), jp("ふつか"), "20th", jp("二十日"), jp("はつか")],
        ["3rd", jp("三日"), jp("みっか"), "24th", jp("二十四日"), jp("にじゅうよっか")],
        ["4th", jp("四日"), jp("よっか"), "29th", jp("二十九日"), jp("にじゅうくにち")],
        ["5th", jp("五日"), jp("いつか"), "", "", ""],
        ["6th", jp("六日"), jp("むいか"), "", "", ""],
        ["7th", jp("七日"), jp("なのか"), "", "", ""],
        ["8th", jp("八日"), jp("ようか"), "", "", ""],
        ["9th", jp("九日"), jp("ここのか"), "", "", ""],
    ]
    day_rows = [
        [cell(c, bold=(ri == 0), center=(ri == 0 or ci in (0, 3)), sz=7) for ci, c in enumerate(row)]
        for ri, row in enumerate(day_data)
    ]
    dw = W / 6
    day_t = Table(day_rows, colWidths=[dw] * 6)
    day_t.setStyle(TableStyle(TABLE_STYLE))

    date_notes: list = [Spacer(1, 1 * mm)]
    date_notes += [
        Paragraph(
            jp("Year: number + 年 (ねん). Era calendars: 平成, 昭和 etc. + year + 年."),
            note_s,
        ),
        Paragraph(
            jp("Month: number + 月 (がつ). Exceptions: 4月=しがつ, 7月=しちがつ, 9月=くがつ."),
            note_s,
        ),
        Paragraph(
            jp("Days: 1st–10th have special readings. Rest = number + にち. Other irregulars:"),
            note_s,
        ),
        day_t,
        Paragraph(jp("Date format: XXXX年YY月ZZ日 — e.g. 2003年12月2日"), ex_s),
    ]
    story.append(section(jp("Dates — 年・月・日"), *date_notes))
    story.append(Spacer(1, 3.5 * mm))

    # --- Time ---
    hr_data = [
        [jp("英語"), "4 o'clock", "7 o'clock", "9 o'clock"],
        [jp("漢字"), jp("四時"), jp("七時"), jp("九時")],
        [jp("読み"), jp("よじ"), jp("しちじ"), jp("くじ")],
    ]
    hrw = W / 4
    hr_t = mini_tbl(hr_data, [hrw] * 4, highlight_row0=False)

    min_data = [
        [jp("英語"), "1 min", "3 min", "4 min", "6 min", "8 min", "10 min"],
        [jp("漢字"), jp("一分"), jp("三分"), jp("四分"), jp("六分"), jp("八分"), jp("十分")],
        [
            jp("読み"),
            jp("いっぷん"),
            jp("さんぷん"),
            jp("よんぷん"),
            jp("ろっぷん"),
            jp("はっぷん"),
            jp("じゅっぷん"),
        ],
    ]
    mw = W / 7
    min_t = mini_tbl(min_data, [mw] * 7, highlight_row0=False)

    time_notes: list = [Spacer(1, 1 * mm)]
    time_notes += [
        Paragraph(
            jp("Hour: number + 時 (じ). Exceptions:"),
            note_s,
        ),
        hr_t,
        Spacer(1, 1 * mm),
        Paragraph(
            jp("Minutes: number + 分 (ふん). Exceptions (ぷん):"),
            note_s,
        ),
        min_t,
        Spacer(1, 1 * mm),
        Paragraph(
            jp("Seconds: number + 秒 (びょう). No exceptions. AM/PM: 午前/午後 before time."),
            note_s,
        ),
        Paragraph(jp("午後4時10分 (ごご・よじ・じゅっぷん) = 4:10 PM"), ex_s),
    ]
    story.append(section(jp("Time — 時・分・秒"), *time_notes))
    story.append(Spacer(1, 3.5 * mm))

    # --- Span of Time ---
    span_notes: list = [Spacer(1, 1 * mm)]
    span_notes += [
        Paragraph(
            jp("間 (かん) attaches to hours, days, weeks, years to express duration."),
            note_s,
        ),
        Paragraph(
            jp("二時間四十分 = 2 hours 40 min / 二十日間 = 20 days / 二年間 = 2 years / 三週間 = 3 weeks"),
            ex_s,
        ),
        Paragraph(
            jp(
                "一日 as duration = いちにち (not ついたち). 一週間 = いっしゅうかん, 八週間 = はっしゅうかん."
            ),
            note_s,
        ),
        Paragraph(
            jp("Counting months: number + ヶ月 (かげつ). The ヶ is abbreviation of 箇. ヶ月 is NOT がつ."),
            note_s,
        ),
    ]

    mo_data = [
        [jp("英語"), "1 month", "6 months", "10 months"],
        [jp("漢字"), jp("一ヶ月"), jp("六ヶ月"), jp("十ヶ月")],
        [jp("読み"), jp("いっかげつ"), jp("ろっかげつ"), jp("じゅっかげつ")],
    ]
    mow = W / 4
    mo_t = mini_tbl(mo_data, [mow] * 4, highlight_row0=False)

    span_notes += [
        mo_t,
        Spacer(1, 1 * mm),
        Paragraph(
            jp("十一ヶ月 (じゅういっかげつ) = 11 months / 三十三ヶ月 (さんじゅうさんかげつ) = 33 months"),
            ex_s,
        ),
    ]
    story.append(section(jp("Span of Time — 間・ヶ月"), *span_notes))
    story.append(Spacer(1, 3.5 * mm))

    # --- Other Counters ---
    cnt_desc = [
        [jp("Counter"), jp("Usage")],
        [jp("人 (にん)"), jp("people")],
        [jp("本 (ほん)"), jp("long, cylindrical objects (bottles, chopsticks)")],
        [jp("枚 (まい)"), jp("thin, flat objects (paper, shirts)")],
        [jp("冊 (さつ)"), jp("bound objects (books)")],
        [jp("匹 (ひき)"), jp("small animals (cats, dogs)")],
        [jp("歳 (さい)"), jp("age of living creatures")],
        [jp("個 (こ)"), jp("small (round) objects")],
        [jp("回 (かい)"), jp("number of times")],
        [jp("ヶ所 (かしょ)"), jp("number of locations")],
        [jp("つ"), jp("generic counter (up to 10 only)")],
    ]
    cnt_rows = [
        [cell(c, bold=(ri == 0), center=(ri == 0 or ci == 0), sz=7) for ci, c in enumerate(row)]
        for ri, row in enumerate(cnt_desc)
    ]
    cnt_t = Table(cnt_rows, colWidths=[28 * mm, W - 28 * mm])
    cnt_t.setStyle(
        TableStyle(
            TABLE_STYLE
            + [
                ("BACKGROUND", (0, 1), (0, -1), CR1),
                ("FONTNAME", (0, 1), (0, -1), "DV-B"),
            ]
        )
    )

    # Big counting table (1-10 for all counters)
    SZ = 6
    big_data = [
        [
            "",
            jp("人"),
            jp("本"),
            jp("枚"),
            jp("冊"),
            jp("匹"),
            jp("歳"),
            jp("個"),
            jp("回"),
            jp("ヶ所"),
            jp("つ"),
        ],
        [
            "1",
            jp("ひとり"),
            jp("いっぽん"),
            jp("いちまい"),
            jp("いっさつ"),
            jp("いっぴき"),
            jp("いっさい"),
            jp("いっこ"),
            jp("いっかい"),
            jp("いっかしょ"),
            jp("ひとつ"),
        ],
        [
            "2",
            jp("ふたり"),
            jp("にほん"),
            jp("にまい"),
            jp("にさつ"),
            jp("にひき"),
            jp("にさい"),
            jp("にこ"),
            jp("にかい"),
            jp("にかしょ"),
            jp("ふたつ"),
        ],
        [
            "3",
            jp("さんにん"),
            jp("さんぼん"),
            jp("さんまい"),
            jp("さんさつ"),
            jp("さんびき"),
            jp("さんさい"),
            jp("さんこ"),
            jp("さんかい"),
            jp("さんかしょ"),
            jp("みっつ"),
        ],
        [
            "4",
            jp("よにん"),
            jp("よんほん"),
            jp("よんまい"),
            jp("よんさつ"),
            jp("よんひき"),
            jp("よんさい"),
            jp("よんこ"),
            jp("よんかい"),
            jp("よんかしょ"),
            jp("よっつ"),
        ],
        [
            "5",
            jp("ごにん"),
            jp("ごほん"),
            jp("ごまい"),
            jp("ごさつ"),
            jp("ごひき"),
            jp("ごさい"),
            jp("ごこ"),
            jp("ごかい"),
            jp("ごかしょ"),
            jp("いつつ"),
        ],
        [
            "6",
            jp("ろくにん"),
            jp("ろっぽん"),
            jp("ろくまい"),
            jp("ろくさつ"),
            jp("ろっぴき"),
            jp("ろくさい"),
            jp("ろっこ"),
            jp("ろっかい"),
            jp("ろっかしょ"),
            jp("むっつ"),
        ],
        [
            "7",
            jp("しちにん"),
            jp("ななほん"),
            jp("ななまい"),
            jp("ななさつ"),
            jp("ななひき"),
            jp("ななさい"),
            jp("ななこ"),
            jp("ななかい"),
            jp("ななかしょ"),
            jp("ななつ"),
        ],
        [
            "8",
            jp("はちにん"),
            jp("はっぽん"),
            jp("はちまい"),
            jp("はっさつ"),
            jp("はっぴき"),
            jp("はっさい"),
            jp("はっこ"),
            jp("はっかい"),
            jp("はっかしょ"),
            jp("やっつ"),
        ],
        [
            "9",
            jp("きゅうにん"),
            jp("きゅうほん"),
            jp("きゅうまい"),
            jp("きゅうさつ"),
            jp("きゅうひき"),
            jp("きゅうさい"),
            jp("きゅうこ"),
            jp("きゅうかい"),
            jp("きゅうかしょ"),
            jp("ここのつ"),
        ],
        [
            "10",
            jp("じゅうにん"),
            jp("じゅっぽん"),
            jp("じゅうまい"),
            jp("じゅっさつ"),
            jp("じゅっぴき"),
            jp("じゅっさい"),
            jp("じゅっこ"),
            jp("じゅっかい"),
            jp("じゅっかしょ"),
            jp("とお"),
        ],
    ]
    big_rows = [[cell(c, bold=(ri == 0), center=True, sz=SZ) for c in row] for ri, row in enumerate(big_data)]
    big_cw = [8 * mm] + [(W - 8 * mm) / 10] * 10
    big_t = Table(big_rows, colWidths=big_cw)
    big_t.setStyle(
        TableStyle(
            TABLE_STYLE
            + [
                ("BACKGROUND", (0, 0), (-1, 0), CR1),
                ("FONTNAME", (0, 0), (-1, 0), "DV-B"),
                ("BACKGROUND", (0, 1), (0, -1), CR1),
                ("FONTNAME", (0, 1), (0, -1), "DV-B"),
            ]
        )
    )

    cnt_notes: list = [Spacer(1, 1 * mm)]
    cnt_notes += [
        Paragraph(
            jp(
                "Wrong counter is grammatically incorrect — you must use the people counter for people. Use a generic counter when unsure."
            ),
            note_s,
        ),
        cnt_t,
        Spacer(1, 1.5 * mm),
        Paragraph(
            jp("Counting 1 to 10 — changed sounds highlighted in the original table:"),
            note_s,
        ),
        big_t,
        Spacer(1, 1 * mm),
        Paragraph(
            jp(
                "一人=ひとり, 二人=ふたり (irregular). Past 10: regular reading + counter. ～つ only up to 10; past that use plain numbers."
            ),
            note_s,
        ),
        Paragraph(
            jp("Age: 才 can replace 歳. Age 20 = はたち (not にじゅっさい)."),
            note_s,
        ),
    ]
    story.append(section(jp("Other Counters"), *cnt_notes))
    story.append(Spacer(1, 3.5 * mm))

    # --- Notes ---
    final_notes: list = [Spacer(1, 1 * mm)]
    for n in [
        jp("Numbers 1–10: いち、に、さん、し/よん、ご、ろく、しち/なな、はち、きゅう、じゅう."),
        jp("Higher: 百 (ひゃく), 千 (せん), 万 (まん), 億 (おく), 兆 (ちょう). Sound changes at 3, 6, 8."),
        jp("Dates: 1st–10th have special readings. Year+年, Month+月 (4/7/9 irregular), Day+日."),
        jp("Time: number+時(じ) [4=よじ, 7=しちじ, 9=くじ]. Minutes+分(ふん/ぷん). Seconds+秒(びょう)."),
        jp(
            "Duration: 間 (かん) for hours/days/weeks/years. ヶ月 (かげつ) for months. Sound changes at 1, 6, 8, 10."
        ),
        jp("Counters: 人/本/枚/冊/匹/歳/個/回/ヶ所/つ. Wrong counter = grammatically incorrect."),
    ]:
        final_notes.append(Paragraph(f"- {n}", note_s))
    story.append(section("Notes", *final_notes))

    return story
