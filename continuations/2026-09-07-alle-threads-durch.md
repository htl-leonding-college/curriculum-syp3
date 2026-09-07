# Continuation Prompt — Curriculum SYP 3. Jahrgang

**Stand:** 2026-09-07 · Threads 1, 2, 4 und 5 abgeschlossen · Specs beider Changes
geschrieben · `curriculum.yaml` befüllt
**Repo:** `curriculum-syp3` · **Changes:** `define-syp3-curriculum`, `setup-curriculum-repository`

> Löst `2026-09-06-thread-5-abgeschlossen.md` ab. Die älteren bleiben als Historie liegen.

---

## Einstieg

```
/opsx:explore
```

Dann diesen Prompt einfügen:

> Wir arbeiten am Curriculum für SYP (SYPPRE), 3. Jahrgang, HTL Informatik,
> Unterrichtssprache Englisch. Die Entscheidungen stehen in
> `openspec/changes/define-syp3-curriculum/{proposal,design}.md` (Inhalt),
> `openspec/changes/setup-curriculum-repository/{proposal,design}.md` (Plattform)
> und den Specs beider Changes unter `openspec/changes/*/specs/`. Die Stoffstruktur
> liegt in `curriculum.yaml` (54 Themen, U1–U28 belegt). Lies das, bevor du antwortest,
> und frage nicht nach Fakten, die dort stehen. Der ursprüngliche Auftrag liegt in
> `chat.adoc`.
> Alle inhaltlichen Threads sind durch. Als Nächstes: **Ablage des Repositories auf
> GitHub**, danach `tasks.md`, `tools/check-curriculum.*` und die ersten Module.

---

## Rolle und Kontext

Der Nutzer ist Lehrer an der HTL Leonding und unterrichtet SYP im 3. Jahrgang auf
Englisch. Er strukturiert seine Stoffinhalte neu und will sie online präsentieren.

Bestehende Infrastruktur:

- Hugo-Website auf dem Schulwebspace
  (`edufs.edu.htl-leonding.ac.at/~t.stuetz/hugo/`) — bleibt vorerst unangetastet,
  enthält Altdaten früherer Projekte
- Mitschriften als AsciiDoc auf GitHub Pages, nach Unterrichtsdatum gegliedert:
  `2526-3bhif-syp.github.io/2526-3bhif-syp-lecture-notes/`,
  `2425-3ahif-syp.github.io/2425-3ahif-syp-lecture-notes/`,
  `2425-3ahitm-itp.github.io/2425-3ahitm-itp-lecture-notes/` (ITP = dasselbe wie SYP,
  weniger UE). 20–31 Kapitel je Schuljahr, stichpunktdicht, 15–25 % Diagramme,
  Diagramme durchwegs als exportierte Bilder ohne Quelltext.
- Personenbezogene Daten (Testergebnisse) in Moodle
- Assignments und Tests über GitHub Classroom, künftig „classroom 50"
- Schülerprojekte in GitHub
- Fragenkatalog: `htl-leonding-college.github.io/fragenkatalog` — gehört ihm allein,
  öffentlich zur Mitbenutzung durch Kollegen. **Bleibt unangetastet**; ein neuer
  Katalog wird generiert aufgebaut (P8).

Materialbestand unter `/Users/stuetz/SynologyDrive/htl/skripten/pre.syp.itp.3jg/`:
Manz-Schulbuch als PDF-Kapitel (`eBooks/SYP-Buch.Manz.Aufl_2013/`), UML-Skripten
Uni Heidelberg (`uml/Uni Heidelberg/UML1.1/`), `01.Vorgehensmodelle.key`,
`PUMA8_12_Kreativitätstechniken.pdf`, `PUMA8_05_Nutzwertanalyse.pdf`,
`PUMA Netzplantechnik/`.

`assets/` enthält zwei Screenshots des Diplomarbeitsantrags mit echten Schülernamen.
Behalten, aber in `.gitignore` — gehört **nicht** ins Repository. Die Feldstruktur des
Antrags ist in `define-syp3-curriculum/design.md` (D2) festgehalten.

