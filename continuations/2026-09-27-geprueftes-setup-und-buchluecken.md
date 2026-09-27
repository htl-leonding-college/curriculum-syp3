# Continuation Prompt — Curriculum SYP 3. Jahrgang

**Stand:** 2026-09-27 · Plattform-Change **42/51**, Curriculum-Change **19/21**
**Site live:** https://htl-leonding-college.github.io/curriculum-syp3/
**Module:** L1–L18 vollständig — **36 von 55 Themen ready**, **199 Fragen**,
alle mit ausformulierter Antwort
**Git:** `curriculum-syp3` hat **2 Commits lokal, nicht gepusht**;
`klassen-setup` und `student-project-template` sind gepusht und grün

> Löst `2026-09-23-buchabgleich-umgesetzt-und-pastellgrafiken.md` ab. Ältere
> liegen in `continuations/archiv/`.

---

## Einstieg

```
/opsx:apply setup-curriculum-repository
```

Struktur steht in `curriculum.yaml` (55 Themen), Entscheidungen in
`openspec/changes/*/design.md`, Abdeckung in
`openspec/changes/define-syp3-curriculum/coverage.md`.

---

## Drei Repositories, nicht mehr eines

Bis heute lagen `klassen-setup` und `student-project-template` nur lokal, ohne
Remote. Beide sind jetzt öffentlich unter `htl-leonding-college`.

| Repository | Stand | Pipeline |
|---|---|---|
| `curriculum-syp3` | 2 Commits **lokal**, `origin/main` auf `a9a7d7a` | zuletzt grün |
| `klassen-setup` | 4 Commits, gepusht | **grün**, 1m42s |
| `student-project-template` | 3 Commits, gepusht | **grün**, Pages live |

`https://htl-leonding-college.github.io/student-project-template/` ist
erreichbar. `klassen-setup` hat keine Pages — dort ist ein 404 richtig.

**Stolperstein beim Anlegen:** ein frisches Repo hat GitHub Pages nicht
aktiviert, der `deploy-pages`-Schritt scheitert dann mit `HttpError: Not Found`.
Einschalten ohne Weboberfläche:

```bash
gh api -X POST repos/<org>/<repo>/pages -f build_type=workflow
gh run rerun <run-id> --failed
```

---

## Am 2026-09-27 erledigt

### 1. Der Arbeitsbaum vom 23.09. ist committet

Docker lief wieder, `./local-convert.sh` einmal vollständig (exit 0) — damit ist
die seit dem 23.09. ausstehende Build-Prüfung erledigt. Drei Commits:
Buchabgleich, Pastellpalette, Continuation.

### 2. Lesson 1 trägt keine Aufgaben und Fragen mehr

`course-overview` ist der Organisationsteil und wird nicht geprüft. Beide
Dateien tragen jetzt eine Nullaussage mit Verweis auf die Module, die den Stoff
wirklich prüfen.

**Der Fallstrick, der wiederkommt:** `check-curriculum.py` verlangt bei
`status: ready` zu jedem Lernziel eine Frage (Prüfung 7). Die drei Lernziele im
`index.adoc` sind deshalb Prosa **ohne `[[lo-N]]`-Anker** — `OUTCOME_RE` in
`tools/adoc.py` greift nur auf `* [[id]] …`, damit ist die Prüfung still und der
Inhalt bleibt lesbar. Für **Praxisthemen geht das nicht**: Prüfung 4 verlangt
dort mindestens eine Frage, das ließe sich nur im Werkzeug lockern.

### 3. Der Live-USB-Test ist ersatzlos entfallen

Entscheidung des Lehrenden: einen Stick vorab erstellen zu lassen ist nicht
sinnvoll, weil es zu wenige tun. Entfernt aus `learning-environment-setup` in
Text, Diagramm, Decisions, Pitfalls, Prüfungsfrage und Aufgabe — und
mitgezogen in `design.md` D7, U1-Ablauf, U1-Hausübung, Risikotabelle,
`proposal.md`, `tasks.md` 3.2 sowie
`specs/curriculum/lernumgebung/spec.md`.

Das **angenommene Restrisiko** steht ausdrücklich in D7 und als eigenes Szenario
im Spec: ein Gerät, dessen WLAN- oder Grafikchip unter Linux nicht läuft, fällt
erst nach dem Partitionieren auf.

