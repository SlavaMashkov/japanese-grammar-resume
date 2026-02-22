from ..styles import *


def build():
    story = []

    story.append(PageBreak())
    story.append(Paragraph(jp("3.8  Particles Used with Verbs  （を、に、へ、で）"), title_s))
    story.append(Table([['']], colWidths=[W], rowHeights=[1.5],
        style=TableStyle([('BACKGROUND',(0,0),(0,0),CD),
                          ('TOPPADDING',(0,0),(-1,-1),0),('BOTTOMPADDING',(0,0),(-1,-1),0)])))
    story.append(Spacer(1, 3*mm))

    story.append(section_header("Vocabulary"))
    story.append(Spacer(1, 1*mm))
    story.append(vocab_two_col(vocab_from_registry([
        "街", "歩く", "高速道路", "毎日", "日本ご", "登録", "日本", "うち",
        "部屋", "宿題", "いす", "台所", "会う", "医者", "なる", "先週",
        "図書館", "来年", "映画館", "昼ご飯", "何", "暇", "学校", "習う",
        "どこ", "勝ち", "向う",
    ])))
    story.append(Spacer(1, 3.5*mm))

    story.append(section_header("Grammar: The Four Verb Particles"))
    story.append(Spacer(1, 1*mm))
    vp = [
        ["Particle", "Name",      "Function",                                          "Example"],
        ["を (o)",   "Direct\nObject",
         "Marks the direct object of a verb.\nAlso used with motion verbs for traversed locations.",
         "魚を食べる。Eat fish.\n街をぶらぶら歩く。Walk through town."],
        ["に (ni)",  "Target",
         "Marks the destination or target of a verb.\nAlso used for time, location of existence, and abstract goals.",
         "日本に行った。Went to Japan.\n猫は部屋にいる。Cat is in room."],
        ["へ (e)",   "Direction",
         "Marks the direction one is heading. Softer than に — does not guarantee final destination.\nOnly used with directional motion verbs.",
         "日本へ行った。Headed towards Japan.\n勝ちへ向かう。Go towards victory."],
        ["で (de)",  "Context",
         "Marks where or by what means an action is performed.\nThink of it as 'by way of'.",
         "映画館で見た。Saw at movie theatre.\nバスで帰る。Go home by bus."],
    ]
    vprows = [[cell(c, bold=(ri==0), center=(ri==0 or ci==0), sz=8) for ci,c in enumerate(row)]
              for ri,row in enumerate(vp)]
    col_vp = [19*mm, 16*mm, 65*mm, W-100*mm]
    vpt = Table(vprows, colWidths=col_vp)
    vpt.setStyle(TableStyle(TABLE_STYLE + [
        ('BACKGROUND', (0,1),(0,-1), CR1),
        ('FONTNAME',   (0,1),(0,-1), 'DV-B'),
    ]))
    story.append(vpt)
    story.append(Spacer(1, 3.5*mm))

    story.append(section_header("Notes"))
    story.append(Spacer(1, 1*mm))
    for n in [
        jp("を cannot be combined with は or も. To make a direct object the topic, just use は alone: 日本語は、習う。"),
        jp("に and へ can both mark destinations, but に implies the final destination while へ implies direction only."),
        jp("Location particles に、へ、で can absorb は or も when the location becomes the topic: 図書館には？"),
        jp("何で can mean 'by what means?' (なにで) or 'why?' (なんで) — context tells them apart."),
        jp("から (from) and まで (up to) can pair with に targets: 今日から明日までする。"),
    ]:
        story.append(Paragraph(f"- {n}", note_s))

    return story
