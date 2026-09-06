# Continuation Prompt — Curriculum SYP 3. Jahrgang

**Stand:** 2026-09-06 · Threads 1 und 2 abgeschlossen und festgeschrieben
**Repo:** `curriculum-syp3` · **Changes:** `define-syp3-curriculum`, `setup-curriculum-repository`

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
> (Plattform: wie es gespeichert und publiziert wird) — lies alle vier, bevor du
> antwortest, und frage nicht nach Fakten, die dort stehen.
> Der ursprüngliche Auftrag liegt in `chat.adoc`.
> Threads 1 und 2 sind abgeschlossen. Als Nächstes: **Thread 5 — Detaillierungsgrad
> und Struktur einer Lernressource**, oder Thread 4 (Rechtslage Schulbuch).

---

## Rolle und Kontext

Der Nutzer ist Lehrer an der HTL Leonding und unterrichtet SYP im 3. Jahrgang auf
Englisch. Er strukturiert seine Stoffinhalte neu und will sie online präsentieren.

Bestehende Infrastruktur:

- Hugo-Website auf dem Schulwebspace
  (`edufs.edu.htl-leonding.ac.at/~t.stuetz/hugo/`) — bleibt vorerst unangetastet,
  enthält Altdaten früherer Projekte
- Mitschrift als AsciiDoc auf GitHub Pages
  (z. B. `2526-3bhif-syp.github.io/2526-3bhif-syp-lecture-notes/`)
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

`assets/` ist leer — die Screenshots des Diplomarbeitsantrags wurden nach der Auswertung
gelöscht (enthielten echte Schülernamen). Die Feldstruktur des Antrags ist in
`define-syp3-curriculum/design.md` (D2) festgehalten.

---

## Arbeitsweise (verbindlich)

- **Nichts erstellen ohne vorherige Zustimmung.** Gilt für Dateien und
  OpenSpec-Artefakte gleichermaßen. Vorher benennen, was angelegt würde, dann fragen.
- **Explore-Modus ist Denkarbeit, keine Umsetzung.**
- **Diagramme bevorzugt PlantUML**, Stoffstruktur als `@startmindmap`.
- **Planungsartefakte auf Deutsch, Lernressourcen auf Englisch.**
- **Eine fokussierte Frage pro Runde**, nicht mehrere parallel.
- Annahmen kennzeichnen, Alternativen mit Begründung verwerfen, nicht nur aufzählen.
- Das Manz-Schulbuch darf inhaltlich verwendet werden (Aufzählungen, Texte in eigenen
  Worten), **keine Abbildungen oder Seitenkopien**.
- Keine personenbezogenen Daten ins Repository.

---

## Was entschieden ist

Vollständig in den beiden `design.md`. Kurzfassung als Gedächtnisstütze:

### Thread 1 — Inhalt (`define-syp3-curriculum`, D1–D10)

| | Entscheidung |
|---|---|
| D1 | Zweiteilung: Governance (außen, verpflichtend, vorgehensmodell-neutral) ↔ Durchführung (innen, SDD) |
| D2 | `specs/` ersetzt Pflichtenheft; Projektauftrag friert ein und bleibt Beurteilungsanker; Mapping der DA-Antragsfelder auf openspec-Artefakte |
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

### Thread 2 — Plattform (`setup-curriculum-repository`, P1–P9)

| | Entscheidung |
|---|---|
| P1 | `curriculum.yaml` ist einzige Strukturwahrheit; `.adoc` trägt nur `:topic-id:` |
| P2 | CI-Check als Vertrag: Bijektion, UE-Budget, Voraussetzungsgraph, Vollständigkeit |
| P3 | Generatoren: PlantUML-Mindmap, Navigation, Fragenkatalog-Tags |
| P4 | Modulformat `index.adoc` / `exercises.adoc` / `questions.adoc`; Prüfungsfragen werden mitgeliefert |
| P5 | Lösungen als `[%collapsible]`; kein Freischalten; Lösungs-Branches nur im Assignment-Repo |
| P6 | Ein Repo pro Jahrgang, bestehender Stack, **Antora verworfen** (umkehrbar) |
| P7 | gh-pages primär, `publish.sh` optional auf Schulwebspace, Hugo koexistiert |
| P8 | **Neuer** Fragenkatalog, generiert aus den Modulen; bestehender bleibt unangetastet |
| P9 | Eigenes Repo `klassen-setup`: `setup-tools.sh` (idempotent) + `setup-identity.sh` (interaktiv), OS-Weiche, SDKMAN für Java-Stack, `versions.env` |

