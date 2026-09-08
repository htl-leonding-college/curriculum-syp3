# Continuation Prompt — Curriculum SYP 3. Jahrgang

**Stand:** 2026-09-07 · Plattform-Change **42/51**, Curriculum-Change **19/21**
**Site live:** https://htl-leonding-college.github.io/curriculum-syp3/ (Pipeline grün)
**Module:** U1–U10 vollständig geschrieben, 20 Themen auf `status: ready`, 97 Fragen

> Löst `2026-09-07-implementierung-gruppen-1-8.md` ab.

---

## Einstieg

```
/opsx:apply setup-curriculum-repository
```

Struktur steht in `curriculum.yaml` (54 Themen, U1–U28), Entscheidungen in
`openspec/changes/*/design.md`, Abdeckung in
`openspec/changes/define-syp3-curriculum/coverage.md`.

## Was steht

```
curriculum-syp3/                 Pipeline grün, Pages veröffentlicht
  tools/                         Prüfungen 1-9 + Strukturattribut-Verbot,
                                 4 Generatoren, new-module.py, rights-report.py
                                 50 Tests (je Prüfung rot und grün)
  modules/                       20 fertige Module (U1-U10) + 1 Skelett
  templates/module/              Vorlage und Autorenleitfaden
  templates/governance/          Projektantrag, Projektauftrag, Meilensteinplan,
                                 Abnahme, Antragsfelder->openspec (zweisprachig)
  site/index.adoc                Landing Page (Mindmap, Navigation, UE-Übersicht)
  local-convert.sh               Prüfung -> Generatoren -> asciidoctor -> revealjs
  publish.sh                     rsync auf den Schulwebspace (noch nie gelaufen)

../klassen-setup/                lokal, 1 Commit, kein Remote
../student-project-template/     lokal, 2 Commits, kein Remote
```

## Konventionen der Module

```adoc
== Learning outcomes
* [[lo-1]] Record a change as a commit      // index.adoc

== What does a commit contain?              // questions.adoc
covers: lo-1

.Scrum framework (free: CC BY-SA 4.0, https://…, retrieved 2026-09-10)
image::images/scrum.png[Scrum framework,600]
```

`status: ready` erst setzen, wenn das Modul fertig ist — dann prüfen Bijektion,
Pflichtabschnitte, Outcome-Kopplung und Modulskelett hart. Probelauf vorher:
`python tools/check-curriculum.py --as-ready <topic-id>`.

## Verifikation

```bash
.venv/bin/python tools/check-curriculum.py          # 54 Themen, 20 ready, 0 Befunde
.venv/bin/python -m pytest tools/tests -q           # 50 passed
PYTHON=.venv/bin/python ./local-convert.sh          # build/site/index.html
```

## Was aussteht

**Braucht GitHub-Aktionen des Lehrenden:**

- `klassen-setup` und `student-project-template` als Repos anlegen und pushen (7.1, 8.1
  ist lokal erledigt)
- `htl-leonding-example/jg03-syp-git-basics` anlegen, `assignment_template` eintragen,
  Check um "Repository existiert" erweitern (9.1, 9.2)
- Hinweis auf den jeweils anderen Katalog auf beiden Einstiegsseiten (6.3)
- Übernahme geeigneter Fragen aus dem bestehenden Katalog mit Modulzuordnung (6.2)

**Braucht Geräte oder Absprachen:**

- `setup-tools.sh` auf frischem Ubuntu 26.04 und auf macOS durchlaufen, dann git-Tag
  2026/27 (7.6, 7.7)
- JDK-Version mit 4./5. Jahrgang abstimmen — `versions.env` trägt `25.0.1-tem` mit TODO
  (7.3, Curriculum-Change 4.2)
- Deployment-Diagramm und Kubernetes-Vertiefung mit 4./5. Jahrgang abstimmen
  (Curriculum-Change 4.1)
- `publish.sh` einmal gegen den Schulwebspace laufen lassen (5.5)

**Nächster inhaltlicher Schritt:** Module U11–U18 schreiben — `sdd-openspec-artifacts`
(Skelett liegt schon), `ai-harness-engineering`, `sdd-change-lifecycle`,
`ai-agentic-loops`, `bridge-progress-and-milestones`, `review-milestone-1`, danach der
Docker-Block. Reihenfolge wie im Jahresplan, jedes fertige Modul auf `status: ready`.
