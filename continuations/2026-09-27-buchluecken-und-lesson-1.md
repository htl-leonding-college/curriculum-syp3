# Continuation Prompt — Curriculum SYP 3. Jahrgang

**Stand:** 2026-09-27 · Plattform-Change **42/51**, Curriculum-Change **19/21**
**Site live:** https://htl-leonding-college.github.io/curriculum-syp3/
**Module:** L1–L18 vollständig — **36 von 55 Themen ready**, **199 Fragen**,
alle mit ausformulierter Antwort
**Git:** alles committet auf `main`, **nicht gepusht** — `origin/main` steht noch
auf `6626ca1`

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

## Am 2026-09-27 erledigt

### Der Arbeitsbaum vom 23.09. ist committet

Docker lief wieder, `./local-convert.sh` ist einmal vollständig durchgelaufen
(exit 0) — damit ist die seit dem 23.09. ausstehende Build-Prüfung erledigt.
Danach in drei Teilen committet:

```
caf71de docs: continuation prompt for the textbook alignment and the palette
5124862 feat(site): give the diagrams a semantic pastel palette      (66 Dateien)
6dece10 feat(curriculum): align the requirements modules with the textbook (7)
```

`chat.adoc` trägt weiter lokale Änderungen und bleibt absichtlich draußen.

### Lesson 1 trägt keine Aufgaben und Fragen mehr

`course-overview` ist der Organisationsteil und wird nicht geprüft. Entfernt
sind die zwei Aufgaben und die vier Prüfungsfragen; beide Dateien tragen jetzt
eine ausdrückliche Nullaussage mit Verweis auf die Module, die den Stoff
tatsächlich prüfen.

**Der Fallstrick dabei:** `check-curriculum.py` erzwingt bei `status: ready`,
dass jedes Lernziel eine Frage hat (Prüfung 7). Die drei `[[lo-N]]`-Lernziele im
`index.adoc` sind deshalb zu Prosa ohne Anker geworden — `OUTCOME_RE` in
`tools/adoc.py` greift nur auf `* [[id]] …`, damit ist die Prüfung still und der
Inhalt bleibt lesbar. Derselbe Weg gilt für jedes weitere Modul, das bewusst
keine Prüfungsfragen tragen soll. Für **Praxisthemen** geht das nicht: Prüfung 4
verlangt dort mindestens eine Frage, das ließe sich nur im Werkzeug lockern.

### Der Live-USB-Test ist ersatzlos entfallen

Entscheidung des Lehrenden: einen Ubuntu-Stick im Vorfeld erstellen zu lassen ist
nicht sinnvoll, weil es zu wenige tun — die Maßnahme entfaltet ihre Wirkung
ohnehin nicht. Entfernt aus `learning-environment-setup` in Text, Diagramm,
Decisions, Pitfalls, Prüfungsfrage und Aufgabe. Das Aktivitätsdiagramm
`setup-order` hat jetzt die Checkliste als Tor statt des Probestarts; die Aufgabe
heißt „Check your machine against the checklist".

**Mitgezogen wurde die Planungsebene** — sonst widerspricht der Entwurf dem
Modul:

* `design.md` D7 — der Absatz *Überbrückung statt Fallback* ist ersetzt durch
  „Kein vorgeschalteter Live-USB-Test" samt **ausdrücklich angenommenem
  Restrisiko**: ein Gerät, dessen WLAN- oder Grafikchip unter Linux nicht läuft,
  fällt erst nach dem Partitionieren auf. Getragen wird das von der
  Hardware-Checkliste, dem Troubleshooting-Puffer in U2 und der bestehen
  bleibenden Windows-Partition
* `design.md` — U1-Ablauf, U1-Hausübung und die Risikotabelle nachgezogen
* `proposal.md` und `tasks.md` 3.2 nachgezogen
* `specs/curriculum/lernumgebung/spec.md` — das SHALL „nachgewiesen …, dass das
  Gerät das Zielsystem startet" heißt jetzt „Hardware-Checkliste vollständig
  abgearbeitet". Szenario *Gerät startet das Zielsystem nicht* ersetzt durch
  *Ein Punkt der Checkliste ist offen*, dazu ein drittes Szenario, das das
  Restrisiko benennt

Die archivierten Continuations nennen D7 noch in der alten Fassung. Das bleibt
so — sie sind Protokoll, nicht Vorgabe.

---

## Buchabgleich auf Kapitelebene — die Lücken

