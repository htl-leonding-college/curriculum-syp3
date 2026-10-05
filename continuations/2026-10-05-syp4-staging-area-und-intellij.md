# Continuation Prompt — Curriculum SYP 3. Jahrgang

**Stand:** 2026-10-05 · Plattform-Change **42/51**, Curriculum-Change **19/21**
**Site live:** https://htl-leonding-college.github.io/curriculum-syp3/
**Module:** 36 von 55 Themen ready (35 in SYP3, 1 verschoben nach SYP4),
**203 Fragen**, alle mit ausformulierter Antwort
**Git:** `curriculum-syp3` gepusht bis `8ce51a3`, Pipeline **queued** (siehe unten)

> Löst `2026-09-27-geprueftes-setup-und-buchluecken.md` ab. Ältere liegen in
> `continuations/archiv/` — dort stehen auch Setup-Skripten, Container-Prüfstand
> und die Buchlücken-Tabelle, die hier nicht wiederholt werden.

---

## Einstieg

```
/opsx:apply setup-curriculum-repository
```

Struktur steht in `curriculum.yaml`, Entscheidungen in
`openspec/changes/*/design.md`, Abdeckung in
`openspec/changes/define-syp3-curriculum/coverage.md`.

---

## Seit dem 27.09. erledigt

### 1. git-Module ausgebaut (28.09., zwei Commits)

* `git-basics`: Commit-Kapitel mit fünf Zeichnungen (untracked, staged, drei
  Snapshots), Kapitel zentral/verteilt, `git init` und `.git`, Übersicht der
  Clients (Konsole, IntelliJ, GitKraken, GitHub-Web). Reihenfolge wie in den
  bestehenden git-lecture-notes: Architektur, Initialisierung, Commits.
* `git-branching`: detached HEAD mit vier Diagrammen, Rettung über Branch oder
  `git reflog`.

### 2. Nutzwertanalyse nach SYP4 (05.10.)

Entscheidung des Lehrenden: `governance-weighted-scoring` wird im 3. Jg nicht
unterrichtet. Umsetzung:

* `taught_in: jg4`, **kein `lesson`**, steht am Ende von `curriculum.yaml` in
  einem eigenen Abschnitt. Modul bleibt `ready` und auf der Site.
* **Neue Modellregel:** `lesson` ist nur für Themen von `meta.jahrgang` Pflicht.
  Ein Thema eines anderen Jahrgangs darf *keine* Lesson tragen (Befund
  `model`), belegt keinen Slot und kein Budget. `Curriculum.current` /
  `.later` in `tools/curriculum.py`; `of_kind`, `ue_by_kind`, Slot-Prüfung
  laufen nur über `current`.
