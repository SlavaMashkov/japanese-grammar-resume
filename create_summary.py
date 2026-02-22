import os
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

pdfmetrics.registerFont(TTFont('DV',   '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'))
pdfmetrics.registerFont(TTFont('DV-B', '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'))
pdfmetrics.registerFont(TTFont('JP',   os.path.join(BASE_DIR, 'fonts', 'NotoSansJP-Light.ttf')))

def jp(text):
    """Inline-switch to JP font for CJK characters, DV for everything else."""
    result, buf, in_jp = [], [], False
    for ch in text:
        is_jp = ('\u3000' <= ch <= '\u9fff') or ('\uff00' <= ch <= '\uffef')
        if is_jp != in_jp:
            if buf:
                chunk = ''.join(buf)
                result.append(f'<font name="JP">{chunk}</font>' if in_jp else chunk)
            buf, in_jp = [ch], is_jp
        else:
            buf.append(ch)
    if buf:
        chunk = ''.join(buf)
        result.append(f'<font name="JP">{chunk}</font>' if in_jp else chunk)
    return ''.join(result)

# Greyscale palette
CK  = colors.HexColor("#1A1A1A")   # near-black
CD  = colors.HexColor("#6A6A6A")   # medium grey (header bg)
CM  = colors.HexColor("#888888")   # mid grey
CL  = colors.HexColor("#D8D8D8")   # light grey (grid)
CR1 = colors.HexColor("#F4F4F4")   # row alt 1
CR2 = colors.white
CW  = colors.white

W = A4[0] - 30*mm

def S(name, **kw):
    return ParagraphStyle(name, **kw)

title_s   = S('title',   fontSize=14, textColor=CK, spaceAfter=2*mm, leading=18, fontName='DV-B')
section_s = S('sec',     fontSize=8,  textColor=CW, leading=10, fontName='DV-B')
note_s    = S('note',    fontSize=8,  leading=11.5, leftIndent=3*mm, textColor=CD)

def cell(text, bold=False, sz=8.5, col=CK, center=False):
    fn = 'DV-B' if bold else 'DV'
    aln = 1 if center else 0
    return Paragraph(jp(text.replace('\n','<br/>')),
                     S(f'x{abs(hash(text))}', fontName=fn, fontSize=sz,
                       leading=sz*1.4, textColor=col, alignment=aln))

def section_header(text):
    t = Table([[Paragraph(jp(text), section_s)]], colWidths=[W],
              style=TableStyle([
                  ('BACKGROUND',   (0,0),(0,0), CD),
                  ('TOPPADDING',   (0,0),(0,0), 3),
                  ('BOTTOMPADDING',(0,0),(0,0), 3),
                  ('LEFTPADDING',  (0,0),(0,0), 6),
              ]))
    return t

TABLE_STYLE = [
    ('BACKGROUND',    (0,0), (-1,0),  CD),
    ('TEXTCOLOR',     (0,0), (-1,0),  CW),
    ('ROWBACKGROUNDS',(0,1), (-1,-1), [CR1, CR2]),
    ('GRID',          (0,0), (-1,-1), 0.4, CL),
    ('VALIGN',        (0,0), (-1,-1), 'TOP'),
    ('TOPPADDING',    (0,0), (-1,-1), 3),
    ('BOTTOMPADDING', (0,0), (-1,-1), 3),
    ('LEFTPADDING',   (0,0), (-1,-1), 5),
    ('RIGHTPADDING',  (0,0), (-1,-1), 4),
]

output_path = os.path.join(BASE_DIR, "output", "japanese_summary.pdf")
os.makedirs(os.path.dirname(output_path), exist_ok=True)
doc = SimpleDocTemplate(output_path, pagesize=A4,
                        leftMargin=15*mm, rightMargin=15*mm,
                        topMargin=12*mm, bottomMargin=12*mm,
                        title="Japanese Grammar Guide — Chapter Summaries",
                        subject="Japanese grammar notes: state-of-being, particles, adjectives",
                        author="Claude (Anthropic)")
story = []

