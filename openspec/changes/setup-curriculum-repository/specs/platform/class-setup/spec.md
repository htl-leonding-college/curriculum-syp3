## Purpose

Stellt auf den Geräten der Schüler eine einheitliche, reproduzierbare Arbeitsumgebung
her und trennt dabei die wiederholbare Werkzeuginstallation von der einmaligen,
personenbezogenen Einrichtung.

## ADDED Requirements

### Requirement: Die Werkzeuginstallation ist wiederholbar
Die Werkzeuginstallation SHALL beliebig oft ausführbar sein und bei jedem Lauf denselben
Endzustand herstellen. Jeder Schritt SHALL zuerst prüfen, ob das Werkzeug bereits
vorhanden ist.

#### Scenario: Lauf bricht ab
- **WHEN** die Installation durch Netzausfall oder Abbruch unterbrochen wird
- **THEN** setzt ein erneuter Lauf fort, ohne bereits Installiertes erneut zu installieren
  oder zu beschädigen

#### Scenario: Lauf auf bereits eingerichtetem Gerät
- **WHEN** die Installation auf einem vollständig eingerichteten Gerät läuft
- **THEN** ändert sie nichts und meldet den Zustand als hergestellt

### Requirement: Ein Ablauf für beide unterstützten Betriebssysteme
Die Werkzeugliste SHALL genau einmal beschrieben sein. Der Unterschied zwischen den
unterstützten Betriebssystemen SHALL sich auf das Installationsverfahren beschränken.

#### Scenario: Werkzeug wird ergänzt
- **WHEN** ein Werkzeug in die Liste aufgenommen wird
- **THEN** genügt eine Ergänzung an einer Stelle, und beide Betriebssysteme erhalten es

### Requirement: Werkzeuginstallation und persönliche Einrichtung sind getrennt
Die wiederholbare Werkzeuginstallation SHALL von der einmaligen, interaktiven
Einrichtung persönlicher Angaben getrennt sein. Zugangsdaten und persönliche Angaben
MUST NOT im Repository liegen.

#### Scenario: Wiederholter Lauf nach der Ersteinrichtung
- **WHEN** die Werkzeuginstallation nach der persönlichen Einrichtung erneut läuft
- **THEN** bleiben Name, Adresse, Schlüssel und Anmeldungen unangetastet

### Requirement: Werkzeugversionen sind an einer Stelle festgelegt
Die verwendeten Werkzeugversionen SHALL an genau einer Stelle festgelegt sein. Der Stand
eines Schuljahres SHALL nachträglich rekonstruierbar sein.

#### Scenario: Fehler tritt nur bei einzelnen Schülern auf
- **WHEN** ein Problem auf einen Versionsunterschied zurückgeführt werden soll
- **THEN** ist die verbindliche Version an einer Stelle nachlesbar

### Requirement: Der Einstieg erfolgt nachvollziehbar, nicht blind
Der erste Bezug der Einrichtung SHALL so ablaufen, dass die auszuführenden Anweisungen
vor der Ausführung lesbar vorliegen. Ein Verfahren, das fremde Anweisungen ungelesen mit
erhöhten Rechten ausführt, MUST NOT vorgesehen werden.

#### Scenario: Schüler richtet ein frisches System ein
- **WHEN** ein Schüler die Einrichtung zum ersten Mal ausführt
- **THEN** hat er die Anweisungen zuvor lokal vorliegen und kann sie lesen

### Requirement: Die Einrichtung ist vor dem ersten Unterricht erprobt
Die Einrichtung SHALL vor dem ersten Einsatz auf einem frisch installierten System jedes
unterstützten Betriebssystems vollständig durchlaufen worden sein.

#### Scenario: Erster Praxisunterricht
- **WHEN** die Klasse die Einrichtung im Unterricht ausführt
- **THEN** ist der Ablauf bereits auf beiden Betriebssystemen erprobt und ein Zeitpuffer
  für Störungen eingeplant
