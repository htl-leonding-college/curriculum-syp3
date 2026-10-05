#!/usr/bin/env python3
"""Website-Navigation in Unterrichtsreihenfolge (P3)."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from tools import generated  # noqa: E402
from tools.curriculum import (  # noqa: E402
    DEFAULT_PATH,
    Curriculum,
    Topic,
    kind_label,
    load,
    subject_year_label,
)

OUTPUT = "nav.adoc"


def _entry(topic: Topic) -> str:
    label = f"{kind_label(topic.kind)}: {topic.title}"
    if topic.is_ready:
        # Neben dem Lerninhalt stehen Aufgaben und Fragen; ohne diese
        # Verweise waeren beide Seiten nur ueber ihre Adresse zu finden.
        entry = (
            f"** xref:modules/{topic.id}/index.adoc[{label}]"
            f" — xref:modules/{topic.id}/exercises.adoc[Exercises]"
            f" · xref:modules/{topic.id}/questions.adoc[Questions]"
        )
    else:
        entry = f"** {label} _(planned)_"
    if topic.assignment_template:
        entry += f" — https://github.com/{topic.assignment_template}[Assignment]"
    return entry


def render(model: Curriculum) -> str:
    # Kein Dokumenttitel: die Navigation wird eingebunden, nicht einzeln gebaut.
    lines: list[str] = []
    by_lesson: dict[int, list] = {}
    for topic in model.current:
        by_lesson.setdefault(topic.lesson, []).append(topic)

    for lesson in sorted(by_lesson):
        lines.append(f"* Lesson {lesson}")
        for topic in sorted(by_lesson[lesson], key=lambda t: t.kind, reverse=True):
            lines.append(_entry(topic))

    # Verschobene Themen stehen ohne Unterricht am Ende, je Jahrgang gruppiert.
    gegenstand = str(model.meta.get("gegenstand", "SYP"))
    for year in sorted({t.taught_in for t in model.later}):
        lines.append(f"* {subject_year_label(gegenstand, year)}")
        for topic in sorted(
            (t for t in model.later if t.taught_in == year),
            key=lambda t: (t.kind, t.id),
            reverse=True,
        ):
            lines.append(_entry(topic))
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