# Title
story.append(Paragraph(jp("3.2  Expressing State-of-Being  (状態の表現)"), title_s))
story.append(Table([['']], colWidths=[W], rowHeights=[1.5],
    style=TableStyle([('BACKGROUND',(0,0),(0,0),CD),
                      ('TOPPADDING',(0,0),(-1,-1),0),
                      ('BOTTOMPADDING',(0,0),(-1,-1),0)])))
story.append(Spacer(1, 3*mm))

# --- Vocabulary ---
story.append(section_header("Vocabulary"))
story.append(Spacer(1, 1*mm))

vocab = [
    ([("ひと","人")],                               "person"),
    ([("がく","学"),("せい","生")],                  "student"),
    ([("げん","元"),("き","気")],                    "healthy; lively  (*used as a greeting about one's wellbeing)"),
    ([("とも","友"),("だち","達")],                  "friend"),
    ([("あした","明日")],                            "tomorrow"),
    ([("きょう","今日")],                            "today"),
    ([("し","試"),("けん","験")],                    "exam"),
    ([("","う"),("","ん")],                          "yes (casual)"),
    ([("","う"),("","う"),("","ん")],                "no (casual)"),
]

def kanji_cell(pairs):
    """Render a word as a 2×N table from list of (furigana, char) pairs.
    furigana='' means no reading above that character."""
    FURI_SZ, FURI_LD = 6, 7
    CHAR_SZ, CHAR_LD = 11, 13

    # pure-kana: all furigana empty → single-row simple paragraph
    if all(f == '' for f, _ in pairs):
        word = ''.join(ch for _, ch in pairs)
        return Paragraph(jp(word),
                         S(f'kc{abs(hash(word))}', fontName='JP',
                           fontSize=CHAR_SZ, leading=CHAR_LD))

    top_row, bot_row, col_w = [], [], []
    for furi, ch in pairs:
        cw = max(len(furi) * 3.8*mm, 4.5*mm)
        col_w.append(cw)
        top_row.append(Paragraph(jp(furi),
            S(f'ft{abs(hash(furi+ch))}', fontName='JP', fontSize=FURI_SZ,
              leading=FURI_LD, alignment=1)))
        bot_row.append(Paragraph(jp(ch),
            S(f'fb{abs(hash(ch))}', fontName='JP', fontSize=CHAR_SZ,
              leading=CHAR_LD, alignment=1)))

    return Table([top_row, bot_row], colWidths=col_w,
                 rowHeights=[FURI_LD, CHAR_LD],
                 style=TableStyle([
                     ('ALIGN',         (0,0), (-1,-1), 'CENTER'),
                     ('VALIGN',        (0,0), (-1,-1), 'BOTTOM'),
                     ('TOPPADDING',    (0,0), (-1,-1), 0),
                     ('BOTTOMPADDING', (0,0), (-1,-1), 0),
                     ('LEFTPADDING',   (0,0), (-1,-1), 1.5),
                     ('RIGHTPADDING',  (0,0), (-1,-1), 1.5),
                 ]))

def vocab_two_col(vocab_list):
    """Split vocab into two side-by-side tables of equal row count."""
    half = (len(vocab_list) + 1) // 2
    left  = vocab_list[:half]
    right = vocab_list[half:]

    GAP = 2*mm
    WC = (W - GAP) / 2          # width of each sub-table
    ww = 36*mm                    # word col width
    mw = WC - ww                  # meaning col width

    ts = TableStyle(TABLE_STYLE + [('VALIGN',(0,1),(-1,-1),'MIDDLE')])

    FURI_LD  = 7    # furigana row leading
    CHAR_LD  = 13   # character row leading
    CELL_PAD_V = 3  # top + bottom padding per side (pt)
    ROW_H  = (FURI_LD + CHAR_LD + 2 * CELL_PAD_V) / 72 * 25.4 * mm
    HEADER_H = 6*mm

    def build(items, pad_to):
        rows = [[cell("Word",bold=True,center=True), cell("Meaning",bold=True,center=True)]]
        for pairs, meaning in items:
            rows.append([kanji_cell(pairs), cell(meaning, sz=8)])
        while len(rows) - 1 < pad_to:
            rows.append([Paragraph('', note_s), Paragraph('', note_s)])
        heights = [HEADER_H] + [ROW_H] * (len(rows) - 1)
        t = Table(rows, colWidths=[ww, mw], rowHeights=heights, repeatRows=1)
        t.setStyle(ts)
        return t

    tl = build(left,  half)
    tr = build(right, half)
    outer = Table([[tl, '', tr]], colWidths=[WC, GAP, WC],
                  style=TableStyle([('VALIGN',(0,0),(-1,-1),'TOP'),
                                    ('LEFTPADDING',(0,0),(-1,-1),0),
                                    ('RIGHTPADDING',(0,0),(-1,-1),0),
                                    ('TOPPADDING',(0,0),(-1,-1),0),
                                    ('BOTTOMPADDING',(0,0),(-1,-1),0)]))
    return outer