### 4. Die Setup-Skripten liefen zum ersten Mal — und liefen nicht

Der Lehrende hat gefragt, woher er weiß, dass die Anleitung funktioniert. Die
ehrliche Antwort war: gar nicht. `setup-tools.sh` war seit dem 07.09.
geschrieben und **nie ausgeführt**. Gegen ein frisches `ubuntu:26.04` im
Container starb es dreimal, bevor es ein einziges Werkzeug des Java-Stacks
erreichte:

* der SDKMAN-Installer verlangt **`zip`**, installiert wurde nur `unzip`
* `JAVA_VERSION="25.0.1-tem"` **existiert in SDKMAN nicht** (nächster Stand
  `25.0.4-tem`)
* **SDKMAN ist nicht `set -u`-fest** — `set -u` direkt nach dem `source` von
  `sdkman-init.sh` lässt jedes `sdk install` mit
  `sdkman-install.sh: line 24: $3: unbound variable` scheitern

Dazu: `set -e` warf bei einem Fehlschlag die anderen elf Werkzeuge weg;
JetBrains meldete auf Linux `[install]`, installierte aber nie; `versions.env`
behauptete, gegen Ubuntu 26.04 getestet zu sein; `ssh-keygen` lief ohne
vorhandenes `~/.ssh`.

Alles behoben. Neu ist das Fehlerverhalten: ein gescheiterter Schritt beendet
den Lauf nicht, sondern landet unter `== Bilanz`, Rückgabewert ≠ 0. `--check`
endet mit 1, wenn etwas fehlt.

**Die JetBrains Toolbox wird jetzt auch auf Linux installiert** — Tarball,
Architektur passend, **SHA-256 gegen die veröffentlichte Prüfsumme geprüft**,
nach `~/.local/share/JetBrains/Toolbox` entpackt. Als einziges Werkzeug
**bewusst nicht gepinnt**: JetBrains hält unter dem Produktcode nur den
aktuellen Build vor, ein Pin wäre eine Zusage, die die Quelle nicht einhält.
Begründung steht in `versions.env`. Damit gibt es keinen Schritt mehr, der sich
nicht selbst installieren kann — die `[manuell]`-Mechanik ist wieder raus, und
„der zweite Lauf meldet `[ok]` für jeden Schritt" stimmt wieder.

### 5. Die Behauptung bleibt prüfbar

`klassen-setup/.github/workflows/setup.yml`: bei jedem Push **und wöchentlich**
läuft das Skript dreimal in einem frischen `ubuntu:26.04`-Container — `--check`
blank muss 1 liefern, die Vollinstallation 0, der dritte Lauf darf **keine
einzige `[install]`-Zeile** enthalten. Dazu `shellcheck -S warning`.

Der wöchentliche Lauf ist der wichtigere: er fängt veraltete Paketnamen und
Download-Adressen, bevor sie im Unterricht auffallen.

### 6. Vorlagen angeglichen, Umlaute hergestellt

`student-project-template/docs/` ist eine Kopie von
`templates/governance/` und war auf dem Stand **vor** dem Buchabgleich. Jetzt
übernommen: Ist-Zustand, Mengengerüst, Zieltabelle mit Art und Priorität,
Stakeholder intern/extern mit Interesse, Zielkonkurrenz. `meilensteinplan.adoc`
und die Architekturskizze trugen noch `skinparam monochrome true`.

Beide neuen Repositories sind auf echte Umlaute umgestellt (121 + 16
Ersetzungen, über eine Wortliste statt über ein Muster, damit `Quelle`,
`Fehlerquelle`, `question` und `sudoers` unangetastet bleiben).

---

## Was der Container-Prüfstand **nicht** kann

Wichtig für die nächste Sitzung, sonst wird derselbe Fehlalarm nochmal
untersucht:

* **Apple Silicon + amd64-Container = kein `tar`.** GNU tar 1.35 scheitert dort
  bei *jedem* Entpacken mit `Cannot open: Function not implemented` — auch bei
  einem selbst erzeugten Archiv mit einer Textdatei. Das ist die Emulation,
  nicht das Skript. Nativ auf arm64 läuft es. Der amd64-`tar`-Pfad wird nur von
  der Pipeline auf echten Runnern abgedeckt, und dort ist er grün
