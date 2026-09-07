"""Erzeugte Artefakte bleiben unversioniert (P3).

Der Ersatz fuer einen Diff-Vergleich: Sie liegen ausschliesslich unter
``build/``, das ignoriert wird, und werden bei jedem Build neu geschrieben.
Eine Handaenderung ist damit beim naechsten Lauf verworfen — versioniert
duerfte sie ueberleben, deshalb faellt genau das hier auf.
"""

from __future__ import annotations

import subprocess

from conftest import REPO_ROOT

from tools.generated import MARKER


def tracked_files() -> list[str]:
    result = subprocess.run(
        ["git", "ls-files"], cwd=REPO_ROOT, capture_output=True, text=True, check=True
    )
    return [line for line in result.stdout.splitlines() if line]


def test_no_generated_artefact_is_versioned() -> None:
    offenders = []
    for name in tracked_files():
        path = REPO_ROOT / name
        if not path.is_file() or path.suffix not in (".adoc", ".puml", ".json", ".txt"):
            continue
        try:
            head = path.read_text(encoding="utf-8")[:400]
        except UnicodeDecodeError:
            continue
        if MARKER in head and not name.startswith("tools/"):
            offenders.append(name)
    assert offenders == [], f"erzeugte Dateien im Versionsstand: {offenders}"


def test_build_directory_is_ignored() -> None:
    result = subprocess.run(
        ["git", "check-ignore", "build/nav.adoc"],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, "build/ muss in .gitignore stehen"