vt = vocab_two_col(vocab)
story.append(vt)
story.append(Spacer(1, 3.5*mm))

# --- Conjugation Table ---
story.append(section_header("Grammar: State-of-Being Conjugation"))
story.append(Spacer(1, 1*mm))

gram = [
    ["",          "Affirmative (+)",                           "Negative (-)"],
    ["Non-Past",  "Noun / na-adj. + だ\n"
                  "  \u300c学生だ\u300d  Is a student\n"
                  "  \u300c元気（だ）\u300d  Is well",
                  "Noun / na-adj. + じゃない\n"
                  "  \u300c学生じゃない\u300d  Is not a student\n"
                  "  \u300c友達じゃない\u300d  Is not a friend"],
    ["Past",      "Noun / na-adj. + だった\n"
                  "  \u300c学生だった\u300d  Was a student\n"
                  "  \u300c友達だった\u300d  Was a friend",
                  "じゃない  ->  じゃなかった\n"
                  "(drop い, add かった)\n"
                  "  \u300c学生じゃなかった\u300d  Was not a student\n"
                  "  \u300c友達じゃなかった\u300d  Was not a friend"],
]

grows = []
for ri, row in enumerate(gram):
    grows.append([cell(c, bold=(ri==0), center=(ri==0 or ci==0), sz=8) for ci,c in enumerate(row)])

hw = (W - 22*mm) / 2
gt = Table(grows, colWidths=[22*mm, hw, hw], repeatRows=1)
gt.setStyle(TableStyle(TABLE_STYLE + [
    ('BACKGROUND', (0,1),(0,-1), CR1),
    ('FONTNAME',   (0,1),(0,-1), 'DV-B'),
]))
story.append(gt)
story.append(Spacer(1, 3.5*mm))

# --- Notes ---
story.append(section_header("Notes"))
story.append(Spacer(1, 1*mm))
notes = [
    jp("「だ」 makes the statement emphatic and declarative. More commonly used by men."),
    jp("Without 「だ」, state-of-being is still implied from context (very common in casual speech)."),
    jp("Negative and past forms are NOT declarative on their own — 「だ」 can be added separately."),
    jp("Casual greeting:  元気？ — 元気。  (Are you well? — I'm well.)"),
]
for n in notes:
    story.append(Paragraph(f"- {n}", note_s))


# ════════════════════════════════════════════════════════════════════════════
# PAGE 2 — 3.3 Introduction to Particles
# ════════════════════════════════════════════════════════════════════════════
story.append(PageBreak())

story.append(Paragraph(jp("3.3  Introduction to Particles  （は、も、が）"), title_s))
story.append(Table([['']], colWidths=[W], rowHeights=[1.5],
    style=TableStyle([('BACKGROUND',(0,0),(0,0),CD),
                      ('TOPPADDING',(0,0),(-1,-1),0),
                      ('BOTTOMPADDING',(0,0),(-1,-1),0)])))
story.append(Spacer(1, 3*mm))

# --- Vocabulary 3.3 ---
story.append(section_header("Vocabulary"))
story.append(Spacer(1, 1*mm))

vocab33 = [
    ([("がく","学"),("せい","生")],                  "student"),
    ([("あした","明日")],                            "tomorrow"),
    ([("きょう","今日")],                            "today"),
    ([("し","試"),("けん","験")],                    "exam"),
    ([("だれ","誰")],                                "who"),
    ([("わたし","私")],                              "me; I"),
    ([("","で"),("","も")],                          "but"),
    ([("","う"),("","ん")],                          "yes (casual)"),
    ([("","う"),("","う"),("","ん")],                "no (casual)"),
]

