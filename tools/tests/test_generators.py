"""Generatoren: eine Änderung im Modell wirkt ohne Handarbeit (P3)."""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path

from conftest import GOOD_INDEX, GOOD_QUESTIONS, REPO_ROOT, Repo, topic


def _script(name: str):
    spec = importlib.util.spec_from_file_location(
        name.replace("-", "_"), REPO_ROOT / "tools" / f"{name}.py"
    )
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


mindmap = _script("gen-mindmap")
nav = _script("gen-nav")
overview = _script("gen-ue-overview")
questions = _script("gen-questions")


def base(repo: Repo) -> None:
    repo.write_model(
        [
            topic("course-overview", kind="theorie", lesson=1),
            topic("git-basics", kind="praxis", lesson=1),
        ]
    )


def test_mindmap_contains_new_topic(repo: Repo) -> None:
    base(repo)
    assert "Git basics" in mindmap.render(repo.model())

    repo.write_model(
        [
            topic("course-overview", kind="theorie", lesson=1),
            topic("git-basics", kind="praxis", lesson=1),
            topic("git-branching", kind="praxis", lesson=2),
        ],
        meta={**repo.model().meta, "budget": {"theorie": 1, "praxis": 4}},
    )
    assert "Git branching" in mindmap.render(repo.model())


def test_mindmap_groups_topics_by_theme(repo: Repo) -> None:
    repo.write_model(
        [
            topic("course-overview", kind="theorie", lesson=1),
            topic("git-basics", kind="praxis", lesson=1, theme="Git"),
        ]
    )
    lines = mindmap.render(repo.model()).splitlines()
    assert "*** Git" in lines
    assert any(line.startswith("****_ ") and "Git basics" in line for line in lines)
    # Ohne theme hängt das Thema eine Ebene höher, direkt unter seinem Block.
    assert any(line.startswith("***_ ") and "Course overview" in line for line in lines)


def test_mindmap_marks_planned_topics(repo: Repo) -> None:
    repo.write_model(
        [
            topic("course-overview", kind="theorie", lesson=1, status="ready"),
            topic("git-basics", kind="praxis", lesson=1),
        ]
    )
    text = mindmap.render(repo.model())
    planned = [line for line in text.splitlines() if "Git basics" in line]
    ready = [line for line in text.splitlines() if "Course overview" in line]
    assert planned and "(offen)" in planned[0] and "<color:" in planned[0]
    assert ready and "(offen)" not in ready[0] and "<color:" not in ready[0]


def test_nav_order_follows_lesson(repo: Repo) -> None:
    repo.write_model(
        [
            topic("course-overview", kind="theorie", lesson=1),
            topic("git-basics", kind="praxis", lesson=1),
            topic("git-branching", kind="praxis", lesson=2),
        ]
    )
    first = nav.render(repo.model())
    assert first.index("Git basics") < first.index("Git branching")

    repo.write_model(
        [
            topic("course-overview", kind="theorie", lesson=1),
            topic("git-basics", kind="praxis", lesson=2),
            topic("git-branching", kind="praxis", lesson=1),
        ]
    )
    moved = nav.render(repo.model())
    assert moved.index("Git branching") < moved.index("Git basics")


def test_nav_marks_planned_topics_as_open(repo: Repo) -> None:
    base(repo)
    rendered = nav.render(repo.model())
    assert "_(offen)_" in rendered
    assert "xref:modules/git-basics" not in rendered


def test_nav_links_assignment_template(repo: Repo) -> None:
    entry = topic("git-basics", kind="praxis", lesson=1)
    entry["assignment_template"] = "htl-leonding-example/jg03-syp-git-basics"
    repo.write_model([topic("course-overview", kind="theorie", lesson=1), entry])
    assert "htl-leonding-example/jg03-syp-git-basics[Angabe]" in nav.render(repo.model())


def test_overview_sums_change_with_the_model(repo: Repo) -> None:
    base(repo)
    assert "|56" not in overview.render(repo.model())
    rendered = overview.render(repo.model())
    assert "|2\n|2" in rendered.replace("\r", "")  # Praxis: 2 UE, Budget 2


def test_overview_reports_progress(repo: Repo) -> None:
    base(repo)
    assert "0 von 2 Themen sind fertig, 2 sind offen." in overview.render(repo.model())