---

## Arbeitsweise (verbindlich)

- **Nichts erstellen ohne vorherige Zustimmung.** Gilt für Dateien und
  OpenSpec-Artefakte gleichermaßen. Vorher benennen, was angelegt würde, dann fragen.
- **Explore-Modus ist Denkarbeit, keine Umsetzung.**
- **Diagramme bevorzugt PlantUML**, Stoffstruktur als `@startmindmap`.
- **Planungsartefakte auf Deutsch, Lernressourcen auf Englisch.** In den Specs bleiben
  SHALL/MUST und WHEN/THEN englisch, der Rest ist deutsch.
- **Eine fokussierte Frage pro Runde**, nicht mehrere parallel.
- Annahmen kennzeichnen, Alternativen mit Begründung verwerfen, nicht nur aufzählen.
- Keine personenbezogenen Daten ins Repository.

---

## Was entschieden ist

### Thread 1 — Inhalt (`define-syp3-curriculum`, D1–D11)

| | Entscheidung |
|---|---|
| D1 | Zweiteilung: Governance (außen, verpflichtend, vorgehensmodell-neutral) ↔ Durchführung (innen, SDD) |
| D2 | `specs/` ersetzt Pflichtenheft; Projektauftrag friert ein und bleibt Beurteilungsanker; Governance-Artefakte folgen der DA-Antragsstruktur, Feldbezeichner zweisprachig |
| D3 | Wasserfall / Scrum / SDD als drei Taktfrequenzen desselben Musters |
| D4 | UML 8 → 5 UE; Deployment-Diagramm in den 4. Jg |
| D5 | Schätz-Hygiene statt Schätzverfahren (Verfahren nur Namenskenntnis) |
| D6 | Kreativitätstechniken (6-3-5) + Nutzwertanalyse gepaart, U3/U4 |
| D7 | Ubuntu 26.04 LTS Dual-Boot ≥ 100 GB oder macOS; kein WSL2; Live-USB als Überbrückung |
| D8 | asciidoctor + GitHub Actions + Pages in den git-Block integriert |
| D9 | Reserve U26–U30 am Ende, gefüllt mit minikube |
| D10 | Sequenz folgt der Werkzeugkette git → AI → openspec |
| **D11** | **Manz-Schulbuch: Inhalte in eigener Formulierung und eigener Gliederung zulässig; keine Abbildungen, keine Seitenkopien, keine Weitergabe der PDF-Kapitel — auch nicht digital an einen abgegrenzten Kurs** |

### Threads 2 und 5 — Plattform und Lernressourcenformat (`setup-curriculum-repository`, P1–P12)

| | Entscheidung |
|---|---|
| P1 | `curriculum.yaml` ist einzige Strukturwahrheit; `.adoc` trägt nur `:topic-id:`; ein Topic = ein Unterricht; Dateipfade werden aus der ID abgeleitet, nicht eingetragen |
| P2 | CI-Check als Vertrag, neun Prüfungen: Bijektion, UE-Budget, Voraussetzungsgraph, Vollständigkeit, Slot-Belegung, Pflichtabschnitte, Outcome-Kopplung, Bildherkunft, Modulskelett |
| P3 | Generatoren: PlantUML-Mindmap, Navigation, UE-Übersicht, Fragenkatalog-Tags |
| P4 | Modulformat `index.adoc` / `exercises.adoc` / `questions.adoc`; feste Abschnittsfolge mit Pflichtteilen `Learning outcomes`, `Decisions`, `Pitfalls`, `Terminology`; Nullaussage erfüllt die Pflicht; `drill`/`project` als Kennzeichnung ohne CI-Zwang, Lösung und Kriterienblock optional |
| P5 | Lösungen als `[%collapsible]`; kein Freischalten; Lösungs-Branches nur im Assignment-Repo |
| P6 | Ein Repo pro Jahrgang, bestehender Stack, Antora verworfen (umkehrbar) |
| P7 | gh-pages primär, `publish.sh` optional auf Schulwebspace, Hugo koexistiert |
| P8 | Neuer Fragenkatalog, generiert aus den Modulen; bestehender bleibt unangetastet |
| P9 | Eigenes Repo `klassen-setup`: `setup-tools.sh` (idempotent) + `setup-identity.sh` (interaktiv), OS-Weiche, SDKMAN, `versions.env` |
| P10 | Kein Unterrichtsjournal im Repo; Module sind vorbereitet, stabil, klassenunabhängig |
| P11 | PlantUML als Diagramm-Default; Bilder erlaubt bei `modules/<id>/images/`, Keynote-Quelle daneben; Herkunftsklassen `own`/`free`/`unclear`; `rights-check`-Job meldet, blockiert nicht; `unclear` wird trotzdem ausgeliefert (bewusst getragenes Restrisiko) |
| P12 | Englisch mit zweisprachigem Governance-Wortschatz; Pflichtabschnitt `Terminology` |

