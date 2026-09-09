# Continuation Prompt — Curriculum SYP 3. Jahrgang

**Stand:** 2026-09-08 (zweite Sitzung des Tages) · Plattform-Change **42/51**,
Curriculum-Change **19/21**
**Site live:** https://htl-leonding-college.github.io/curriculum-syp3/
**Module:** U1–U10 Praxis und U1–U11 Theorie fertig — **21 Module ready**,
**110 Fragen**, alle mit ausformulierter Antwort

> Löst `2026-09-08-mindmap-umlaute-git-basics.md` ab. Ältere liegen in
> `continuations/archiv/`.

---

## Einstieg

```
/opsx:apply setup-curriculum-repository
```

Struktur steht in `curriculum.yaml` (55 Themen), Entscheidungen in
`openspec/changes/*/design.md`, Abdeckung in
`openspec/changes/define-syp3-curriculum/coverage.md`.

## Am 2026-09-08 (zweite Sitzung) dazugekommen

* **Antworten in den Fragen.** Jede der 110 Prüfungsfragen trägt ihre Antwort im
  selben Dokument, eingeklappt als `.Answer` / `[%collapsible]` — dieselbe Form
  wie die Lösungen in `exercises.adoc`. Die Antworten sind ausformuliert
  (Erläuterung zuerst, danach „Points the answer must contain“), nicht mehr nur
  Stichpunkte.
* **Grafiken in den Antworten.** Commit-Graphen und Ähnliches als
  `[graphviz,q-…,svg]`, Prozessbilder weiter als PlantUML. Neu unter anderem:
  fast-forward gegen Merge-Commit, die drei lokalen Orte, die Netzgrenze,
  Kontextfenster, Pipeline, magisches Dreieck, Erhebungsreihenfolge.
  Diagrammnamen im Fragenkatalog beginnen mit `q-`.
* **Schalter „Alle aufklappen“.** `templates/site/docinfo-footer.html` wird von
  `local-convert.sh` als gemeinsames docinfo eingebunden
  (`-a docinfo=shared -a docinfodir=/documents/build/site`). Der Schalter
  erscheint auf jeder Seite mit mindestens zwei `<details>` — also auf allen
  Fragen- und Übungsseiten. Das docinfo bringt außerdem den Stil des
  Fragenkatalogs mit (Filter, Tags).
* **Prüfung 10** `answers`: jede Frage eines `ready`-Moduls braucht einen
  Antwortblock. `tools/adoc.py` erkennt `[%collapsible]`; zwei Tests (rot/grün),
  Suite jetzt **57 Tests**.
* **Leistungsfeststellung korrigiert.** `course-overview` nennt jetzt *vier
  schriftliche Prüfungen* (in der Regel zwei je Semester) **zusätzlich** zur
  mündlichen Prüfung; beide schöpfen aus demselben veröffentlichten
  Fragenkatalog. Thema `assessment-oral-exams` heißt jetzt
  `assessment-written-and-oral`, Titel „Written exams and oral assessment“.
* **Kreativitätstechniken nach dem Buch.** `governance-idea-generation` deckt
  jetzt **Brainstorming, Methode 6-3-5, Morphologischer Kasten, Mindmapping,
  Bionik, Delphi-Methode** ab — SCAMPER ist raus. 5 Lernziele, 6 Fragen,
  6 Aufgaben (inkl. morphologischem Kasten, Bionik-Analogie, Delphi-Schätzung).
* **Neues Theoriethema U6: `governance-requirements-elicitation`** —
  Erhebungstechniken der Anforderungsanalyse: Interview, Fragebogen,
  Beobachtung und vor allem **Dokumentenanalyse**. Reihenfolge
  Dokumente → Interview → Beobachtung → Fragebogen. Vollständiges Modul,
  `status: ready`. Alle Theoriethemen ab U6 sind um einen Unterricht nach hinten
  gerückt (Projektauftrag jetzt U7, UML U22–U26, Leistungsfeststellung U27).
  Budget: `theorie: 27`, `governance: 10`.

* **Lastenheft und Pflichtenheft** werden jetzt wirklich behandelt, nicht nur
  als Kontrastfolie erwähnt: neuer Abschnitt in `sdd-why-specs` mit DIN-69901-5-
  Rollenverteilung (Auftraggeber schreibt das Lastenheft, Auftragnehmer das
  Pflichtenheft), klassischer Gliederung (Zielbestimmung mit Muss-, Wunsch- und
  Abgrenzungskriterien, `/F10/`, `/D10/`, `/L10/`, `/Q10/`, Testfälle, Glossar)
  und der Zuordnung auf Projektauftrag und `openspec/specs/`. Neues Lernziel
  `lo-5` plus Frage; Querverweis aus `governance-requirements-elicitation`.
