# Continuation Prompt — Curriculum SYP 3. Jahrgang

**Stand:** 2026-09-12 · Plattform-Change **42/51**, Curriculum-Change **19/21**
**Site live:** https://htl-leonding-college.github.io/curriculum-syp3/
**Module:** L1–L18 vollständig — **36 von 55 Themen ready**, **200 Fragen**,
alle mit ausformulierter Antwort
**Git:** unverändert seit 09.09., `main` == `origin/main`, nur `chat.adoc` lokal

> Löst `2026-09-09-englische-site-und-module-u11-u18.md` ab. Ältere liegen in
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

## Am 2026-09-12: Abgleich mit dem Schulbuch

Die Sitzung hat nichts geschrieben, sondern geprüft. Ergebnis sind zwei Befunde
und eine offene Entscheidung. **Nichts davon ist umgesetzt** — das ist der
nächste inhaltliche Schritt, vor L19.

Quelle ist das Manz-Buch in
`pre.syp.itp.3jg/eBooks/SYP-Buch.Manz.Aufl_2013/`, gelesen wurden
Kapitel 7 Lerneinheit 2 „Das Pflichtenheft" (S. 245–249) und Kapitel 2
Lerneinheit 3 „Zielbestimmung" (S. 54–57). Die PDFs sind Scans ohne Textebene,
lesbar nur seitenweise über das Read-Tool.

### Befund 1: Die Gliederung in `sdd-why-specs` ist Balzert, nicht das Buch

Die Pflichtenheft-Gliederung im Modul stammt aus Helmut Balzert, *Lehrbuch der
Software-Technik* — erkennbar am Nummernschema `/F10/`, `/D10/`, `/L10/`,
`/Q10/`. Sie ist inhaltlich in Ordnung und in deutschsprachiger SE-Literatur
Standard, **steht aber ohne Quellenangabe im Modul**. Das ist zu ergänzen.

### Befund 2: Muss-, Wunsch- und Abgrenzungskriterien sind falsch zugeordnet

Das Modul schreibt sie der *Zielbestimmung* zu. Das ist Balzert. **Im Buch
gehören sie zum Kriterienkatalog** (S. 246): einem *internen* Papier des
Auftraggebers, parallel zum Pflichtenheft erstellt, Zweck ist die Evaluation
eingehender Offerten.

* Muss- oder K.o.-Kriterien — Nichterfüllung führt zum Ausscheiden des Angebots
* Wunschkriterien (Soll-Kriterien) — bessere Erfüllung verbessert die Bewertung
* Abgrenzungskriterien — informativ, erleichtern dem Anbieter die Dimensionierung

Anderes Dokument, anderer Adressat. Sachlicher Fehler, muss korrigiert werden.

### Die Buchgliederung des Pflichtenhefts (S. 247–248)

1. **Beschreibung der Ausgangslage** — Unternehmensart und -größe, Standorte,
   Produkt- und Dienstleistungspalette, Kundenstruktur, IT-Organisation, Gründe
   für die Beschaffung
2. **Ist-Zustand** — nur die projektrelevanten Bereiche: Aufbauorganisation,
   Ablauforganisation mit Geschäftsprozessen und eingesetzten Applikationen,
   bestehende Systemplattform
3. **Zielsetzung** — Ziele mit Prioritäten, realistisch und überprüfbar. Arten:
   nutzenrelevante Ziele, Systemziele, Vorgehensziele
4. **Anforderungen (Soll)** — an die Applikationssoftware, an die
   Systemplattform, anbieterbezogen
5. **Mengengerüst** — Datenbewegungen, Datenbestände, Anzahl gleichzeitiger
   Benutzer
6. **Aufbau und Inhalt der Offerte** — nur bei einer Ausschreibung
7. **Administratives** — Vertraulichkeit, Copyright, Verteiler, Budgetrahmen,
   Termine

