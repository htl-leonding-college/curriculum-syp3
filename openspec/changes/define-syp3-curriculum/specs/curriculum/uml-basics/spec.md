## Purpose

Vermittelt die im dritten Jahrgang tragenden UML-Diagrammarten auf Überblicksniveau und
mit den Notationselementen, die das Projekt braucht, durchgehend als versionierbarer
Diagramm-Quelltext statt als Zeichnung.

## ADDED Requirements

### Requirement: Diagrammtypen einordnen
Der Schüler SHALL die Diagrammtypen der UML nach Struktur-, Verhaltens- und
Interaktionsdiagrammen gliedern und die im Projekt verwendeten darin verorten können.

#### Scenario: Unbekannter Diagrammtyp
- **WHEN** dem Schüler ein Diagrammtyp begegnet, der im Unterricht nicht behandelt wurde
- **THEN** ordnet er ihn mit Hilfe der Übersicht seiner Diagrammart zu

### Requirement: Klassendiagramm als Domain Object Model erstellen und lesen
Der Schüler SHALL die fachlichen Entitäten seines Projekts als Klassendiagramm ohne
technische Klassen und ohne Operationen modellieren und ein Objektdiagramm als
Momentaufnahme dazu angeben können.

#### Scenario: Beziehung wird modelliert
- **WHEN** zwei Entitäten in Beziehung stehen
- **THEN** gibt der Schüler die Art der Beziehung, ihren Namen und die Multiplizitäten an

#### Scenario: Beziehung mit eigenen Daten
- **WHEN** eine m:n-Beziehung eigene Attribute trägt, etwa Beginn und Ende einer Ausleihe
- **THEN** modelliert der Schüler sie als Assoziationsklasse, wie er es im ERD mit
  einer Zwischentabelle täte

#### Scenario: Technische Klasse im Modell
- **WHEN** im Entwurf eine Klasse wie Controller, Service oder Repository auftaucht
- **THEN** erkennt der Schüler, dass sie nicht ins Domain Object Model gehört

#### Scenario: Momentaufnahme zu einem Modell
- **WHEN** der Schüler ein Klassendiagramm durch ein Beispiel erläutern soll
- **THEN** gibt er ein Objektdiagramm mit konkreten Ausprägungen an

### Requirement: Anwendungsfalldiagramm erstellen und lesen
Der Schüler SHALL für sein Projekt ein Anwendungsfalldiagramm erstellen können, das
Akteure, Anwendungsfälle und Systemgrenze korrekt unterscheidet, und den Unterschied
zur User Story benennen können.

#### Scenario: Systemgrenze wird gezogen
- **WHEN** der Schüler sein Projekt modelliert
- **THEN** stehen Akteure außerhalb und Anwendungsfälle innerhalb der Systemgrenze

#### Scenario: Use Case oder User Story
- **WHEN** der Schüler Use Case und User Story vergleichen soll
- **THEN** nennt er, dass der Use Case das Zusammenspiel von Akteur und System
  vollständig beschreibt, die User Story dagegen einen Wunsch aus Nutzersicht als
  planbare Einheit im Backlog festhält

### Requirement: Aktivitäts- und Zustandsdiagramm mit Grundelementen
Der Schüler SHALL einen Ablauf als Aktivitätsdiagramm darstellen können, einschließlich
Verzweigung, Zusammenführung und paralleler Zweige, und ein Zustandsdiagramm aus
Zuständen und Übergängen lesen können. Notationselemente über die Grundelemente hinaus
MUST NOT verlangt werden.

#### Scenario: Ablauf mit Entscheidung
- **WHEN** ein Ablauf eine Fallunterscheidung enthält
- **THEN** stellt der Schüler sie als Verzweigung mit benannten Bedingungen dar

#### Scenario: Vorgelegtes Zustandsdiagramm
- **WHEN** dem Schüler ein Zustandsdiagramm vorgelegt wird
- **THEN** benennt er Zustände, Ereignisse und Übergänge und sagt, wofür die
  Diagrammart geeignet ist

### Requirement: Architektur des Projekts darstellen
Der Schüler SHALL den Aufbau seines Projekts als Komponenten- und Verteilungsdiagramm
darstellen und als C4-Diagramm auf den Ebenen Context und Container skizzieren können.

#### Scenario: Wo läuft was
- **WHEN** das Projekt aus mehreren Containern besteht, etwa Anwendung und Datenbank
- **THEN** zeigt das Verteilungsdiagramm Knoten, Artefakte und Kommunikationspfade so,
  dass es zur `compose`-Datei des Projekts passt

#### Scenario: Systemkontext
- **WHEN** der Schüler das Projekt einem Außenstehenden erklären soll
- **THEN** zeigt er ein C4-Context-Diagramm mit Nutzern und Nachbarsystemen

### Requirement: Diagramme werden als Quelltext geführt
Der Schüler SHALL UML-Diagramme als Diagramm-Quelltext erstellen, der versioniert und im
Änderungsvergleich lesbar ist.

#### Scenario: Diagramm ändert sich im Projektverlauf
- **WHEN** ein Modell im Lauf des Projekts angepasst wird
- **THEN** ist die Änderung im Versionsvergleich nachvollziehbar, ohne die alte
  Zeichnung danebenzulegen
