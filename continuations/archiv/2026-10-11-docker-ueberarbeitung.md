# Continuation Prompt — Curriculum SYP 3. Jahrgang

**Stand:** 2026-10-11 · Plattform-Change **42/51**, Curriculum-Change **19/21**
**Site live:** https://htl-leonding-college.github.io/curriculum-syp3/
**Module:** 36 von 55 Themen ready (35 in SYP3, 1 verschoben nach SYP4),
**203 Fragen**, alle mit ausformulierter Antwort
**Git:** Docker-Überarbeitung (`daa65c6`) und die Git-Bilder vom 11.10. sind
**gepusht**; Pipeline-Ergebnis mit `gh run list --limit 3` prüfen.

> Löst `2026-10-05-syp4-staging-area-und-intellij.md` ab. Ältere liegen in
> `continuations/archiv/` — dort stehen auch Setup-Skripten, Container-Prüfstand
> und die Buchlücken-Tabelle, die hier nicht wiederholt werden.

> **Seit 05.10.:** zwei Inhaltscommits — `daa65c6`, die Überarbeitung der vier
> Docker-Module, und danach kbd-Fix plus Fork-/Template-/Workflow-Bilder in den
> git-Modulen (beide siehe unten). Arbeitsbaum sonst sauber bis auf `chat.adoc`,
> `.chat.adoc.swp` und die Datei `continuations/2026-09-23-…` (unversioniert,
> vom Lehrenden noch nicht freigegeben).

---

## Einstieg

```
/opsx:apply setup-curriculum-repository
```

Struktur steht in `curriculum.yaml`, Entscheidungen in
`openspec/changes/*/design.md`, Abdeckung in
`openspec/changes/define-syp3-curriculum/coverage.md`.

---

## Docker-Module überarbeitet (11.10., Commit `daa65c6`)

Der Lehrende hat die Überarbeitung von L14–L17 (`docker-basics`,
`docker-images`, `docker-volumes-config`, `docker-multiarch`) **an Claude
übergeben** — die frühere Vereinbarung „er gestaltet selbst um" gilt nicht mehr.
Grund der Unzufriedenheit wurde nie genannt; es wurde deshalb **nur** getan, was
er verlangte, nicht neu geschrieben.

**Umgesetzt**

* **Eigene Zeichnungen** aus seinen Kursunterlagen
  (htl-leonding-college.github.io/docker-lecture-notes), ins Englische übersetzt:
  Virtualisierung, Image/Container, Port-Mapping, Build-Context, Bind Mount vs.
  Volume, nginx (zwei Bilder), Netzwerk, `build-image.svg`. Bildtitel `(own)`.
  - `docker-basics`: `-lightweight-virt`, `-image-container-v2`, `-port-mapping`,
    neuer Abschnitt „Containers talk to each other" mit `docker-network-en.png`
  - `docker-images`: `build-image.svg`, neuer Abschnitt „The build context"
  - `docker-volumes-config`: Bind-Mount-vs-Volume, nginx-Beispiel mit zwei Bildern
  - `docker-multiarch`: **kein** passendes Bild, unverändert
* **CLI-Syntax neu:** `docker container ls|rm|stop|exec|logs`, `docker image
  ls|rm|history|tag`. `run`, `build`, `pull`, `push`, `login` bleiben.
* **Alpine 3.24** statt 3.20 (vom Lehrenden genannt, nicht gegengeprüft).
  nginx 1.27 und postgres 17 unverändert.
* **Englische Begriffe, deutsche in Klammern** bei der ersten Verwendung;
  Terminology-Tabellen der vier Module jetzt *English | Deutsch*.
* `docker-basics/exercises`: Lösung zu `docker run alpine:3.24 sh` nennt `exit`
  bzw. Ctrl+D.

**Nicht ins Repo:** `docker-architecture-v2.png` ist von ByteByteGo, nicht
eigen — nicht verwendet. Memory `docker-konventionen-lessons` hält CLI-Syntax,
Alpine, Begriffsregel und diesen Hinweis fest.

**Übersetzungsweg (falls weitere Zeichnungen folgen):** Quellen liegen in
`assets/Notizen-20-21.key` (Docker-Folien 118, 119, 120, 133, 134, 141) und
`assets/Notizen-23-25.key` (Build-Context, Folie 259). Keynote öffnet nur Kopien
per `open -a Keynote <datei>` (AppleScript-`open` scheitert an der Sandbox);
vorher `xattr -c` auf der Kopie. Texte per AppleScript ersetzen (Treffer mit
`starts with`, **`it` ist reserviert**), Folien als PNG exportieren
(`export … as slide images`), mit Pillow zuschneiden. Originale nie speichern.

**Offen aus dieser Überarbeitung**

1. **Übungen und Fragen nicht angepasst** an die neuen Bilder und den
   nginx-/Netzwerk-Abschnitt. Der Netzwerk-Abschnitt hat **kein Lernziel und
   keine Frage**; die nginx-Befehle (`-p 8081:80`, `docker exec`) kommen in den
   Drills nicht vor
2. **Template** `templates/module/index.adoc` hat noch *Deutsch | English*; alle
   anderen Module ebenfalls. Angleichen nur nach Rücksprache
3. **Klammerregel nur an den wichtigsten Stellen** gesetzt, nicht bei jedem
   Fachwort
4. Zeichnungen stammen aus Keynote-Folien mit etwas hellerem Gelb als die alten
   PNGs; untereinander einheitlich
5. Im Build-Context-Bild zeigt der Baum in der Mitte weiter *alle* Dateien, das
   `.dockerignore` lässt aber nur `*.java` durch (Screenshot, nicht änderbar)
