# Continuation Prompt — Curriculum SYP 3. Jahrgang

**Stand:** 2026-09-06 · Thread 1 abgeschlossen und festgeschrieben
**Repo:** `curriculum-syp3` · **Change:** `define-syp3-curriculum`

---

## Einstieg

```
/opsx:explore
```

Dann diesen Prompt einfügen:

> Wir arbeiten am Curriculum für SYP (SYPPRE), 3. Jahrgang, HTL Informatik,
> Unterrichtssprache Englisch. Die bisherigen Entscheidungen stehen in
> `openspec/changes/define-syp3-curriculum/proposal.md` und `design.md` —
> lies beide, bevor du antwortest, und frage nicht nach Fakten, die dort stehen.
> Der ursprüngliche Auftrag liegt in `chat.adoc`.
> Wir sind in Thread 1 (Theoriegewichtung und Sequenz) fertig. Als Nächstes:
> **Thread 2 — Speicherformat der Stoffstruktur.**

---

## Rolle und Kontext

Der Nutzer ist Lehrer an der HTL Leonding und unterrichtet SYP im 3. Jahrgang auf
Englisch. Er strukturiert seine Stoffinhalte neu und will sie online präsentieren.

Bestehende Infrastruktur:

- Lernressourcen öffentlich auf einer Hugo-Website
  (`edufs.edu.htl-leonding.ac.at/~t.stuetz/hugo/`)
- Mitschrift als AsciiDoc auf GitHub Pages
  (z. B. `2526-3bhif-syp.github.io/2526-3bhif-syp-lecture-notes/`)
- Personenbezogene Daten (Testergebnisse) in Moodle
- Assignments und Tests über GitHub Classroom, künftig „classroom 50"
- Schülerprojekte in GitHub
- Fragenkatalog: `htl-leonding-college.github.io/fragenkatalog`

Materialbestand unter `/Users/stuetz/SynologyDrive/htl/skripten/pre.syp.itp.3jg/`:
Manz-Schulbuch als PDF-Kapitel (`eBooks/SYP-Buch.Manz.Aufl_2013/`), UML-Skripten
Uni Heidelberg (`uml/Uni Heidelberg/UML1.1/`), `01.Vorgehensmodelle.key`,
`PUMA8_12_Kreativitätstechniken.pdf`, `PUMA8_05_Nutzwertanalyse.pdf`,
`PUMA Netzplantechnik/`.

`assets/` im Repo enthält Screenshots des Diplomarbeitsantrags (Antragsdatenbank)
— Referenz für die Governance-Feldstruktur. **Enthält echte Schülernamen.**

---

## Arbeitsweise (verbindlich)

- **Nichts erstellen ohne vorherige Zustimmung.** Gilt für Dateien und
  OpenSpec-Artefakte gleichermaßen. Vorher benennen, was angelegt würde, dann fragen.
- **Explore-Modus ist Denkarbeit, keine Umsetzung.**
- **Diagramme bevorzugt PlantUML**, Stoffstruktur als `@startmindmap`.
- **Planungsartefakte auf Deutsch, Lernressourcen auf Englisch.**
- **Ein fokussierte Frage pro Runde**, nicht mehrere parallel.
- Annahmen kennzeichnen, Alternativen mit Begründung verwerfen, nicht nur aufzählen.
- Das Manz-Schulbuch darf inhaltlich verwendet werden (Aufzählungen, Texte in eigenen
  Worten), **keine Abbildungen oder Seitenkopien**.

---

## Was entschieden ist

Vollständig in `openspec/changes/define-syp3-curriculum/design.md` (D1–D10).
Kurzfassung als Gedächtnisstütze:

| | Entscheidung |
|---|---|
| D1 | Zweiteilung: Governance (außen, verpflichtend, vorgehensmodell-neutral) ↔ Durchführung (innen, SDD) |
| D2 | `specs/` ersetzt Pflichtenheft; Projektauftrag friert ein und bleibt Beurteilungsanker |
| D3 | Wasserfall / Scrum / SDD als drei Taktfrequenzen desselben Musters |
| D4 | UML 8 → 5 UE; Deployment-Diagramm in den 4. Jg |
| D5 | Schätz-Hygiene statt Schätzverfahren (Verfahren nur Namenskenntnis) |
| D6 | Kreativitätstechniken (6-3-5) + Nutzwertanalyse gepaart, U3/U4 |
| D7 | Ubuntu 24.04 LTS Dual-Boot ≥ 100 GB oder macOS; kein WSL2; Live-USB als Überbrückung |
| D8 | asciidoctor + GitHub Actions + Pages in den git-Block integriert |
| D9 | Reserve U26–U30 am Ende, gefüllt mit minikube |
| D10 | Sequenz folgt der Werkzeugkette git → AI → openspec |