* **Mindmap:** eine Wurzel je Jahrgang — `SYP3` (vorher „SYP / Year 3 /
  2026/27"), darunter `SYP4` mit dem verschobenen Thema ohne L-Nummer.
  Navigation listet es unter „SYP4" nach den Lessons, die Umfangsübersicht in
  „Moved to a later year", der Fragenkatalog zeigt „SYP4" statt „L4".
* Theorie ab altem L5 **rückt eine Lesson vor**. Budget Theorie 27 → 26,
  governance 10 → 9. **Theorieslot L27 ist frei.**
* `governance-stakeholders-goals` setzt jetzt `governance-idea-generation`
  voraus. Querverweise in idea-generation und stakeholders-goals sagen
  „in year 4".
* Mitgezogen: Non-Goal und Nachtrag D6 in `define-syp3-curriculum/design.md`,
  `coverage.md`, Requirement im Spec `projekt-governance`.

Damit hat sich Gliederungspunkt 2 vom 27.09. teilweise erledigt: die doppelte
L27 (Assessment + minikube-deploy) gibt es nicht mehr, Assessment liegt auf L26.

### 3. „staging area" statt „index" (05.10.)

In `git-basics` durchgehend, auch in Diagrammen. Grund: die Bilder der
git-lecture-notes (z. B. `workflow03.png`), die die Klasse kennt, sagen
„staging area". **Einzige verbliebene Nennung:** Terminology-Tabelle („git's
own documentation calls it the index"). `docker-multiarch` spricht vom
*image index* — anderer Begriff, bleibt.

### 4. IntelliJ in `git-conflicts-remotes` (05.10.)

* Neues Lernziel lo-5, Abschnitt „The same work in IntelliJ": Tabelle Aktion →
  git-Befehl, Merge-Werkzeug (Diagramm der drei Fenster, fünf Schritte,
  Abort Merge), Push-Rejected-Dialog
* Eine Frage (Accept Yours / Theirs / Merge…), zwei Drills: Konflikt in
  IntelliJ lösen mit Setup-Skript, abgelehnten Push reparieren
* Das Setup-Skript ist gegen echtes git geprüft: je eine konfliktfreie Änderung
  pro Seite plus genau ein Konflikt in `average`
* **Nicht in IntelliJ geprüft.** Dialognamen, Buttons und Tastenkürzel stammen
  aus der JetBrains-Doku (resolving-conflicts, commit-and-push,
  sync-with-a-remote-repository), der IDEA-MCP-Server war nicht erreichbar.
  Offen: Drill einmal selbst durchklicken, Screenshot des Merge-Werkzeugs
  (`modules/git-conflicts-remotes/images/`, Rechte `own`)

Kurs-Linie bleibt: Konsole zuerst, IDE als zweites — jeder Klick hat einen
Befehl, und in der Prüfung wird der Befehl genannt.

---

## Pipeline

Lauf `37370257099` für `8ce51a3` stand beim Schreiben dieses Prompts seit
über 15 Minuten auf **`queued`** — kein Runner hat ihn aufgenommen.
githubstatus.com meldete für Actions **`degraded_performance`**, Pages
`operational`. Lokal war alles grün (Prüfung 0 Befunde, 65 Tests, Build exit 0).

**Als Erstes prüfen:** `gh run view 37370257099`. Bleibt er hängen oder
scheitert er ohne inhaltlichen Grund: `gh run rerun 37370257099`. Bis dahin
zeigt die Live-Site noch den Stand von `4e7eb1d` — ohne SYP4, ohne IntelliJ.

---

## Offen

### Zuerst

1. Drill „Resolve the same conflict in IntelliJ" einmal in IntelliJ 2026.2
   durchklicken, Screenshot ergänzen
2. Entscheidungen vom 27.09. (Details im archivierten Prompt):
   * **Buchlücken** K3, K4, K5, K6.2/6.5, K8.4/8.6, K9, K10.1 — je Lücke jg4/jg5
     als Non-Goal oder Slot. **Neu:** L27 Theorie ist frei, also ein Slot ohne
     Streichung verfügbar. Größte Lücke bleibt K9 (Qualitätssicherung)
   * **Gliederung:** `what-is-software-engineering` (L10) nach
     `process-models-overview` (L7), ohne `requires` — Begriffsklärung nach
     Anwendung
   * **Diagramme gefälliger machen** — nicht angefangen (51 von 68
     PlantUML-Blöcken ohne `defaultFontName`)
3. Dann L18 Theorie und L19 Praxis

### Mit SYP4 abzustimmen

* `governance-weighted-scoring` liegt jetzt dort — mit dem 4. Jg klären, ob es
  übernommen wird
* JDK-Version, Deployment-Diagramm, Kubernetes-Vertiefung (unverändert offen)

### Unverändert offen (Details im Archiv)

* GitHub: `jg03-syp-git-basics` anlegen, Katalog-Hinweise, Fragenübernahme
* Rechte `vibe-coding-vs-software-engineering.jpeg`, ISO-25010-Original
* `setup-tools.sh` auf echter Hardware, git-Tag 2026/27 in `klassen-setup`
* `publish.sh --dry-run` gegen den Schulwebspace
* Umlaute in `curriculum-syp3` selbst nicht nachgesehen

---

## Danach: noch 19 Module

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

Empfehlung unverändert: Compose L19–L21 am Stück, UML L21–L25 als
geschlossener Strang. `process-waterfall` kann auf die Pflichtenheft-Gliederung
in `sdd-why-specs` aufsetzen.

---

## Konventionen und Fallstricke

Unverändert gegenüber dem archivierten Prompt: Site englisch, IDs deutsch;
Fragenformat mit `covers:` und `.Answer`; Pflichtabschnitte; Farbpalette in
`templates/module/README.adoc`; `#Farbe:text;` in Aktivitätsdiagrammen
scheitert; `status: ready` erst nach
`.venv/bin/python tools/check-curriculum.py --as-ready <id>`.

**Neu:** In PlantUML-Notizen beginnt eine Zeile nicht mit `=` — das wird zur
Überschrift (`\n= git add` war fett und groß).

**Neu:** Ein Thema in einen anderen Jahrgang verschieben heißt: `taught_in`
ändern, `lesson` *löschen*, abhängige `requires` umhängen, Lücke durch
Nachrücken schließen, Budget anpassen. `check-curriculum.py` meldet jeden
vergessenen Schritt.

## Verifikation

```bash
.venv/bin/python tools/check-curriculum.py    # 55 Themen, 36 ready, 0 Befunde
.venv/bin/python -m pytest tools/tests -q     # 65 passed
PYTHON=.venv/bin/python ./local-convert.sh    # build/site/index.html, exit 0
.venv/bin/python tools/rights-report.py       # unclear=1 → exit 1 (bekannt)
gh run list --limit 3
```

`chat.adoc` ist der private Notizblock des Lehrenden: nicht lesen, nicht
committen.
