#!/usr/bin/env python3
"""UE-Uebersicht je Block und je Art (P3)."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from tools import generated  # noqa: E402
from tools.curriculum import DEFAULT_PATH, Curriculum, load  # noqa: E402

OUTPUT = "ue-overview.adoc"


def render(model: Curriculum) -> str:
    budget = model.meta.get("budget") or {}
    per_block_budget = model.meta.get("budget_je_block") or {}
    by_kind = model.ue_by_kind()
    theory_by_block = model.theory_ue_by_block()

    # Kein Dokumenttitel: die Uebersicht wird eingebunden, nicht einzeln gebaut.
    lines = [
        "== Je Art",
        "",
        '[cols="1,1,1,3",options="header"]',
        "|===",
        "|Art |UE |Budget |Themen",
        "",
    ]
    for kind in sorted(by_kind):
        topics = model.of_kind(kind)
        lines += [
            f"|{kind}",
            f"|{by_kind[kind]}",
            f"|{budget.get(kind, '—')}",
            f"|{len(topics)}",
            "",
        ]
    lines += ["|===", "", "== Theorie je Block", "",
              '[cols="1,1,1,3",options="header"]', "|===",
              "|Block |UE |Budget |Themen", ""]
    for block in model.blocks:
        topics = [t for t in model.of_kind("theorie") if t.block == block.id]
        lines += [
            f"|{block.title}",
            f"|{theory_by_block.get(block.id, 0)}",
            f"|{per_block_budget.get(block.id, '—')}",
            f"|{len(topics)}",
            "",
        ]
    lines += ["|===", "", "== Praxis je Block", "",
              '[cols="1,1,3",options="header"]', "|===", "|Block |UE |Themen", ""]
    for block in model.blocks:
        topics = [t for t in model.of_kind("praxis") if t.block == block.id]
        lines += [f"|{block.title}", f"|{sum(t.ue for t in topics)}", f"|{len(topics)}", ""]
    lines += ["|===", ""]

    ready, planned = len(model.ready), len(model.planned)
    lines += [
        "== Bearbeitungsstand",
        "",
        f"{ready} von {len(model.topics)} Themen sind fertig, {planned} sind offen.",
        "",
    ]
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
