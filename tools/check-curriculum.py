#!/usr/bin/env python3
"""Der CI-Check ist der Vertrag zwischen Modell und Lernressourcen (P2).

Alle Pruefungen laufen immer; gemeldet wird gesammelt, damit ein Lauf alle
Fehler zeigt und nicht nur den ersten. Exit-Code 1, sobald ein Befund vorliegt.
"""

from __future__ import annotations

import argparse
import sys
from collections import defaultdict
from dataclasses import replace
from pathlib import Path
from typing import Callable

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from tools import adoc  # noqa: E402
from tools.curriculum import (  # noqa: E402
    DEFAULT_PATH,
    UE_BY_KIND,
    Curriculum,
    CurriculumError,
    Finding,
    Topic,
    load,
)

Check = Callable[[Curriculum], list[Finding]]

#: Attribute, die Struktur transportieren und deshalb nicht im AsciiDoc stehen
#: duerfen — sonst gibt es zwei Wahrheiten (P1).
FORBIDDEN_ATTRIBUTES = (
    "ue",
    "block",
    "kind",
    "lesson",
    "unterricht",
    "taught-in",
    "taught_in",
    "prerequisite-for",
    "prerequisite_for",
    "requires",
    "jahrgang",
    "status",
)

REQUIRED_SECTIONS = ("Learning outcomes", "Decisions", "Pitfalls", "Terminology")

CHECKS: dict[str, tuple[str, Check]] = {}


def check(name: str, description: str):
    def register(func: Check) -> Check:
        CHECKS[name] = (description, func)
        return func

    return register


def _module_adocs(model: Curriculum) -> tuple[Path, ...]:
    return model.adoc_files()


def _year(value: str) -> int | None:
    digits = "".join(c for c in value if c.isdigit())
    return int(digits) if digits else None


# --------------------------------------------------------------------------
@check("bijection", "1 Bijektion zwischen Modell und Lernressourcen")
def check_bijection(model: Curriculum) -> list[Finding]:
    findings: list[Finding] = []

    for topic in model.ready:
        if not topic.index_path.is_file():
            findings.append(
                Finding(
                    check="bijection",
                    message=(
                        f"Thema '{topic.id}' ist ready, aber "
                        f"{topic.index_path.relative_to(model.root)} fehlt"
                    ),
                    path=model.path,
                    line=topic.line,
                )
            )

    known = {topic.id for topic in model.topics}
    for path in _module_adocs(model):
        document = adoc.read(path)
        if not any(line.strip() for line in document.lines):
            # Die Aufgabendatei darf inhaltsleer sein (Pruefung 9); eine leere
            # Datei kann keine Themen-ID tragen.
            continue
        topic_id = document.topic_id
        if not topic_id:
            findings.append(
                Finding(
                    check="bijection",
                    message="Datei traegt keine :topic-id:",
                    path=path,
                    line=1,
                )
            )
            continue
        if topic_id not in known:
            findings.append(
                Finding(
                    check="bijection",
                    message=f"topic-id '{topic_id}' kommt im Modell nicht vor",
                    path=path,
                    line=document.attribute_lines.get("topic-id", 1),
                )
            )
            continue
        expected_dir = model.root / "modules" / topic_id
        if expected_dir not in path.parents:
            findings.append(
                Finding(
                    check="bijection",
                    message=(
                        f"Datei nennt '{topic_id}', liegt aber nicht in "
                        f"modules/{topic_id}/"
                    ),
                    path=path,
                    line=document.attribute_lines.get("topic-id", 1),
                )
            )
    return findings