### Thread 4 — Rechtslage (Recherchestand 2026-09-06, keine Rechtsberatung)

Die Trennlinie ist **öffentlich ↔ abgegrenzt**, nicht „Unterricht ↔ kein Unterricht":

```
Moodle (Login, abgegrenzter Kurs)      -> § 42g UrhG greift
gh-pages / Schulwebspace (oeffentlich) -> § 42g UrhG greift NICHT
```

- § 42 Abs 6 (Schulgebrauch) nimmt Werke aus, die für den Unterrichtsgebrauch bestimmt
  sind → Schulbücher fallen heraus, auch auf Papier, auch in Klassenstärke
- § 42g ebenso, und deckt nur einen abgegrenzten Teilnehmerkreis
- § 42f (Zitat) gilt auch öffentlich, verlangt aber **Belegfunktion** — ein Bild, das nur
  illustriert, ist kein Zitat
- § 6 (Sammelwerk) schützt Auswahl und Anordnung → Gliederungen nicht 1:1 übernehmen
- Fakten sind nie geschützt, nur ihre konkrete sprachliche Darstellung

Ausführlich in `setup-curriculum-repository/design.md` — P11 (Bilder) und
`define-syp3-curriculum/design.md` — D11 (Manz).

### Leitgedanke aus Thread 5

Erklärtext ist keine knappe Ware mehr. Was ein Agent **nicht** liefern kann: was in diesem
Jahrgang dazugehört, was geprüft wird, welche Entscheidung hier gilt, in welcher
Reihenfolge. Deshalb ist `index.adoc` **Kanon und Anker**, kein Lehrbuchkapitel.

---

## Stand der Artefakte

```
curriculum.yaml                        54 Themen, U1-U28 belegt, U29/U30 Puffer
                                       26 UE Theorie / 56 UE Praxis, Budgets stimmen
openspec/changes/
  define-syp3-curriculum/
    proposal.md  design.md             aktuell (D1-D11)
    specs/curriculum/                  8 Capabilities, 43 Requirements
    tasks.md                           FEHLT
  setup-curriculum-repository/
    proposal.md  design.md             aktuell (P1-P12)
    specs/platform/                    7 Capabilities, 44 Requirements
    tasks.md                           FEHLT
```

`openspec validate --all` ist grün. Noch nicht angelegt: `modules/`, `tools/`,
`templates/`, `.github/workflows/`, `publish.sh`.

### Jahresplan aus `curriculum.yaml`