story.append(vocab_two_col(vocab33))
story.append(Spacer(1, 3.5*mm))

# --- Particles Table ---
story.append(section_header("Grammar: The Three Particles"))
story.append(Spacer(1, 1*mm))

particles = [
    ["Particle", "Name", "Function", "Example"],
    ["は\n(wa)",
     "Topic",
     "Marks what the sentence is about.\nPronounced は /ha/ normally, /wa/ as particle.",
     "アリスは学生？\nIs Alice a student?"],
    ["も\n(mo)",
     "Inclusive\nTopic",
     "Like は but adds meaning of \"also\".\nMust be consistent: all positive or all negative.",
     "トムも学生。\nTom is also a student."],
    ["が\n(ga)",
     "Identifier",
     "Identifies a specific answer to an unspecified question.\nOften answers \"who?\" or \"what?\".",
     "誰が学生？ — ジョンが学生。\nWho is the student? — John is."],
]

prows = []
for ri, row in enumerate(particles):
    prows.append([cell(c, bold=(ri==0), center=(ri==0 or ci==0), sz=8) for ci,c in enumerate(row)])

col_p = [19*mm, 20*mm, 65*mm, W-104*mm]
pt = Table(prows, colWidths=col_p, repeatRows=1)
pt.setStyle(TableStyle(TABLE_STYLE + [
    ('BACKGROUND', (0,1),(0,-1), CR1),
    ('FONTNAME',   (0,1),(0,-1), 'DV-B'),
]))
story.append(pt)
story.append(Spacer(1, 3.5*mm))

# --- は vs が comparison ---
story.append(section_header(jp("Note: は vs が")))
story.append(Spacer(1, 1*mm))

hg = [
    ["", jp("私は学生。"), jp("私が学生。")],
    ["Translation", "As for me, I am a student.", "I am the one who is a student."],
    ["Use", "Introduces a new topic (me).", "Identifies me as the specific answer."],
]
hgrows = [[cell(c, bold=(ri==0), center=(ci==0), sz=8) for ci,c in enumerate(row)]
          for ri,row in enumerate(hg)]
hw2 = (W - 28*mm) / 2
hgt = Table(hgrows, colWidths=[28*mm, hw2, hw2])
hgt.setStyle(TableStyle(TABLE_STYLE + [
    ('BACKGROUND', (0,1),(0,-1), CR1),
    ('FONTNAME',   (0,1),(0,-1), 'DV-B'),
]))
story.append(hgt)
story.append(Spacer(1, 3.5*mm))

story.append(section_header("Notes"))
story.append(Spacer(1, 1*mm))
notes33 = [
    jp("Once a topic is set with は, it doesn't need to be repeated — context carries it forward."),
    jp("も must be consistent: if one is negative, all も-linked items must also be negative."),
    jp("が always answers (or implies) a question like \"who?\" or \"what?\" — it identifies."),
    jp("Think of は as \"as for...\" and が as \"the one that is...\""),
]
for n in notes33:
    story.append(Paragraph(f"- {n}", note_s))


# ════════════════════════════════════════════════════════════════════════════
# PAGE 3 — 3.4 Adjectives
# ════════════════════════════════════════════════════════════════════════════
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


# ════════════════════════════════════════════════════════════════════════════
# PAGE 4 — 3.5 Verb Basics
# ════════════════════════════════════════════════════════════════════════════
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


# ════════════════════════════════════════════════════════════════════════════
# PAGE 5 — 3.6 Negative Verbs
# ════════════════════════════════════════════════════════════════════════════
story.append(PageBreak())
story.append(Paragraph(jp("3.6  Negative Verbs  （否定形）"), title_s))
story.append(Table([['']], colWidths=[W], rowHeights=[1.5],
    style=TableStyle([('BACKGROUND',(0,0),(0,0),CD),
                      ('TOPPADDING',(0,0),(-1,-1),0),('BOTTOMPADDING',(0,0),(-1,-1),0)])))
story.append(Spacer(1, 3*mm))

