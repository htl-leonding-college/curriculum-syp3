#!/usr/bin/env python3
"""Stoffstruktur als PlantUML-Mindmap (P3).

Vier Ebenen: Gegenstand -> Block -> Strang (``theme``) -> Thema. Ein Thema ohne
``theme`` hängt direkt unter seinem Block. Fertige Themen stehen schwarz,
geplante grau — der Stand ist damit auf einen Blick sichtbar.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from tools import generated  # noqa: E402
from tools.curriculum import DEFAULT_PATH, Curriculum, Topic, load  # noqa: E402

OUTPUT = "stoffstruktur.puml"

ROOT_COLOR = "#lightblue"

#: Farbe je Block. Ein unbekannter Block fällt auf FALLBACK_COLOR zurück,
#: damit ein neuer Block die Mindmap nicht bricht.
BLOCK_COLORS = {
    "governance": "#lightgreen",
    "vorgehen": "#lightyellow",
    "modellierung": "#plum",
    "werkzeuge": "#peachpuff",
}
FALLBACK_COLOR = "#whitesmoke"

PLANNED_COLOR = "#808080"


def _topic_line(topic: Topic, depth: int) -> str:
    label = f"U{topic.lesson} {topic.title}"
    if not topic.is_ready:
        label = f"<color:{PLANNED_COLOR}>{label} (offen)</color>"
    return f"{'*' * depth}_ {label}"


def _sorted_topics(topics: list[Topic]) -> list[Topic]:
    return sorted(topics, key=lambda t: (t.lesson, t.kind))


def _themes(topics: list[Topic]) -> list[str]:
    """Stränge in der Reihenfolge ihres ersten Unterrichts."""
    first: dict[str, int] = {}
    for topic in topics:
        if topic.theme and topic.lesson < first.get(topic.theme, 10**6):
            first[topic.theme] = topic.lesson
    return sorted(first, key=lambda name: (first[name], name))


def _block_lines(model: Curriculum, block) -> list[str]:
    topics = [t for t in model.topics if t.block == block.id]
    theorie = sum(t.ue for t in topics if t.kind == "theorie")
    praxis = sum(t.ue for t in topics if t.kind == "praxis")
    color = BLOCK_COLORS.get(block.id, FALLBACK_COLOR)
    lines = [f"**[{color}] {block.title}\\n{theorie} UE T / {praxis} UE P"]
    for topic in _sorted_topics([t for t in topics if not t.theme]):
        lines.append(_topic_line(topic, 3))
    for theme in _themes(topics):
        lines.append(f"*** {theme}")
        for topic in _sorted_topics([t for t in topics if t.theme == theme]):
            lines.append(_topic_line(topic, 4))
    return lines


def render(model: Curriculum) -> str:
    meta = model.meta
    root = str(meta.get("gegenstand", "SYP"))
    jahrgang = str(meta.get("jahrgang", "")).strip()
    if jahrgang.startswith("jg") and jahrgang[2:].isdigit():
        root += f"\\n{int(jahrgang[2:])}. Jahrgang"
    elif jahrgang:
        root += f"\\n{jahrgang}"
    schuljahr = str(meta.get("schuljahr", "")).strip()
    if schuljahr:
        root += f"\\n{schuljahr}"

    lines = [
        "@startmindmap",
        "skinparam shadowing false",
        "skinparam defaultFontName Helvetica",
        f"*[{ROOT_COLOR}] {root}",
    ]
    # Alles auf einer Seite: zweiseitig wird die Karte so breit, dass die
    # Schrift beim Skalieren auf Seitenbreite unlesbar klein wird.
    for block in model.blocks:
        lines.extend(_block_lines(model, block))
    lines.append("legend right")
    lines.append(f"  <color:{PLANNED_COLOR}>grau</color> = geplant, Modul offen")
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