* **Fork im Pull-Request-Modul.** Bisher fehlte, dass ein Pull Request aus einem
  fremden Repository einen eigenen Fork braucht. Neu in `git-pull-requests`:
  Abschnitt „Branch or fork: who is allowed to push?" mit Entscheidungstabelle,
  Diagramm upstream/origin/lokaler Klon, `gh repo fork --clone`,
  `git remote add upstream`, Pull Request gegen das Original, Fork
  synchronisieren (`git fetch upstream` / `gh repo sync`). Neues Lernziel
  `lo-5`, zwei Fragen, zwei Aufgaben, vier neue Pitfalls. Regel im Kurs:
  Übungsrepositories werden geforkt, das Projektrepository nicht — dort sind
  alle Collaborator.

## Arbeitsstand im Git

**Nichts davon ist committet.** Letzter Commit ist `438448b fix: make the module
screenshot resolve in the built site`; der gesamte Stand dieser Sitzung liegt
unversioniert im Arbeitsverzeichnis (42 Pfade, darunter das neue Modul
`modules/governance-requirements-elicitation/` und
`templates/site/docinfo-footer.html`).

Vorgeschlagene Aufteilung, falls noch nicht geschehen:

1. `feat(questions): answer blocks with explanations and diagrams` — die 21
   `questions.adoc`, `tools/adoc.py`, Prüfung 10 in `check-curriculum.py`,
   Tests, `templates/module/*`, `tools/new-module.py`
2. `feat(site): shared docinfo with an expand-all switch` —
   `templates/site/docinfo-footer.html`, `local-convert.sh`, `README.adoc`
3. `feat(idea-generation): six techniques from the textbook` — das Modul
   `governance-idea-generation`, `coverage.md`
4. `feat(curriculum): teach requirements elicitation as U6` — neues Modul,
   `curriculum.yaml` (Renummerierung, Budget), `course-overview` mit den vier
   schriftlichen Prüfungen, `coverage.md`
5. `feat(sdd): teach Lastenheft and Pflichtenheft` — `sdd-why-specs`,
   Querverweis in `governance-requirements-elicitation`
6. `feat(pull-requests): fork workflow for repositories you cannot push to` —
   `git-pull-requests` (index, questions, exercises)

## Entscheidungen dieser Sitzung

* **Docker wird nicht vorgezogen.** Der Praxis-Strang bleibt wie er ist
  (AI ab U8, Docker ab U14).
* Anforderungsanalyse als **eigenes Theoriethema** vor dem Projektauftrag, nicht
  in `governance-stakeholders-goals` eingebaut.

## Konventionen der Module

```adoc
== What does a commit contain?          // questions.adoc
covers: lo-1

.Answer
[%collapsible]
====
Erläuterung — warum ist das so, woran merkt man es, was folgt daraus.

Points the answer must contain:

* Stichpunkt
====
```

Enthält der Antworttext selbst ein `====`-Beispiel (etwa ein Admonition-Block im
`[source,adoc]`), braucht der Antwortblock einen längeren Begrenzer (`=====`) —
sonst meldet asciidoctor „unterminated listing block“. Ein Fall im Repository:
`asciidoctor-basics`, zweite Frage.

`status: ready` erst setzen, wenn das Modul fertig ist. Probelauf:
`python tools/check-curriculum.py --as-ready <topic-id>`.

## Verifikation

```bash
.venv/bin/python tools/check-curriculum.py    # 55 Themen, 21 ready, 0 Befunde
.venv/bin/python -m pytest tools/tests -q     # 57 passed
PYTHON=.venv/bin/python ./local-convert.sh    # build/site/index.html
.venv/bin/python tools/rights-report.py       # 1 Bild, own=1
```

## Was aussteht

**Braucht GitHub-Aktionen des Lehrenden:**

- `klassen-setup` und `student-project-template` als Repos anlegen und pushen
- `htl-leonding-example/jg03-syp-git-basics` anlegen, `assignment_template`
  eintragen, Check um „Repository existiert“ erweitern
- Hinweis auf den jeweils anderen Katalog auf beiden Einstiegsseiten
- Übernahme geeigneter Fragen aus dem bestehenden Katalog mit Modulzuordnung

**Braucht Geräte oder Absprachen:**

- `setup-tools.sh` auf frischem Ubuntu 26.04 und auf macOS, dann git-Tag 2026/27
- JDK-Version mit 4./5. Jahrgang abstimmen (`versions.env` trägt `25.0.1-tem`)
- Deployment-Diagramm und Kubernetes-Vertiefung mit 4./5. Jahrgang abstimmen
- `publish.sh` einmal gegen den Schulwebspace laufen lassen, zuerst `--dry-run`

**Zuerst, falls offen:** die sechs Commits oben setzen und pushen — die Pipeline
hat den Stand dieser Sitzung noch nie gebaut.

**Nächster inhaltlicher Schritt:** Module U11–U18 schreiben —
`sdd-openspec-artifacts` (Skelett liegt, Fragen-Skelett trägt schon den
Antwortblock), `ai-harness-engineering`, `sdd-change-lifecycle`,
`ai-agentic-loops`, `bridge-progress-and-milestones`, `review-milestone-1`,
danach der Docker-Block. Empfehlung weiterhin: SDD/AI-Theoriestrang am Stück,
damit die Querverweise in einem Zug stimmen.
