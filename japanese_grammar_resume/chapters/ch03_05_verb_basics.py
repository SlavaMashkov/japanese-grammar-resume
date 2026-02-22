from ..styles import *


def build():
    story = []

    story.append(PageBreak())
    story.append(Paragraph(jp("3.5  Verb Basics  （動詞）"), title_s))
    story.append(Table([['']], colWidths=[W], rowHeights=[1.5],
        style=TableStyle([('BACKGROUND',(0,0),(0,0),CD),
                          ('TOPPADDING',(0,0),(-1,-1),0),('BOTTOMPADDING',(0,0),(-1,-1),0)])))
    story.append(Spacer(1, 3*mm))

    story.append(section_header("Vocabulary"))
    story.append(Spacer(1, 1*mm))
    vocab35 = [
        ([("た","食"),("","べ"),("","る")],              "to eat  (ru-verb)"),
        ([("わ","分"),("","か"),("","る")],              "to understand  (u-verb)"),
        ([("み","見"),("","る")],                        "to see  (ru-verb)"),
        ([("ね","寝"),("","る")],                        "to sleep  (ru-verb)"),
        ([("お","起"),("","き"),("","る")],              "to wake; to occur  (ru-verb)"),
        ([("かんが","考"),("","え"),("","る")],          "to think  (ru-verb)"),
        ([("おし","教"),("","え"),("","る")],            "to teach; to inform  (ru-verb)"),
        ([("で","出"),("","る")],                        "to come out  (ru-verb)"),
        ([("","い"),("","る")],                          "to exist — animate  (ru-verb)"),
        ([("き","着"),("","る")],                        "to wear  (ru-verb)"),
        ([("はな","話"),("","す")],                      "to speak  (u-verb)"),
        ([("き","聞"),("","く")],                        "to ask; to listen  (u-verb)"),
        ([("およ","泳"),("","ぐ")],                      "to swim  (u-verb)"),
        ([("あそ","遊"),("","ぶ")],                      "to play  (u-verb)"),
        ([("ま","待"),("","つ")],                        "to wait  (u-verb)"),
        ([("の","飲"),("","む")],                        "to drink  (u-verb)"),
        ([("か","買"),("","う")],                        "to buy  (u-verb)"),
        ([("","あ"),("","る")],                          "to exist — inanimate  (u-verb)"),
        ([("し","死"),("","ぬ")],                        "to die  (u-verb)"),
        ([("","す"),("","る")],                          "to do  (exception)"),
        ([("く","来"),("","る")],                        "to come  (exception)"),
        ([("お","お"),("かね","金")],                    "money"),
        ([("わたし","私")],                              "me; I"),
        ([("かえ","帰"),("","る")],                      "to go home  (u-verb)"),
        ([("ねこ","猫")],                                "cat"),
    ]
    story.append(vocab_two_col(vocab35))
    story.append(Spacer(1, 3.5*mm))

    story.append(section_header("Grammar: Verb Types"))
    story.append(Spacer(1, 1*mm))
    vtype = [
        ["Type",       "Rule",                                                  "Examples"],
        ["ru-verb",    "Ends in る, preceded by /i/ or /e/ vowel sound.",
                       "食べる、見る、寝る、起きる、いる"],
        ["u-verb",     "Ends in any u-vowel sound (including る preceded by /a/, /u/, /o/).",
                       "話す、聞く、買う、分かる、ある"],
        ["Exception",  "Neither ru nor u rules apply. Must be memorized.",
                       "する、来る"],
    ]
    vtrows = [[cell(c, bold=(ri==0), center=(ri==0 or ci==0), sz=8) for ci,c in enumerate(row)]
              for ri,row in enumerate(vtype)]
    col_vt = [22*mm, 75*mm, W-97*mm]
    vtt = Table(vtrows, colWidths=col_vt)
    vtt.setStyle(TableStyle(TABLE_STYLE + [
        ('BACKGROUND', (0,1),(0,-1), CR1),
        ('FONTNAME',   (0,1),(0,-1), 'DV-B'),
    ]))
    story.append(vtt)
    story.append(Spacer(1, 3.5*mm))

    story.append(section_header("Notes"))
    story.append(Spacer(1, 1*mm))
    for n in [
        "Verbs always come at the end of a clause in Japanese.",
        "A verb alone is a grammatically complete sentence — no subject required.",
        jp("If a verb ends in る but the preceding vowel is /a/, /u/, or /o/ → always u-verb."),
        jp("If preceding vowel is /i/ or /e/ → usually ru-verb, but exceptions exist (e.g. 帰る、切る、走る)."),
        jp("ある (inanimate) and いる (animate) both mean 'to exist' but are not interchangeable."),
    ]:
        story.append(Paragraph(f"- {n}", note_s))

    return story