Neu erhoben am 27.09. aus dem Inhaltsverzeichnis des Manz-Buchs
(`pre.syp.itp.3jg/eBooks/SYP-Buch.Manz.Aufl_2013/`, Kapitel 00) gegen
`curriculum.yaml`. **Nichts davon ist umgesetzt** — es ist eine
Entscheidungsliste, keine Aufgabenliste.

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

Bewusst und dokumentiert weggelassen sind dagegen: Schätzverfahren (D5),
UML-Umfang (D4), das Pflichtenheft als Dokument (D2). „Teambildung" steht im
U4-Plan der Eröffnungssequenz in `design.md`, trägt aber kein Topic.

**Der Kern der Entscheidung:** das Theoriebudget ist voll — 26 Slots, alle
belegt. Jede Aufnahme verlangt eine Streichung. Pro Lücke ist also zu klären, ob
sie nach jg4/jg5 gehört — dann als Non-Goal in `design.md` festschreiben — oder
einen Slot bekommt, und dann welches Thema weicht. Die größte Lücke ist K9.

---

## Offen aus dem Gespräch vom 27.09.

Der Lehrende wollte drei Dinge durchgehen. Erledigt ist keines davon
vollständig:

1. **Buchabgleich** — auf Kapitelebene erhoben (oben), Entscheidung je Lücke
   steht aus. Ein Abgleich *innerhalb* der gedeckten Kapitel ist nicht gelaufen;
   der am 12.09. gefundene Sachfehler (Kriterienkatalog) zeigt, dass so etwas
   nur beim seitenweisen Lesen auffällt. Die PDFs sind Scans ohne Textebene
2. **Gliederung** — zwei Auffälligkeiten notiert, nicht entschieden:
   * `what-is-software-engineering` liegt auf L11, `process-models-overview`
     schon auf L8 und nennt es nicht in `requires` — die Begriffsklärung kommt
     nach ihrer Anwendung
   * in der Reserve springt die Nummerierung: `assessment-written-and-oral` und
     `minikube-deploy` liegen beide auf L27, der Theorieslot von L26 bleibt leer
3. **Diagramme gefälliger machen** — nicht angefangen. Befund: von 54
   PlantUML-Blöcken setzen nur 16 `skinparam defaultFontName Helvetica`, der Rest
   nicht, also uneinheitliche Typografie auf der Site. Sonst durchgängig flache
   `rectangle`-Kästen mit zwei bis drei Zeilen Prosa, keine Rundungen, keine
   Formunterscheidung, Layout meist nur `-right->`-Ketten

---

## Stand der Module

L1–L18 sind geschrieben, je `index.adoc` + `exercises.adoc` + `questions.adoc`
mit sechs beantworteten Fragen und vier Aufgaben. Ausnahmen: `sdd-why-specs` und
`governance-stakeholders-goals` tragen sieben Fragen, `course-overview` seit dem
27.09. keine.

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

Die Linien, an denen die Module hängen — falls später etwas angepasst wird, sind
das die Aussagen, die tragen:

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
  die Leistung wirklich verstellbar, alles andere verstellt still die Qualität.

## Die Site ist englisch

Alles, was gerendert wird, ist übersetzt — Navigation, Mindmap, Umfangstabellen,
Fragenkatalog, Startseite und der Aufklapp-Schalter im docinfo.

* **Die IDs bleiben deutsch.** `theorie`, `praxis`, `vorgehen`, `werkzeuge`,
  `jg3` sind das Vokabular von `curriculum.yaml`, der Prüfungen und der
  `data-`Attribute, auf die der Katalogfilter filtert. Danebengestellt sind
  Anzeigenamen in `tools/curriculum.py`: `kind_label`, `lesson_label`,
  `year_label`.
* **Ein Unterricht heißt `L7`**, nicht `U7`. Nur in der erzeugten Ausgabe.
* **Die deutschen Governance-Begriffe bleiben**, in den `Terminology`-Tabellen.
  Formulare und Diplomarbeit heißen weiter Lastenheft und Pflichtenheft; dazu
  Ist-Zustand, Mengengerüst, Kriterienkatalog, Ergebnis- und Vorgehensziel,
  Zielkonkurrenz.
* `test_site_output_is_english` prüft die gerenderte Ausgabe gegen die deutschen
  Wörter. Suite **58 Tests**.

## Bild im AI-Kapitel

`modules/ai-basics-prompting/images/vibe-coding-vs-software-engineering.jpeg`,
Abschnitt `== What this chapter is about`. **Rechtelage `unclear`** — einzige
Zuordnung ist das Wasserzeichen „@fromcodetocloud", Urheber nicht kontaktiert.

