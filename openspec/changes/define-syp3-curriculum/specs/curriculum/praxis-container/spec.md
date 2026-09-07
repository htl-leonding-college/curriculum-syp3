## Purpose

Vermittelt Containerisierung als reproduzierbare Beschreibung einer Laufzeitumgebung —
vom einzelnen Abbild ueber Anwendungen aus mehreren Diensten bis zum lokalen Betrieb
eines Orchestrierers.

## ADDED Requirements

### Requirement: Container-Grundlagen
Der Schueler SHALL erklaeren koennen, welches Problem Container loesen, und ein Abbild
aus einer Beschreibungsdatei erzeugen und ausfuehren koennen.

#### Scenario: Anwendung auf fremdem Geraet
- **WHEN** eine Anwendung auf einem Geraet laufen soll, auf dem sie nie eingerichtet wurde
- **THEN** genuegt das Abbild, und keine Einrichtung von Hand ist noetig

### Requirement: Daten und Konfiguration ueberleben den Container
Der Schueler SHALL unterscheiden koennen, was im Abbild liegt und was ausserhalb gehalten
werden muss, und beides entsprechend einrichten.

#### Scenario: Container wird ersetzt
- **WHEN** ein Container durch eine neue Version ersetzt wird
- **THEN** bleiben die Daten erhalten, und die Konfiguration muss nicht neu eingegeben
  werden

### Requirement: Abbilder laufen auf unterschiedlichen Prozessorarchitekturen
Der Schueler SHALL erkennen koennen, dass ein Abbild an die Architektur des erzeugenden
Geraets gebunden sein kann, und ein Abbild fuer mehrere Architekturen erzeugen koennen.

#### Scenario: Abbild vom Notebook laeuft auf dem Server nicht
- **WHEN** ein auf einem Geraet mit anderer Architektur erzeugtes Abbild anderswo starten
  soll
- **THEN** erkennt der Schueler die Ursache und erzeugt ein Abbild fuer beide
  Architekturen

### Requirement: Anwendungen aus mehreren Diensten
Der Schueler SHALL eine Anwendung aus mehreren zusammenwirkenden Diensten als eine
Beschreibung definieren und gemeinsam starten koennen, einschliesslich Netzwerk,
Abhaengigkeiten und Startreihenfolge.

#### Scenario: Anwendung mit Datenbank
- **WHEN** eine Anwendung eine Datenbank benoetigt
- **THEN** startet ein einziger Befehl beide Dienste in der richtigen Reihenfolge

### Requirement: Orchestrierung im lokalen Ueberblick
Der Schueler SHALL die Grundbegriffe eines Orchestrierers benennen und eine Anwendung
lokal darauf betreiben koennen, sofern die Reservezone des Jahresplans nicht durch
Terminausfaelle aufgebraucht ist.

#### Scenario: Reservezone bleibt erhalten
- **WHEN** keine wesentlichen Termine ausgefallen sind
- **THEN** betreibt der Schueler eine Anwendung lokal auf dem Orchestrierer

#### Scenario: Reservezone entfaellt
- **WHEN** Termine ausgefallen sind und die Reservezone aufgebraucht ist
- **THEN** entfaellt dieser Inhalt, ohne dass Kerninhalte des Jahres betroffen sind
