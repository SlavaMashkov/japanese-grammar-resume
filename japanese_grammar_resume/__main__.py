import argparse

from .styles import *

from .chapters import ch03_02_state_of_being
from .chapters import ch03_03_particles
from .chapters import ch03_04_adjectives
from .chapters import ch03_05_verb_basics
from .chapters import ch03_06_negative_verbs
from .chapters import ch03_07_past_tense
from .chapters import ch03_08_verb_particles
from .chapters import ch03_09_transitive
from .chapters import ch03_10_relative_clauses
from .chapters import ch03_11_noun_particles


def main():
    parser = argparse.ArgumentParser(description="Generate Japanese grammar summary PDF")
    parser.add_argument("-o", "--output-dir", default=os.path.join(BASE_DIR, "output"),
                        help="Output directory (default: output/)")
    args = parser.parse_args()

    output_path = os.path.join(args.output_dir, "japanese_summary.pdf")
    os.makedirs(args.output_dir, exist_ok=True)
    doc = SimpleDocTemplate(output_path, pagesize=A4,
                            leftMargin=15*mm, rightMargin=15*mm,
                            topMargin=12*mm, bottomMargin=12*mm,
                            title="Japanese Grammar Guide — Chapter Summaries",
                            subject="Japanese grammar notes: state-of-being, particles, adjectives",
                            author="Claude (Anthropic)")

    story = []
    story += ch03_02_state_of_being.build()
    story += ch03_03_particles.build()
    story += ch03_04_adjectives.build()
    story += ch03_05_verb_basics.build()
    story += ch03_06_negative_verbs.build()
    story += ch03_07_past_tense.build()
    story += ch03_08_verb_particles.build()
    story += ch03_09_transitive.build()
    story += ch03_10_relative_clauses.build()
    story += ch03_11_noun_particles.build()

    doc.build(story)
    print("Done:", output_path)


if __name__ == "__main__":
    main()
