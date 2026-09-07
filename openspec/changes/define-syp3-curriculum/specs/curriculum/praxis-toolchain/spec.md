## Purpose

Vermittelt die Werkzeugkette, mit der die Schueler ihr Projekt und dessen Dokumentation
gemeinsam bearbeiten, versionieren und veroeffentlichen.

## ADDED Requirements

### Requirement: Versionsverwaltung im Alleingang
Der Schueler SHALL ein Repository anlegen, Aenderungen in nachvollziehbaren Schritten
festhalten, die Historie lesen und einen frueheren Stand wiederherstellen koennen.

#### Scenario: Fehlerhafte Aenderung
- **WHEN** eine Aenderung sich als falsch erweist
- **THEN** stellt der Schueler den vorherigen Stand wieder her, ohne Arbeit von Hand
  rueckgaengig zu machen

### Requirement: Parallele Arbeit ueber Zweige
Der Schueler SHALL Arbeit in einem eigenen Zweig fuehren und zusammenfuehren koennen.

#### Scenario: Zwei Teammitglieder arbeiten gleichzeitig
- **WHEN** zwei Teammitglieder zur selben Zeit an unterschiedlichen Themen arbeiten
- **THEN** behindern sie einander nicht, und beide Ergebnisse gelangen in den Hauptstand

### Requirement: Aenderungen werden vor der Uebernahme begutachtet
Der Schueler SHALL eine Aenderung zur Begutachtung vorlegen, fremde Aenderungen
begutachten und Rueckmeldung einarbeiten koennen.

#### Scenario: Aenderung eines Teammitglieds
- **WHEN** ein Teammitglied eine Aenderung vorlegt
- **THEN** liest ein anderes sie, gibt Rueckmeldung, und erst danach gelangt sie in den
  Hauptstand

### Requirement: Konflikte werden aufgeloest
Der Schueler SHALL einen Konflikt zwischen gleichzeitigen Aenderungen erkennen und
inhaltlich aufloesen koennen, statt eine Seite blind zu verwerfen.

#### Scenario: Dieselbe Stelle wurde zweimal geaendert
- **WHEN** zwei Aenderungen dieselbe Stelle betreffen
- **THEN** entscheidet der Schueler inhaltlich und begruendet die Aufloesung

### Requirement: Dokumentation entsteht als Text neben dem Projekt
Der Schueler SHALL die Projektdokumentation als strukturierten Text im selben Repository
fuehren, einschliesslich eingebetteter Diagramme.

#### Scenario: Projektdokumentation am Jahresende
- **WHEN** die Dokumentation abgegeben wird
- **THEN** ist sie ueber das Jahr mitgewachsen und in der Historie nachvollziehbar,
  statt am Ende entstanden zu sein

### Requirement: Veroeffentlichung laeuft automatisch
Der Schueler SHALL eine Automatisierung einrichten koennen, die aus dem Text bei jeder
Aenderung eine Website erzeugt und veroeffentlicht.

#### Scenario: Aenderung wird eingebracht
- **WHEN** der Schueler eine Aenderung an der Dokumentation einbringt
- **THEN** ist sie ohne weiteren Handgriff als Website erreichbar

### Requirement: Praesentationen entstehen aus derselben Quelle
Der Schueler SHALL aus seinem Dokumentationstext eine Praesentation erzeugen koennen,
ohne die Inhalte ein zweites Mal zu pflegen.

#### Scenario: Meilenstein-Praesentation
- **WHEN** ein Zwischenstand praesentiert wird
- **THEN** stammt die Praesentation aus derselben Quelle wie die Dokumentation

### Requirement: Eine neutrale Bauumgebung entscheidet Streitfaelle
Der Schueler SHALL erklaeren koennen, warum eine einheitliche automatische Bauumgebung
darueber entscheidet, ob etwas funktioniert, und nicht das eigene Geraet.

#### Scenario: Unterschiedliches Verhalten auf zwei Geraeten
- **WHEN** ein Ergebnis auf einem Geraet funktioniert und auf einem anderen nicht
- **THEN** gilt das Ergebnis der automatischen Bauumgebung als massgeblich