story.append(section_header("Grammar: Negative Conjugation Rules"))
story.append(Spacer(1, 1*mm))
neg_rules = [
    ["Type",        "Rule",                                   "Example"],
    ["ru-verb",     "Drop る, add ない",                      "食べる → 食べない"],
    ["u-verb (う)", "Replace う with わ, add ない",           "買う → 買わない"],
    ["u-verb (other)","Replace ending with a-vowel, add ない","待つ → 待たない\n聞く → 聞かない"],
    ["する",        "Exception → しない",                     "する → しない"],
    ["くる",        "Exception → こない",                     "来る → こない"],
    ["ある",        "Special exception → ない",               "ある → ない"],
]
nrrows = [[cell(c, bold=(ri==0), center=(ri==0 or ci==0), sz=8) for ci,c in enumerate(row)]
          for ri,row in enumerate(neg_rules)]
col_nr = [28*mm, 62*mm, W-90*mm]
nrt = Table(nrrows, colWidths=col_nr)
nrt.setStyle(TableStyle(TABLE_STYLE + [
    ('BACKGROUND', (0,1),(0,-1), CR1),
    ('FONTNAME',   (0,1),(0,-1), 'DV-B'),
]))
story.append(nrt)
story.append(Spacer(1, 3.5*mm))

story.append(section_header("Negative Conjugation Examples"))
story.append(Spacer(1, 1*mm))
neg_ex = [
    ["ru-verb",          "u-verb",            "exception"],
    ["見る → 見ない",    "話す → 話さない",  "する → しない"],
    ["食べる → 食べない","聞く → 聞かない",  "来る → こない"],
    ["寝る → 寝ない",    "泳ぐ → 泳がない",  "ある → ない"],
    ["起きる → 起きない","遊ぶ → 遊ばない",  ""],
    ["考える → 考えない","待つ → 待たない",  ""],
    ["教える → 教えない","飲む → 飲まない",  ""],
    ["出る → 出ない",    "買う → 買わない",  ""],
    ["着る → 着ない",    "帰る → 帰らない",  ""],
    ["いる → いない",    "死ぬ → 死なない",  ""],
]
nerows = [[cell(c, bold=(ri==0), center=(ri==0), sz=8) for ci,c in enumerate(row)]
          for ri,row in enumerate(neg_ex)]
hw6 = W / 3
net = Table(nerows, colWidths=[hw6, hw6, hw6])
net.setStyle(TableStyle(TABLE_STYLE))
story.append(net)


# ════════════════════════════════════════════════════════════════════════════
# PAGE 6 — 3.7 Past Tense
# ════════════════════════════════════════════════════════════════════════════
story.append(PageBreak())
story.append(Paragraph(jp("3.7  Past Tense  （過去形）"), title_s))
story.append(Table([['']], colWidths=[W], rowHeights=[1.5],
    style=TableStyle([('BACKGROUND',(0,0),(0,0),CD),
                      ('TOPPADDING',(0,0),(-1,-1),0),('BOTTOMPADDING',(0,0),(-1,-1),0)])))
story.append(Spacer(1, 3*mm))

story.append(section_header("Vocabulary"))
story.append(Spacer(1, 1*mm))
vocab37 = [
    ([("す","捨"),("","て"),("","る")],              "to throw away  (ru-verb)"),
    ([("か","書"),("","く")],                        "to write  (u-verb)"),
    ([("も","持"),("","つ")],                        "to hold  (u-verb)"),
    ([("い","行"),("","く")],                        "to go  (u-verb)"),
    ([("はし","走"),("","る")],                      "to run  (u-verb)"),
    ([("","ご"),("はん","飯")],                      "rice; meal"),
    ([("えい","映"),("","が")],                      "movie"),
    ([("ぜん","全"),("","ぶ")],                      "everything"),
    ([("べん","勉"),("きょう","強")],                "study"),
    ([("とも","友"),("だち","達")],                  "friend"),
]
story.append(vocab_two_col(vocab37))
story.append(Spacer(1, 3.5*mm))

story.append(section_header("Grammar: Past Tense Conjugation Rules"))
story.append(Spacer(1, 1*mm))

