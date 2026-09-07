#!/usr/bin/env python3
"""Stoffstruktur als PlantUML-Mindmap (P3)."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from tools import generated  # noqa: E402
from tools.curriculum import DEFAULT_PATH, Curriculum, load  # noqa: E402

OUTPUT = "stoffstruktur.puml"


def render(model: Curriculum) -> str:
    meta = model.meta
    lines = [
        "@startmindmap",
        "skinparam monochrome true",
        "skinparam shadowing false",
        f"* {meta.get('gegenstand', 'SYP')} {meta.get('jahrgang', '')}".rstrip(),
    ]
    for block in model.blocks:
        topics = [t for t in model.topics if t.block == block.id]
        theorie = sum(t.ue for t in topics if t.kind == "theorie")
        praxis = sum(t.ue for t in topics if t.kind == "praxis")
        lines.append(f"** {block.title}\\n{theorie} UE T / {praxis} UE P")
        for topic in sorted(topics, key=lambda t: (t.lesson, t.kind)):
            open_marker = "" if topic.is_ready else " (offen)"
            lines.append(f"*** U{topic.lesson} {topic.title}{open_marker}")
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