def test_questions_carry_tags_from_the_model(repo: Repo, tmp_path: Path) -> None:
    repo.write_model(
        [
            topic("course-overview", kind="theorie", lesson=1),
            topic("git-basics", kind="praxis", lesson=1, status="ready"),
        ]
    )
    repo.write_module("git-basics", index=GOOD_INDEX, questions=GOOD_QUESTIONS)
    model = repo.model()
    rows = questions.collect(model)
    assert rows and rows[0]["block"] == "werkzeuge"
    assert rows[0]["prerequisite_for"] == "jg4"
    assert rows[0]["covers"] == ["lo-1"]

    rendered = questions.render(model, rows)
    assert "taught_in: jg3" in rendered
    assert "What does a commit contain?" in rendered


def test_generated_files_carry_the_marker(repo: Repo, tmp_path: Path) -> None:
    base(repo)
    build = tmp_path / "out"
    mindmap.main(["--curriculum", str(repo.root / "curriculum.yaml"), "--build-dir", str(build)])
    nav.main(["--curriculum", str(repo.root / "curriculum.yaml"), "--build-dir", str(build)])
    overview.main(["--curriculum", str(repo.root / "curriculum.yaml"), "--build-dir", str(build)])
    questions.main(["--curriculum", str(repo.root / "curriculum.yaml"), "--build-dir", str(build)])

    produced = sorted(p.name for p in build.rglob("*") if p.is_file())
    assert produced == ["index.adoc", "nav.adoc", "questions.json", "stoffstruktur.puml", "ue-overview.adoc"]
    for path in build.rglob("*.adoc"):
        assert path.read_text(encoding="utf-8").startswith("// GENERATED")
    assert (build / "stoffstruktur.puml").read_text(encoding="utf-8").startswith("' GENERATED")
    payload = json.loads((build / "questions" / "questions.json").read_text(encoding="utf-8"))
    assert payload["questions"] == []
    assert payload["generated"].startswith("GENERATED")


def test_new_module_skeleton_passes_all_checks(repo: Repo) -> None:
    """Ein frisches Skelett fällt nur inhaltlich auf, nicht strukturell."""
    new_module = _script("new-module")
    repo.write_model(
        [
            topic("course-overview", kind="theorie", lesson=1),
            topic("git-basics", kind="praxis", lesson=1, status="ready"),
        ]
    )
    model = repo.model()
    written = new_module.create(model.by_id("git-basics"))
    assert [p.name for p in written] == ["index.adoc", "exercises.adoc", "questions.adoc"]
    assert repo.run() == []


def test_questions_can_be_selected_by_model_attributes(repo: Repo) -> None:
    repo.write_model(
        [
            topic("course-overview", kind="theorie", lesson=1, status="ready"),
            topic("git-basics", kind="praxis", lesson=1, status="ready", prerequisite_for="jg5"),
        ]
    )
    repo.write_module("git-basics", index=GOOD_INDEX, questions=GOOD_QUESTIONS)
    repo.write_module(
        "course-overview",
        index=GOOD_INDEX.replace("git-basics", "course-overview"),
        questions=GOOD_QUESTIONS.replace("git-basics", "course-overview").replace(
            "What does a commit contain?", "How is the year organised?"
        ),
    )
    rows = questions.collect(repo.model())
    assert len(rows) == 2
    assert [r["topic"] for r in questions.select(rows, prerequisite_for="jg5")] == ["git-basics"]
    assert [r["topic"] for r in questions.select(rows, prerequisite_for="jg4")] == ["course-overview"]
    assert questions.select(rows, block="werkzeuge", kind="praxis")[0]["question"] == (
        "What does a commit contain?"
    )


def test_filter_ui_carries_the_tags_as_data_attributes(repo: Repo) -> None:
    repo.write_model(
        [
            topic("course-overview", kind="theorie", lesson=1),
            topic("git-basics", kind="praxis", lesson=1, status="ready"),
        ]
    )
    repo.write_module("git-basics", index=GOOD_INDEX, questions=GOOD_QUESTIONS)
    model = repo.model()
    rendered = questions.render(model, questions.collect(model))
    assert 'data-prerequisite_for="jg4"' in rendered
    assert 'data-topic="git-basics"' in rendered
    assert "<select data-field=\"block\">" in rendered


def test_questions_of_planned_modules_stay_out_of_the_catalogue(repo: Repo) -> None:
    repo.write_model(
        [
            topic("course-overview", kind="theorie", lesson=1),
            topic("git-basics", kind="praxis", lesson=1),  # planned
        ]
    )
    repo.write_module("git-basics", index=GOOD_INDEX, questions=GOOD_QUESTIONS)
    assert questions.collect(repo.model()) == []