past_rules = [
    ["Type",          "Rule",                          "Example"],
    ["ru-verb",       "Drop る, add た",               "食べる → 食べた"],
    ["u-verb  す",    "す → した",                     "話す → 話した"],
    ["u-verb  く",    "く → いた",                     "書く → 書いた"],
    ["u-verb  ぐ",    "ぐ → いだ",                     "泳ぐ → 泳いだ"],
    ["u-verb  む ぬ ぶ","む/ぬ/ぶ → んだ",             "飲む→飲んだ、死ぬ→死んだ、遊ぶ→遊んだ"],
    ["u-verb  る つ う","る/つ/う → った",              "切る→切った、持つ→持った、買う→買った"],
    ["する",          "Exception → した",              "する → した"],
    ["くる",          "Exception → きた",              "来る → きた"],
    ["行く",          "Exception → 行った  (not 行いた)","行く → 行った"],
]
prrows = [[cell(c, bold=(ri==0), center=(ri==0 or ci==0), sz=8) for ci,c in enumerate(row)]
          for ri,row in enumerate(past_rules)]
col_pr = [30*mm, 42*mm, W-72*mm]
prt = Table(prrows, colWidths=col_pr)
prt.setStyle(TableStyle(TABLE_STYLE + [
    ('BACKGROUND', (0,1),(0,-1), CR1),
    ('FONTNAME',   (0,1),(0,-1), 'DV-B'),
]))
story.append(prt)
story.append(Spacer(1, 3.5*mm))

story.append(section_header("Past-Negative Tense  (all verb types)"))
story.append(Spacer(1, 1*mm))
pastneg = [
    ["Rule",                                                           "Examples"],
    ["Take the negative form, drop い from ない, add かった",
     "食べない → 食べなかった\n行かない → 行かなかった\nしない → しなかった\nない → なかった"],
]
pnrows = [[cell(c, bold=(ri==0), center=(ri==0 and ci==0), sz=8) for ci,c in enumerate(row)]
          for ri,row in enumerate(pastneg)]
col_pn = [65*mm, W-65*mm]
pnt = Table(pnrows, colWidths=col_pn)
pnt.setStyle(TableStyle(TABLE_STYLE))
story.append(pnt)
story.append(Spacer(1, 3.5*mm))

story.append(section_header("Notes"))
story.append(Spacer(1, 1*mm))
for n in [
    jp("Past-negative works the same for ALL verbs: negative form → drop い → add かった."),
    jp("行く is a regular u-verb in all conjugations except past tense (行った, not 行いた)."),
    jp("ある in past-negative: ない → なかった (there was no...)."),
]:
    story.append(Paragraph(f"- {n}", note_s))


# ════════════════════════════════════════════════════════════════════════════
# PAGE 7 — 3.8 Particles used with verbs
# ════════════════════════════════════════════════════════════════════════════
story.append(PageBreak())
story.append(Paragraph(jp("3.8  Particles Used with Verbs  （を、に、へ、で）"), title_s))
story.append(Table([['']], colWidths=[W], rowHeights=[1.5],
    style=TableStyle([('BACKGROUND',(0,0),(0,0),CD),
                      ('TOPPADDING',(0,0),(-1,-1),0),('BOTTOMPADDING',(0,0),(-1,-1),0)])))
story.append(Spacer(1, 3*mm))

