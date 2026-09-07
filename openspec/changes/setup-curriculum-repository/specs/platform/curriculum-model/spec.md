## Purpose

Bildet die Stoffstruktur eines Jahrgangs als maschinenlesbares Modell ab — Themen,
Umfang, Reihenfolge, Jahrgangszuordnung und Voraussetzungen — und ist die einzige Quelle
dieser Angaben.

## ADDED Requirements

### Requirement: Strukturangaben stehen ausschliesslich im Modell
Das Curriculum-Modell SHALL die einzige Quelle fuer Themenzuschnitt, Umfang in
Unterrichtseinheiten, Blockzuordnung, Unterrichtsnummer, Jahrgangszuordnung und
Voraussetzungen sein. Eine Lernressource SHALL ausser ihrer Themen-ID keine
Strukturangabe tragen.

#### Scenario: Strukturangabe im AsciiDoc
- **WHEN** eine Datei unter `modules/` ein Attribut mit UE-Zahl, Block, Jahrgang oder
  Voraussetzung traegt
- **THEN** meldet die Pruefung einen Fehler und nennt Datei und Attribut

#### Scenario: Umfang wird geaendert
- **WHEN** die UE-Zahl eines Themas geaendert wird
- **THEN** genuegt eine Aenderung im Modell, und keine Lernressource muss angefasst werden

### Requirement: Themen und Lernressourcen sind ueber eine ID gekoppelt
Jedes Thema SHALL eine eindeutige, unveraenderliche ID tragen. Jede Lernressource SHALL
genau eine Themen-ID nennen, und jede genannte ID SHALL im Modell existieren.

#### Scenario: Ressource ohne Themen-ID
- **WHEN** eine Datei unter `modules/` keine Themen-ID traegt
- **THEN** meldet die Pruefung einen Fehler

#### Scenario: Themen-ID ohne Eintrag im Modell
- **WHEN** eine Lernressource eine ID nennt, die im Modell nicht vorkommt
- **THEN** meldet die Pruefung einen Fehler

### Requirement: Ein Thema entspricht einem Unterricht
Ein Thema SHALL genau den Umfang eines Unterrichtsslots haben — eine
Unterrichtseinheit Theorie oder zwei Unterrichtseinheiten Praxis. Groessere
Stoffmengen MUST in mehrere Themen zerlegt werden.

#### Scenario: Thema ueberschreitet einen Slot
- **WHEN** ein Thema mehr Unterrichtseinheiten beansprucht, als sein Slot fasst
- **THEN** meldet die Pruefung einen Fehler und nennt das Thema

### Requirement: Themen tragen Jahrgangszuordnung und Voraussetzungen
Jedes Thema SHALL angeben, in welchem Jahrgang es unterrichtet wird und fuer welchen
Jahrgang es Voraussetzung ist. Voraussetzungen zwischen Themen SHALL als Verweis auf
Themen-IDs ausgedrueckt werden, nicht als Text.

#### Scenario: Planung eines Themas ohne vorhandene Lernressource
- **WHEN** ein Thema im Modell angelegt wird, bevor seine Lernressource existiert
- **THEN** ist es in Jahresplanung, Mindmap und UE-Uebersicht sichtbar und als offen
  erkennbar

### Requirement: Themen tragen einen Bearbeitungsstand
Jedes Thema SHALL einen Bearbeitungsstand tragen: geplant oder fertig. Geplant SHALL der
Standard sein. Die Pruefungen, die eine vollstaendige Lernressource verlangen, SHALL nur
fuer fertige Themen gelten; Pruefungen auf verwaiste Dateien und unbekannte Themen-IDs
SHALL unabhaengig vom Bearbeitungsstand gelten.

#### Scenario: Geplantes Thema ohne Lernressource
- **WHEN** ein Thema geplant ist und seine Lernressource noch nicht existiert
- **THEN** schlaegt die Pruefung nicht fehl, und das Thema ist in den abgeleiteten
  Darstellungen als offen erkennbar

#### Scenario: Thema wird auf fertig gesetzt
- **WHEN** der Bearbeitungsstand eines Themas auf fertig wechselt
- **THEN** verlangt die Pruefung ab diesem Zeitpunkt die vollstaendige Lernressource

#### Scenario: Datei ohne bekanntes Thema
- **WHEN** eine Datei unter `modules/` keinem Thema zugeordnet ist
- **THEN** schlaegt die Pruefung fehl, unabhaengig vom Bearbeitungsstand der Themen

### Requirement: Das Modell ist die Grundlage abgeleiteter Darstellungen
Jahresuebersicht, Stoffstruktur-Darstellung, Website-Navigation und Fragenkatalog-Tags
SHALL aus dem Modell abgeleitet werden und MUST NOT unabhaengig gepflegt werden.

#### Scenario: Thema wird verschoben
- **WHEN** die Unterrichtsnummer eines Themas geaendert wird
- **THEN** aendern sich alle abgeleiteten Darstellungen beim naechsten Build ohne
  weitere Handarbeit
