from ...styles import *


def build():
    story = []

    story.append(PageBreak())
    story.append(Paragraph("1.1  The Problem with Conventional Textbooks", title_s))
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

    for n in [
        "Textbooks try to teach Japanese through English — forcing English phrases into Japanese structure.",
        'They prioritize polite form and "useful" phrases before explaining how the language actually works.',
        "Kanji is avoided, leaving learners unable to read anything real when they arrive in Japan.",
        'The result: a patchwork of "say this to mean that" rules with no understanding of the underlying logic.',
    ]:
        story.append(Paragraph(n, note_s))

    return story
