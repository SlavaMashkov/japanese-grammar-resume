from ...styles import *


def build():
    story = []

    story.append(PageBreak())
    story.append(Paragraph("1.3  Suggestions", title_s))
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
        "Don't translate from English — if you don't already know how to say it, ask and learn from the answer.",
        "Learn by example: move on if something is unclear, revisit as you see more contexts.",
        "Read Japanese everywhere — websites, books, manga. Vocabulary grows with exposure.",
        "Speaking and listening require real conversation with fluent speakers — audio alone is not enough.",
    ]:
        story.append(Paragraph(f"- {n}", note_s))

    return story
