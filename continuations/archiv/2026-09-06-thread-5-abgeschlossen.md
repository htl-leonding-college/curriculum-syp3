# Continuation Prompt — Curriculum SYP 3. Jahrgang

**Stand:** 2026-09-06 · Threads 1, 2 und 5 abgeschlossen · Plattform-Specs geschrieben
**Repo:** `curriculum-syp3` · **Changes:** `define-syp3-curriculum`, `setup-curriculum-repository`

> Dieses Dokument loest `2026-09-06-threads-1-2-abgeschlossen.md` ab. Das aeltere bleibt
> als Historie liegen.

---

## Einstieg

```
/opsx:explore
```

Dann diesen Prompt einfügen:

> Wir arbeiten am Curriculum für SYP (SYPPRE), 3. Jahrgang, HTL Informatik,
> Unterrichtssprache Englisch. Die bisherigen Entscheidungen stehen in
> `openspec/changes/define-syp3-curriculum/{proposal,design}.md` (Inhalt: was
> unterrichtet wird) und `openspec/changes/setup-curriculum-repository/{proposal,design}.md`
> (Plattform: wie es gespeichert und publiziert wird), die Plattform-Anforderungen in
> `openspec/changes/setup-curriculum-repository/specs/platform/*/spec.md` — lies das alles,
> bevor du antwortest, und frage nicht nach Fakten, die dort stehen.
> Der ursprüngliche Auftrag liegt in `chat.adoc`.
> Threads 1, 2 und 5 sind abgeschlossen. Als Nächstes: **Thread 4 — Rechtslage
> Schulbuch und Bildrechte**, oder die Specs für `define-syp3-curriculum`.

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
Sie werden vorerst behalten, stehen aber in `.gitignore` und gehören **nicht** ins
Repository. Die Feldstruktur des Antrags ist in `define-syp3-curriculum/design.md` (D2)
festgehalten.

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
- Das Manz-Schulbuch darf inhaltlich verwendet werden (Aufzählungen, Texte in eigenen
  Worten), **keine Abbildungen oder Seitenkopien**.
- Keine personenbezogenen Daten ins Repository.

---

## Was entschieden ist

Vollständig in den beiden `design.md` und den Specs. Kurzfassung als Gedächtnisstütze:

### Thread 1 — Inhalt (`define-syp3-curriculum`, D1–D10)

| | Entscheidung |
|---|---|
| D1 | Zweiteilung: Governance (außen, verpflichtend, vorgehensmodell-neutral) ↔ Durchführung (innen, SDD) |
| D2 | `specs/` ersetzt Pflichtenheft; Projektauftrag friert ein und bleibt Beurteilungsanker; Mapping der DA-Antragsfelder auf openspec-Artefakte; **Governance-Artefakte folgen der DA-Antragsstruktur, Feldbezeichner zweisprachig** |
| D3 | Wasserfall / Scrum / SDD als drei Taktfrequenzen desselben Musters |
| D4 | UML 8 → 5 UE; Deployment-Diagramm in den 4. Jg |
| D5 | Schätz-Hygiene statt Schätzverfahren (Verfahren nur Namenskenntnis) |
| D6 | Kreativitätstechniken (6-3-5) + Nutzwertanalyse gepaart, U3/U4 |
| D7 | Ubuntu 26.04 LTS Dual-Boot ≥ 100 GB oder macOS; kein WSL2; Live-USB als Überbrückung |
| D8 | asciidoctor + GitHub Actions + Pages in den git-Block integriert |
| D9 | Reserve U26–U30 am Ende, gefüllt mit minikube |
| D10 | Sequenz folgt der Werkzeugkette git → AI → openspec |

Rahmen: 30 Unterrichte à 3 UE (1 Theorie + 2 Praxis), ~25 UE Theorie / ~50 UE Praxis,
Projektarbeit zu Hause, ~7 UE für Reviews im Unterricht. Eröffnungssequenz U1–U10 steht.

### Threads 2 und 5 — Plattform und Lernressourcenformat (`setup-curriculum-repository`, P1–P12)

