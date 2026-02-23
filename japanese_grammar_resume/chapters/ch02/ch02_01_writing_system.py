from ...styles import *


def build():
    story = []

    story.append(PageBreak())
    story.append(Paragraph(jp("2  The Writing System  （書記体系）"), title_s))
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

    # --- 2.1 The Scripts ---
    story.append(section("2.1  The Scripts"))
    story.append(Spacer(1, 1 * mm))
    for n in [
        jp(
            "Three scripts: Hiragana + Katakana (kana — phonetic, ~46 characters each)"
            " and Kanji (Chinese characters)."
        ),
        jp(
            "Kanji: nouns, verbs, adjectives. ~2,000 cover 95% of text."
            " Separates words (no spaces) and distinguishes homophones."
        ),
        jp("Hiragana: grammar (particles, endings), rare-kanji words, colloquial expressions, onomatopoeia."),
        jp("Katakana: foreign loanwords, emphasis (like italics), scientific terms."),
    ]:
        story.append(Paragraph(f"- {n}", note_s))
    story.append(Spacer(1, 3.5 * mm))

    # --- 2.2 Intonation ---
    story.append(section("2.2  Intonation"))
    story.append(Spacer(1, 1 * mm))
    for n in [
        jp(
            "Each kana = one syllable: [vowel] or [consonant + vowel]. Only exception: ん / ン (standalone /n/)."
        ),
        "Pitch accent (high/low tones) is crucial — homophones often differ only in pitch.",
        "Don't memorize pitch rules (they vary by context and dialect). Learn by mimicking native speakers.",
    ]:
        story.append(Paragraph(f"- {n}", note_s))
    return story