6. Der Lehrende kann weiterhin sagen, was ihm an den Docker-Modulen **inhaltlich**
   nicht gefällt — danach erst tiefer eingreifen
7. Compose L19–L21 baut auf diesem Stand auf: dieselbe Bildsprache, neue
   CLI-Syntax, Netzwerk-Bild ist in `docker-basics` schon verwendet

## kbd-Fix und Git-Bilder (11.10., nach `daa65c6`)

* **`kbd:[…]` wurde in Übungen und Fragen roh ausgegeben** — dort fehlte
  `:experimental:`. Jetzt global: `local-convert.sh` setzt `-a experimental`
  für asciidoctor *und* revealjs (Pipeline nutzt dasselbe Skript). Zusätzlich
  `:experimental:` im Kopf von `templates/module/exercises.adoc`,
  `questions.adoc` und den drei betroffenen Dateien (für die GitHub-Vorschau).
* **`git-pull-requests`**, drei eigene Zeichnungen aus den git-lecture-notes
  (`themen/git/git-lecture-notes/asciidocs/images/`):
  - `git-forked-from.png` nach der Fork-Definition
  - `git-fork-and-branch.png` **ersetzt** das Graphviz-Diagramm `fork-flow`
  - `git-template-repository.png` in neuem Unterabschnitt „Fork or template
    repository?" (Tabelle Fork/Template, `gh repo create --template`, GitHub
    Classroom nutzt Templates — vom Lehrenden bestätigt). „Variante 1/2" per
    Pillow auf „Variant 1/2" übersetzt. Terminology: Vorlagen-Repository
  - **Bewusst kein Lernziel und keine Frage** zum Template-Abschnitt
    (Entscheidung des Lehrenden)
  - Rote Rechtschreib-Wellenlinien unter „github-account" in zwei Bildern:
    **bleiben**, der Lehrende kümmert sich später selbst darum
* **`git-basics`**, Abschnitt „Four places, not one": Folie 3 aus
  `assets/Notizen-22-23.key` („GitHub Workflow", add/commit/push mit v1/v2) als
  `git-workflow-add-commit-push.png`, ohne Folientitel und ohne Zeile
  „4bhitm, 20.09.2022" zugeschnitten. Steht unter dem PlantUML-Diagramm.
  Export: alle Folien außer 3 auf `skipped` setzen, dann `export … as slide
  images with properties {skipped slides:false}` — liefert genau ein PNG.

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

**Grün.** Beide Läufe vom 05.10. — `37370257099` (`8ce51a3`) und
`37371762006` (`ee726d9`) — liefen im zweiten Versuch durch. Die Live-Site
zeigt SYP3/SYP4 in der Mindmap, den IntelliJ-Abschnitt in
`git-conflicts-remotes` und „staging area" in `git-basics`.

Der erste Versuch scheiterte an GitHub, nicht am Inhalt: Actions meldete
erst `degraded_performance`, dann `major_outage`. „Curriculum prüfen" bekam
15 Minuten keinen Runner und wurde ohne einen einzigen Schritt abgebrochen,
„Site bauen" und „Veröffentlichen" wurden übersprungen. **Erkennungsmerkmal:**
Job `cancelled` mit leerer Schrittliste und ohne `runner_name`. Abhilfe:
githubstatus.com abwarten, dann `gh run rerun <id> --failed`.

Wegen `concurrency: cancel-in-progress` bricht ein neuer Push einen noch
wartenden Lauf ab — bei einem Ausfall also nicht nachschieben, sondern den
letzten Lauf neu starten.

---

## Offen

### Zuerst

0. Pipeline des letzten Pushs prüfen; offene Punkte der Docker-Überarbeitung
   (siehe oben) mit dem Lehrenden klären. Danach Compose L19–L21.
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

Empfehlung: UML L21–L25 als geschlossener Strang. Compose L19–L21 am Stück,
jetzt möglich (Docker-Module überarbeitet; Muster siehe oben, vorher die offenen
Punkte 1–2 klären). `process-waterfall` kann auf die Pflichtenheft-Gliederung
in `sdd-why-specs` aufsetzen.

---

## Konventionen und Fallstricke

Unverändert gegenüber dem archivierten Prompt: Site englisch, IDs deutsch;
Fragenformat mit `covers:` und `.Answer`; Pflichtabschnitte; Farbpalette in
`templates/module/README.adoc`; `#Farbe:text;` in Aktivitätsdiagrammen
scheitert; `status: ready` erst nach
`.venv/bin/python tools/check-curriculum.py --as-ready <id>`.

**Neu (11.10.):** Bildtitel-Herkunft heißt `(own)`, `(free: …)` oder `(unclear: …)`
— `(own; Zusatz)` wird **nicht** erkannt, Zusatz nur mit Doppelpunkt. Alt-Text mit
Komma in Anführungszeichen setzen (`image::x.png["a, b",700]`), sonst bricht
Asciidoc ihn auf. Docker-Befehle in der Management-Syntax (`docker container ls`).

**Neu (11.10.):** `kbd:[…]` braucht `experimental` — ist jetzt global gesetzt,
in neuen Dateien trotzdem `:experimental:` in den Kopf (GitHub-Vorschau).

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
.venv/bin/python tools/rights-report.py       # 15 Bilder, own=14, unclear=1 → exit 1 (bekannt)
gh run list --limit 3
```

`chat.adoc` ist der private Notizblock des Lehrenden: nicht lesen, nicht
committen. `continuations/2026-09-23-…` bleibt unversioniert, bis der Lehrende
sie ausdrücklich freigibt. Dazu liegt `.chat.adoc.swp` im Arbeitsbaum (Datei ist in einem
Editor offen) — ebenfalls nicht committen.
