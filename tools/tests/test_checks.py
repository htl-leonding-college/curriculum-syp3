"""Je Pruefung ein roter und ein gruener Fall (P2, Aufgabe 2.12)."""

from __future__ import annotations

from conftest import DEFAULT_META, GOOD_INDEX, GOOD_QUESTIONS, Repo, topic


def ready(topic_id: str, **kwargs) -> dict:
    return topic(topic_id, status="ready", **kwargs)


def base_topics(**kwargs) -> list[dict]:
    return [
        topic("course-overview", kind="theorie", lesson=1),
        topic("git-basics", kind="praxis", lesson=1, **kwargs),
    ]


# --- 1 Bijektion ----------------------------------------------------------
def test_bijection_ready_topic_without_file(repo: Repo) -> None:
    repo.write_model([topic("course-overview", kind="theorie", lesson=1), ready("git-basics")])
    assert "ist ready, aber modules/git-basics/index.adoc fehlt" in repo.messages("bijection")


def test_bijection_planned_topic_without_file_is_fine(repo: Repo) -> None:
    repo.write_model(base_topics())
    assert repo.run("bijection") == []


def test_bijection_orphan_file(repo: Repo) -> None:
    repo.write_model(base_topics())
    repo.write_module("stray-module", index="= Stray\n:topic-id: stray-module\n")
    assert "kommt im Modell nicht vor" in repo.messages("bijection")


def test_bijection_file_without_topic_id(repo: Repo) -> None:
    repo.write_model(base_topics())
    repo.write_module("git-basics", index="= Git basics\n\nNo attribute here.\n")
    assert "traegt keine :topic-id:" in repo.messages("bijection")


# --- 2 Budget -------------------------------------------------------------
def test_budget_exceeded(repo: Repo) -> None:
    repo.write_model(
        [
            topic("course-overview", kind="theorie", lesson=1),
            topic("second-theory", kind="theorie", lesson=2),
            topic("git-basics", kind="praxis", lesson=1),
        ]
    )
    messages = repo.messages("budget")
    assert "theorie: 2 UE, vorgesehen sind 1" in messages
    assert "Block 'werkzeuge': 2 UE Theorie, vorgesehen sind 1" in messages


def test_budget_matches(repo: Repo) -> None:
    repo.write_model(base_topics())
    assert repo.run("budget") == []


# --- 3 Graph --------------------------------------------------------------
def test_graph_unknown_requirement(repo: Repo) -> None:
    repo.write_model(base_topics(requires=["does-not-exist"]))
    assert "setzt 'does-not-exist' voraus — unbekannt" in repo.messages("graph")


def test_graph_forward_reference(repo: Repo) -> None:
    repo.write_model(
        [
            topic("course-overview", kind="theorie", lesson=1, requires=["git-basics"]),
            topic("git-basics", kind="praxis", lesson=2),
        ]
    )
    assert "Vorwaertsreferenz: 'course-overview' (U1) setzt 'git-basics' (U2)" in repo.messages("graph")


def test_graph_cycle(repo: Repo) -> None:
    repo.write_model(
        [
            topic("course-overview", kind="theorie", lesson=1, requires=["git-basics"]),
            topic("git-basics", kind="praxis", lesson=1, requires=["course-overview"]),
        ]
    )
    assert "Zyklus:" in repo.messages("graph")


def test_graph_valid_chain(repo: Repo) -> None:
    repo.write_model(
        [
            topic("course-overview", kind="theorie", lesson=1),
            topic("git-basics", kind="praxis", lesson=2, requires=["course-overview"]),
        ]
    )
    assert [f for f in repo.run("graph")] == []


# --- 4 Vollstaendigkeit ---------------------------------------------------
def test_completeness_missing_required_field(repo: Repo) -> None:
    entry = topic("git-basics")
    del entry["taught_in"]
    repo.write_model([topic("course-overview", kind="theorie", lesson=1), entry])
    assert "fehlt: taught_in" in repo.messages("completeness")


def test_completeness_practice_topic_without_question(repo: Repo) -> None:
    repo.write_model([topic("course-overview", kind="theorie", lesson=1), ready("git-basics")])
    repo.write_module("git-basics", index=GOOD_INDEX, questions="= Questions\n:topic-id: git-basics\n")
    assert "hat keine Pruefungsfrage" in repo.messages("completeness")


def test_completeness_theory_topic_without_question_is_fine(repo: Repo) -> None:
    repo.write_model(
        [
            ready("course-overview", kind="theorie", lesson=1),
            topic("git-basics", kind="praxis", lesson=1),
        ]
    )
    repo.write_module(
        "course-overview",
        index=GOOD_INDEX.replace("git-basics", "course-overview"),
        questions="= Questions\n:topic-id: course-overview\n",
    )
    assert repo.run("completeness") == []