| | Entscheidung |
|---|---|
| P1 | `curriculum.yaml` ist einzige Strukturwahrheit; `.adoc` trägt nur `:topic-id:`. **Granularität: ein Topic = ein Unterricht (1 UE Theorie bzw. 2 UE Praxis), ~48 Topics** |
| P2 | CI-Check als Vertrag, **neun Prüfungen**: Bijektion, UE-Budget, Voraussetzungsgraph, Vollständigkeit, Slot-Belegung, Pflichtabschnitte, Outcome-Kopplung, Bildherkunft, Modulskelett |
| P3 | Generatoren: PlantUML-Mindmap, Navigation, UE-Übersicht, Fragenkatalog-Tags |
| P4 | Modulformat `index.adoc` / `exercises.adoc` / `questions.adoc`; **feste Abschnittsfolge**, Pflichtteile `Learning outcomes`, `Decisions`, `Pitfalls`, `Terminology`; Nullaussage erfüllt die Pflicht; **`drill`/`project` als Kennzeichnung ohne CI-Zwang, Lösung und Kriterienblock optional** |
| P5 | Lösungen als `[%collapsible]`; kein Freischalten; Lösungs-Branches nur im Assignment-Repo |
| P6 | Ein Repo pro Jahrgang, bestehender Stack, **Antora verworfen** (umkehrbar) |
| P7 | gh-pages primär, `publish.sh` optional auf Schulwebspace, Hugo koexistiert |
| P8 | **Neuer** Fragenkatalog, generiert aus den Modulen; bestehender bleibt unangetastet |
| P9 | Eigenes Repo `klassen-setup`: `setup-tools.sh` (idempotent) + `setup-identity.sh` (interaktiv), OS-Weiche, SDKMAN für Java-Stack, `versions.env` |
| **P10** | **Kein Unterrichtsjournal im Repo.** Module sind vorbereitet, stabil, klassenunabhängig; der Verlauf wird außerhalb geführt |
| **P11** | **PlantUML als Diagramm-Default** (inline). Bilder erlaubt, wo PlantUML nicht trägt; liegen bei `modules/<id>/images/`, Keynote-Quelle daneben. **Herkunftsklassen `own`/`free`/`unclear`**; eigener `rights-check`-Job, der meldet aber nicht blockiert |
| **P12** | **Englisch mit zweisprachigem Governance-Wortschatz**; Pflichtabschnitt `Terminology`; Vorlagen mit zweisprachigen Feldbezeichnern |

Kein LLM-Wiki — der Defekt war Struktur-in-Prosa, nicht die Speicherform.

Bewertungsmodell: Übungsaufgaben zu Hause, Nachweis über mündliche Prüfungen anhand der
mitgelieferten Prüfungsfragen. Verbergen ist bei Agentenverfügbarkeit wirkungslos;
Mitliefern ist erlaubt, aber nicht verpflichtend.

### Leitgedanke aus Thread 5

Erklärtext ist keine knappe Ware mehr — jeder Schüler kann sich eine beliebig lange
Erklärung generieren lassen. Was ein Agent **nicht** liefern kann: was in diesem Jahrgang
dazugehört, was geprüft wird, welche Entscheidung hier gilt, in welcher Reihenfolge.
Deshalb ist `index.adoc` **Kanon und Anker**, kein Lehrbuchkapitel, und deshalb sind
`Decisions` und `Learning outcomes` Pflichtabschnitte.

---

## Stand der Artefakte

```
openspec/changes/
  define-syp3-curriculum/
    proposal.md          aktuell
    design.md            aktuell (D1-D10)
    specs/               FEHLT -> openspec validate schlaegt fehl
    tasks.md             fehlt
  setup-curriculum-repository/
    proposal.md          aktuell
    design.md            aktuell (P1-P12)
    specs/platform/      7 Capabilities, validate --strict: gruen
      curriculum-model/ curriculum-validation/ curriculum-generators/
      learning-resource-format/ publication/ question-catalogue/ class-setup/
    tasks.md             fehlt
```