Innerhalb von Kapitel 4 liegt die Achse **funktional / nichtfunktional**:
fachlicher Ablauf und Datenfelder funktional; Effizienz, Leistung,
Zuverlässigkeit, Robustheit, Benutzerfreundlichkeit, Datenschutz
nichtfunktional. Das Buch benennt die Achse nicht, macht sie aber auf. Sie
ausdrücklich zu machen ist eine Verbesserung, keine Verfälschung.

### Beschlossener Umbau von `sdd-why-specs` (L9)

* **Variante A, primär: die Buchgliederung**, sieben Kapitel, mit
  funktional/nichtfunktional als ausdrücklicher Achse in Kapitel 4
* **Variante B: Balzert**, als zweite gebräuchliche Gliederung, *mit*
  Quellennennung. Das `/F10/`-Schema trägt didaktisch — Referenzierbarkeit einer
  Anforderung ist genau der Job einer Spec-ID — und bleibt deshalb drin
* **Kriterienkatalog** als eigener Abschnitt mit der richtigen Rolle
* Mapping-Tabelle auf openspec erweitern: `Ausgangslage`, `Ist-Zustand` und
  `Mengengerüst` haben bei uns **bisher keine Entsprechung**. Ist-Zustand und
  Mengengerüst fehlen in `templates/governance/projektauftrag.adoc` vollständig

### Nachzutragen in `governance-stakeholders-goals` (L5)

Aus Kapitel 2 Lerneinheit 3, was das Modul nicht hat:

* Ziele hinsichtlich **Leistung (Umfang und Qualität), Termine, Kosten**
* **Ergebnisziele gegen Vorgehensziele**
* **Coverdale-Vierer** der Zielvereinbarung: WOZU? / FÜR WEN? / ENDERGEBNIS? /
  ERFOLGSKRITERIEN? — didaktisch der stärkste Teil des Kapitels
* **Zielbeziehungen**: Zielkonkurrenz, Zielkomplementarität, Zielneutralität
* Teilziele, hierarchisch zerlegt; Gewichtung über Nutzwertanalyse — schließt an
  `governance-weighted-scoring` an

### Offene Entscheidung: das Stakeholder-Raster

Das Modul benutzt **Interesse × Einfluss** (Standard-Raster des
Projektmanagements). Das Buch benutzt auf S. 63 **Macht × Konfliktpotenzial**,
mit Stakeholder-Definition nach ÖNORM ISO 21500:2012, Unterscheidung intern und
extern und einer dreischrittigen Stakeholderanalyse.

Zwei verschiedene Raster. **Offen: auf das Buch umstellen oder beide zeigen?**
Diese Frage ist an den Lehrenden gestellt und noch nicht beantwortet — vor dem
Umbau von L5 klären.

### Rechtslage

Unkritisch, solange es bei Aufzählungen und eigenen Formulierungen bleibt. Keine
Abbildungen, keine Seitenkopien, keine Übungen aus dem Buch — so steht es auch
in `chat.adoc`.

---

## Stand der Module

L1–L18 sind geschrieben, je `index.adoc` + `exercises.adoc` + `questions.adoc`
mit sechs beantworteten Fragen und vier Aufgaben.

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

## Die Site ist englisch

Alles, was gerendert wird, ist übersetzt — Navigation, Mindmap, Umfangstabellen,
Fragenkatalog, Startseite und der Aufklapp-Schalter im docinfo.

* **Die IDs bleiben deutsch.** `theorie`, `praxis`, `vorgehen`, `werkzeuge`,
  `jg3` sind das Vokabular von `curriculum.yaml`, der Prüfungen und der
  `data-`Attribute, auf die der Katalogfilter filtert. Danebengestellt sind
  Anzeigenamen in `tools/curriculum.py`: `kind_label`, `lesson_label`,
  `year_label`. Ein Auswahlfeld zeigt „Project governance" und „Practice", der
  Wert bleibt `governance` und `praxis`.
* **Ein Unterricht heißt `L7`**, nicht `U7`. Nur in der erzeugten Ausgabe.
* **Die deutschen Governance-Begriffe bleiben**, in den `Terminology`-Tabellen.
  Formulare und Diplomarbeit heißen weiter Lastenheft und Pflichtenheft.