@check("budget", "2 UE-Budget je Art und je Block")
def check_budget(model: Curriculum) -> list[Finding]:
    findings: list[Finding] = []
    budget = model.meta.get("budget") or {}
    actual = model.ue_by_kind()
    for kind, allowed in budget.items():
        have = actual.get(kind, 0)
        if have != allowed:
            findings.append(
                Finding(
                    check="budget",
                    message=f"{kind}: {have} UE, vorgesehen sind {allowed}",
                    path=model.path,
                    line=model.meta.get("__budget_line__", 1),
                )
            )
    for kind in actual:
        if kind not in budget:
            findings.append(
                Finding(
                    check="budget",
                    message=f"Art '{kind}' hat kein Budget in meta.budget",
                    path=model.path,
                )
            )

    per_block = model.meta.get("budget_je_block") or {}
    actual_blocks = model.theory_ue_by_block()
    for block, allowed in per_block.items():
        have = actual_blocks.get(block, 0)
        if have != allowed:
            findings.append(
                Finding(
                    check="budget",
                    message=(
                        f"Block '{block}': {have} UE Theorie, vorgesehen sind {allowed}"
                    ),
                    path=model.path,
                )
            )
    for block, have in actual_blocks.items():
        if block not in per_block:
            findings.append(
                Finding(
                    check="budget",
                    message=f"Block '{block}' hat kein Budget in meta.budget_je_block",
                    path=model.path,
                )
            )
    return findings


@check("graph", "3 Voraussetzungsgraph: Existenz, Zyklen, Vorwaertsreferenzen")
def check_graph(model: Curriculum) -> list[Finding]:
    findings: list[Finding] = []
    known = {topic.id: topic for topic in model.topics}

    for topic in model.topics:
        for required in topic.requires:
            other = known.get(required)
            if other is None:
                findings.append(
                    Finding(
                        check="graph",
                        message=f"'{topic.id}' setzt '{required}' voraus — unbekannt",
                        path=model.path,
                        line=topic.line,
                    )
                )
                continue
            own_year, other_year = _year(topic.taught_in), _year(other.taught_in)
            if own_year is not None and other_year is not None and other_year > own_year:
                findings.append(
                    Finding(
                        check="graph",
                        message=(
                            f"'{topic.id}' ({topic.taught_in}) setzt '{other.id}' "
                            f"({other.taught_in}) voraus — spaeterer Jahrgang"
                        ),
                        path=model.path,
                        line=topic.line,
                    )
                )
            elif own_year == other_year and other.lesson >= topic.lesson:
                findings.append(
                    Finding(
                        check="graph",
                        message=(
                            f"Vorwaertsreferenz: '{topic.id}' (U{topic.lesson}) setzt "
                            f"'{other.id}' (U{other.lesson}) voraus"
                        ),
                        path=model.path,
                        line=topic.line,
                    )
                )

    colours: dict[str, int] = defaultdict(int)
    stack: list[str] = []

    def visit(topic_id: str) -> None:
        if colours[topic_id] == 2:
            return
        if colours[topic_id] == 1:
            cycle = stack[stack.index(topic_id) :] + [topic_id]
            findings.append(
                Finding(
                    check="graph",
                    message="Zyklus: " + " -> ".join(cycle),
                    path=model.path,
                    line=known[topic_id].line,
                )
            )
            return
        colours[topic_id] = 1
        stack.append(topic_id)
        for required in known[topic_id].requires:
            if required in known:
                visit(required)
        stack.pop()
        colours[topic_id] = 2

    for topic in model.topics:
        visit(topic.id)
    return findings


@check("completeness", "4 Pflichtangaben und Fragen zu Praxisthemen")
def check_completeness(model: Curriculum) -> list[Finding]:
    findings = list(model.findings)
    for topic in model.ready:
        if topic.kind != "praxis":
            continue
        if not topic.questions_path.is_file():
            continue
        questions = adoc.read(topic.questions_path).questions()
        if not questions:
            findings.append(
                Finding(
                    check="completeness",
                    message=f"Praxisthema '{topic.id}' hat keine Pruefungsfrage",
                    path=topic.questions_path,
                    line=1,
                )
            )
    return findings


