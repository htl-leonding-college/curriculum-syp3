# Continuation Prompt — Curriculum SYP 3. Jahrgang

**Stand:** 2026-11-02 · Plattform-Change **42/51**, Curriculum-Change **19/21**
**Site live:** https://htl-leonding-college.github.io/curriculum-syp3/
**Module:** 36 von 55 Themen ready (35 in SYP3, 1 verschoben nach SYP4)
**Git:** letzter Push `6c5dbcb` (englische Begriffe, Zielhierarchie), Pipeline
grün. Remote `origin` steht seit 02.11. auf **SSH**
(`git@github.com:htl-leonding-college/curriculum-syp3.git`) — über HTTPS hat das
gh-Konto `thomasstuetz` nur Leserechte (403).

> Löst `2026-10-11-docker-ueberarbeitung.md` ab und führt die offenen Punkte
> aller früheren Prompts zusammen. Ältere liegen in `continuations/archiv/` —
> dort stehen Setup-Skripten, Container-Prüfstand, Buchlücken-Tabelle und der
> Keynote-Übersetzungsweg im Detail.

---

## Einstieg

```
/opsx:apply setup-curriculum-repository
```

Struktur in `curriculum.yaml`, Entscheidungen in `openspec/changes/*/design.md`,
Abdeckung in `openspec/changes/define-syp3-curriculum/coverage.md`.

**Umgebung seit 02.11.:** Claude läuft in einer Ubuntu-VM (192.168.1.80), der
Lehrende greift per SSH zu. Vorschau vor dem Push: siehe README, Abschnitt
„Vorschau vor dem Push" (`python3 -m http.server 8000 --bind 0.0.0.0
--directory build/site`, im Browser `http://192.168.1.80:8000/`). Kein `.venv`
in diesem Checkout — `python3` direkt verwenden.

---

## Heute, 02.11. — Auftrag des Lehrenden

Empfohlene Reihenfolge: 2, dann 5 und 1 zusammen, dann 3 und 4.

1. **Pflichtenheft als eigenes Dokument beschreiben**, mit der Gliederung aus dem
   Manz-Buch. Die Klasse muss es kennen und im Projekt einmal selbst eines
   geschrieben haben; im laufenden Projekt ersetzen es danach die
   openspec-Specs. Anknüpfen an `sdd-why-specs` (Gliederung steht dort kurz) und
   `sdd-specs-replace-requirements`.
