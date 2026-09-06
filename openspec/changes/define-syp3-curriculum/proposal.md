# Curriculum SYP 3. Jahrgang definieren

## Why

Der Gegenstand SYP/SYPPRE im 3. Jahrgang (HTL Informatik, Unterrichtssprache Englisch)
wird derzeit nach einem Curriculum unterrichtet, das klassisches Projektmanagement
(Wasserfall, Manz-Schulbuch) mit Scrum als Durchführungsmodell kombiniert. Durch den
Einsatz von AI-Agenten hat sich die tatsächliche Arbeitsweise in Schülerprojekten auf
spec-driven development (openspec) verschoben, während die verpflichtenden
Governance-Artefakte (Projektantrag, Projektauftrag, Meilensteinplan, Abnahme)
unverändert gefordert bleiben — im 3. Jg für das Jahresprojekt, im 4./5. Jg für das
zweijährige Projekt und die Diplomarbeit.

Das Curriculum muss diese Verschiebung abbilden, ohne die Governance-Kompetenz zu
verlieren, die Schüler in der Diplomarbeit nachweisen müssen. Zusätzlich sollen die
Lernressourcen auf Englisch neu erstellt und die Stoffstruktur maschinenlesbar
abgelegt werden.

## What Changes

### Entschieden (Thread 1: Theoriegewichtung und Sequenz)

- **Zweiteilung statt Entweder-oder.** Projekt-Governance (außen, verpflichtend,
  vorgehensmodell-neutral) wird von der Durchführung (innen, frei wählbar) getrennt.
  Der DA-Antrag schreibt kein Vorgehensmodell vor; Scrum war eine Wahl, keine Vorgabe.
  SDD ersetzt daher Scrum auf der Innenebene, ohne Governance zu berühren.
- **Neuer Lernblock „Brücke Governance ↔ SDD"** (2 UE): Abbildung der
  Antragsfelder auf openspec-Artefakte (Untersuchungsanliegen → `proposal.md`,
  Geplantes Ergebnis → `spec.md` Requirements/Scenarios, Meilenstein → archivierter
  Change, Verantwortlichkeit → Change-Ownership).
- **Pflichtenheft wird durch `specs/` ersetzt.** Der Projektauftrag friert ein und
  bleibt Beurteilungsanker; die specs leben und werden durch `changes/` fortgeschrieben.
  `changes/archive/` ersetzt die Change-Request-Historie. Optionale Baseline per git-Tag.
- **UML wird von 8 UE auf 5 UE gekürzt.** Use-Case-, Klassen- (inkl. Objekt-) und
  Aktivitätsdiagramm bleiben; Zustandsdiagramm nur im Überblick; Deployment-Diagramm
  wandert in den 4. Jg zum Kubernetes-Block.
- **Klassische Aufwandsschätzverfahren entfallen** (Function Points, COCOMO,
  Planning Poker) — ohne Kalibrierungsdaten nicht anwendbar, und sie messen den
  Posten, der durch Agenteneinsatz geschrumpft ist. Ersetzt durch Schätz-Hygiene;
  finale Entscheidung bei der Detailausarbeitung.
- **Kreativitätstechniken (divergieren) und Nutzwertanalyse (konvergieren) werden
  gepaart** und jeweils sofort angewendet. Die Projektauswahl wird dadurch
  kriterienbasiert und nachvollziehbar statt willkürlich.
- **Jahresrahmen 30 Unterrichte à 3 UE** (1 UE Theorie + 2 UE Praxis), davon U1
  Vorstellungseinheit und U26–U30 Reserve. Die Reserve liegt am Ende und ist mit dem
  verzichtbarsten Inhalt (minikube) gefüllt, damit Ausfälle automatisch das Richtige treffen.
- **Lernumgebung**: Ubuntu 26.04 LTS als Dual-Boot-Partition (≥ 100 GB) oder macOS.
  WSL2 ist kein Fallback, da es die Windows-Fehlkonfiguration erbt; Überbrückung per
  Ubuntu-Live-USB mit Persistenz. Klassenweites `setup.sh` (apt/brew) als
  versionierter Standard und späterer Anknüpfungspunkt für den Docker-Block.