@check("slots", "5 Slot-Belegung: je Unterricht ein Theorie- und ein Praxisthema")
def check_slots(model: Curriculum) -> list[Finding]:
    findings: list[Finding] = []
    occupied: dict[tuple[int, str], list[Topic]] = defaultdict(list)
    for topic in model.topics:
        occupied[topic.slot].append(topic)
        expected = UE_BY_KIND.get(topic.kind)
        if expected is None:
            findings.append(
                Finding(
                    check="slots",
                    message=f"'{topic.id}': unbekannte Art '{topic.kind}'",
                    path=model.path,
                    line=topic.line,
                )
            )
        elif topic.ue != expected:
            findings.append(
                Finding(
                    check="slots",
                    message=(
                        f"'{topic.id}' beansprucht {topic.ue} UE, ein Slot der Art "
                        f"{topic.kind} fasst {expected}"
                    ),
                    path=model.path,
                    line=topic.line,
                )
            )

    for (lesson, kind), topics in sorted(occupied.items()):
        if len(topics) > 1:
            findings.append(
                Finding(
                    check="slots",
                    message=(
                        f"U{lesson} traegt {len(topics)} Themen der Art {kind}: "
                        + ", ".join(t.id for t in topics)
                    ),
                    path=model.path,
                    line=topics[1].line,
                )
            )

    lessons = {topic.lesson for topic in model.topics}
    for lesson in range(1, max(lessons) + 1):
        if lesson not in lessons:
            findings.append(
                Finding(
                    check="slots",
                    message=f"U{lesson} traegt kein Thema — Luecke im Jahresplan",
                    path=model.path,
                )
            )
    return findings


@check("sections", "6 Pflichtabschnitte der Lernressource")
def check_sections(model: Curriculum) -> list[Finding]:
    findings: list[Finding] = []
    for topic in model.ready:
        if not topic.index_path.is_file():
            continue
        document = adoc.read(topic.index_path)
        for title in REQUIRED_SECTIONS:
            section = document.section(title)
            if section is None:
                findings.append(
                    Finding(
                        check="sections",
                        message=f"Abschnitt '{title}' fehlt",
                        path=topic.index_path,
                        line=1,
                    )
                )
            elif section.is_empty:
                findings.append(
                    Finding(
                        check="sections",
                        message=(
                            f"Abschnitt '{title}' ist leer — eine ausdrueckliche "
                            "Nullaussage genuegt"
                        ),
                        path=topic.index_path,
                        line=section.line,
                    )
                )
    return findings


@check("outcomes", "7 Kopplung von Lernzielen und Pruefungsfragen")
def check_outcomes(model: Curriculum) -> list[Finding]:
    findings: list[Finding] = []
    for topic in model.ready:
        if not topic.index_path.is_file() or not topic.questions_path.is_file():
            continue
        outcomes = adoc.read(topic.index_path).outcomes()
        questions = adoc.read(topic.questions_path).questions()

        covered: set[str] = set()
        for question in questions:
            if not question.covers:
                findings.append(
                    Finding(
                        check="outcomes",
                        message=(
                            f"Frage '{question.title}' nennt kein Lernziel "
                            "(Zeile 'covers: lo-N' fehlt)"
                        ),
                        path=topic.questions_path,
                        line=question.line,
                    )
                )
                continue
            known = {outcome.id for outcome in outcomes}
            for reference in question.covers:
                if reference not in known:
                    findings.append(
                        Finding(
                            check="outcomes",
                            message=(
                                f"Frage '{question.title}' verweist auf '{reference}' — "
                                "kein solches Lernziel"
                            ),
                            path=topic.questions_path,
                            line=question.covers_line or question.line,
                        )
                    )
                else:
                    covered.add(reference)

        for outcome in outcomes:
            if outcome.id not in covered:
                findings.append(
                    Finding(
                        check="outcomes",
                        message=f"Lernziel '{outcome.id}' hat keine Pruefungsfrage",
                        path=topic.index_path,
                        line=outcome.line,
                    )
                )
    return findings