2. **`assets/01.Vorgehensmodelle.key` durchsehen** (Präsentation des Lehrenden,
   nicht ins Repo). Die gezeichneten Grafiken „ARTEN VON VORGEHENSMODELLEN" in
   `process-models-overview` („Process models as three tempos of one pattern")
   einbauen. Dazu Vorschlag: Inhalte in Module übernehmen oder die Präsentation
   im Unterricht verwenden und aus den Modulen auf die Folien verweisen
   (vermutlich einfacher).
3. **Projektthemen für die Schüler festlegen.**
4. **Noch nicht ausgearbeitete Themen ausarbeiten** — welche, mit dem Lehrenden
   klären (Liste unten, „Noch 19 Module").
5. **„Structure of the project application and charter" ausbauen**
   (`governance-project-charter`): Gliederung von Projektantrag und
   Projektauftrag an das Buch anpassen, außer es gibt einen Grund abzuweichen —
   dann den Grund nennen.

---

## Am 02.11. erledigt

### Englische Fachbegriffe im Text (`6c5dbcb`, gepusht)

Regel des Lehrenden, festgehalten in `templates/module/README.adoc`, Abschnitt
„Sprache":

* Modultext englisch, **auch die Fachbegriffe** (*outcome goal*, nicht
  *Ergebnisziel*). Deutsche Begriffe als Paar in `== Terminology` am Ende.
* Deutsch **in Klammern bei der ersten Verwendung** erlaubt und in
  Theoriemodulen erwünscht: `*outcome goal* (Ergebnisziel)`. Nicht bei
  Lehnwörtern, nicht in Überschriften oder Lernzielen. In Technologiemodulen nur
  wo nötig.
* **Feldnamen deutscher Formulare bleiben als Paar**:
  `Ausgangslage / initial situation` (z. B. lo-4 in `governance-project-charter`,
  Mapping-Tabelle in `bridge-charter-to-specs`).
* Titel deutscher Quellen und wörtliche Kundenbegriffe bleiben.

Umgesetzt in allen Governance-, SDD- und Bridge-Modulen sowie
course-overview, process-models-overview, what-is-software-engineering.
Wichtige Zuordnungen: Lastenheft → *requirements specification*,
Pflichtenheft → *functional specification*, Kriterienkatalog → *criteria
catalogue*, Nutzwertanalyse → *weighted scoring*, Abnahme → *acceptance*.

### Zielhierarchie in `governance-stakeholders-goals` (`6c5dbcb`)

Neuer Abschnitt „Operationalising goals: the goal hierarchy" nach dem Buch
(Kap. 2, Lektion 3 „Zielbestimmung"): Gesamtziel → Zielklassen → Teilziele mit
Kriterium und Ausmaß; Top-down, Bottom-up, gemischter Ansatz. Graphviz
`goal-hierarchy`, neues lo-7 mit Frage.

### Governance-Grafik — **noch nicht committet**

* `modules/course-overview/images/governance-steering.svg`, Bildtitel
  `(own)`. Vorlage: Zeichnung des Lehrenden in `assets/Notizen-23-25.key`,
  englisch und inhaltlich überarbeitet: Bereiche Governance / Execution,
  Steering board (client · supervisor) übergibt **nur die Charter** (problem
  statement, task, goals, constraints, milestones) und *Decisions*; zurück gehen
  status, product, risks, change requests. Im Zyklus „Team", Iterations
  (Scrum), Praktiken spec-driven / test-driven / AI-assisted, Kästchen „Specs
  (openspec) — written by the team, not handed down".
* Text in `course-overview` nach der Tabelle Governance/Execution: Board übergibt
  genau ein Dokument; das Pflichtenheft kommt nicht vom Board, im Kurs ersetzen
  es die Specs. Terminology: Lenkungsausschuss, Problemstellung,
  Aufgabenstellung, Rahmenbedingungen, Projektauftrag, Änderungsantrag,
  Pflichtenheft.
* Die SVG ist von Hand bzw. per Python-Skript geschrieben (Pfeilspitzen am
  Kreis berechnet) und direkt editierbar. Rendern zur Sichtkontrolle:
  `cairosvg` in einem Wegwerf-venv (kein rsvg/inkscape auf der VM).
* README: neuer Abschnitt „Vorschau vor dem Push".

---

## Weiterhin offen

### Aus der Docker-Überarbeitung (11.10., `daa65c6`)

1. Übungen und Fragen nicht an die neuen Bilder angepasst; der Netzwerk-Abschnitt
   in `docker-basics` hat **kein Lernziel und keine Frage**, nginx-Befehle
   (`-p 8081:80`, `docker exec`) fehlen in den Drills
2. Terminology-Reihenfolge: Docker-Module *English | Deutsch*, alle anderen und
   das Template *Deutsch | English* — angleichen nur nach Rücksprache
3. Im Build-Context-Bild zeigt der Baum alle Dateien, `.dockerignore` lässt nur
   `*.java` durch (Screenshot, nicht änderbar)
4. Der Lehrende kann noch sagen, was ihm an den Docker-Modulen inhaltlich nicht
   gefällt — erst danach tiefer eingreifen

### Kurs und Gliederung

* Drill „Resolve the same conflict in IntelliJ" (`git-conflicts-remotes`) nie in
  IntelliJ durchgeklickt; Screenshot des Merge-Werkzeugs fehlt
* **Buchlücken** K3, K4, K5, K6.2/6.5, K8.4/8.6, K9, K10.1 — je Lücke jg4/jg5 als
  Non-Goal oder Slot. Theorie-Slot L27 ist frei; größte Lücke K9
  (Qualitätssicherung)
* `what-is-software-engineering` (L10) nach `process-models-overview` (L7)
  ziehen? Ohne `requires`
* Diagramme gefälliger machen (viele PlantUML-Blöcke ohne `defaultFontName`) —
  nicht angefangen

### Mit SYP4 abzustimmen

* `governance-weighted-scoring` liegt dort (`taught_in: jg4`) — übernehmen sie es?
* JDK-Version (`versions.env`: `25.0.1-tem`), Deployment-Diagramm,
  Kubernetes-Vertiefung

### Braucht den Lehrenden, GitHub oder Geräte

* `htl-leonding-example/jg03-syp-git-basics` anlegen, `assignment_template`
  eintragen; Hinweis auf den anderen Fragenkatalog; Fragenübernahme
* Rechte an `vibe-coding-vs-software-engineering.jpeg` (einziges `unclear`-Bild,
  Job „Bildrechte melden" bleibt bis dahin rot, blockiert nichts); ob statt der
  eigenen ISO-25010-Zeichnung das Original hinein soll
* `setup-tools.sh` auf echter Hardware, git-Tag 2026/27 in `klassen-setup`
* `publish.sh --dry-run` gegen den Schulwebspace
* **Ausführungsrechte:** zehn Skripte haben im Arbeitsbaum 644 statt 755
  (`config.sh`, `local-convert.sh`, `publish.sh`, `tools/*.py`). Absichtlich
  nicht committet; `chmod +x` stellt den Repo-Stand wieder her

---

## Noch 19 Module

```
L18  sdd-principle-not-tool          (Praxis fertig: review-milestone-2)
L19  process-waterfall               compose-basics
L20  process-scrum                   compose-multi-service
L21  uml-overview                    compose-networks-dependencies
L22  uml-use-case                    revealjs-presentations
L23  uml-class-object                ai-result-verification
L24  uml-activity                    review-milestone-3
L25  uml-state-overview              ai-project-integration
L26  assessment-written-and-oral     minikube-basics
L27  — frei —                        minikube-deploy
L28  —                               minikube-services
```

Compose L19–L21 am Stück (gleiche Bildsprache und CLI-Syntax wie die
Docker-Module), UML L21–L25 als geschlossener Strang. `process-waterfall` setzt
auf die Pflichtenheft-Gliederung auf — mit Punkt 1 von heute abstimmen.
`review-milestone-3` erst nach `governance-milestones` lesen.

---

## Konventionen und Fallstricke

**Module:** Pflichtabschnitte `Learning outcomes`, fachliche Abschnitte,
`Decisions`, `Pitfalls`, `Terminology`, `Further reading`; leerer
Pflichtabschnitt trägt eine Nullaussage. Jedes Lernziel braucht mindestens eine
Frage. `status: ready` erst nach
`python3 tools/check-curriculum.py --as-ready <id>`.

**Fragen:** `covers: lo-N`, `.Answer` mit `[%collapsible]`, „Points the answer
must contain:". Enthält die Antwort selbst `====`, braucht der Block `=====`.
Diagrammnamen im Fragenkatalog beginnen mit `q-`.

**Site englisch, IDs deutsch** (`theorie`, `praxis`, `jg3` …); Lessons heißen
`L7`. `test_site_output_is_english` prüft die Ausgabe.

**Diagramme:** Pastellpalette mit Bedeutung in `templates/module/README.adoc`
(blau vorgegeben, grün Ergebnis, sand Arbeit, rosa Risiko, lila Nebenschauplatz,
grau Infrastruktur). In Aktivitätsdiagrammen scheitert `#Farbe:text;` — Klassen
`.key .work .ok .bad .aside .muted` als Stereotyp. In PlantUML-Notizen beginnt
keine Zeile mit `=`. Ist ein PlantUML-Layout unruhig, Graphviz nehmen.

**Bilder:** nach `modules/<id>/images/`; Bildtitel endet auf `(own)`,
`(free: …)` oder `(unclear: …)` — `(own; …)` wird nicht erkannt. Alt-Text mit
Komma in Anführungszeichen. `kbd:[…]` ist global aktiv, in neuen Dateien
trotzdem `:experimental:` in den Kopf.

**Docker:** Management-Syntax (`docker container ls`), Alpine 3.24.

**Thema in anderen Jahrgang verschieben:** `taught_in` ändern, `lesson`
löschen, `requires` umhängen, Lücke durch Nachrücken schließen, Budget anpassen.

**Assets:** `assets/` ist in `.gitignore` und bleibt draußen — Keynote-Notizen,
`01.Vorgehensmodelle.key`, Manz-Buch (`assets/SYP-Buch.Manz.Aufl_2013`, Scans
ohne Textebene: Seiten mit `pdftoppm -r 100 -png -f N -l M` rendern und als Bild
lesen; PDF-Seite = Buchseite − Kapitelanfang + 1).

**Nicht committen:** `chat.adoc` (privater Notizblock des Lehrenden, auch nicht
lesen), `.chat.adoc.swp`, die Modusänderungen der Skripte.

**Pipeline:** Job `cancelled` mit leerer Schrittliste und ohne `runner_name` ist
ein GitHub-Ausfall — githubstatus.com abwarten, dann `gh run rerun <id>
--failed`, nicht nachpushen (`cancel-in-progress`).

## Verifikation

```bash
python3 tools/check-curriculum.py      # 55 Themen, 36 ready, 0 Befunde
python3 -m pytest tools/tests -q       # 65 passed
PYTHON=python3 bash local-convert.sh   # build/site/index.html, exit 0, ~2 min
python3 tools/rights-report.py         # 16 Bilder, own=15, unclear=1 → exit 1 (bekannt)
gh run list --limit 3
```
