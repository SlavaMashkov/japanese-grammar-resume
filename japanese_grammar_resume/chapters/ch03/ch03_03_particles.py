from ...styles import *


def build():
    story = []

    story.append(PageBreak())

    story.append(Paragraph(jp("3.3  Introduction to Particles  （は、も、が）"), title_s))
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

    # --- Vocabulary 3.3 ---
    story.append(section("Vocabulary"))
    story.append(Spacer(1, 1 * mm))

    story.append(
        vocab_two_col(
            vocab_from_registry(
                [
                    "誰",
                    "私",
                    "でも",
                ]
            )
        )
    )
    story.append(Spacer(1, 3.5 * mm))

    # --- Particles Table ---
    particles = [
        ["Particle", "Name", "Function", "Example"],
        [
            "は\n(wa)",
            "Topic",
            "Marks what the sentence is about.\nPronounced は /ha/ normally, /wa/ as particle.",
            "アリスは学生？\nIs Alice a student?",
        ],
        [
            "も\n(mo)",
            "Inclusive\nTopic",
            'Like は but adds meaning of "also".\nMust be consistent: all positive or all negative.',
            "トムも学生。\nTom is also a student.",
        ],
        [
            "が\n(ga)",
            "Identifier",
            'Identifies a specific answer to an unspecified question.\nOften answers "who?" or "what?".',
            "誰が学生？ — ジョンが学生。\nWho is the student? — John is.",
        ],
    ]

    prows = []
    for ri, row in enumerate(particles):
        prows.append([cell(c, bold=(ri == 0), center=(ri == 0 or ci == 0), sz=8) for ci, c in enumerate(row)])

    col_p = [19 * mm, 20 * mm, 65 * mm, W - 104 * mm]
    pt = Table(prows, colWidths=col_p, repeatRows=1)
    pt.setStyle(
        TableStyle(
            TABLE_STYLE
            + [
                ("BACKGROUND", (0, 1), (0, -1), CR1),
                ("FONTNAME", (0, 1), (0, -1), "DV-B"),
            ]
        )
    )
    story.append(section("Grammar: The Three Particles", pt))
    story.append(Spacer(1, 3.5 * mm))

    # --- は vs が comparison ---
    story.append(section(jp("Note: は vs が")))
    story.append(Spacer(1, 1 * mm))

    hg = [
        ["", jp("私は学生。"), jp("私が学生。")],
        ["Translation", "As for me, I am a student.", "I am the one who is a student."],
        ["Use", "Introduces a new topic (me).", "Identifies me as the specific answer."],
    ]
    hgrows = [
        [cell(c, bold=(ri == 0), center=(ci == 0), sz=8) for ci, c in enumerate(row)]
        for ri, row in enumerate(hg)
    ]
    hw2 = (W - 28 * mm) / 2
    hgt = Table(hgrows, colWidths=[28 * mm, hw2, hw2])
    hgt.setStyle(
        TableStyle(
            TABLE_STYLE
            + [
                ("BACKGROUND", (0, 1), (0, -1), CR1),
                ("FONTNAME", (0, 1), (0, -1), "DV-B"),
            ]
        )
    )
    story.append(hgt)
    story.append(Spacer(1, 3.5 * mm))

    story.append(section("Notes"))
    story.append(Spacer(1, 1 * mm))
    notes33 = [
        jp("Once a topic is set with は, it doesn't need to be repeated — context carries it forward."),
        jp("も must be consistent: if one is negative, all も-linked items must also be negative."),
        jp('が always answers (or implies) a question like "who?" or "what?" — it identifies.'),
        jp('Think of は as "as for..." and が as "the one that is..."'),
    ]
    for n in notes33:
        story.append(Paragraph(f"- {n}", note_s))

    return story
