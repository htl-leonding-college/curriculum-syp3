"""Fixtures: ein Miniatur-Repository je Test, nur so groß wie nötig."""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path
from textwrap import dedent

import pytest
import yaml

REPO_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO_ROOT))

from tools.curriculum import load  # noqa: E402


def _load_checker():
    spec = importlib.util.spec_from_file_location(
        "check_curriculum", REPO_ROOT / "tools" / "check-curriculum.py"
    )
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


checker = _load_checker()

DEFAULT_META = {
    "jahrgang": "jg3",
    "gegenstand": "SYP",
    "unterrichte": 2,
    "ue_je_unterricht": 3,
    "budget": {"theorie": 1, "praxis": 2},
    "budget_je_block": {"werkzeuge": 1},
}

DEFAULT_BLOCKS = [{"id": "werkzeuge", "title": "Tools and practice"}]


def topic(
    topic_id: str,
    *,
    kind: str = "praxis",
    lesson: int = 1,
    block: str = "werkzeuge",
    status: str | None = None,
    requires: list[str] | None = None,
    ue: int | None = None,
    theme: str | None = None,
    taught_in: str = "jg3",
    prerequisite_for: str = "jg4",
) -> dict:
    entry = {
        "id": topic_id,
        "title": topic_id.replace("-", " ").capitalize(),
        "block": block,
        "kind": kind,
        "ue": ue if ue is not None else (1 if kind == "theorie" else 2),
        "lesson": lesson,
        "taught_in": taught_in,
        "prerequisite_for": prerequisite_for,
        "requires": requires or [],
    }
    if status is not None:
        entry["status"] = status
    if theme is not None:
        entry["theme"] = theme
    return entry


class Repo:
    """Ein Wegwerf-Repository mit curriculum.yaml und modules/."""

    def __init__(self, root: Path) -> None:
        self.root = root
        (root / "modules").mkdir(parents=True, exist_ok=True)

    def write_model(self, topics: list[dict], *, meta: dict | None = None,
                    blocks: list[dict] | None = None) -> None:
        document = {
            "meta": meta or DEFAULT_META,
            "blocks": blocks or DEFAULT_BLOCKS,
            "topics": topics,
        }
        (self.root / "curriculum.yaml").write_text(
            yaml.safe_dump(document, sort_keys=False, allow_unicode=True),
            encoding="utf-8",
        )

    def write_module(
        self,
        topic_id: str,
        *,
        index: str | None = None,
        exercises: str | None = "",
        questions: str | None = None,
    ) -> Path:
        directory = self.root / "modules" / topic_id
        directory.mkdir(parents=True, exist_ok=True)
        if index is not None:
            (directory / "index.adoc").write_text(dedent(index).lstrip(), encoding="utf-8")
        if exercises is not None:
            (directory / "exercises.adoc").write_text(dedent(exercises), encoding="utf-8")
        if questions is not None:
            (directory / "questions.adoc").write_text(
                dedent(questions).lstrip(), encoding="utf-8"
            )
        return directory

    def model(self):
        return load(self.root / "curriculum.yaml", root=self.root)

    def run(self, *checks: str):
        return checker.run(self.model(), checks or None)

    def messages(self, *checks: str) -> str:
        return "\n".join(f.message for f in self.run(*checks))


@pytest.fixture
def repo(tmp_path: Path) -> Repo:
    return Repo(tmp_path)


GOOD_INDEX = """
    = Git basics
    :topic-id: git-basics

    == Learning outcomes

    * [[lo-1]] Record a change as a commit

    == Working with commits

    Some content.

    == Decisions

    None specific to this topic.

    == Pitfalls

    None specific to this topic.

    == Terminology

    * commit / Commit

    == Further reading

    * Manz, Kapitel 3
    """

GOOD_QUESTIONS = """
    = Questions: Git basics
    :topic-id: git-basics

    == What does a commit contain?

    covers: lo-1

    .Answer
    [%collapsible]
    ====
    A commit records the complete state of the tracked files.

    Points the answer must contain: tree, parent, author, message.
    ====
    """
