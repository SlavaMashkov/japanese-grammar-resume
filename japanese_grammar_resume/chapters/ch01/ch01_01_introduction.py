from ...styles import *


def build():
    story = []

    # Title
    story.append(Paragraph("1  Introduction", title_s))
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

    # --- 1.1 The problem with conventional textbooks ---
    story.append(section_header("1.1  The Problem with Conventional Textbooks"))
    story.append(Spacer(1, 1 * mm))
    for n in [
        "Textbooks try to teach Japanese through English — forcing English phrases into Japanese structure.",
        'They prioritize polite form and "useful" phrases before explaining how the language actually works.',
        "Kanji is avoided, leaving learners unable to read anything real when they arrive in Japan.",
        'The result: a patchwork of "say this to mean that" rules with no understanding of the underlying logic.',
    ]:
        story.append(Paragraph(f"- {n}", note_s))
    story.append(Spacer(1, 3.5 * mm))

    # --- 1.2 A Japanese guide to learning Japanese grammar ---
    story.append(section_header("1.2  A Japanese Guide to Learning Japanese Grammar"))
    story.append(Spacer(1, 1 * mm))
    for n in [
        "This guide explains Japanese from a Japanese point of view — no artificial ties to English.",
        "Material is ordered logically: if [A] is needed to understand [B], [A] is covered first.",
        "Early translations are intentionally literal (no articles, no subjects) to convey the Japanese sense.",
        "The hardest concepts come first, building a solid foundation; everything after becomes easier.",
        jp("Japanese quotation marks: 「 」 (half brackets)."),
    ]:
        story.append(Paragraph(f"- {n}", note_s))
    story.append(Spacer(1, 3.5 * mm))

    # --- 1.3 Suggestions ---
    story.append(section_header("1.3  Suggestions"))
    story.append(Spacer(1, 1 * mm))
    for n in [
        "Don't translate from English — if you don't already know how to say it, ask and learn from the answer.",
        "Learn by example: move on if something is unclear, revisit as you see more contexts.",
        "Read Japanese everywhere — websites, books, manga. Vocabulary grows with exposure.",
        "Speaking and listening require real conversation with fluent speakers — audio alone is not enough.",
    ]:
        story.append(Paragraph(f"- {n}", note_s))

    return story
