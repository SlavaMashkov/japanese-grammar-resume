from ..styles import *


def build():
    story = []

    story.append(PageBreak())
    story.append(Paragraph(jp("3.10  Relative Clauses and Sentence Order"), title_s))
    story.append(Table([['']], colWidths=[W], rowHeights=[1.5],
        style=TableStyle([('BACKGROUND',(0,0),(0,0),CD),
                          ('TOPPADDING',(0,0),(-1,-1),0),('BOTTOMPADDING',(0,0),(-1,-1),0)])))
    story.append(Spacer(1, 3*mm))

    story.append(section_header("Vocabulary"))
    story.append(Spacer(1, 1*mm))
    story.append(vocab_two_col(vocab_from_registry([
        "子供", "立派", "大人", "仕事", "辞める", "いつも", "赤い",
        "晩ご飯", "銀行", "公園", "お弁当",
    ])))
    story.append(Spacer(1, 3.5*mm))

    story.append(section_header("Grammar: Relative Clauses as Adjectives"))
    story.append(Spacer(1, 1*mm))
    rc = [
        ["Form",                "Can modify noun?", "Example"],
        ["Verb (non-past)",     "Yes",              "いつも勉強する人 — person who always studies"],
        ["Verb (negative)",     "Yes",              "食べなかった人 — person who did not eat"],
        ["Verb (past)",         "Yes",              "映画を見た人 — person who watched the movie"],
        ["Noun + だ",           "NO",               "だ cannot directly modify a noun"],
        ["Noun + だった",        "Yes",              "子供だったアリス — Alice who was a child"],
        ["Noun + じゃない",     "Yes",              "学生じゃない人 — person who is not a student"],
        ["Noun + じゃなかった", "Yes",              "友達じゃなかったアリス — Alice who was not a friend"],
    ]
    rcrows = [[cell(c, bold=(ri==0), center=(ri==0 or ci==0 or ci==1), sz=8)
               for ci,c in enumerate(row)]
              for ri,row in enumerate(rc)]
    col_rc = [40*mm, 26*mm, W-66*mm]
    rct = Table(rcrows, colWidths=col_rc)
    rct.setStyle(TableStyle(TABLE_STYLE + [
        ('BACKGROUND', (0,1),(0,-1), CR1),
        ('FONTNAME',   (0,1),(0,-1), 'DV-B'),
    ]))
    story.append(rct)
    story.append(Spacer(1, 3.5*mm))

    story.append(section_header("Grammar: Japanese Sentence Order"))
    story.append(Spacer(1, 1*mm))
    so = [
        ["Rule",                          "Notes"],
        ["The verb must come at the end.", "This is the only strict rule."],
        ["Everything before the verb can appear in any order.",
         "Particles identify roles, so word order is flexible."],
        ["Only the verb is required for a complete sentence.",
         "Subject, object — all optional if clear from context."],
        ["Relative clauses (except だ) can nest before any noun.",
         "お弁当を食べた学生が公園に行った。\nStudent who ate lunch went to the park."],
    ]
    sorows = [[cell(c, bold=(ri==0), sz=8) for c in row] for ri,row in enumerate(so)]
    col_so = [60*mm, W-60*mm]
    sot = Table(sorows, colWidths=col_so)
    sot.setStyle(TableStyle(TABLE_STYLE + [
        ('BACKGROUND', (0,1),(0,-1), CR1),
        ('FONTNAME',   (0,1),(0,-1), 'DV-B'),
    ]))
    story.append(sot)

    return story
