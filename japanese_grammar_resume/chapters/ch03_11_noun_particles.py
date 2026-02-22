from ..styles import *


def build():
    story = []

    story.append(PageBreak())
    story.append(Paragraph(jp("3.11  Noun-related Particles  （と、や、とか、の）"), title_s))
    story.append(Table([['']], colWidths=[W], rowHeights=[1.5],
        style=TableStyle([('BACKGROUND',(0,0),(0,0),CD),
                          ('TOPPADDING',(0,0),(-1,-1),0),('BOTTOMPADDING',(0,0),(-1,-1),0)])))
    story.append(Spacer(1, 3*mm))

    story.append(section_header("Vocabulary"))
    story.append(Spacer(1, 1*mm))
    vocab311 = [
        ([("ほん","本")],                                "book"),
        ([("ざっ","雑"),("し","誌")],                    "magazine"),
        ([("はが","葉"),("き","書")],                    "postcard"),
        ([("せん","先"),("せい","生")],                  "teacher"),
        ([("の","飲"),("み","み"),("もの","物")],         "beverage"),
        ([("くつ","靴")],                                "shoes"),
        ([("だい","大"),("がく","学")],                  "college"),
        ([("しろ","白"),("","い")],                      "white  (i-adj)"),
        ([("","か"),("","わ"),("","い"),("","い")],      "cute  (i-adj)"),
        ([("じゅ","授"),("ぎょう","業")],                "class"),
        ([("わす","忘"),("","れ"),("","る")],            "to forget  (ru-verb)"),
        ([("","こ"),("","と")],                          "event; matter (abstract noun)"),
        ([("たい","大"),("へん","変")],                  "tough; hard time  (na-adj)"),
        ([("おな","同"),("","じ")],                      "same"),
        ([("もの","物")],                                "object; thing"),
        ([("おも","面"),("しろ","白"),("","い")],        "interesting  (i-adj)"),
        ([("いま","今")],                                "now"),
        ([("いそが","忙"),("","し"),("","い")],          "busy  (i-adj)"),
        ([("あさ","朝"),("","ご"),("はん","飯")],        "breakfast"),
    ]
    story.append(vocab_two_col(vocab311))
    story.append(Spacer(1, 3.5*mm))

    story.append(section_header("Grammar: Noun-related Particles"))
    story.append(Spacer(1, 1*mm))
    np_data = [
        ["Particle", "Meaning",          "Usage",                                       "Example"],
        ["と",       "and (exhaustive)", "Lists all items. Also: 'together with'.",
         "本と雑誌を買った。\nBought book and magazine.\n友達と話した。Talked with friend."],
        ["や",       "and/or etc.",      "Vague listing — implies other items exist.",
         "靴や服を買う。\nBuy (things like) shoes and clothes, etc."],
        ["とか",     "and/or etc.",      "Same as や but more colloquial.",
         "靴とか服を買う。\nBuy (things like) shoes and clothes, etc."],
        ["の",       "of; 's",           "Links nouns (possession, description).\nModified noun can be omitted if clear from context.",
         "ボブの本。Bob's book.\nアメリカの大学の学生。\nStudent of an American college."],
    ]
    nprows = [[cell(c, bold=(ri==0), center=(ri==0 or ci==0), sz=8) for ci,c in enumerate(row)]
              for ri,row in enumerate(np_data)]
    col_np = [19*mm, 22*mm, 53*mm, W-94*mm]
    npt = Table(nprows, colWidths=col_np)
    npt.setStyle(TableStyle(TABLE_STYLE + [
        ('BACKGROUND', (0,1),(0,-1), CR1),
        ('FONTNAME',   (0,1),(0,-1), 'DV-B'),
    ]))
    story.append(npt)
    story.append(Spacer(1, 3.5*mm))

    story.append(section_header(jp("Grammar: の as Nominalizer and Explanatory んだ")))
    story.append(Spacer(1, 1*mm))
    no_data = [
        ["Usage",                    "Rule",                                   "Example"],
        ["Nominalize verb/adj",      "Add の after verb or adj clause\n→ turns it into a noun phrase.",
         "授業に行くのを忘れた。\nForgot (the thing of) going to class.\n白いのはかわいい。The white one is cute."],
        ["Explanatory の／んだ",     "Add の (or んだ) at end of sentence\n→ conveys 'the reason is...' or 'the thing is...'.\nNouns/na-adj need な before の.",
         "今は忙しいんだ。\nThe thing is I'm busy now.\nジムなのだ。It is (because it's) Jim."],
    ]
    norows = [[cell(c, bold=(ri==0), sz=8, center=(ri==0 or ci==0)) for ci,c in enumerate(row)]
              for ri,row in enumerate(no_data)]
    col_no = [38*mm, 60*mm, W-98*mm]
    not_ = Table(norows, colWidths=col_no)
    not_.setStyle(TableStyle(TABLE_STYLE + [
        ('BACKGROUND', (0,1),(0,-1), CR1),
        ('FONTNAME',   (0,1),(0,-1), 'DV-B'),
    ]))
    story.append(not_)
    story.append(Spacer(1, 3.5*mm))

    story.append(section_header("Notes"))
    story.append(Spacer(1, 1*mm))
    for n in [
        jp("と lists everything; や/とか imply an incomplete list ('among other things')."),
        jp("の can replace a noun when context is clear: 誰の？ — ボブのだ。"),
        jp("の as nominalizer turns any clause into a noun: verbs, adjectives — but NOT bare nouns+だ."),
        jp("な-adj still needs な before の: 静かなのがアリスの部屋だ。"),
        jp("んだ (spoken) = のだ (written). Used to give or seek explanations."),
    ]:
        story.append(Paragraph(f"- {n}", note_s))

    return story
