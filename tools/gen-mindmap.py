#!/usr/bin/env python3
"""Stoffstruktur als PlantUML-Mindmap (P3).

Vier Ebenen: Gegenstand -> Block -> Strang (``theme``) -> Thema. Ein Thema ohne
``theme`` hängt direkt unter seinem Block. Fertige Themen stehen schwarz,
geplante grau — der Stand ist damit auf einen Blick sichtbar.

Je Jahrgang eine Wurzel: ``SYP3`` trägt den Jahresplan, ``SYP4`` die Themen,
die in den nächsten Jahrgang verschoben sind — ohne Unterrichtsnummer.
"""

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
    lesson_label,
    load,
    subject_year_label,
)

OUTPUT = "stoffstruktur.puml"

ROOT_COLOR = "#E3ECF8"

#: Farbe je Block. Ein unbekannter Block fällt auf FALLBACK_COLOR zurück,
#: damit ein neuer Block die Mindmap nicht bricht.
BLOCK_COLORS = {
    "governance": "#E4F0E4",
    "vorgehen": "#FAF0D9",
    "modellierung": "#ECE6F7",
    "werkzeuge": "#F9E6DC",
}
FALLBACK_COLOR = "#F0F2F5"

PLANNED_COLOR = "#808080"


def _topic_line(topic: Topic, depth: int) -> str:
    label = topic.title
    if topic.lesson is not None:
        label = f"{lesson_label(topic.lesson)} {label}"
    if not topic.is_ready:
        label = f"<color:{PLANNED_COLOR}>{label} (planned)</color>"
    return f"{'*' * depth}_ {label}"


def _sorted_topics(topics: list[Topic]) -> list[Topic]:
    return sorted(topics, key=lambda t: (t.lesson or 0, t.kind, t.id))


def _themes(topics: list[Topic]) -> list[str]:
    """Stränge in der Reihenfolge ihres ersten Unterrichts."""
    first: dict[str, int] = {}
    for topic in topics:
        lesson = topic.lesson or 0
        if topic.theme and lesson < first.get(topic.theme, 10**6):
            first[topic.theme] = lesson
    return sorted(first, key=lambda name: (first[name], name))


def _units(count: int) -> str:
    return f"{count} unit" if count == 1 else f"{count} units"


def _block_lines(block, topics: list[Topic]) -> list[str]:
    topics = [t for t in topics if t.block == block.id]
    theorie = sum(t.ue for t in topics if t.kind == "theorie")
    praxis = sum(t.ue for t in topics if t.kind == "praxis")
    color = BLOCK_COLORS.get(block.id, FALLBACK_COLOR)
    lines = [
        f"**[{color}] {block.title}\\n"
        f"{_units(theorie)} theory / {_units(praxis)} practice"
    ]
    for topic in _sorted_topics([t for t in topics if not t.theme]):
        lines.append(_topic_line(topic, 3))
    for theme in _themes(topics):
        lines.append(f"***[{color}] {theme}")
        for topic in _sorted_topics([t for t in topics if t.theme == theme]):
            lines.append(_topic_line(topic, 4))
    return lines


def _years(model: Curriculum) -> list[str]:
    """Eigener Jahrgang zuerst, danach die übrigen aufsteigend."""
    others = sorted({t.taught_in for t in model.later})
    return [model.jahrgang, *others]


def render(model: Curriculum) -> str:
    gegenstand = str(model.meta.get("gegenstand", "SYP"))
    lines = [
        "@startmindmap",
        "skinparam shadowing false",
        "skinparam defaultFontName Helvetica",
    ]
    # Alles auf einer Seite: zweiseitig wird die Karte so breit, dass die
    # Schrift beim Skalieren auf Seitenbreite unlesbar klein wird.
    for year in _years(model):
        topics = [t for t in model.topics if t.taught_in == year]
        if not topics:
            continue
        lines.append(f"*[{ROOT_COLOR}] {subject_year_label(gegenstand, year)}")
        for block in model.blocks:
            if any(t.block == block.id for t in topics):
                lines.extend(_block_lines(block, topics))
    lines.append("legend right")
    lines.append(
        f"  <color:{PLANNED_COLOR}>grey</color> = planned, module not written yet"
    )
    lines.append("endlegend")
    lines.append("@endmindmap")
    return "\n".join(lines) + "\n"


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
