## Purpose

Stellt auf den Geraeten der Schueler eine einheitliche, reproduzierbare Arbeitsumgebung
her und trennt dabei die wiederholbare Werkzeuginstallation von der einmaligen,
personenbezogenen Einrichtung.

## ADDED Requirements

### Requirement: Die Werkzeuginstallation ist wiederholbar
Die Werkzeuginstallation SHALL beliebig oft ausfuehrbar sein und bei jedem Lauf denselben
Endzustand herstellen. Jeder Schritt SHALL zuerst pruefen, ob das Werkzeug bereits
vorhanden ist.

#### Scenario: Lauf bricht ab
- **WHEN** die Installation durch Netzausfall oder Abbruch unterbrochen wird
- **THEN** setzt ein erneuter Lauf fort, ohne bereits Installiertes erneut zu installieren
  oder zu beschaedigen

#### Scenario: Lauf auf bereits eingerichtetem Geraet
- **WHEN** die Installation auf einem vollstaendig eingerichteten Geraet laeuft
- **THEN** aendert sie nichts und meldet den Zustand als hergestellt

### Requirement: Ein Ablauf fuer beide unterstuetzten Betriebssysteme
Die Werkzeugliste SHALL genau einmal beschrieben sein. Der Unterschied zwischen den
unterstuetzten Betriebssystemen SHALL sich auf das Installationsverfahren beschraenken.

#### Scenario: Werkzeug wird ergaenzt
- **WHEN** ein Werkzeug in die Liste aufgenommen wird
- **THEN** genuegt eine Ergaenzung an einer Stelle, und beide Betriebssysteme erhalten es

### Requirement: Werkzeuginstallation und persoenliche Einrichtung sind getrennt
Die wiederholbare Werkzeuginstallation SHALL von der einmaligen, interaktiven
Einrichtung persoenlicher Angaben getrennt sein. Zugangsdaten und persoenliche Angaben
MUST NOT im Repository liegen.

#### Scenario: Wiederholter Lauf nach der Ersteinrichtung
- **WHEN** die Werkzeuginstallation nach der persoenlichen Einrichtung erneut laeuft
- **THEN** bleiben Name, Adresse, Schluessel und Anmeldungen unangetastet

### Requirement: Werkzeugversionen sind an einer Stelle festgelegt
Die verwendeten Werkzeugversionen SHALL an genau einer Stelle festgelegt sein. Der Stand
eines Schuljahres SHALL nachtraeglich rekonstruierbar sein.

#### Scenario: Fehler tritt nur bei einzelnen Schuelern auf
- **WHEN** ein Problem auf einen Versionsunterschied zurueckgefuehrt werden soll
- **THEN** ist die verbindliche Version an einer Stelle nachlesbar

### Requirement: Der Einstieg erfolgt nachvollziehbar, nicht blind
Der erste Bezug der Einrichtung SHALL so ablaufen, dass die auszufuehrenden Anweisungen
vor der Ausfuehrung lesbar vorliegen. Ein Verfahren, das fremde Anweisungen ungelesen mit
erhoehten Rechten ausfuehrt, MUST NOT vorgesehen werden.

#### Scenario: Schueler richtet ein frisches System ein
- **WHEN** ein Schueler die Einrichtung zum ersten Mal ausfuehrt
- **THEN** hat er die Anweisungen zuvor lokal vorliegen und kann sie lesen

### Requirement: Die Einrichtung ist vor dem ersten Unterricht erprobt
Die Einrichtung SHALL vor dem ersten Einsatz auf einem frisch installierten System jedes
unterstuetzten Betriebssystems vollstaendig durchlaufen worden sein.

#### Scenario: Erster Praxisunterricht
- **WHEN** die Klasse die Einrichtung im Unterricht ausfuehrt
- **THEN** ist der Ablauf bereits auf beiden Betriebssystemen erprobt und ein Zeitpuffer
  fuer Stoerungen eingeplant