* `test_site_output_is_english` prüft die gerenderte Ausgabe gegen die deutschen
  Wörter. Suite **58 Tests**.

## Bild im AI-Kapitel

`modules/ai-basics-prompting/images/vibe-coding-vs-software-engineering.jpeg`,
Abschnitt `== What this chapter is about` vor `== What the thing actually does`.
**Rechtelage `unclear`** — einzige Zuordnung ist das Wasserzeichen
„@fromcodetocloud", Urheber nicht kontaktiert.

`rights-report.py` meldet das in jedem Build; der Job `Bildrechte melden` endet
mit exit 1, ist `continue-on-error`, der Run bleibt grün. **Die Meldung steht,
bis die Rechte geklärt sind.**

`assets/` ist in `.gitignore` (Arbeitsmaterial mit personenbezogenen Daten).
Bilder gehören nach `modules/<id>/images/`, der Modulkopf braucht dann
`:imagesdir: images`.

## Arbeitsstand im Git

Alles auf **`main`**, gepusht, Pipeline grün (Run 34323413795).

```
6626ca1 docs: continuation prompt for the English site and lessons 11 to 18
211ec17 feat(curriculum): write the modules of lessons 16 to 18
afa9e6c feat(curriculum): write the container start and the specs module of lessons 14 and 15
fdc7f43 feat(curriculum): write the milestone and life-cycle modules of lessons 13 and 14
a51007c feat(curriculum): write the AI and SDD modules of lessons 11 and 12
3bd9bb8 feat(site): publish the site in English
8b1919d feat(ai-basics): open the AI chapter with the rocket picture
```

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
`index.adoc` kollidieren.

Pflichtabschnitte: `Learning outcomes`, fachliche Abschnitte, `Decisions`,
`Pitfalls`, `Terminology`, `Further reading`. Ein leerer Pflichtabschnitt trägt
eine ausdrückliche Nullaussage.

`status: ready` erst setzen, wenn das Modul fertig ist. Probelauf:
`.venv/bin/python tools/check-curriculum.py --as-ready <topic-id>`.

## Verifikation

```bash
.venv/bin/python tools/check-curriculum.py    # 55 Themen, 36 ready, 0 Befunde
.venv/bin/python -m pytest tools/tests -q     # 58 passed
PYTHON=.venv/bin/python ./local-convert.sh    # build/site/index.html
.venv/bin/python tools/rights-report.py       # 2 Bilder, own=1, unclear=1 → exit 1
```

## Was aussteht

### Zuerst: der Buchabgleich von oben

`sdd-why-specs` umbauen, `governance-stakeholders-goals` ergänzen,
`projektauftrag.adoc` um Ist-Zustand und Mengengerüst erweitern. Vorher die
offene Frage zum Stakeholder-Raster klären.

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

### Braucht GitHub-Aktionen des Lehrenden

- `klassen-setup` und `student-project-template` als Repos anlegen und pushen
- `htl-leonding-example/jg03-syp-git-basics` anlegen, `assignment_template`
  eintragen, Check um „Repository existiert" erweitern
- Hinweis auf den jeweils anderen Katalog auf beiden Einstiegsseiten
- Übernahme geeigneter Fragen aus dem bestehenden Katalog mit Modulzuordnung

### Braucht Geräte oder Absprachen

- Stakeholder-Raster: Buch (Macht × Konfliktpotenzial) oder beide Raster?
- Rechte am Bild `vibe-coding-vs-software-engineering.jpeg` klären
- `setup-tools.sh` auf frischem Ubuntu 26.04 und auf macOS, dann git-Tag 2026/27
- JDK-Version mit 4./5. Jahrgang abstimmen (`versions.env` trägt `25.0.1-tem`)
- Deployment-Diagramm und Kubernetes-Vertiefung mit 4./5. Jahrgang abstimmen
- `publish.sh` einmal gegen den Schulwebspace laufen lassen, zuerst `--dry-run`
