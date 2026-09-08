#!/usr/bin/env python3
"""Meldet Bilder mit ungeklärter Rechtelage (P11).

Eigener Schritt, nicht Teil des Builds: `unclear` soll sichtbar sein, aber die
Veröffentlichung von 48 Modulen nicht an einem einzigen Bild aufhängen —
sonst wird die Klasse gemieden und das Feld wertlos.
"""

from __future__ import annotations

import argparse
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from tools import adoc  # noqa: E402
from tools.curriculum import DEFAULT_PATH, load  # noqa: E402


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--curriculum", type=Path, default=DEFAULT_PATH)
    args = parser.parse_args(argv)

    model = load(args.curriculum)
    counts: Counter[str] = Counter()
    unclear: list[str] = []

    for path in model.adoc_files():
        for image in adoc.read(path).images():
            counts[image.provenance or "ohne Angabe"] += 1
            if image.provenance == "unclear":
                relative = path.relative_to(model.root)
                unclear.append(
                    f"{relative}:{image.line}: {image.target} "
                    f"({image.provenance_detail or 'ohne Begründung'})"
                )

    total = sum(counts.values())
    print(f"{total} Bilder: " + ", ".join(f"{k}={v}" for k, v in sorted(counts.items())))
    for line in unclear:
        print(line)

    if unclear:
        print(
            f"\n{len(unclear)} Bilder mit ungeklärter Rechtelage. "
            "Die Veröffentlichung läuft weiter; die Klärung steht aus.",
            file=sys.stderr,
        )
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