# --- 5 Slot-Belegung ------------------------------------------------------
def test_slots_double_booking(repo: Repo) -> None:
    repo.write_model(
        [
            topic("course-overview", kind="theorie", lesson=1),
            topic("second-theory", kind="theorie", lesson=1),
            topic("git-basics", kind="praxis", lesson=1),
        ]
    )
    assert "U1 traegt 2 Themen der Art theorie" in repo.messages("slots")


def test_slots_gap(repo: Repo) -> None:
    repo.write_model(
        [
            topic("course-overview", kind="theorie", lesson=1),
            topic("git-basics", kind="praxis", lesson=3),
        ]
    )
    assert "U2 traegt kein Thema" in repo.messages("slots")


def test_slots_oversized_topic(repo: Repo) -> None:
    repo.write_model(
        [topic("course-overview", kind="theorie", lesson=1, ue=2), topic("git-basics", lesson=1)]
    )
    assert "beansprucht 2 UE, ein Slot der Art theorie fasst 1" in repo.messages("slots")


def test_slots_valid(repo: Repo) -> None:
    repo.write_model(base_topics())
    assert repo.run("slots") == []


# --- 6 Pflichtabschnitte --------------------------------------------------
def test_sections_missing(repo: Repo) -> None:
    repo.write_model([topic("course-overview", kind="theorie", lesson=1), ready("git-basics")])
    index = GOOD_INDEX.replace("== Decisions\n\n    None specific to this topic.\n\n", "")
    repo.write_module("git-basics", index=index, questions=GOOD_QUESTIONS)
    assert "Abschnitt 'Decisions' fehlt" in repo.messages("sections")


def test_sections_empty(repo: Repo) -> None:
    repo.write_model([topic("course-overview", kind="theorie", lesson=1), ready("git-basics")])
    index = GOOD_INDEX.replace("None specific to this topic.\n\n    == Pitfalls", "\n    == Pitfalls")
    repo.write_module("git-basics", index=index, questions=GOOD_QUESTIONS)
    assert "ist leer" in repo.messages("sections")


def test_sections_null_statement_counts(repo: Repo) -> None:
    repo.write_model([topic("course-overview", kind="theorie", lesson=1), ready("git-basics")])
    repo.write_module("git-basics", index=GOOD_INDEX, questions=GOOD_QUESTIONS)
    assert repo.run("sections") == []


# --- 7 Outcome-Kopplung ---------------------------------------------------
def test_outcomes_without_question(repo: Repo) -> None:
    repo.write_model([topic("course-overview", kind="theorie", lesson=1), ready("git-basics")])
    index = GOOD_INDEX.replace(
        "* [[lo-1]] Record a change as a commit",
        "* [[lo-1]] Record a change as a commit\n    * [[lo-2]] Read the log",
    )
    repo.write_module("git-basics", index=index, questions=GOOD_QUESTIONS)
    assert "Lernziel 'lo-2' hat keine Pruefungsfrage" in repo.messages("outcomes")


def test_outcomes_question_without_outcome(repo: Repo) -> None:
    repo.write_model([topic("course-overview", kind="theorie", lesson=1), ready("git-basics")])
    questions = GOOD_QUESTIONS.replace("covers: lo-1", "covers: lo-9")
    repo.write_module("git-basics", index=GOOD_INDEX, questions=questions)
    assert "verweist auf 'lo-9'" in repo.messages("outcomes")


def test_outcomes_coupled(repo: Repo) -> None:
    repo.write_model([topic("course-overview", kind="theorie", lesson=1), ready("git-basics")])
    repo.write_module("git-basics", index=GOOD_INDEX, questions=GOOD_QUESTIONS)
    assert repo.run("outcomes") == []


# --- 8 Bildherkunft -------------------------------------------------------
IMAGE_BLOCK = """

    .Kanban board
    image::images/kanban.png[Kanban board,600]
    """


def test_images_without_provenance(repo: Repo) -> None:
    repo.write_model([topic("course-overview", kind="theorie", lesson=1), ready("git-basics")])
    repo.write_module("git-basics", index=GOOD_INDEX + IMAGE_BLOCK, questions=GOOD_QUESTIONS)
    assert "ohne Herkunftsklasse" in repo.messages("images")


