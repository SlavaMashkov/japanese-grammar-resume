from ...styles import *


def build():
    story = []

    story.append(PageBreak())
    story.append(Paragraph("1.2  A Japanese Guide to Learning Japanese Grammar", title_s))
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
        "This guide explains Japanese from a Japanese point of view — no artificial ties to English.",
        "Material is ordered logically: if [A] is needed to understand [B], [A] is covered first.",
        "Early translations are intentionally literal (no articles, no subjects) to convey the Japanese sense.",
        "The hardest concepts come first, building a solid foundation; everything after becomes easier.",
        jp("Japanese quotation marks: 「 」 (half brackets)."),
    ]:
        story.append(Paragraph(n, note_s))

    return story
