#!/usr/bin/env python3
"""Legt das Skelett eines Moduls aus der Vorlage an (P4).

Der Zuschnitt kommt aus dem Modell: Titel und Pfad folgen der Themen-ID,
Struktur kommt aus ``templates/module/``.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from tools.curriculum import DEFAULT_PATH, REPO_ROOT, Topic, load  # noqa: E402

TEMPLATE_DIR = REPO_ROOT / "templates" / "module"

PLACEHOLDERS = {
    "OUTCOME": "TODO: was nach diesem Unterricht gekonnt werden muss",
    "SECTION": "TODO: Abschnittstitel",
    "TERM_DE": "TODO",
    "TERM_EN": "TODO",
    "SOURCE": "TODO: Quelle",
    "EXERCISE_TITLE": "TODO: Aufgabentitel",
    "EXERCISE_TASK": "TODO: Arbeitsauftrag",
    "EXERCISE_SOLUTION": "TODO: Loesung oder Abschnitt loeschen",
    "QUESTION": "TODO: Pruefungsfrage",
    "ANSWER_POINT": "TODO: erwarteter Punkt",
}


def render(template: str, topic: Topic) -> str:
    text = template.replace("{{TITLE}}", topic.title).replace("{{TOPIC_ID}}", topic.id)
    for key, value in PLACEHOLDERS.items():
        text = text.replace("{{" + key + "}}", value)
    return text


def create(
    topic: Topic,
    *,
    template_dir: Path = TEMPLATE_DIR,
    force: bool = False,
) -> list[Path]:
    written: list[Path] = []
    topic.module_dir.mkdir(parents=True, exist_ok=True)
    topic.images_dir.mkdir(exist_ok=True)
    (topic.images_dir / ".gitkeep").touch()
    for name in ("index.adoc", "exercises.adoc", "questions.adoc"):
        target = topic.module_dir / name
        if target.exists() and not force:
            continue
        target.write_text(
            render((template_dir / name).read_text(encoding="utf-8"), topic),
            encoding="utf-8",
        )
        written.append(target)
    return written


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("topic_id", nargs="+")
    parser.add_argument("--curriculum", type=Path, default=DEFAULT_PATH)
    parser.add_argument("--force", action="store_true", help="vorhandene Dateien ueberschreiben")
    args = parser.parse_args(argv)

    model = load(args.curriculum)
    exit_code = 0
    for topic_id in args.topic_id:
        topic = model.by_id(topic_id)
        if topic is None:
            print(f"unbekanntes Thema: {topic_id}", file=sys.stderr)
            exit_code = 1
            continue
        written = create(topic)
        if written:
            for path in written:
                print(path.relative_to(model.root))
        else:
            print(f"{topic_id}: Modul existiert bereits (--force ueberschreibt)")
    print(
        "\nHinweis: status bleibt 'planned'. Erst wenn das Modul fertig ist, "
        "'status: ready' in curriculum.yaml setzen.",
        file=sys.stderr,
    )
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