Kein LLM-Wiki — der Defekt war Struktur-in-Prosa, nicht die Speicherform.

Bewertungsmodell: Übungsaufgaben zu Hause, Lösungen liegen bei (Verbergen ist bei
Agentenverfügbarkeit wirkungslos), Nachweis über mündliche Prüfungen anhand der
mitgelieferten Prüfungsfragen.

---

## Offene Threads

### Thread 5 — Detaillierungsgrad und Struktur einer Lernressource *(nächster Schritt)*

Wie tief, wie lang, wie aufgebaut ist ein einzelnes Modul? Betrifft `index.adoc`,
`exercises.adoc` und `questions.adoc` gleichermaßen. Der Nutzer wollte das ausdrücklich
vorab besprechen, bevor Inhalte entstehen. Formatrahmen steht bereits durch P4.

### Thread 4 — Rechtslage Manz-Schulbuch

Zu recherchieren: aktuell gültige österreichische Bestimmungen. Bisheriger Stand aus dem
Gespräch, **nicht belastbar recherchiert**: § 42 Abs 6 UrhG (Vervielfältigung zum eigenen
Schulgebrauch) nimmt Werke aus, die ihrer Beschaffenheit nach für den Unterrichtsgebrauch
bestimmt sind — Schulbücher fallen darunter. Gleichzeitig sind Fakten und Gliederungen
nicht geschützt, nur die konkrete Formulierung.

### Thread 3 — Rest: Ablösung der Hugo-Site

Weitgehend beantwortet (P6/P7): Curriculum läuft auf gh-pages, Hugo bleibt parallel
bestehen. Offen nur, wann und ob abgelöst wird — entscheidbar, sobald Inhalt vorliegt.

---

## Aus Thread 1 und 2 vertagt

- Schätzverfahren doch aufnehmen? Betrifft 1 UE Detailinhalt, ändert weder Sequenz
  noch Budget.
- Feinaufteilung der 15 AI-UE zwischen Grundlagen (vor U10) und Vertiefung (nach U10).
- Zeitpunkt des revealjs-Blocks.
- Ob die 3.-Jg-Governance-Artefakte formal an die DA-Antragsstruktur angelehnt werden.
- Netzplantechnik (PUMA-Material): gleiche Frage wie beim Schätzverfahren — kritischer
  Pfad bringt in einem 4-Personen-Schuljahresprojekt vermutlich keinen Erkenntnisgewinn.
  Noch nicht durchgesprochen.
- Sprache der Werkzeuge in `tools/` (Python, Node, Shell).
- Welche JDK-Version in `versions.env` gepinnt wird — abhängig von den übrigen
  Gegenständen im 4./5. Jg.
- Ob `templates/student-project/` im Curriculum-Repo liegt oder ein eigenes
  Template-Repository wird (für „classroom 50" bequemer).
- Ob der neue Fragenkatalog Teil der Curriculum-Site wird oder ein eigenes Repo bekommt.

---

## Umsetzung, sobald die Threads durch sind

1. `curriculum.yaml` mit den Themen aus `define-syp3-curriculum/design.md` befüllen
2. `tools/check-curriculum.*` schreiben und in die Pipeline hängen — **vor** den ersten
   Lernressourcen, damit der Vertrag von Beginn an greift
3. Modulgerüst für `git-basics` und `sdd-openspec`
4. Generatoren (Mindmap, Navigation)
5. `templates/student-project/`
5a. Repo `klassen-setup` anlegen, auf frischem Ubuntu und macOS durchtesten
6. Neuen Fragenkatalog aufbauen
7. Lernressourcen inhaltlich erstellen — eigener Change
