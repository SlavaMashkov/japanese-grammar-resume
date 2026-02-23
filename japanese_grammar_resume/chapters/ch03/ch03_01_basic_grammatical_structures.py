from ...styles import *


def build():
    story = []

    story.append(PageBreak())
    story.append(Paragraph("3.1  Basic Grammatical Structures", title_s))
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
        "This section covers all the parts of speech: nouns, adjectives, verbs, and adverbs.",
        "It describes how to integrate the various parts of speech into a coherent sentence by using particles.",
        "By the end of this section, you should have an understanding of how basic sentences are constructed.",
    ]:
        story.append(Paragraph(f"- {n}", note_s))

    return story