story.append(section_header("Vocabulary"))
story.append(Spacer(1, 1*mm))
vocab38 = [
    ([("さかな","魚")],                              "fish"),
    ([("まち","街")],                                "town"),
    ([("ある","歩"),("","く")],                      "to walk  (u-verb)"),
    ([("こう","高"),("そく","速"),("どう","道"),("ろ","路")], "expressway"),
    ([("まい","毎"),("にち","日")],                  "everyday"),
    ([("に","日"),("ほん","本"),("","ご")],          "Japanese (language)"),
    ([("とう","登"),("ろく","録")],                  "register"),
    ([("に","日"),("ほん","本")],                    "Japan"),
    ([("","う"),("","ち")],                          "one's own home"),
    ([("へ","部"),("や","屋")],                        "room"),
    ([("しゅく","宿"),("だい","題")],                "homework"),
    ([("","い"),("","す")],                          "chair"),
    ([("だい","台"),("どころ","所")],                "kitchen"),
    ([("あ","会"),("","う")],                        "to meet  (u-verb)"),
    ([("い","医"),("しゃ","者")],                    "doctor"),
    ([("","な"),("","る")],                          "to become  (u-verb)"),
    ([("せん","先"),("しゅう","週")],                "last week"),
    ([("と","図"),("しょ","書"),("かん","館")],      "library"),
    ([("らい","来"),("ねん","年")],                  "next year"),
    ([("えい","映"),("が","画"),("かん","館")],      "movie theatre"),
    ([("ひる","昼"),("","ご"),("はん","飯")],        "lunch"),
    ([("なに","何")],                                "what"),
    ([("ひま","暇")],                                "free (not busy)"),
    ([("がっ","学"),("こう","校")],                  "school"),
    ([("なら","習"),("","う")],                      "to learn  (u-verb)"),
    ([("","ど"),("","こ")],                          "where"),
    ([("かち","勝"),("","ち")],                      "victory"),
    ([("むか","向"),("","う")],                      "to face; to go towards  (u-verb)"),
]
story.append(vocab_two_col(vocab38))
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


# ════════════════════════════════════════════════════════════════════════════
# PAGE 8 — 3.9 Transitive and Intransitive Verbs
# ════════════════════════════════════════════════════════════════════════════
story.append(PageBreak())
story.append(Paragraph(jp("3.9  Transitive and Intransitive Verbs"), title_s))
story.append(Table([['']], colWidths=[W], rowHeights=[1.5],
    style=TableStyle([('BACKGROUND',(0,0),(0,0),CD),
                      ('TOPPADDING',(0,0),(-1,-1),0),('BOTTOMPADDING',(0,0),(-1,-1),0)])))
story.append(Spacer(1, 3*mm))

story.append(section_header("Vocabulary"))
story.append(Spacer(1, 1*mm))
vocab39 = [
    ([("でん","電"),("き","気")],                    "electricity; lights"),
    ([("まど","窓")],                                "window"),
    ([("はこ","箱")],                                "box"),
    ([("お","落"),("","と"),("","す")],              "to drop  (u-verb, transitive)"),
    ([("お","落"),("","ち"),("","る")],              "to fall  (ru-verb, intransitive)"),
    ([("だ","出"),("","す")],                        "to take out  (u-verb, transitive)"),
    ([("い","入"),("","れ"),("","る")],              "to insert  (ru-verb, transitive)"),
    ([("はい","入"),("","る")],                      "to enter  (u-verb, intransitive)"),
    ([("あ","開"),("","け"),("","る")],              "to open  (ru-verb, transitive)"),
    ([("あ","開"),("","く")],                        "to be opened  (u-verb, intransitive)"),
    ([("し","閉"),("","め"),("","る")],              "to close  (ru-verb, transitive)"),
    ([("し","閉"),("","ま"),("","る")],              "to be closed  (u-verb, intransitive)"),
    ([("","つ"),("","け"),("","る")],                "to attach  (ru-verb, transitive)"),
    ([("","つ"),("","く")],                          "to be attached  (u-verb, intransitive)"),
    ([("け","消"),("","す")],                        "to erase; turn off  (u-verb, transitive)"),
    ([("き","消"),("","え"),("","る")],              "to disappear  (ru-verb, intransitive)"),
    ([("ぬ","抜"),("","く")],                        "to extract  (u-verb, transitive)"),
    ([("ぬ","抜"),("","け"),("","る")],              "to be extracted  (ru-verb, intransitive)"),
]
story.append(vocab_two_col(vocab39))
story.append(Spacer(1, 3.5*mm))

story.append(section_header("Grammar: Transitive vs Intransitive"))
story.append(Spacer(1, 1*mm))
ti_intro = [
    ["",              "Transitive",                     "Intransitive"],
    ["Agent",         "Active agent performs action",   "No direct agent — event just happens"],
    ["Particle",      "を (direct object)",             "が or は (subject of event)"],
    ["Example",       "電気をつけた。\nTurned on the lights.",
                      "電気がついた。\nThe lights turned on."],
]
tirows = [[cell(c, bold=(ri==0), center=(ri==0 or ci==0), sz=8) for ci,c in enumerate(row)]
          for ri,row in enumerate(ti_intro)]
