# Continuation Prompt — Curriculum SYP 3. Jahrgang

**Stand:** 2026-09-08 · Plattform-Change **42/51**, Curriculum-Change **19/21**
**Site live:** https://htl-leonding-college.github.io/curriculum-syp3/ (Pipeline grün)
**Module:** U1–U10 vollständig, 20 Themen auf `status: ready`, 100 Fragen

> Löst `2026-09-07-module-u1-u10-fertig.md` ab. Ältere liegen in `continuations/archiv/`.

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
                                 54 Tests (je Prüfung rot und grün)
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

## Am 2026-09-08 dazugekommen

* **Mindmap** hat eine Ebene mehr: `theme` in `curriculum.yaml` gruppiert die
  Themen innerhalb ihres Blocks (Git, Containers, Milestone reviews …). Farbe je
  Block, geplante Themen grau, alles auf **einer** Seite — zweiseitig wurde die
  Karte 2235 px breit und die Schrift beim Skalieren unlesbar.
* **Navigation** verlinkt je fertigem Modul zusätzlich `Übungen` und `Fragen`;
  vorher waren beide Seiten nur über ihre Adresse erreichbar.
* **Umlaute:** deutscher Text im ganzen Repository mit ä/ö/ü/ß statt ae/oe/ue.
  Bezeichner, Topic-IDs und Dateinamen bleiben ASCII. `chat.adoc` und
  `continuations/archiv/` sind Protokolle und bleiben unverändert.
* **README.adoc** dokumentiert `local-convert.sh` und `publish.sh` samt der
  `WEBSPACE_*`-Vorgaben und der Warnung zu `rsync --delete`.
* **git-basics** deutlich ausgebaut: Architekturbild (working tree, index, local
  repository, remote), Abschnitt zur Netzgrenze, Conventional Commits mit
  Typtabelle und Task-Id aus den Projektrichtlinien, IntelliJ-Screenshot des
  Git-Log-Fensters, zwei neue Drills (GitHub-Repo anlegen und pushen; Historie
  nach Typ lesen), zwei neue Fragen, `lo-5`.
* **asciidoctor-Container** von 1.83 auf **1.107** gehoben (`config.sh`).

## Konventionen der Module

```adoc
== Learning outcomes
* [[lo-1]] Record a change as a commit      // index.adoc

== What does a commit contain?              // questions.adoc
covers: lo-1

.Git log in IntelliJ IDEA 2026.2 (own)      // Werkzeugversion im Dateinamen
image::images/git-log-intellij-2026.2.png[Git log in IntelliJ,700]
```

`status: ready` erst setzen, wenn das Modul fertig ist — dann prüfen Bijektion,
Pflichtabschnitte, Outcome-Kopplung und Modulskelett hart. Probelauf vorher:
`python tools/check-curriculum.py --as-ready <topic-id>`.

Commit-Messages folgen Conventional Commits (Projektrichtlinien
https://htl-leo-projekte.github.io/project-checklist/#_commit_messages), im
Schülerprojekt zusätzlich mit Task-Id.

## Verifikation

```bash
.venv/bin/python tools/check-curriculum.py          # 54 Themen, 20 ready, 0 Befunde
.venv/bin/python -m pytest tools/tests -q           # 54 passed
PYTHON=.venv/bin/python ./local-convert.sh          # build/site/index.html
.venv/bin/python tools/rights-report.py             # 1 Bild, own=1
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
- `publish.sh` einmal gegen den Schulwebspace laufen lassen, zuerst `--dry-run` (5.5)

**Nächster inhaltlicher Schritt:** Module U11–U18 schreiben — `sdd-openspec-artifacts`
(Skelett liegt schon), `ai-harness-engineering`, `sdd-change-lifecycle`,
`ai-agentic-loops`, `bridge-progress-and-milestones`, `review-milestone-1`, danach der
Docker-Block. Reihenfolge wie im Jahresplan, jedes fertige Modul auf `status: ready`.
Zuschnitt offen: Theorie-Strang am Stück, Unterricht für Unterricht, oder Docker vorziehen.
