# Continuation Prompt — Curriculum SYP 3. Jahrgang

**Stand:** 2026-09-23 · Plattform-Change **42/51**, Curriculum-Change **19/21**
**Site live:** https://htl-leonding-college.github.io/curriculum-syp3/
**Module:** L1–L18 vollständig — **36 von 55 Themen ready**, **203 Fragen**,
alle mit ausformulierter Antwort
**Git:** 74 Dateien geändert, **nichts committet**, `main` == `origin/main`

> Löst `2026-09-12-buchabgleich-pflichtenheft-und-ziele.md` ab. Ältere liegen in
> `continuations/archiv/`.

---

## Einstieg

```
/opsx:apply setup-curriculum-repository
```

Struktur steht in `curriculum.yaml` (55 Themen), Entscheidungen in
`openspec/changes/*/design.md`, Abdeckung in
`openspec/changes/define-syp3-curriculum/coverage.md`.

---

## Am 2026-09-23 erledigt

Zwei Dinge: der Buchabgleich vom 12.09. ist umgesetzt, und alle Grafiken sind
von Graustufen auf Pastell umgestellt. **Alles im Arbeitsbaum, nichts
committet** — das ist der erste Schritt der nächsten Sitzung.

### Buchabgleich (die vier offenen Punkte, alle beantwortet)

Der Lehrende hat entschieden:

* **Stakeholder nur kurz** — Definition, Beispiele, intern/extern, und der
  Hinweis, dass jeder Stakeholder eigene Interessen verfolgt. Das Raster
  *Interesse × Einfluss* ist damit erledigt: es ist aus dem Modul entfernt,
  ebenso die Quadranten-Frage. Das Raster des Buches (Macht ×
  Konfliktpotenzial) wird **nicht** übernommen — die Frage ist abgeschlossen
* **Nur die Buchgliederung** des Pflichtenhefts. Balzert mit `/F10/`, `/D10/`,
  `/Q10/` ist ersatzlos raus. Das didaktisch tragende Argument — eine
  Anforderung muss referenzierbar sein — bleibt, jetzt ohne das Schema
* Kriterienkatalog, `governance-stakeholders-goals` und `projektauftrag.adoc`
  wie am 12.09. vorgeschlagen

`modules/sdd-why-specs/`:

* sieben Kapitel nach dem Buch, mit der Kette *Ausgangslage → Ist-Zustand →
  Zielsetzung → Anforderungen* als Leseschlüssel
* funktional / nichtfunktional ausdrücklich in Kapitel 4
* **ISO/IEC 25010 neu** als Katalog der nichtfunktionalen Merkmale: neun
  Merkmale mit Untermerkmalen als 3×3-Raster, nach Gruppen sortiert
  (Nutzungssicht / Verhalten und Schutz / Entwicklersicht). Mit dem Hinweis auf
  2011 → 2023: Usability wurde Interaction capability, Portability wurde
  Flexibility plus scalability, Safety kam dazu. Verlinkt sind der
  Monterail-Artikel und iso25000.com
* **Kriterienkatalog** als eigener Abschnitt mit der richtigen Rolle, plus
  WARNING gegen die verbreitete Falschzuordnung
* neues Lernziel `lo-6` und eine neue Prüfungsfrage dazu

`modules/governance-stakeholders-goals/`:

* Stakeholder kurz, Definition nach ÖNORM ISO 21500 inklusive „hält sich für
  betroffen", intern/extern-Tabelle, Beispiele mit dem jeweiligen Interesse
* neu: Leistung / Termine / Kosten (mit Diagramm), Ergebnis- gegen
  Vorgehensziele, Coverdale-Vierer (WOZU / FÜR WEN / ENDERGEBNIS /
  ERFOLGSKRITERIEN), Zielbeziehungen, Teilziele mit Gewichtung
* `lo-4` bis `lo-6` mit je einer Frage, zwei neue Aufgaben

`templates/governance/`:

* `projektauftrag.adoc` — **Ist-Zustand** und **Mengengerüst** ergänzt,
  Zieltabelle um Art (E / V) und Priorität, Zeile für Zielkonkurrenz,
  Stakeholder-Tabelle auf intern/extern plus Interesse umgestellt
* `antragsfelder-und-openspec.adoc` — zwei Mapping-Zeilen dazu: Ist-Zustand
  nach `config.yaml → context:`, Mengengerüst als nichtfunktionales Requirement

### Bild im ISO-Kapitel