* **Emulierte Läufe dauern lang** (JDK + Docker + 151 MB Toolbox). Für schnelle
  Durchläufe `--platform linux/arm64` nehmen
* Nicht prüfbar bleiben: Partitionierung, BitLocker, UEFI und Secure Boot,
  WLAN- und Grafiktreiber — und `setup-identity.sh`, das interaktiv ist und
  einen echten GitHub-Login braucht

---

## Buchabgleich auf Kapitelebene — die Lücken

Erhoben am 27.09. aus dem Inhaltsverzeichnis des Manz-Buchs
(`pre.syp.itp.3jg/eBooks/SYP-Buch.Manz.Aufl_2013/`, Kapitel 00) gegen
`curriculum.yaml`. **Nichts davon ist umgesetzt** — Entscheidungsliste, keine
Aufgabenliste.

Ohne Modul und **nicht** als Non-Goal in `design.md` dokumentiert:

| Buch | Inhalt |
|---|---|
| K3 (S. 79–112) | Projektstart, Organisationsformen, Teambildung und -führung, internationale Teams |
| K4 (S. 113–138) | Projektstrukturpläne, Arbeitspakete und Verantwortungsmatrix, Zeitplanung |
| K5 (S. 139–182) | Risikomanagement, Projektcontrolling, Berichtswesen, Projektabschluss |
| K6.2 / K6.5 | Teams in der Software-Entwicklung, RUP |
| K8.4 / K8.6 | Interaktionsdiagramme (Sequenz), weitere Strukturdiagramme |
| K9 (S. 309–336) | Qualitätssicherung komplett — Qualitätsbegriff, konstruktive Maßnahmen, Testen, Testautomatisierung |
| K10.1 | Dokumentation (nur implizit über `asciidoctor-basics`) |

Gedeckt sind K1.1, K2 vollständig, K6.1/6.3/6.4, K7.1/7.2, K8.1/8.2/8.3/8.5,
K10.2. Aus K5 ist nur die Meilenstein-Trendanalyse angekommen, in
`governance-milestones`.

Bewusst und dokumentiert weggelassen: Schätzverfahren (D5), UML-Umfang (D4),
Pflichtenheft als Dokument (D2). „Teambildung" steht im U4-Plan der
Eröffnungssequenz in `design.md`, trägt aber kein Topic.

**Der Kern:** das Theoriebudget ist voll — 26 Slots, alle belegt. Jede Aufnahme
verlangt eine Streichung. Pro Lücke klären, ob sie nach jg4/jg5 gehört (dann als
Non-Goal in `design.md` festschreiben) oder einen Slot bekommt, und dann welches
Thema weicht. Größte Lücke ist K9.

---

## Offen

### Zuerst

1. `git push` in `curriculum-syp3` — 2 Commits liegen lokal
2. Die drei Punkte unten entscheiden
3. Erst dann L19

### Die drei Punkte aus dem Gespräch vom 27.09.

1. **Buchlücken** — Tabelle oben, Entscheidung je Lücke steht aus. Ein Abgleich
   *innerhalb* der gedeckten Kapitel ist nie gelaufen; der Sachfehler vom 12.09.
   (Kriterienkatalog) wäre nur beim seitenweisen Lesen aufgefallen. Die PDFs
   sind Scans ohne Textebene, lesbar nur seitenweise über das Read-Tool
2. **Gliederung** — zwei Auffälligkeiten, nicht entschieden:
   * `what-is-software-engineering` liegt auf L11, `process-models-overview`
     schon auf L8 und nennt es nicht in `requires` — die Begriffsklärung kommt
     nach ihrer Anwendung
   * in der Reserve springt die Nummerierung: `assessment-written-and-oral` und
     `minikube-deploy` liegen beide auf L27, der Theorieslot von L26 bleibt leer
3. **Diagramme gefälliger machen** — nicht angefangen. Befund: von 54
   PlantUML-Blöcken setzen nur 16 `skinparam defaultFontName Helvetica`, der Rest
   nicht, also uneinheitliche Typografie. Sonst durchgängig flache
   `rectangle`-Kästen mit zwei bis drei Zeilen Prosa, keine Rundungen, keine
   Formunterscheidung, Layout meist nur `-right->`-Ketten

### Ungeprüft geblieben

* Umlaute in `curriculum-syp3` selbst — in den beiden neuen Repositories
  hergestellt, hier nicht nachgesehen