`rights-report.py` meldet das in jedem Build; der Job `Bildrechte melden` endet
mit exit 1, ist `continue-on-error`, der Run bleibt grün. **Die Meldung steht,
bis die Rechte geklärt sind.**

`assets/` ist in `.gitignore` (Arbeitsmaterial mit personenbezogenen Daten).
Bilder gehören nach `modules/<id>/images/`, der Modulkopf braucht dann
`:imagesdir: images`.

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
einen längeren Begrenzer (`=====`) — sonst „unterminated listing block".
Ein Fall im Repository: `asciidoctor-basics`, zweite Frage.

Diagrammnamen im Fragenkatalog beginnen mit `q-`, damit sie nicht mit denen aus
`index.adoc` kollidieren. Diagrammkopf und Farbpalette stehen in
`templates/module/README.adoc`. Die Palette ist semantisch: blau eingefroren,
grün fertig, sand in Bewegung, rosa Risiko, lila Nebenschauplatz, grau
Infrastruktur.

**Fallstrick, der Zeit kostet:** in Aktivitätsdiagrammen scheitert
`#Farbe:text;` in PlantUML 1.2026.8 mit „Error line" — auch ohne
`<style>`-Block. Dort stehen die Klassen `.key .work .ok .bad .aside .muted` im
`<style>` und die Aktivität trägt sie als Stereotyp: `:deploy to Pages; <<ok>>`.

Pflichtabschnitte: `Learning outcomes`, fachliche Abschnitte, `Decisions`,
`Pitfalls`, `Terminology`, `Further reading`. Ein leerer Pflichtabschnitt trägt
eine ausdrückliche Nullaussage. Jedes Lernziel braucht mindestens eine Frage —
`check-curriculum.py` prüft das in beide Richtungen.

`status: ready` erst setzen, wenn das Modul fertig ist. Probelauf:
`.venv/bin/python tools/check-curriculum.py --as-ready <topic-id>`.

## Verifikation

```bash
.venv/bin/python tools/check-curriculum.py    # 55 Themen, 36 ready, 0 Befunde
.venv/bin/python -m pytest tools/tests -q     # 58 passed
PYTHON=.venv/bin/python ./local-convert.sh    # build/site/index.html, exit 0
.venv/bin/python tools/rights-report.py       # 2 Bilder, own=1, unclear=1 → exit 1
```

Alle vier am 27.09. gelaufen.

## Was aussteht

### Zuerst

1. `git push` — `origin/main` steht noch auf `6626ca1`, drei Commits liegen lokal
2. Die drei offenen Punkte oben entscheiden: Buchlücken, Gliederung, Diagramme
3. Erst dann L19

### Danach: L19–L28, 19 Module

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

Empfehlung: **Compose L19–L21 am Stück** (baut direkt auf
`docker-volumes-config` auf), danach **UML L22–L26** als geschlossener Strang,
damit die Querverweise in einem Zug stimmen. `review-milestone-3` erst nach
`governance-milestones` lesen — die Trendanalyse kommt von dort.

`process-waterfall` (L20) kann auf die Buchgliederung des Pflichtenhefts
aufsetzen — sie steht in `sdd-why-specs` und muss dort nicht wiederholt werden.

### Braucht GitHub-Aktionen des Lehrenden

- `klassen-setup` und `student-project-template` als Repos anlegen und pushen
- `htl-leonding-example/jg03-syp-git-basics` anlegen, `assignment_template`
  eintragen, Check um „Repository existiert" erweitern
- Hinweis auf den jeweils anderen Katalog auf beiden Einstiegsseiten
- Übernahme geeigneter Fragen aus dem bestehenden Katalog mit Modulzuordnung

### Braucht Geräte oder Absprachen

- Rechte am Bild `vibe-coding-vs-software-engineering.jpeg` klären
- Offen: soll statt der eigenen ISO-25010-Zeichnung das Original von
  iso25000.com hinein? Dann als `unclear` mit Begründung im Bildtitel
- `setup-tools.sh` auf frischem Ubuntu 26.04 und auf macOS, dann git-Tag 2026/27
- JDK-Version mit 4./5. Jahrgang abstimmen (`versions.env` trägt `25.0.1-tem`)
- Deployment-Diagramm und Kubernetes-Vertiefung mit 4./5. Jahrgang abstimmen
- `publish.sh` einmal gegen den Schulwebspace laufen lassen, zuerst `--dry-run`
