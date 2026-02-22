from ..styles import *


def build():
    story = []

    story.append(PageBreak())

    story.append(Paragraph(jp("3.4  Adjectives  （形容詞）"), title_s))
    story.append(Table([['']], colWidths=[W], rowHeights=[1.5],
        style=TableStyle([('BACKGROUND',(0,0),(0,0),CD),
                          ('TOPPADDING',(0,0),(-1,-1),0),
                          ('BOTTOMPADDING',(0,0),(-1,-1),0)])))
    story.append(Spacer(1, 3*mm))

    # --- Vocabulary 3.4 ---
    story.append(section_header("Vocabulary"))
    story.append(Spacer(1, 1*mm))

    vocab34 = [
        ([("しず","静"),("","か")],                      "quiet  (na-adj)"),
        ([("","き"),("","れ"),("","い")],                "pretty; clean  (na-adj)"),
        ([("しん","親"),("せつ","切")],                  "kind  (na-adj)"),
        ([("す","好"),("","き")],                          "likable; desirable  (na-adj)"),
        ([("き","嫌"),("","ら"),("","い")],                "distasteful; hateful  (na-adj)"),
        ([("","い"),("","い")],                          "good  (i-adj)  *conjugates from よい"),
        ([("","お"),("","い"),("","し"),("","い")],      "tasty  (i-adj)"),
        ([("たか","高"),("","い")],                      "high; tall; expensive  (i-adj)"),
        ([("","か"),("","っ"),("","こ"),("","い"),("","い")], "cool; handsome  (i-adj)  *conjugates from かっこよい"),
        ([("ひと","人")],                                "person"),
        ([("さかな","魚")],                              "fish"),
        ([("にく","肉")],                                "meat"),
        ([("","や"),("さい","菜")],                      "vegetables"),
        ([("た","食"),("","べ"),("もの","物")],           "food"),
        ([("ね","値"),("だん","段")],                     "price"),
        ([("かれ","彼")],                                "he; boyfriend"),
        ([("","あ"),("","ま"),("","り")],                "not very  (used with negative)"),
    ]

    story.append(vocab_two_col(vocab34))
    story.append(Spacer(1, 3.5*mm))

    # --- Adjective Types ---
    story.append(section_header("Grammar: na-adjectives vs i-adjectives"))
    story.append(Spacer(1, 1*mm))

    types = [
        ["",              "na-adjective",                        "i-adjective"],
        ["Identify by",   "Does NOT end in い (usually).\nExceptions: きれい、嫌い",
                          "Always ends in い"],
        ["Modify noun",   "Add な before noun\n静かな人  (quiet person)",
                          "Directly before noun (no な)\nおいしい食べ物  (tasty food)"],
        ["Conjugation",   "Same rules as nouns\n(see ch. 3.2)",
                          "Remove い, then add suffix\n(see table below)"],
        ["Attach だ?",    "Yes — 静かだ",
                          "NO — never attach だ to i-adj"],
    ]

    trows = [[cell(c, bold=(ri==0), center=(ri==0 or ci==0), sz=8) for ci,c in enumerate(row)]
             for ri,row in enumerate(types)]
    hw3 = (W - 28*mm) / 2
    tt = Table(trows, colWidths=[28*mm, hw3, hw3])
    tt.setStyle(TableStyle(TABLE_STYLE + [
        ('BACKGROUND', (0,1),(0,-1), CR1),
        ('FONTNAME',   (0,1),(0,-1), 'DV-B'),
    ]))
    story.append(tt)
    story.append(Spacer(1, 3.5*mm))

    # --- i-adjective conjugation ---
    story.append(section_header(jp("i-adjective Conjugation  (example: 高い)")))
    story.append(Spacer(1, 1*mm))

    iconj = [
        ["",          "Affirmative",      "Negative"],
        ["Non-Past",  "高い",              "高い → 高く + ない  =  高くない"],
        ["Past",      "高い → 高か + った  =  高かった",
                      "高くない → 高くなか + った  =  高くなかった"],
    ]
    icrows = [[cell(c, bold=(ri==0), center=(ri==0 or ci==0), sz=8) for ci,c in enumerate(row)]
              for ri,row in enumerate(iconj)]
    hw4 = (W - 22*mm) / 2
    it = Table(icrows, colWidths=[22*mm, hw4, hw4])
    it.setStyle(TableStyle(TABLE_STYLE + [
        ('BACKGROUND', (0,1),(0,-1), CR1),
        ('FONTNAME',   (0,1),(0,-1), 'DV-B'),
    ]))
    story.append(it)
    story.append(Spacer(1, 3.5*mm))

    # --- Exception: いい / かっこいい ---
    story.append(section_header(jp("Exception: いい and かっこいい  (conjugate from よい)")))
    story.append(Spacer(1, 1*mm))

    exc = [
        ["",          "Affirmative",   "Negative"],
        ["Non-Past",  "いい",           "よくない"],
        ["Past",      "よかった",       "よくなかった"],
        ["Non-Past",  "かっこいい",     "かっこよくない"],
        ["Past",      "かっこよかった", "かっこよくなかった"],
    ]
    erows = [[cell(c, bold=(ri==0), center=(ri==0 or ci==0), sz=8) for ci,c in enumerate(row)]
             for ri,row in enumerate(exc)]
    hw5 = (W - 22*mm) / 2
    et = Table(erows, colWidths=[22*mm, hw5, hw5])
    et.setStyle(TableStyle(TABLE_STYLE + [
        ('BACKGROUND', (0,1),(0,-1), CR1),
        ('FONTNAME',   (0,1),(0,-1), 'DV-B'),
    ]))
    story.append(et)

    return story