* `student-project-template` inhaltlich: nur die Vorlagen angeglichen und der
  Build geprüft, der Rest nicht gelesen

### Braucht GitHub-Aktionen des Lehrenden

- `htl-leonding-example/jg03-syp-git-basics` anlegen, `assignment_template`
  eintragen, Check um „Repository existiert" erweitern
- Hinweis auf den jeweils anderen Katalog auf beiden Einstiegsseiten
- Übernahme geeigneter Fragen aus dem bestehenden Katalog mit Modulzuordnung

### Braucht Geräte oder Absprachen

- Rechte am Bild `vibe-coding-vs-software-engineering.jpeg` klären
- Offen: statt der eigenen ISO-25010-Zeichnung das Original von iso25000.com?
  Dann als `unclear` mit Begründung im Bildtitel
- `setup-tools.sh` auf echter Hardware, dann git-Tag 2026/27 in `klassen-setup`
- JDK-Version mit 4./5. Jahrgang abstimmen (`versions.env` trägt jetzt
  `25.0.4-tem`, vorher stand dort eine nicht existierende Kennung)
- Deployment-Diagramm und Kubernetes-Vertiefung mit 4./5. Jahrgang abstimmen
- `publish.sh` einmal gegen den Schulwebspace laufen lassen, zuerst `--dry-run`

---

## Stand der Module

L1–L18 geschrieben, je `index.adoc` + `exercises.adoc` + `questions.adoc` mit
sechs beantworteten Fragen und vier Aufgaben. Ausnahmen: `sdd-why-specs` und
`governance-stakeholders-goals` tragen sieben Fragen, `course-overview` keine.

| | Theorie | Praxis |
|---|---|---|
| L11 | *(war fertig)* | `ai-harness-engineering` |
| L12 | `sdd-openspec-artifacts` | `ai-agentic-loops` |
| L13 | `sdd-change-lifecycle` | `review-milestone-1` |
| L14 | `bridge-progress-and-milestones` | `docker-basics` |
| L15 | `sdd-specs-replace-requirements` | `docker-images` |
| L16 | `governance-estimation-hygiene` | `docker-volumes-config` |
| L17 | `governance-milestones` | `docker-multiarch` |
| L18 | `governance-acceptance` | `review-milestone-2` |

Die Linien, an denen die Module hängen:

* **Harness statt Prompt.** Drei der vier Teile um das Modell gehören dir;
  Berechtigungsstufen folgen der Umkehrbarkeit, nicht der Nützlichkeit.
* **Abbruchbedingung plus Budget.** Eine Schleife ohne Budget wird nicht
  gestartet; „grün durch Abriss" ist der Fehlschlag, der wie Erfolg aussieht.
* **`specs/` Gegenwart, `changes/` Delta.** Archivieren ist der einzige Übergang,
  der etwas außerhalb der Änderung verändert.
* **Kein Prozentsatz.** Fortschritt ist archivierte Capability je Charter-Ziel;
  was das Repository *nicht* zeigt, wird ausdrücklich benannt.
* **Meilenstein = Zeitpunkt plus prüfbare Bedingung plus Beobachter außerhalb
  des Teams.** Eine Phase kann man nicht verfehlen.
* **Schätzung ≠ Zusage.** Der stille Umbau der einen in die andere ist der
  Schaden; Bandbreite mit benannter Annahme statt Zahl.
* **Ein Image für alle Umgebungen.** Was getestet wurde, muss das sein, was
  läuft — daraus folgen Volumes und Laufzeitkonfiguration.
* **Abnahme ist ein Zeitpunkt**, die Kriterien stehen am Anfang, der Kunde sitzt
  an der Tastatur.
* **Ausgangslage, Ist-Zustand, Ziel, Anforderung** — eine Anforderung, deren
  Herkunft nicht bis zur Ausgangslage zurückreicht, ist jemandes Privatwunsch.
* **Ziele in drei Dimensionen.** Leistung, Termine, Kosten; im Schuljahr ist nur
  die Leistung wirklich verstellbar.
* *(neu)* **Eine ungeprüfte Anleitung ist eine Vermutung.** Was im Unterricht
  laufen soll, läuft vorher in CI — sonst steht die Klasse.

## Danach: L19–L28, 19 Module