Rahmen: 30 Unterrichte à 3 UE (1 Theorie + 2 Praxis), ~25 UE Theorie / ~50 UE Praxis,
Projektarbeit zu Hause, ~7 UE für Reviews im Unterricht.

---

## Offene Threads

### Thread 2 — Speicherformat der Stoffstruktur *(nächster Schritt, blockiert die anderen)*

Zentrale Frage des Nutzers: Ist ein LLM-Wiki für den Lernstoff sinnvoll, oder wie sonst
soll die Stoffstruktur gespeichert werden?

Bisheriger Vorschlag (noch **nicht** entschieden, nur skizziert): kein separates Wiki,
sondern maschinenlesbare Daten im selben Git-Repo — eine `topics.yaml` mit
`id`, `title`, `taught_in`, `requires`, `ue`, `resources`, `questions` als Single Source
of Truth, aus der PlantUML-Mindmap, Website-Navigation und Fragenkatalog-Tags generiert
werden. Begründung: ein zweites System wäre eine zweite Wahrheitsquelle.

Hängt daran: Umbau des Fragenkatalogs. Die neuen Tags („Voraussetzung für 3./4./5. Jg")
mischen zwei Dimensionen — *wann unterrichtet* und *wofür Voraussetzung*. Als
`taught_in` + `requires` im Datenmodell wird daraus ein Abhängigkeitsgraph, die Tags
fallen als Ableitung ab.

### Thread 3 — Konsolidierung der Publikationswege

Aktuell laufen Hugo-Website und AsciiDoc-auf-GitHub-Pages parallel für ähnliche Inhalte.
Kandidat für Konsolidierung: **Antora** (AsciiDoc, mehrere Repos, versionierte
Navigation, PlantUML nativ). Moodle bleibt für personenbezogene Daten, „classroom 50"
für Assignments. Noch nicht angesprochen: Warum es historisch zwei Wege gibt.

### Thread 4 — Rechtslage Manz-Schulbuch

Zu recherchieren: aktuell gültige österreichische Bestimmungen. Bisheriger Stand aus
dem Gespräch, **nicht belastbar recherchiert**: § 42 Abs 6 UrhG (Vervielfältigung zum
eigenen Schulgebrauch) nimmt Werke aus, die ihrer Beschaffenheit nach für den
Unterrichtsgebrauch bestimmt sind — Schulbücher fallen darunter. Gleichzeitig sind
Fakten und Gliederungen nicht geschützt, nur die konkrete Formulierung.

### Thread 5 — Detaillierungsgrad einer Lernressource

Struktur, Tiefe und Umfang einer einzelnen Lernressource inklusive Übungsaufgaben und
Lösungen. Sinnvoll erst nach Thread 2, weil das Speicherformat die Struktur mitbestimmt.

---

## Aus Thread 1 vertagt

- Schätzverfahren doch aufnehmen? Betrifft 1 UE Detailinhalt, ändert weder Sequenz
  noch Budget.
- Feinaufteilung der 15 AI-UE zwischen Grundlagen (vor U10) und Vertiefung (nach U10).
- Zeitpunkt des revealjs-Blocks.
- Ob die 3.-Jg-Governance-Artefakte formal an die DA-Antragsstruktur angelehnt werden,
  damit die Schüler im 5. Jg ein bekanntes Formular ausfüllen.
- Netzplantechnik (PUMA-Material): gleiche Entscheidung wie beim Schätzverfahren —
  kritischer Pfad bringt in einem 4-Personen-Schuljahresprojekt keinen Erkenntnisgewinn.
  Noch nicht durchgesprochen.

---

## Nach Thread 2–5

1. `specs/` je Capability aus `proposal.md` schreiben (Lernziele als prüfbare Requirements)
2. `tasks.md` ableiten: Lernressourcen auf Englisch, `setup.sh`, Vorlagen-Repository
   für Schülerprojekte
3. Fragenkatalog-Umbau als eigener Change
