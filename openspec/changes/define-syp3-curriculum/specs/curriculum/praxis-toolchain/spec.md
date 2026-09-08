## Purpose

Vermittelt die Werkzeugkette, mit der die Schüler ihr Projekt und dessen Dokumentation
gemeinsam bearbeiten, versionieren und veröffentlichen.

## ADDED Requirements

### Requirement: Versionsverwaltung im Alleingang
Der Schüler SHALL ein Repository anlegen, Änderungen in nachvollziehbaren Schritten
festhalten, die Historie lesen und einen früheren Stand wiederherstellen können.

#### Scenario: Fehlerhafte Änderung
- **WHEN** eine Änderung sich als falsch erweist
- **THEN** stellt der Schüler den vorherigen Stand wieder her, ohne Arbeit von Hand
  rückgängig zu machen

### Requirement: Parallele Arbeit über Zweige
Der Schüler SHALL Arbeit in einem eigenen Zweig führen und zusammenführen können.

#### Scenario: Zwei Teammitglieder arbeiten gleichzeitig
- **WHEN** zwei Teammitglieder zur selben Zeit an unterschiedlichen Themen arbeiten
- **THEN** behindern sie einander nicht, und beide Ergebnisse gelangen in den Hauptstand

### Requirement: Änderungen werden vor der Übernahme begutachtet
Der Schüler SHALL eine Änderung zur Begutachtung vorlegen, fremde Änderungen
begutachten und Rückmeldung einarbeiten können.

#### Scenario: Änderung eines Teammitglieds
- **WHEN** ein Teammitglied eine Änderung vorlegt
- **THEN** liest ein anderes sie, gibt Rückmeldung, und erst danach gelangt sie in den
  Hauptstand

### Requirement: Konflikte werden aufgelöst
Der Schüler SHALL einen Konflikt zwischen gleichzeitigen Änderungen erkennen und
inhaltlich auflösen können, statt eine Seite blind zu verwerfen.

#### Scenario: Dieselbe Stelle wurde zweimal geändert
- **WHEN** zwei Änderungen dieselbe Stelle betreffen
- **THEN** entscheidet der Schüler inhaltlich und begründet die Auflösung

### Requirement: Dokumentation entsteht als Text neben dem Projekt
Der Schüler SHALL die Projektdokumentation als strukturierten Text im selben Repository
führen, einschließlich eingebetteter Diagramme.

#### Scenario: Projektdokumentation am Jahresende
- **WHEN** die Dokumentation abgegeben wird
- **THEN** ist sie über das Jahr mitgewachsen und in der Historie nachvollziehbar,
  statt am Ende entstanden zu sein

### Requirement: Veröffentlichung läuft automatisch
Der Schüler SHALL eine Automatisierung einrichten können, die aus dem Text bei jeder
Änderung eine Website erzeugt und veröffentlicht.

#### Scenario: Änderung wird eingebracht
- **WHEN** der Schüler eine Änderung an der Dokumentation einbringt
- **THEN** ist sie ohne weiteren Handgriff als Website erreichbar

### Requirement: Präsentationen entstehen aus derselben Quelle
Der Schüler SHALL aus seinem Dokumentationstext eine Präsentation erzeugen können,
ohne die Inhalte ein zweites Mal zu pflegen.

#### Scenario: Meilenstein-Präsentation
- **WHEN** ein Zwischenstand präsentiert wird
- **THEN** stammt die Präsentation aus derselben Quelle wie die Dokumentation

### Requirement: Eine neutrale Bauumgebung entscheidet Streitfälle
Der Schüler SHALL erklären können, warum eine einheitliche automatische Bauumgebung
darüber entscheidet, ob etwas funktioniert, und nicht das eigene Gerät.

#### Scenario: Unterschiedliches Verhalten auf zwei Geräten
- **WHEN** ein Ergebnis auf einem Gerät funktioniert und auf einem anderen nicht
- **THEN** gilt das Ergebnis der automatischen Bauumgebung als maßgeblich