- **asciidoctor + GitHub Actions + GitHub Pages werden in den git-Block integriert.**
  Projektdokumentation entsteht als Nebenprodukt; CI bekommt einen echten Anlass;
  `ubuntu-latest` wird zum Schiedsrichter zwischen Linux- und macOS-Geräten.

### Offen (Threads 2–5)

- Speicherformat der Stoffstruktur (maschinenlesbare `topics.yaml` vs. LLM-Wiki) und
  daraus abgeleitet der Umbau des Fragenkatalogs auf Voraussetzungs-Tags je Jahrgang
- Konsolidierung der Publikationswege (Hugo-Website vs. AsciiDoc auf GitHub Pages)
- Urheberrechtliche Bedingungen für die Verwendung des Manz-Schulbuchs
- Detaillierungsgrad und Struktur einer einzelnen Lernressource

## Capabilities

### New Capabilities

- `curriculum/jahresplanung`: Jahresrahmen, UE-Budget, Unterrichtssequenz,
  Reservestrategie, Verzahnung Theorie/Praxis/Hausübung
- `curriculum/projekt-governance`: Projektbegriff, Ausgangslage, Kreativitätstechniken,
  Nutzwertanalyse, Stakeholder, Zielsetzung, Projektantrag, Projektauftrag,
  Meilensteinplanung, Abnahme
- `curriculum/vorgehen-sdd`: Vorgehensmodelle im Überblick (Wasserfall, Scrum, SDD als
  drei Taktfrequenzen), openspec in der Anwendung, Brücke Governance ↔ SDD
- `curriculum/uml-basics`: Use-Case-, Klassen-/Objekt-, Aktivitätsdiagramm; Zustands-
  diagramm im Überblick; Darstellung durchgängig mit PlantUML
- `curriculum/lernumgebung`: Ubuntu-/macOS-Setup, Dual-Boot-Verfahren, `setup.sh`,
  Umgang mit heterogenen Geräten
- `curriculum/praxis-toolchain`: git (Repo, Branch, Merge, PR, Konflikte),
  asciidoctor, GitHub Actions, GitHub Pages, revealjs
- `curriculum/praxis-ai`: AI-Grundlagen, Prompt Engineering, Kontext- und
  Continuation-Prompts, Harness Engineering, Loops
- `curriculum/praxis-container`: Docker (inkl. Multi-Arch für Apple Silicon),
  docker compose, minikube

### Modified Capabilities

Keine — dies ist die Erstdefinition des Curriculums; unter `openspec/specs/` existieren
noch keine Capabilities.

## Impact

- **Unterrichtsmaterial**: Lernressourcen werden auf Englisch neu erstellt. Bestehende
  Keynote-/PDF-Materialien (`01.Vorgehensmodelle`, PUMA-Kreativitätstechniken,
  PUMA-Nutzwertanalyse, UML Uni Heidelberg) werden weiterverwendet bzw. abgelöst.
- **Manz-Schulbuch**: Weiterhin Quelle, aber nur Aufzählungen und Texte in eigener
  Formulierung; keine Abbildungen oder Seitenkopien (rechtliche Prüfung offen).
- **Schülerprojekte**: Repository-Struktur mit openspec, Projektdokumentation als
  AsciiDoc, Publikation über GitHub Pages.
- **Fragenkatalog** (htl-leonding-college.github.io/fragenkatalog): Tag-Schema wird
  von „Foundation/Advanced" auf Voraussetzungs-Tags je Jahrgang umgestellt — Umfang
  und Verfahren offen (Thread 2).
- **4./5. Jahrgang**: Deployment-Diagramm und Kubernetes-Vertiefung werden dorthin
  verschoben; Abstimmung mit der dortigen Jahresplanung erforderlich.
- **Nicht im Umfang**: Ausarbeitung der Lernressourcen selbst, Umbau des
  Fragenkatalogs, Curriculum des 4. und 5. Jahrgangs, Moodle-Kurs.
