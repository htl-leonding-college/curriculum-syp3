## Purpose

Vermittelt die im dritten Jahrgang tragenden UML-Diagrammarten auf Ueberblicksniveau,
durchgehend als versionierbarer Diagramm-Quelltext statt als Zeichnung.

## ADDED Requirements

### Requirement: Anwendungsfalldiagramm erstellen und lesen
Der Schueler SHALL fuer sein Projekt ein Anwendungsfalldiagramm erstellen koennen, das
Akteure, Anwendungsfaelle und Systemgrenze korrekt unterscheidet.

#### Scenario: Systemgrenze wird gezogen
- **WHEN** der Schueler sein Projekt modelliert
- **THEN** stehen Akteure ausserhalb und Anwendungsfaelle innerhalb der Systemgrenze

### Requirement: Klassen- und Objektdiagramm erstellen und lesen
Der Schueler SHALL ein Klassendiagramm mit Klassen, Attributen, Operationen und
Beziehungen erstellen und ein Objektdiagramm als Momentaufnahme dazu angeben koennen.

#### Scenario: Beziehung wird modelliert
- **WHEN** zwei Klassen in Beziehung stehen
- **THEN** gibt der Schueler die Art der Beziehung und die Multiplizitaeten an

#### Scenario: Momentaufnahme zu einem Modell
- **WHEN** der Schueler ein Klassendiagramm durch ein Beispiel erlaeutern soll
- **THEN** gibt er ein Objektdiagramm mit konkreten Auspraegungen an

### Requirement: Aktivitaetsdiagramm erstellen und lesen
Der Schueler SHALL einen Ablauf als Aktivitaetsdiagramm darstellen koennen,
einschliesslich Verzweigung, Zusammenfuehrung und paralleler Zweige.

#### Scenario: Ablauf mit Entscheidung
- **WHEN** ein Ablauf eine Fallunterscheidung enthaelt
- **THEN** stellt der Schueler sie als Verzweigung mit benannten Bedingungen dar

### Requirement: Zustandsdiagramm im Ueberblick
Der Schueler SHALL ein Zustandsdiagramm lesen und seinen Einsatzzweck benennen koennen.
Eine eigenstaendige Modellierung MUST NOT verlangt werden.

#### Scenario: Vorgelegtes Zustandsdiagramm
- **WHEN** dem Schueler ein Zustandsdiagramm vorgelegt wird
- **THEN** benennt er Zustaende, Ereignisse und Uebergaenge und sagt, wofuer die
  Diagrammart geeignet ist

### Requirement: Diagramme werden als Quelltext gefuehrt
Der Schueler SHALL UML-Diagramme als Diagramm-Quelltext erstellen, der versioniert und im
Aenderungsvergleich lesbar ist.

#### Scenario: Diagramm aendert sich im Projektverlauf
- **WHEN** ein Modell im Lauf des Projekts angepasst wird
- **THEN** ist die Aenderung im Versionsvergleich nachvollziehbar, ohne die alte
  Zeichnung danebenzulegen