hw_ti = (W - 28*mm) / 2
tit = Table(tirows, colWidths=[28*mm, hw_ti, hw_ti])
tit.setStyle(TableStyle(TABLE_STYLE + [
    ('BACKGROUND', (0,1),(0,-1), CR1),
    ('FONTNAME',   (0,1),(0,-1), 'DV-B'),
]))
story.append(tit)
story.append(Spacer(1, 3.5*mm))

story.append(section_header("Transitive / Intransitive Pairs"))
story.append(Spacer(1, 1*mm))
pairs_data = [
    ["Transitive (を)", "Meaning",     "Intransitive (が)", "Meaning"],
    ["落とす",  "to drop",    "落ちる",  "to fall"],
    ["出す",    "to take out","出る",    "to come out"],
    ["入れる",  "to insert",  "入る",    "to enter"],
    ["開ける",  "to open",    "開く",    "to be opened"],
    ["閉める",  "to close",   "閉まる",  "to be closed"],
    ["つける",  "to attach",  "つく",    "to be attached"],
    ["消す",    "to erase",   "消える",  "to disappear"],
    ["抜く",    "to extract", "抜ける",  "to be extracted"],
]
prows = [[cell(c, bold=(ri==0), center=(ri==0), sz=8) for ci,c in enumerate(row)]
         for ri,row in enumerate(pairs_data)]
hw_p = W / 4
pt2 = Table(prows, colWidths=[hw_p]*4)
pt2.setStyle(TableStyle(TABLE_STYLE))
story.append(pt2)
story.append(Spacer(1, 3.5*mm))

story.append(section_header("Notes"))
story.append(Spacer(1, 1*mm))
for n in [
    jp("Intransitive verbs CANNOT take を. Use が or は instead: 電気がついた not 電気をついた."),
    jp("Exception: を can be used with intransitive motion verbs for traversed locations: 部屋を出た。"),
    "When unsure whether a verb is transitive or intransitive, check a dictionary (e.g. jisho.org).",
]:
    story.append(Paragraph(f"- {jp(n) if isinstance(n,str) else n}", note_s))


# ════════════════════════════════════════════════════════════════════════════
# PAGE 9 — 3.10 Relative Clauses and Sentence Order
# ════════════════════════════════════════════════════════════════════════════
story.append(PageBreak())
story.append(Paragraph(jp("3.10  Relative Clauses and Sentence Order"), title_s))
story.append(Table([['']], colWidths=[W], rowHeights=[1.5],
    style=TableStyle([('BACKGROUND',(0,0),(0,0),CD),
                      ('TOPPADDING',(0,0),(-1,-1),0),('BOTTOMPADDING',(0,0),(-1,-1),0)])))
story.append(Spacer(1, 3*mm))

story.append(section_header("Vocabulary"))
story.append(Spacer(1, 1*mm))
vocab310 = [
    ([("こ","子"),("ども","供")],                    "child"),
    ([("りっ","立"),("ぱ","派")],                    "fine; elegant  (na-adj)"),
    ([("おとな","大人")],                            "adult"),
    ([("し","仕"),("ごと","事")],                    "job"),
    ([("や","辞"),("","め"),("","る")],              "to quit  (ru-verb)"),
    ([("","い"),("","つ"),("","も")],                "always"),
    ([("あか","赤"),("","い")],                      "red  (i-adj)"),
    ([("ばん","晩"),("","ご"),("はん","飯")],        "dinner"),
    ([("ぎん","銀"),("こう","行")],                  "bank"),
    ([("こう","公"),("えん","園")],                  "park"),
    ([("","お"),("べん","弁"),("とう","当")],        "box lunch"),
]
story.append(vocab_two_col(vocab310))
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


# ════════════════════════════════════════════════════════════════════════════
# PAGE 10 — 3.11 Noun-related Particles
# ════════════════════════════════════════════════════════════════════════════
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
if False:
    pass

doc.build(story)
print("Done:", output_path)
