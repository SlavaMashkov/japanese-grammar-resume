from ...styles import *


def build():
    story = []

    story.append(PageBreak())
    story.append(Paragraph("2.2  Intonation", title_s))
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
        jp(
            "Each kana = one syllable: [vowel] or [consonant + vowel]. Only exception: ん / ン (standalone /n/)."
        ),
        "Pitch accent (high/low tones) is crucial — homophones often differ only in pitch.",
        "Don't memorize pitch rules (they vary by context and dialect). Learn by mimicking native speakers.",
    ]:
        story.append(Paragraph(f"- {n}", note_s))

    return story
