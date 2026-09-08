"""Lademodul fuer curriculum.yaml — die einzige Strukturwahrheit (P1).

Alle Werkzeuge unter ``tools/`` lesen das Modell ausschliesslich hierueber.
Modulpfade werden aus der Themen-ID abgeleitet, nicht aus der yaml gelesen.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Iterator

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_PATH = REPO_ROOT / "curriculum.yaml"
MODULES_DIRNAME = "modules"

#: Pflichtfelder je Thema (curriculum-model — "Themen tragen Jahrgangszuordnung
#: und Voraussetzungen").
REQUIRED_TOPIC_FIELDS = (
    "id",
    "title",
    "block",
    "kind",
    "ue",
    "lesson",
    "taught_in",
    "prerequisite_for",
    "requires",
)

#: ``theme`` fasst Themen eines Blocks zu einem Strang zusammen (Git, Container,
#: Meilenstein-Reviews …). Es ist eine reine Darstellungsgruppe der Mindmap und
#: aendert weder Budget noch Reihenfolge; Themen ohne ``theme`` haengen direkt
#: unter ihrem Block.
OPTIONAL_TOPIC_FIELDS = ("assignment_template", "note", "status", "theme")

#: Bearbeitungsstand eines Themas. ``planned`` ist der Default: das Thema ist
#: geplant und in allen abgeleiteten Darstellungen als offen sichtbar, seine
#: Lernressource wird noch nicht erwartet. ``ready`` heisst: das Modul ist
#: vollstaendig und wird hart geprueft.
TOPIC_STATUS = ("planned", "ready")
DEFAULT_STATUS = "planned"

#: Ein Thema entspricht einem Unterrichtsslot: 1 UE Theorie bzw. 2 UE Praxis.
UE_BY_KIND = {"theorie": 1, "praxis": 2}

LINE_KEY = "__line__"


class CurriculumError(Exception):
    """Das Modell ist so defekt, dass keine Pruefung darauf sinnvoll ist."""


@dataclass(frozen=True)
class Finding:
    """Ein Befund mit Fundstelle — das Ausgabeformat aller Werkzeuge."""

    check: str
    message: str
    path: Path | None = None
    line: int | None = None

    def format(self, root: Path = REPO_ROOT) -> str:
        if self.path is None:
            where = "-"
        else:
            try:
                where = str(self.path.relative_to(root))
            except ValueError:
                where = str(self.path)
            if self.line is not None:
                where = f"{where}:{self.line}"
        return f"{where}: {self.check}: {self.message}"


class _LineLoader(yaml.SafeLoader):
    """SafeLoader, der jeder Abbildung ihre Zeilennummer beilegt."""


def _construct_mapping(loader: _LineLoader, node: yaml.MappingNode) -> dict[str, Any]:
    mapping = yaml.SafeLoader.construct_mapping(loader, node, deep=True)
    mapping[LINE_KEY] = node.start_mark.line + 1
    return mapping


_LineLoader.add_constructor(
    yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, _construct_mapping
)


@dataclass(frozen=True)
class Block:
    id: str
    title: str
    line: int


@dataclass(frozen=True)
class Topic:
    id: str
    title: str
    block: str
    kind: str
    ue: int
    lesson: int
    taught_in: str
    prerequisite_for: str
    requires: tuple[str, ...]
    line: int
    root: Path
    assignment_template: str | None = None
    theme: str | None = None
    status: str = DEFAULT_STATUS
    unknown_fields: tuple[str, ...] = ()

    @property
    def is_ready(self) -> bool:
        """Wird die Lernressource bereits erwartet und hart geprueft?"""
        return self.status == "ready"

    @property
    def module_dir(self) -> Path:
        return self.root / MODULES_DIRNAME / self.id

    @property
    def index_path(self) -> Path:
        return self.module_dir / "index.adoc"

    @property
    def exercises_path(self) -> Path:
        return self.module_dir / "exercises.adoc"

    @property
    def questions_path(self) -> Path:
        return self.module_dir / "questions.adoc"

    @property
    def images_dir(self) -> Path:
        return self.module_dir / "images"

    @property
    def module_files(self) -> tuple[Path, Path, Path]:
        return (self.index_path, self.exercises_path, self.questions_path)

    @property
    def slot(self) -> tuple[int, str]:
        """Ein Slot ist ein Unterricht plus Art — je Slot genau ein Thema."""
        return (self.lesson, self.kind)


@dataclass
class Curriculum:
    meta: dict[str, Any]
    blocks: tuple[Block, ...]
    topics: tuple[Topic, ...]
    path: Path
    root: Path
    findings: tuple[Finding, ...] = ()

    def __iter__(self) -> Iterator[Topic]:
        return iter(self.topics)

    def by_id(self, topic_id: str) -> Topic | None:
        return self._index.get(topic_id)

    @property
    def _index(self) -> dict[str, Topic]:
        return {t.id: t for t in self.topics}

    @property
    def block_ids(self) -> tuple[str, ...]:
        return tuple(b.id for b in self.blocks)

    def of_kind(self, kind: str) -> tuple[Topic, ...]:
        return tuple(t for t in self.topics if t.kind == kind)

    @property
    def ready(self) -> tuple[Topic, ...]:
        """Themen, deren Lernressource vollstaendig sein muss."""
        return tuple(t for t in self.topics if t.is_ready)

    @property
    def planned(self) -> tuple[Topic, ...]:
        """Themen ohne fertige Lernressource — in Darstellungen als offen."""
        return tuple(t for t in self.topics if not t.is_ready)

    def ue_by_kind(self) -> dict[str, int]:
        totals: dict[str, int] = {}
        for topic in self.topics:
            totals[topic.kind] = totals.get(topic.kind, 0) + topic.ue
        return totals

    def theory_ue_by_block(self) -> dict[str, int]:
        """UE-Summen je Block ueber die Theoriethemen.

        ``meta.budget_je_block`` ist als Theorie-Budget definiert
        (define-syp3-curriculum/design.md — Jahresrahmen).
        """
        totals = {block.id: 0 for block in self.blocks}
        for topic in self.of_kind("theorie"):
            totals[topic.block] = totals.get(topic.block, 0) + topic.ue
        return totals

    def module_dirs(self) -> tuple[Path, Path]:
        return self.root / MODULES_DIRNAME

    def adoc_files(self) -> tuple[Path, ...]:
        modules = self.root / MODULES_DIRNAME
        if not modules.is_dir():
            return ()
        return tuple(sorted(modules.rglob("*.adoc")))


def _pop_line(raw: dict[str, Any]) -> int:
    return int(raw.pop(LINE_KEY, 0))


def _as_topic(raw: dict[str, Any], root: Path, path: Path) -> tuple[Topic | None, list[Finding]]:
    line = _pop_line(raw)
    findings: list[Finding] = []
    missing = [f for f in REQUIRED_TOPIC_FIELDS if f not in raw]
    if missing:
        findings.append(
            Finding(
                check="model",
                message=(
                    f"Thema '{raw.get('id', '<ohne id>')}' fehlt: "
                    + ", ".join(missing)
                ),
                path=path,
                line=line,
            )
        )
        return None, findings

    known = set(REQUIRED_TOPIC_FIELDS) | set(OPTIONAL_TOPIC_FIELDS)
    unknown = tuple(sorted(k for k in raw if k not in known))
    status = str(raw.get("status") or DEFAULT_STATUS)
    if status not in TOPIC_STATUS:
        findings.append(
            Finding(
                check="model",
                message=(
                    f"Thema '{raw['id']}': status '{status}' ist unbekannt, "
                    f"erlaubt sind {' | '.join(TOPIC_STATUS)}"
                ),
                path=path,
                line=line,
            )
        )
        status = DEFAULT_STATUS

    requires = raw.get("requires") or []
    if not isinstance(requires, list):
        findings.append(
            Finding(
                check="model",
                message=f"Thema '{raw['id']}': 'requires' ist keine Liste",
                path=path,
                line=line,
            )
        )
        requires = []

    topic = Topic(
        id=str(raw["id"]),
        title=str(raw["title"]),
        block=str(raw["block"]),
        kind=str(raw["kind"]),
        ue=int(raw["ue"]),
        lesson=int(raw["lesson"]),
        taught_in=str(raw["taught_in"]),
        prerequisite_for=str(raw["prerequisite_for"]),
        requires=tuple(str(r) for r in requires),
        line=line,
        root=root,
        assignment_template=(
            str(raw["assignment_template"]) if raw.get("assignment_template") else None
        ),
        theme=str(raw["theme"]) if raw.get("theme") else None,
        status=status,
        unknown_fields=unknown,
    )
    return topic, findings


def load(path: Path | str = DEFAULT_PATH, root: Path | None = None) -> Curriculum:
    """Liest das Modell.

    Fehlende Pflichtfelder werden als :class:`Finding` mit Zeilenangabe
    gemeldet, nicht geworfen — die Pruefung soll alle Fehler auf einmal zeigen.
    """
    path = Path(path)
    root = Path(root) if root is not None else path.resolve().parent
    if not path.is_file():
        raise CurriculumError(f"{path} nicht gefunden")

    data = yaml.load(path.read_text(encoding="utf-8"), Loader=_LineLoader)
    if not isinstance(data, dict):
        raise CurriculumError(f"{path}: erwartet wird eine Abbildung auf oberster Ebene")

    findings: list[Finding] = []

    meta = data.get("meta")
    if not isinstance(meta, dict):
        raise CurriculumError(f"{path}: Abschnitt 'meta' fehlt")
    _pop_line(meta)
    for key in ("budget", "budget_je_block", "zonen", "slots_je_unterricht"):
        if isinstance(meta.get(key), dict):
            _pop_line(meta[key])

    blocks: list[Block] = []
    for raw in data.get("blocks") or []:
        line = _pop_line(raw)
        blocks.append(Block(id=str(raw["id"]), title=str(raw.get("title", "")), line=line))

    topics: list[Topic] = []
    for raw in data.get("topics") or []:
        topic, problems = _as_topic(dict(raw), root=root, path=path)
        findings.extend(problems)
        if topic is not None:
            topics.append(topic)

    if not topics:
        raise CurriculumError(f"{path}: keine Themen gefunden")

    return Curriculum(
        meta=meta,
        blocks=tuple(blocks),
        topics=tuple(topics),
        path=path,
        root=root,
        findings=tuple(findings),
    )


def _cli() -> int:
    """Kleines Abfragewerkzeug: `python tools/curriculum.py ready` gibt die IDs
    der fertigen Themen aus — der Site-Build baut nur diese."""
    import argparse

    parser = argparse.ArgumentParser(description=_cli.__doc__)
    parser.add_argument("what", choices=("ready", "planned", "all"))
    parser.add_argument("--curriculum", type=Path, default=DEFAULT_PATH)
    args = parser.parse_args()
    model = load(args.curriculum)
    topics = {"ready": model.ready, "planned": model.planned, "all": model.topics}[args.what]
    for topic in topics:
        print(topic.id)
    return 0


if __name__ == "__main__":
    raise SystemExit(_cli())
