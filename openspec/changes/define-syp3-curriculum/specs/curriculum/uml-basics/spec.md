## Purpose

Vermittelt die im dritten Jahrgang tragenden UML-Diagrammarten auf Überblicksniveau,
durchgehend als versionierbarer Diagramm-Quelltext statt als Zeichnung.

## ADDED Requirements

### Requirement: Anwendungsfalldiagramm erstellen und lesen
Der Schüler SHALL für sein Projekt ein Anwendungsfalldiagramm erstellen können, das
Akteure, Anwendungsfälle und Systemgrenze korrekt unterscheidet.

#### Scenario: Systemgrenze wird gezogen
- **WHEN** der Schüler sein Projekt modelliert
- **THEN** stehen Akteure außerhalb und Anwendungsfälle innerhalb der Systemgrenze

### Requirement: Klassen- und Objektdiagramm erstellen und lesen
Der Schüler SHALL ein Klassendiagramm mit Klassen, Attributen, Operationen und
Beziehungen erstellen und ein Objektdiagramm als Momentaufnahme dazu angeben können.

#### Scenario: Beziehung wird modelliert
- **WHEN** zwei Klassen in Beziehung stehen
- **THEN** gibt der Schüler die Art der Beziehung und die Multiplizitäten an

#### Scenario: Momentaufnahme zu einem Modell
- **WHEN** der Schüler ein Klassendiagramm durch ein Beispiel erläutern soll
- **THEN** gibt er ein Objektdiagramm mit konkreten Ausprägungen an

### Requirement: Aktivitätsdiagramm erstellen und lesen
Der Schüler SHALL einen Ablauf als Aktivitätsdiagramm darstellen können,
einschließlich Verzweigung, Zusammenführung und paralleler Zweige.

#### Scenario: Ablauf mit Entscheidung
- **WHEN** ein Ablauf eine Fallunterscheidung enthält
- **THEN** stellt der Schüler sie als Verzweigung mit benannten Bedingungen dar

### Requirement: Zustandsdiagramm im Überblick
Der Schüler SHALL ein Zustandsdiagramm lesen und seinen Einsatzzweck benennen können.
Eine eigenständige Modellierung MUST NOT verlangt werden.

#### Scenario: Vorgelegtes Zustandsdiagramm
- **WHEN** dem Schüler ein Zustandsdiagramm vorgelegt wird
- **THEN** benennt er Zustände, Ereignisse und Übergänge und sagt, wofür die
  Diagrammart geeignet ist

### Requirement: Diagramme werden als Quelltext geführt
Der Schüler SHALL UML-Diagramme als Diagramm-Quelltext erstellen, der versioniert und im
Änderungsvergleich lesbar ist.

#### Scenario: Diagramm ändert sich im Projektverlauf
- **WHEN** ein Modell im Lauf des Projekts angepasst wird
- **THEN** ist die Änderung im Versionsvergleich nachvollziehbar, ohne die alte
  Zeichnung danebenzulegen