@check("images", "8 Herkunftsklasse jedes Bildes")
def check_images(model: Curriculum) -> list[Finding]:
    findings: list[Finding] = []
    for path in _module_adocs(model):
        for image in adoc.read(path).images():
            if image.provenance is None:
                findings.append(
                    Finding(
                        check="images",
                        message=(
                            f"Bild '{image.target}' ohne Herkunftsklasse "
                            f"({' | '.join(adoc.PROVENANCE_CLASSES)}) im Bildtitel"
                        ),
                        path=path,
                        line=image.line,
                    )
                )
            elif image.provenance == "free" and not adoc.free_licence_is_complete(
                image.provenance_detail
            ):
                findings.append(
                    Finding(
                        check="images",
                        message=(
                            f"Bild '{image.target}': 'free' verlangt Lizenzname und "
                            "Quelladresse"
                        ),
                        path=path,
                        line=image.line,
                    )
                )
    return findings


@check("skeleton", "9 Modulskelett: Inhalt, Aufgaben, Pruefungsfragen")
def check_skeleton(model: Curriculum) -> list[Finding]:
    findings: list[Finding] = []
    for topic in model.ready:
        for path in topic.module_files:
            if not path.is_file():
                findings.append(
                    Finding(
                        check="skeleton",
                        message=(
                            f"Modul '{topic.id}': {path.name} fehlt"
                            + (" (darf inhaltsleer sein)" if path.name == "exercises.adoc" else "")
                        ),
                        path=model.path,
                        line=topic.line,
                    )
                )
    return findings


@check("attributes", "Z Strukturangaben gehoeren nicht ins AsciiDoc")
def check_attributes(model: Curriculum) -> list[Finding]:
    findings: list[Finding] = []
    for path in _module_adocs(model):
        document = adoc.read(path)
        for name, line in document.attribute_lines.items():
            if name in FORBIDDEN_ATTRIBUTES:
                findings.append(
                    Finding(
                        check="attributes",
                        message=(
                            f"Attribut ':{name}:' traegt Struktur — die steht "
                            "ausschliesslich in curriculum.yaml"
                        ),
                        path=path,
                        line=line,
                    )
                )
    return findings


# --------------------------------------------------------------------------
def run(model: Curriculum, only: tuple[str, ...] | None = None) -> list[Finding]:
    selected = only or tuple(CHECKS)
    findings: list[Finding] = []
    for name in selected:
        if name not in CHECKS:
            raise SystemExit(f"unbekannte Pruefung: {name} (bekannt: {', '.join(CHECKS)})")
        findings.extend(CHECKS[name][1](model))
    return findings


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--curriculum", type=Path, default=DEFAULT_PATH)
    parser.add_argument("--only", help="Kommaliste von Pruefungen (siehe --list)")
    parser.add_argument("--list", action="store_true", help="Pruefungen auflisten")
    parser.add_argument(
        "--as-ready",
        help=(
            "Kommaliste von Themen, die fuer diesen Lauf als fertig gelten — "
            "prueft ein Skelett, bevor es in curriculum.yaml auf ready gesetzt wird"
        ),
    )
    args = parser.parse_args(argv)

    if args.list:
        for name, (description, _) in CHECKS.items():
            print(f"{name:<13} {description}")
        return 0

    try:
        model = load(args.curriculum)
    except CurriculumError as error:
        print(f"{error}", file=sys.stderr)
        return 2

    if args.as_ready:
        wanted = {part.strip() for part in args.as_ready.split(",") if part.strip()}
        unknown = wanted - {topic.id for topic in model.topics}
        if unknown:
            print(f"unbekannte Themen: {', '.join(sorted(unknown))}", file=sys.stderr)
            return 2
        model.topics = tuple(
            replace(topic, status="ready") if topic.id in wanted else topic
            for topic in model.topics
        )

    only = tuple(part.strip() for part in args.only.split(",")) if args.only else None
    findings = run(model, only)

    for finding in sorted(
        findings, key=lambda f: (str(f.path or ""), f.line or 0, f.check)
    ):
        print(finding.format(model.root))

    planned = len(model.planned)
    print(
        f"\n{len(model.topics)} Themen ({len(model.ready)} ready, {planned} planned), "
        f"{len(findings)} Befunde",
        file=sys.stderr,
    )
    return 1 if findings else 0


if __name__ == "__main__":
    raise SystemExit(main())
