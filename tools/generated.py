"""Gemeinsames Schreiben erzeugter Artefakte (P3).

Erzeugte Dateien landen ausschliesslich unter ``build/``, tragen einen
Kopfhinweis und werden bei jedem Build neu geschrieben. Eine Handaenderung ist
damit beim naechsten Lauf verworfen.
"""

from __future__ import annotations

from pathlib import Path

from tools.curriculum import REPO_ROOT

BUILD_DIR = REPO_ROOT / "build"

MARKER = "GENERATED — do not edit. Quelle: curriculum.yaml"

COMMENT_PREFIX = {
    ".adoc": "//",
    ".puml": "'",
    ".txt": "#",
    # JSON kennt keinen Kommentar — der Hinweis steht dort im Feld "generated".
    ".json": None,
}


def write(relative: str | Path, body: str, *, build_dir: Path | None = None) -> Path:
    """Schreibt ``body`` mit Kopfhinweis nach ``build/<relative>``."""
    target = (build_dir or BUILD_DIR) / Path(relative)
    target.parent.mkdir(parents=True, exist_ok=True)
    prefix = COMMENT_PREFIX.get(target.suffix, "#")
    header = f"{prefix} {MARKER}\n" if prefix else ""
    target.write_text(header + body, encoding="utf-8")
    return target