`openspec validate --all` meldet weiterhin einen Fehler für `define-syp3-curriculum`
(„no deltas found"), solange dessen `specs/` fehlen. Das ist kein Defekt, sondern der
nächste offene Arbeitsschritt.

---

## Offene Threads

### Thread 4 — Rechtslage Manz-Schulbuch und Bilder *(nächster Schritt)*

Zu recherchieren: aktuell gültige österreichische Bestimmungen. Bisheriger Stand aus dem
Gespräch, **nicht belastbar recherchiert**: § 42 Abs 6 UrhG (Vervielfältigung zum eigenen
Schulgebrauch) nimmt Werke aus, die ihrer Beschaffenheit nach für den Unterrichtsgebrauch
bestimmt sind — Schulbücher fallen darunter. Gleichzeitig sind Fakten und Gliederungen
nicht geschützt, nur die konkrete Formulierung.

**Erweitert um Bildrechte:** Die Curriculum-Site ist öffentlich auf gh-pages. § 42 UrhG
deckt Vervielfältigung für den eigenen Schulgebrauch, nicht öffentliche
Zugänglichmachung im Web. Das betrifft die bestehenden Lecture-Notes-Sites bereits heute.
P11 legt nur die Struktur fest (`own`/`free`/`unclear`), die eine spätere Bereinigung
möglich macht — die inhaltliche Klärung steht aus.

### Thread 3 — Rest: Ablösung der Hugo-Site

Weitgehend beantwortet (P6/P7): Curriculum läuft auf gh-pages, Hugo bleibt parallel
bestehen. Offen nur, wann und ob abgelöst wird — entscheidbar, sobald Inhalt vorliegt.

---

## Vertagt

- Schätzverfahren doch aufnehmen? Betrifft 1 UE Detailinhalt, ändert weder Sequenz
  noch Budget.
- Feinaufteilung der 15 AI-UE zwischen Grundlagen (vor U10) und Vertiefung (nach U10).
- Zeitpunkt des revealjs-Blocks.
- Netzplantechnik (PUMA-Material): gleiche Frage wie beim Schätzverfahren — kritischer
  Pfad bringt in einem 4-Personen-Schuljahresprojekt vermutlich keinen Erkenntnisgewinn.
  Noch nicht durchgesprochen.
- Sprache der Werkzeuge in `tools/` (Python, Node, Shell).
- Welche JDK-Version in `versions.env` gepinnt wird — abhängig von den übrigen
  Gegenständen im 4./5. Jg.
- Ob `templates/student-project/` im Curriculum-Repo liegt oder ein eigenes
  Template-Repository wird (für „classroom 50" bequemer).
- Ob der neue Fragenkatalog Teil der Curriculum-Site wird oder ein eigenes Repo bekommt.
- Ob Theoriethemen ebenfalls Pflichtfragen bekommen (CI-Prüfung 4 ausweiten).
- Wie das containerisierte asciidoctor-Image um `asciidoctor-diagram` und Graphviz
  ergänzt wird — betrifft auch `local-convert.sh`.

---

## Umsetzung, sobald die Threads durch sind

1. `specs/` für `define-syp3-curriculum` schreiben — Lernziele je Capability als prüfbare
   Requirements. Sie sind zugleich das Rohmaterial für die `Learning outcomes`-Abschnitte
   der ~48 Module.
2. `tasks.md` für beide Changes ableiten
3. `curriculum.yaml` mit den ~48 Topics befüllen (Blöcke, UE, Slots, `requires:`)
4. `tools/check-curriculum.*` mit den neun Prüfungen schreiben und in die Pipeline
   hängen — **vor** den ersten Lernressourcen, damit der Vertrag von Beginn an greift
5. Modulgerüst für die ersten Themen (`git-basics`, `sdd-why-specs`)
6. Generatoren (Mindmap, Navigation, UE-Übersicht, Katalog-Tags)
7. `templates/student-project/` mit zweisprachigen Feldbezeichnern
7a. Repo `klassen-setup` anlegen, auf frischem Ubuntu und macOS durchtesten
8. Neuen Fragenkatalog aufbauen
9. Lernressourcen inhaltlich erstellen — eigener Change
