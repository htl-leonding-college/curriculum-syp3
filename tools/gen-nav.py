#!/usr/bin/env python3
"""Website-Navigation in Unterrichtsreihenfolge (P3)."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from tools import generated  # noqa: E402
from tools.curriculum import DEFAULT_PATH, Curriculum, load  # noqa: E402

OUTPUT = "nav.adoc"
KIND_LABEL = {"theorie": "Theorie", "praxis": "Praxis"}


def render(model: Curriculum) -> str:
    # Kein Dokumenttitel: die Navigation wird eingebunden, nicht einzeln gebaut.
    lines: list[str] = []
    by_lesson: dict[int, list] = {}
    for topic in model.topics:
        by_lesson.setdefault(topic.lesson, []).append(topic)

    for lesson in sorted(by_lesson):
        lines.append(f"* U{lesson}")
        for topic in sorted(by_lesson[lesson], key=lambda t: t.kind, reverse=True):
            label = f"{KIND_LABEL.get(topic.kind, topic.kind)}: {topic.title}"
            if topic.is_ready:
                # Neben dem Lerninhalt stehen Aufgaben und Fragen; ohne diese
                # Verweise waeren beide Seiten nur ueber ihre Adresse zu finden.
                entry = (
                    f"** xref:modules/{topic.id}/index.adoc[{label}]"
                    f" — xref:modules/{topic.id}/exercises.adoc[Übungen]"
                    f" · xref:modules/{topic.id}/questions.adoc[Fragen]"
                )
            else:
                entry = f"** {label} _(offen)_"
            if topic.assignment_template:
                entry += (
                    f" — https://github.com/{topic.assignment_template}[Angabe]"
                )
            lines.append(entry)
    lines.append("")
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--curriculum", type=Path, default=DEFAULT_PATH)
    parser.add_argument("--build-dir", type=Path, default=None)
    args = parser.parse_args(argv)
    target = generated.write(OUTPUT, render(load(args.curriculum)), build_dir=args.build_dir)
    print(target)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