def test_images_free_without_source(repo: Repo) -> None:
    repo.write_model([topic("course-overview", kind="theorie", lesson=1), ready("git-basics")])
    block = IMAGE_BLOCK.replace(".Kanban board", ".Kanban board (free: CC BY-SA 4.0)")
    repo.write_module("git-basics", index=GOOD_INDEX + block, questions=GOOD_QUESTIONS)
    assert "verlangt Lizenzname und Quelladresse" in repo.messages("images")


def test_images_classified(repo: Repo) -> None:
    repo.write_model([topic("course-overview", kind="theorie", lesson=1), ready("git-basics")])
    block = IMAGE_BLOCK.replace(
        ".Kanban board",
        ".Kanban board (free: CC BY-SA 4.0, https://example.org/kanban, retrieved 2026-09-07)",
    )
    repo.write_module("git-basics", index=GOOD_INDEX + block, questions=GOOD_QUESTIONS)
    assert repo.run("images") == []


def test_images_unclear_is_accepted(repo: Repo) -> None:
    repo.write_model([topic("course-overview", kind="theorie", lesson=1), ready("git-basics")])
    block = IMAGE_BLOCK.replace(".Kanban board", ".Kanban board (unclear: rights not checked)")
    repo.write_module("git-basics", index=GOOD_INDEX + block, questions=GOOD_QUESTIONS)
    assert repo.run("images") == []


# --- 9 Modulskelett -------------------------------------------------------
def test_skeleton_missing_exercises(repo: Repo) -> None:
    repo.write_model([topic("course-overview", kind="theorie", lesson=1), ready("git-basics")])
    repo.write_module("git-basics", index=GOOD_INDEX, exercises=None, questions=GOOD_QUESTIONS)
    assert "exercises.adoc fehlt" in repo.messages("skeleton")


def test_skeleton_empty_exercises_is_fine(repo: Repo) -> None:
    repo.write_model([topic("course-overview", kind="theorie", lesson=1), ready("git-basics")])
    repo.write_module("git-basics", index=GOOD_INDEX, exercises="", questions=GOOD_QUESTIONS)
    assert repo.run("skeleton") == []


# --- Z Strukturattribute --------------------------------------------------
def test_attributes_structure_in_adoc(repo: Repo) -> None:
    repo.write_model([topic("course-overview", kind="theorie", lesson=1), ready("git-basics")])
    index = GOOD_INDEX.replace(":topic-id: git-basics", ":topic-id: git-basics\n    :ue: 2")
    repo.write_module("git-basics", index=index, questions=GOOD_QUESTIONS)
    assert "Attribut ':ue:' traegt Struktur" in repo.messages("attributes")


def test_attributes_only_topic_id(repo: Repo) -> None:
    repo.write_model([topic("course-overview", kind="theorie", lesson=1), ready("git-basics")])
    repo.write_module("git-basics", index=GOOD_INDEX, questions=GOOD_QUESTIONS)
    assert repo.run("attributes") == []


# --- Sammelverhalten ------------------------------------------------------
def test_all_findings_are_reported_not_only_the_first(repo: Repo) -> None:
    repo.write_model(
        [
            topic("course-overview", kind="theorie", lesson=1),
            ready("git-basics", requires=["nope"]),
        ]
    )
    findings = repo.run()
    checks = {f.check for f in findings}
    assert {"bijection", "graph"} <= checks


def test_clean_repository_has_no_findings(repo: Repo) -> None:
    repo.write_model([ready("course-overview", kind="theorie", lesson=1), ready("git-basics")])
    repo.write_module("git-basics", index=GOOD_INDEX, questions=GOOD_QUESTIONS)
    repo.write_module(
        "course-overview",
        index=GOOD_INDEX.replace("git-basics", "course-overview").replace("Git basics", "Course overview"),
        questions=GOOD_QUESTIONS.replace("git-basics", "course-overview"),
    )
    assert repo.run() == []


def test_bijection_ignores_empty_exercise_file(repo: Repo) -> None:
    repo.write_model([topic("course-overview", kind="theorie", lesson=1), ready("git-basics")])
    repo.write_module("git-basics", index=GOOD_INDEX, exercises="", questions=GOOD_QUESTIONS)
    assert [f for f in repo.run("bijection") if "exercises" in str(f.path)] == []


def test_bijection_reports_non_empty_file_without_topic_id(repo: Repo) -> None:
    repo.write_model([topic("course-overview", kind="theorie", lesson=1), ready("git-basics")])
    repo.write_module(
        "git-basics",
        index=GOOD_INDEX,
        exercises="= Exercises\n\nWrite a commit message.\n",
        questions=GOOD_QUESTIONS,
    )
    assert "traegt keine :topic-id:" in repo.messages("bijection")
