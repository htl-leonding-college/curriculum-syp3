## Purpose

Vermittelt Containerisierung als reproduzierbare Beschreibung einer Laufzeitumgebung —
vom einzelnen Abbild über Anwendungen aus mehreren Diensten bis zum lokalen Betrieb
eines Orchestrierers.

## ADDED Requirements

### Requirement: Container-Grundlagen
Der Schüler SHALL erklären können, welches Problem Container lösen, und ein Abbild
aus einer Beschreibungsdatei erzeugen und ausführen können.

#### Scenario: Anwendung auf fremdem Gerät
- **WHEN** eine Anwendung auf einem Gerät laufen soll, auf dem sie nie eingerichtet wurde
- **THEN** genügt das Abbild, und keine Einrichtung von Hand ist nötig

### Requirement: Daten und Konfiguration überleben den Container
Der Schüler SHALL unterscheiden können, was im Abbild liegt und was außerhalb gehalten
werden muss, und beides entsprechend einrichten.

#### Scenario: Container wird ersetzt
- **WHEN** ein Container durch eine neue Version ersetzt wird
- **THEN** bleiben die Daten erhalten, und die Konfiguration muss nicht neu eingegeben
  werden

### Requirement: Abbilder laufen auf unterschiedlichen Prozessorarchitekturen
Der Schüler SHALL erkennen können, dass ein Abbild an die Architektur des erzeugenden
Geräts gebunden sein kann, und ein Abbild für mehrere Architekturen erzeugen können.

#### Scenario: Abbild vom Notebook läuft auf dem Server nicht
- **WHEN** ein auf einem Gerät mit anderer Architektur erzeugtes Abbild anderswo starten
  soll
- **THEN** erkennt der Schüler die Ursache und erzeugt ein Abbild für beide
  Architekturen

### Requirement: Anwendungen aus mehreren Diensten
Der Schüler SHALL eine Anwendung aus mehreren zusammenwirkenden Diensten als eine
Beschreibung definieren und gemeinsam starten können, einschließlich Netzwerk,
Abhängigkeiten und Startreihenfolge.

#### Scenario: Anwendung mit Datenbank
- **WHEN** eine Anwendung eine Datenbank benötigt
- **THEN** startet ein einziger Befehl beide Dienste in der richtigen Reihenfolge

### Requirement: Orchestrierung im lokalen Überblick
Der Schüler SHALL die Grundbegriffe eines Orchestrierers benennen und eine Anwendung
lokal darauf betreiben können, sofern die Reservezone des Jahresplans nicht durch
Terminausfälle aufgebraucht ist.

#### Scenario: Reservezone bleibt erhalten
- **WHEN** keine wesentlichen Termine ausgefallen sind
- **THEN** betreibt der Schüler eine Anwendung lokal auf dem Orchestrierer

#### Scenario: Reservezone entfällt
- **WHEN** Termine ausgefallen sind und die Reservezone aufgebraucht ist
- **THEN** entfällt dieser Inhalt, ohne dass Kerninhalte des Jahres betroffen sind