```
U1  course-overview                 learning-environment-setup
U2  governance-project-basics       git-basics
U3  governance-idea-generation      git-branching
U4  governance-weighted-scoring     git-pull-requests
U5  governance-stakeholders-goals   git-conflicts-remotes
U6  governance-project-charter      asciidoctor-basics
U7  process-models-overview         gh-actions-pages
U8  sdd-why-specs                   ai-basics-prompting
U9  bridge-charter-to-specs         ai-context-continuation
U10 what-is-software-engineering    openspec-hands-on
U11 sdd-openspec-artifacts          ai-harness-engineering
U12 sdd-change-lifecycle            ai-agentic-loops
U13 bridge-progress-and-milestones  review-milestone-1
U14 sdd-specs-replace-requirements  docker-basics
U15 governance-estimation-hygiene   docker-images
U16 governance-milestones           docker-volumes-config
U17 governance-acceptance           docker-multiarch
U18 sdd-principle-not-tool          review-milestone-2
U19 process-waterfall               compose-basics
U20 process-scrum                   compose-multi-service
U21 uml-overview                    compose-networks-dependencies
U22 uml-use-case                    revealjs-presentations
U23 uml-class-object                ai-result-verification
U24 uml-activity                    review-milestone-3
U25 uml-state-overview              ai-project-integration
U26 assessment-oral-exams           minikube-basics      <- Reserve ab hier
U27 --                              minikube-deploy
U28 --                              minikube-services
U29 --                              --
U30 --                              --
```

---

## Offen

### Ablage auf GitHub *(nächster Schritt)*

Noch nicht besprochen: Organisation oder persönlicher Account, Sichtbarkeit,
Namensschema im Verhältnis zu den bestehenden `<jahr>-<klasse>-<gegenstand>`-Repos,
Verhältnis zu `htl-leonding-college`, Umgang mit den Repos für `klassen-setup` und
`templates/student-project/`.

### Thread 3 — Ablösung der Hugo-Site

Weitgehend beantwortet (P6/P7): Curriculum läuft auf gh-pages, Hugo bleibt parallel.
Offen nur, wann und ob abgelöst wird.

### Detailfragen aus der Befüllung von `curriculum.yaml`

- **UML liegt auf U21–U25**, also am Jahresende, obwohl Use-Case und Klassendiagramm zur
  Anforderungsanalyse gehören und ab U10 nützlich wären. Vorschlag war ein Tausch mit dem
  Governance-Nachzüglerblock (U15–U17). Nicht entschieden.
- U29/U30 und die Theorieslots von U27/U28 sind unbelegt — 8 UE reiner Puffer.

### Vertagt

- Schätzverfahren doch aufnehmen? Betrifft 1 UE Detailinhalt.
- Netzplantechnik (PUMA-Material) — noch nicht durchgesprochen.
- Sprache der Werkzeuge in `tools/` (Python, Node, Shell).
- Welche JDK-Version in `versions.env` gepinnt wird.
- Ob `templates/student-project/` im Curriculum-Repo liegt oder ein eigenes
  Template-Repository wird (für „classroom 50" bequemer).
- Ob der neue Fragenkatalog Teil der Curriculum-Site wird oder ein eigenes Repo bekommt.
- Ob Theoriethemen ebenfalls Pflichtfragen bekommen (CI-Prüfung 4 ausweiten).
- Wie das containerisierte asciidoctor-Image um `asciidoctor-diagram` und Graphviz
  ergänzt wird — betrifft auch `local-convert.sh`.

---

## Umsetzung

1. Repository auf GitHub ablegen, Sichtbarkeit und Namensschema festlegen
2. `tasks.md` für beide Changes ableiten
3. `tools/check-curriculum.*` mit den neun Prüfungen schreiben und in die Pipeline
   hängen — **vor** den ersten Lernressourcen, damit der Vertrag von Beginn an greift
4. `.github/workflows/` für adoc → HTML → gh-pages, plus `rights-check`-Job
5. Modulgerüst für die ersten Themen (`git-basics`, `sdd-why-specs`)
6. Generatoren (Mindmap, Navigation, UE-Übersicht, Katalog-Tags)
7. `templates/student-project/` mit zweisprachigen Feldbezeichnern
7a. Repo `klassen-setup` anlegen, auf frischem Ubuntu und macOS durchtesten
8. Neuen Fragenkatalog aufbauen
9. Lernressourcen inhaltlich erstellen — eigener Change