Der Lehrende hat ein Bild von monterail bzw. iso25000.com gewünscht. Beide sind
urheberrechtlich geschützt und wären als `unclear` in `rights-report.py`
gelandet. Stattdessen steht dort eine **eigene PlantUML-Nachzeichnung**, die
Merkmalsnamen nach iso25000.com, Quelle im Text genannt — bleibt `own`. Falls
das Original doch gewünscht ist, ist das offen.

### Alle Grafiken auf Pastell

79 Diagramme: 56 PlantUML, 22 Graphviz, dazu die generierte Stoffstruktur.
`skinparam monochrome true` ist überall ersetzt durch:

```
<style>
element { BackgroundColor #EDF3FA; LineColor #7C93AD; FontColor #21303F }
arrow { LineColor #5A6B7D; FontColor #21303F }
</style>
skinparam shadowing false
```

Die Palette ist **semantisch, nicht dekorativ** — sie steht mit ihrer Bedeutung
in `templates/module/README.adoc`:

| Farbe | Hex | Rolle |
|---|---|---|
| blau | `#E3ECF8` | eingefroren, vorgegeben, Ausgangspunkt |
| grün | `#E4F0E4` | Ergebnis, fertig, der gute Weg |
| sand | `#FAF0D9` | Arbeit in Bewegung, was sich oft ändert |
| rosa | `#F8E5E5` | Risiko, Fehlerfall, der schlechte Weg |
| lila | `#ECE6F7` | Nebenschauplatz, Werkzeug, Ablage |
| grau | `#F0F2F5` | Infrastruktur, Kontext, nicht deins |

Eine Box: `rectangle "image" as I #E3ECF8`.

**Fallstrick, der Zeit kostet:** in Aktivitätsdiagrammen scheitert
`#Farbe:text;` in PlantUML 1.2026.8 mit „Error line" — auch ohne
`<style>`-Block. Dort stehen die Klassen `.key .work .ok .bad .aside .muted` im
`<style>` und die Aktivität trägt sie als Stereotyp: `:deploy to Pages; <<ok>>`.
Für Graphviz gilt dieselbe Palette über `node [fillcolor="#EDF3FA",
color="#7C93AD"]`.

Mindmaps tragen die Blockfarbe jetzt bis auf die Themenebene;
`tools/gen-mindmap.py` führt dieselbe Palette (lightblue/plum/peachpuff sind
raus), `test_mindmap_groups_topics_by_theme` prüft das neue Format.

---

## Stand der Module

L1–L18 sind geschrieben, je `index.adoc` + `exercises.adoc` + `questions.adoc`
mit sechs beantworteten Fragen und vier Aufgaben. `sdd-why-specs` und
`governance-stakeholders-goals` tragen nach dem Umbau sieben Fragen.

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
  jetzt Ist-Zustand, Mengengerüst, Kriterienkatalog, Ergebnis- und
  Vorgehensziel, Zielkonkurrenz.
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

## Arbeitsstand im Git

**74 geänderte Dateien im Arbeitsbaum, nichts committet.** Letzter Commit ist
weiterhin:

```
6626ca1 docs: continuation prompt for the English site and lessons 11 to 18
```

Sinnvolle Aufteilung beim Committen: der Buchabgleich (`sdd-why-specs`,
`governance-stakeholders-goals`, beide Templates) und die Farbumstellung (alle
übrigen Module, `tools/gen-mindmap.py`, `tools/tests/`,
`templates/module/README.adoc`) sind zwei verschiedene Commits.

`chat.adoc` trägt lokale Änderungen (der laufende Prompt) und ist absichtlich
nicht committet.

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
`templates/module/README.adoc`.

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
PYTHON=.venv/bin/python ./local-convert.sh    # build/site/index.html
.venv/bin/python tools/rights-report.py       # 2 Bilder, own=1, unclear=1 → exit 1
```

**Der Site-Build ist seit dem 23.09. nicht gelaufen — der Docker-Daemon war
aus** („Cannot connect to the Docker daemon"). Die Diagramme wurden stattdessen
einzeln mit dem lokalen `plantuml` (1.2026.8) und `dot` gerendert: 79 von 79
ohne Syntaxfehler. `asciidoctor` lokal über alle geänderten Dateien: keine
Warnung. **Der vollständige Build steht als Prüfung noch aus** — das ist das
Erste, sobald Docker läuft.

## Was aussteht

### Zuerst

1. Docker starten, `./local-convert.sh` einmal vollständig durchlaufen lassen
2. Committen, in den zwei oben genannten Teilen
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

`process-waterfall` (L20) kann jetzt auf die Buchgliederung des Pflichtenhefts
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