```
L19  sdd-principle-not-tool          compose-basics
L20  process-waterfall               compose-multi-service
L21  process-scrum                   compose-networks-dependencies
L22  uml-overview                    revealjs-presentations
L23  uml-use-case                    ai-result-verification
L24  uml-class-object                review-milestone-3
L25  uml-activity                    ai-project-integration
L26  uml-state-overview              minikube-basics
L27  assessment-written-and-oral     minikube-deploy
L28  —                               minikube-services
```

Empfehlung: **Compose L19–L21 am Stück** (baut auf `docker-volumes-config` auf),
danach **UML L22–L26** als geschlossener Strang. `review-milestone-3` erst nach
`governance-milestones`. `process-waterfall` kann auf die Buchgliederung des
Pflichtenhefts aufsetzen — sie steht in `sdd-why-specs`.

## Die Site ist englisch

Alles Gerenderte ist übersetzt. **Die IDs bleiben deutsch** (`theorie`, `praxis`,
`vorgehen`, `werkzeuge`, `jg3`) — sie sind das Vokabular von `curriculum.yaml`,
der Prüfungen und der `data-`Attribute des Katalogfilters; Anzeigenamen stehen
daneben in `tools/curriculum.py`. Ein Unterricht heißt `L7`, nicht `U7`, nur in
der Ausgabe. Die deutschen Governance-Begriffe bleiben in den
`Terminology`-Tabellen. `test_site_output_is_english` prüft das, Suite **58
Tests**.

## Bild im AI-Kapitel

`modules/ai-basics-prompting/images/vibe-coding-vs-software-engineering.jpeg` —
**Rechtelage `unclear`**, einzige Zuordnung das Wasserzeichen
„@fromcodetocloud". `rights-report.py` meldet das in jedem Build, der Job endet
mit exit 1, ist `continue-on-error`, der Run bleibt grün. Die Meldung steht, bis
die Rechte geklärt sind.

`assets/` ist in `.gitignore`. Bilder gehören nach `modules/<id>/images/`, der
Modulkopf braucht `:imagesdir: images`.

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

Enthält der Antworttext selbst ein `====`-Beispiel, braucht der Antwortblock
einen längeren Begrenzer (`=====`). Ein Fall im Repository:
`asciidoctor-basics`, zweite Frage.

Diagrammnamen im Fragenkatalog beginnen mit `q-`. Diagrammkopf und Farbpalette
stehen in `templates/module/README.adoc` — blau eingefroren, grün fertig, sand
in Bewegung, rosa Risiko, lila Nebenschauplatz, grau Infrastruktur.

**Fallstrick:** in Aktivitätsdiagrammen scheitert `#Farbe:text;` in PlantUML
1.2026.8 mit „Error line" — auch ohne `<style>`-Block. Dort stehen die Klassen
`.key .work .ok .bad .aside .muted` im `<style>` und die Aktivität trägt sie als
Stereotyp: `:deploy to Pages; <<ok>>`.

Pflichtabschnitte: `Learning outcomes`, fachliche Abschnitte, `Decisions`,
`Pitfalls`, `Terminology`, `Further reading`. Ein leerer Pflichtabschnitt trägt
eine ausdrückliche Nullaussage.

`status: ready` erst setzen, wenn das Modul fertig ist. Probelauf:
`.venv/bin/python tools/check-curriculum.py --as-ready <topic-id>`.

## Verifikation

```bash
.venv/bin/python tools/check-curriculum.py    # 55 Themen, 36 ready, 0 Befunde
.venv/bin/python -m pytest tools/tests -q     # 58 passed
PYTHON=.venv/bin/python ./local-convert.sh    # build/site/index.html, exit 0
.venv/bin/python tools/rights-report.py       # 2 Bilder, own=1, unclear=1 → exit 1
```

In `klassen-setup` zusätzlich, ohne echte Hardware:

```bash
docker run --rm -v "$PWD:/mnt" koalaman/shellcheck:stable -S warning \
  setup-tools.sh setup-identity.sh
gh run list --limit 3          # der Drei-Läufe-Test auf echtem amd64
```

`chat.adoc` ist der private Notizblock des Lehrenden: nicht lesen, nicht
committen. Durchgesetzt über `.claude/settings.json` →
`permissions.deny: ["Read(./chat.adoc)"]`.
