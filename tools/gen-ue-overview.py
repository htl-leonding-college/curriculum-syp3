#!/usr/bin/env python3
"""Umfangsübersicht je Block und je Art (P3). Ausgabe englisch."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from tools import generated  # noqa: E402
from tools.curriculum import (  # noqa: E402
    DEFAULT_PATH,
    Curriculum,
    kind_label,
    load,
)

OUTPUT = "ue-overview.adoc"


def render(model: Curriculum) -> str:
    budget = model.meta.get("budget") or {}
    per_block_budget = model.meta.get("budget_je_block") or {}
    by_kind = model.ue_by_kind()
    theory_by_block = model.theory_ue_by_block()

    # Kein Dokumenttitel: die Übersicht wird eingebunden, nicht einzeln gebaut.
    lines = [
        "== By kind",
        "",
        '[cols="1,1,1,3",options="header"]',
        "|===",
        "|Kind |Units |Budget |Topics",
        "",
    ]
    for kind in sorted(by_kind):
        topics = model.of_kind(kind)
        lines += [
            f"|{kind_label(kind)}",
            f"|{by_kind[kind]}",
            f"|{budget.get(kind, '—')}",
            f"|{len(topics)}",
            "",
        ]
    lines += ["|===", "", "== Theory units per block", "",
              '[cols="1,1,1,3",options="header"]', "|===",
              "|Block |Units |Budget |Topics", ""]
    for block in model.blocks:
        topics = [t for t in model.of_kind("theorie") if t.block == block.id]
        lines += [
            f"|{block.title}",
            f"|{theory_by_block.get(block.id, 0)}",
            f"|{per_block_budget.get(block.id, '—')}",
            f"|{len(topics)}",
            "",
        ]
    lines += ["|===", "", "== Practice units per block", "",
              '[cols="1,1,3",options="header"]', "|===", "|Block |Units |Topics", ""]
    for block in model.blocks:
        topics = [t for t in model.of_kind("praxis") if t.block == block.id]
        lines += [f"|{block.title}", f"|{sum(t.ue for t in topics)}", f"|{len(topics)}", ""]
    lines += ["|===", ""]

    ready, planned = len(model.ready), len(model.planned)
    lines += [
        "== Progress",
        "",
        f"{ready} of {len(model.topics)} topics are finished, {planned} are still open.",
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
