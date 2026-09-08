## Purpose

Bildet die Stoffstruktur eines Jahrgangs als maschinenlesbares Modell ab — Themen,
Umfang, Reihenfolge, Jahrgangszuordnung und Voraussetzungen — und ist die einzige Quelle
dieser Angaben.

## ADDED Requirements

### Requirement: Strukturangaben stehen ausschließlich im Modell
Das Curriculum-Modell SHALL die einzige Quelle für Themenzuschnitt, Umfang in
Unterrichtseinheiten, Blockzuordnung, Unterrichtsnummer, Jahrgangszuordnung und
Voraussetzungen sein. Eine Lernressource SHALL außer ihrer Themen-ID keine
Strukturangabe tragen.

#### Scenario: Strukturangabe im AsciiDoc
- **WHEN** eine Datei unter `modules/` ein Attribut mit UE-Zahl, Block, Jahrgang oder
  Voraussetzung trägt
- **THEN** meldet die Prüfung einen Fehler und nennt Datei und Attribut

#### Scenario: Umfang wird geändert
- **WHEN** die UE-Zahl eines Themas geändert wird
- **THEN** genügt eine Änderung im Modell, und keine Lernressource muss angefasst werden

### Requirement: Themen und Lernressourcen sind über eine ID gekoppelt
Jedes Thema SHALL eine eindeutige, unveränderliche ID tragen. Jede Lernressource SHALL
genau eine Themen-ID nennen, und jede genannte ID SHALL im Modell existieren.

#### Scenario: Ressource ohne Themen-ID
- **WHEN** eine Datei unter `modules/` keine Themen-ID trägt
- **THEN** meldet die Prüfung einen Fehler

#### Scenario: Themen-ID ohne Eintrag im Modell
- **WHEN** eine Lernressource eine ID nennt, die im Modell nicht vorkommt
- **THEN** meldet die Prüfung einen Fehler

### Requirement: Ein Thema entspricht einem Unterricht
Ein Thema SHALL genau den Umfang eines Unterrichtsslots haben — eine
Unterrichtseinheit Theorie oder zwei Unterrichtseinheiten Praxis. Größere
Stoffmengen MUST in mehrere Themen zerlegt werden.

#### Scenario: Thema überschreitet einen Slot
- **WHEN** ein Thema mehr Unterrichtseinheiten beansprucht, als sein Slot fasst
- **THEN** meldet die Prüfung einen Fehler und nennt das Thema

### Requirement: Themen tragen Jahrgangszuordnung und Voraussetzungen
Jedes Thema SHALL angeben, in welchem Jahrgang es unterrichtet wird und für welchen
Jahrgang es Voraussetzung ist. Voraussetzungen zwischen Themen SHALL als Verweis auf
Themen-IDs ausgedrückt werden, nicht als Text.

#### Scenario: Planung eines Themas ohne vorhandene Lernressource
- **WHEN** ein Thema im Modell angelegt wird, bevor seine Lernressource existiert
- **THEN** ist es in Jahresplanung, Mindmap und UE-Übersicht sichtbar und als offen
  erkennbar

### Requirement: Themen tragen einen Bearbeitungsstand
Jedes Thema SHALL einen Bearbeitungsstand tragen: geplant oder fertig. Geplant SHALL der
Standard sein. Die Prüfungen, die eine vollständige Lernressource verlangen, SHALL nur
für fertige Themen gelten; Prüfungen auf verwaiste Dateien und unbekannte Themen-IDs
SHALL unabhängig vom Bearbeitungsstand gelten.

#### Scenario: Geplantes Thema ohne Lernressource
- **WHEN** ein Thema geplant ist und seine Lernressource noch nicht existiert
- **THEN** schlägt die Prüfung nicht fehl, und das Thema ist in den abgeleiteten
  Darstellungen als offen erkennbar

#### Scenario: Thema wird auf fertig gesetzt
- **WHEN** der Bearbeitungsstand eines Themas auf fertig wechselt
- **THEN** verlangt die Prüfung ab diesem Zeitpunkt die vollständige Lernressource

#### Scenario: Datei ohne bekanntes Thema
- **WHEN** eine Datei unter `modules/` keinem Thema zugeordnet ist
- **THEN** schlägt die Prüfung fehl, unabhängig vom Bearbeitungsstand der Themen

### Requirement: Das Modell ist die Grundlage abgeleiteter Darstellungen
Jahresübersicht, Stoffstruktur-Darstellung, Website-Navigation und Fragenkatalog-Tags
SHALL aus dem Modell abgeleitet werden und MUST NOT unabhängig gepflegt werden.

#### Scenario: Thema wird verschoben
- **WHEN** die Unterrichtsnummer eines Themas geändert wird
- **THEN** ändern sich alle abgeleiteten Darstellungen beim nächsten Build ohne
  weitere Handarbeit
