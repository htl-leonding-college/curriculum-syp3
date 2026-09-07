#!/usr/bin/env python3
"""Fragenkatalog aus den questions.adoc der Module (P3, P8).

Die Zuordnungsmerkmale — Block, unterrichtender Jahrgang, voraussetzender
Jahrgang, Thema — stammen aus dem Modell und stehen nicht im Fragentext.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from tools import adoc, generated  # noqa: E402
from tools.curriculum import DEFAULT_PATH, Curriculum, load  # noqa: E402

OUTPUT = "questions/index.adoc"
DATA_OUTPUT = "questions/questions.json"


def collect(model: Curriculum) -> list[dict]:
    rows: list[dict] = []
    for topic in model.topics:
        if not topic.questions_path.is_file():
            continue
        for question in adoc.read(topic.questions_path).questions():
            rows.append(
                {
                    "question": question.title,
                    "topic": topic.id,
                    "topic_title": topic.title,
                    "block": topic.block,
                    "kind": topic.kind,
                    "lesson": topic.lesson,
                    "taught_in": topic.taught_in,
                    "prerequisite_for": topic.prerequisite_for,
                    "covers": list(question.covers),
                    "source": str(topic.questions_path.relative_to(model.root)),
                    "line": question.line,
                }
            )
    return rows


def render(model: Curriculum, rows: list[dict]) -> str:
    titles = {block.id: block.title for block in model.blocks}
    lines = [
        f"= Fragenkatalog {model.meta.get('gegenstand', 'SYP')} "
        f"{model.meta.get('jahrgang', '')}".rstrip(),
        ":toc: left",
        ":toc-title: Inhalt",
        ":toclevels: 3",
        ":icons: font",
        "",
        "ifdef::env-github[]",
        ":tip-caption: :bulb:",
        ":note-caption: :information_source:",
        ":important-caption: :heavy_exclamation_mark:",
        ":caution-caption: :fire:",
        ":warning-caption: :warning:",
        "endif::[]",
        "",
        f"{len(rows)} Fragen aus {len({r['topic'] for r in rows})} Modulen. "
        "Massgeblich fuer SYP 3. Jahrgang ab dem Schuljahr 2026/27; der bestehende "
        "https://htl-leonding-college.github.io/fragenkatalog[Fragenkatalog] bleibt "
        "als Archiv erhalten.",
        "",
    ]
    if not rows:
        lines += ["Noch keine Fragen — die Module tragen ihre Fragen selbst.", ""]

    for block in model.blocks:
        block_rows = [r for r in rows if r["block"] == block.id]
        if not block_rows:
            continue
        lines += [f"== {titles.get(block.id, block.id)}", ""]
        for topic_id in sorted({r["topic"] for r in block_rows}):
            topic_rows = [r for r in block_rows if r["topic"] == topic_id]
            head = topic_rows[0]
            lines += [
                f"=== U{head['lesson']} {head['topic_title']}",
                "",
                f"[.tags]#block: {head['block']}# "
                f"[.tags]#taught_in: {head['taught_in']}# "
                f"[.tags]#prerequisite_for: {head['prerequisite_for']}# "
                f"[.tags]#topic: {topic_id}#",
                "",
            ]
            for row in topic_rows:
                covers = ", ".join(row["covers"]) or "—"
                lines += [
                    f". {row['question']} "
                    f"[.covers]#({covers})#",
                ]
            lines += [""]
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--curriculum", type=Path, default=DEFAULT_PATH)
    parser.add_argument("--build-dir", type=Path, default=None)
    args = parser.parse_args(argv)
    model = load(args.curriculum)
    rows = collect(model)
    target = generated.write(OUTPUT, render(model, rows), build_dir=args.build_dir)
    payload = {"generated": generated.MARKER, "questions": rows}
    data = generated.write(
        DATA_OUTPUT, json.dumps(payload, indent=2, ensure_ascii=False) + "\n",
        build_dir=args.build_dir,
    )
    print(target)
    print(data)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
