"""Lesen der Lernressourcen — so viel AsciiDoc, wie die Prüfungen brauchen.

Kein vollständiger Parser: Attribute, Abschnitte, Lernziele, Prüfungsfragen
und Bilder mit Herkunftsangabe. Alles zeilenbasiert, damit jeder Befund eine
Zeilennummer nennen kann.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

ATTRIBUTE_RE = re.compile(r"^:([A-Za-z0-9_-]+):\s*(.*?)\s*$")
SECTION_RE = re.compile(r"^(=+)\s+(.*?)\s*$")
IMAGE_RE = re.compile(r"^image::([^\[]+)\[(.*)\]\s*$")
BLOCK_TITLE_RE = re.compile(r"^\.(?!\.)(.+?)\s*$")
OUTCOME_RE = re.compile(r"^\*+\s*\[\[([A-Za-z0-9_-]+)\]\]\s*(.*?)\s*$")
COVERS_RE = re.compile(r"^covers:\s*(.+?)\s*$", re.IGNORECASE)
DELIMITER_RE = re.compile(r"^(-{4,}|\.{4,}|={4,}|\*{4,})$")
PROVENANCE_RE = re.compile(r"\((own|free|unclear)(?::\s*(.*?))?\)\s*$")
URL_RE = re.compile(r"https?://\S+")

#: Herkunftsklassen eines Bildes (P11).
PROVENANCE_CLASSES = ("own", "free", "unclear")


@dataclass(frozen=True)
class Section:
    level: int
    title: str
    line: int
    body: str

    @property
    def is_empty(self) -> bool:
        return not self.body.strip()


@dataclass(frozen=True)
class Outcome:
    id: str
    text: str
    line: int


@dataclass(frozen=True)
class Question:
    title: str
    line: int
    covers: tuple[str, ...]
    covers_line: int | None


@dataclass(frozen=True)
class Image:
    target: str
    line: int
    caption: str | None
    provenance: str | None
    provenance_detail: str


@dataclass(frozen=True)
class Document:
    path: Path
    lines: tuple[str, ...]
    attributes: dict[str, str]
    attribute_lines: dict[str, int]
    sections: tuple[Section, ...]

    @property
    def topic_id(self) -> str | None:
        return self.attributes.get("topic-id")

    def section(self, title: str) -> Section | None:
        wanted = title.casefold()
        for section in self.sections:
            if section.title.casefold() == wanted:
                return section
        return None

    def outcomes(self) -> tuple[Outcome, ...]:
        section = self.section("Learning outcomes")
        if section is None:
            return ()
        found: list[Outcome] = []
        for offset, line in enumerate(section.body.splitlines(), start=section.line + 1):
            match = OUTCOME_RE.match(line)
            if match:
                found.append(Outcome(id=match.group(1), text=match.group(2), line=offset))
        return tuple(found)

    def questions(self) -> tuple[Question, ...]:
        found: list[Question] = []
        for section in self.sections:
            if section.level < 2:
                continue
            covers: tuple[str, ...] = ()
            covers_line: int | None = None
            for offset, line in enumerate(section.body.splitlines(), start=section.line + 1):
                match = COVERS_RE.match(line)
                if match:
                    covers = tuple(
                        part.strip()
                        for part in re.split(r"[,;]", match.group(1))
                        if part.strip()
                    )
                    covers_line = offset
                    break
            found.append(
                Question(
                    title=section.title,
                    line=section.line,
                    covers=covers,
                    covers_line=covers_line,
                )
            )
        return tuple(found)

    def images(self) -> tuple[Image, ...]:
        found: list[Image] = []
        delimiter: str | None = None
        for index, line in enumerate(self.lines):
            stripped = line.rstrip()
            if delimiter is None:
                if DELIMITER_RE.match(stripped):
                    delimiter = stripped
                    continue
            else:
                # Ein Block endet nur an seiner eigenen Begrenzung; längere
                # Begrenzer schachteln (Beispiel im Beispiel).
                if stripped == delimiter:
                    delimiter = None
                continue
            match = IMAGE_RE.match(line)
            if not match:
                continue
            caption = None
            for back in range(index - 1, max(index - 4, -1), -1):
                previous = self.lines[back].strip()
                if not previous:
                    continue
                if previous.startswith("["):
                    continue
                title_match = BLOCK_TITLE_RE.match(previous)
                if title_match and not previous.startswith(".."):
                    caption = title_match.group(1)
                break
            provenance = None
            detail = ""
            if caption:
                provenance_match = PROVENANCE_RE.search(caption)
                if provenance_match:
                    provenance = provenance_match.group(1)
                    detail = provenance_match.group(2) or ""
            found.append(
                Image(
                    target=match.group(1).strip(),
                    line=index + 1,
                    caption=caption,
                    provenance=provenance,
                    provenance_detail=detail,
                )
            )
        return tuple(found)


def _sections(lines: tuple[str, ...]) -> tuple[Section, ...]:
    starts: list[tuple[int, int, str]] = []
    in_source_block = False
    for index, line in enumerate(lines):
        if line.startswith("----") or line.startswith("...."):
            in_source_block = not in_source_block
            continue
        if in_source_block:
            continue
        match = SECTION_RE.match(line)
        if match:
            starts.append((len(match.group(1)), index, match.group(2)))

    sections: list[Section] = []
    for position, (level, index, title) in enumerate(starts):
        end = starts[position + 1][1] if position + 1 < len(starts) else len(lines)
        body = "\n".join(lines[index + 1 : end])
        sections.append(Section(level=level, title=title, line=index + 1, body=body))
    return tuple(sections)


def read(path: Path) -> Document:
    text = Path(path).read_text(encoding="utf-8")
    lines = tuple(text.splitlines())
    attributes: dict[str, str] = {}
    attribute_lines: dict[str, int] = {}
    for index, line in enumerate(lines):
        match = ATTRIBUTE_RE.match(line)
        if match:
            name = match.group(1).casefold()
            attributes[name] = match.group(2)
            attribute_lines.setdefault(name, index + 1)
    return Document(
        path=Path(path),
        lines=lines,
        attributes=attributes,
        attribute_lines=attribute_lines,
        sections=_sections(lines),
    )


def free_licence_is_complete(detail: str) -> bool:
    """`free` verlangt Lizenzname und Quelladresse (P11)."""
    if not URL_RE.search(detail):
        return False
    before_url = URL_RE.split(detail, maxsplit=1)[0]
    return bool(before_url.strip(" ,;"))
