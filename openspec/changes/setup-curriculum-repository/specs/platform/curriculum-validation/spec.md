## Purpose

Koppelt Curriculum-Modell und Lernressourcen durch automatisierte Pruefungen, sodass
Abweichungen beim Build auffallen statt im Unterrichtsjahr.

## ADDED Requirements

### Requirement: Bijektion zwischen Modell und Lernressourcen
Die Pruefung SHALL sicherstellen, dass jedes fertige Thema mindestens eine existierende
Lernressource hat und jede Lernressource genau einem Thema zugeordnet ist. Fuer geplante
Themen SHALL keine Lernressource verlangt werden.

#### Scenario: Fertiges Thema ohne Datei
- **WHEN** ein als fertig gekennzeichnetes Thema eine Ressource nennt, die im Dateisystem
  fehlt
- **THEN** schlaegt die Pruefung fehl und nennt Thema und erwarteten Pfad

#### Scenario: Geplantes Thema ohne Datei
- **WHEN** ein geplantes Thema noch keine Lernressource hat
- **THEN** schlaegt die Pruefung nicht fehl

#### Scenario: Verwaiste Lernressource
- **WHEN** eine Datei unter `modules/` keinem Thema zugeordnet ist
- **THEN** schlaegt die Pruefung fehl und nennt die Datei

### Requirement: Unterrichtseinheiten-Budget wird eingehalten
Die Pruefung SHALL die Summe der Unterrichtseinheiten je Art und je Block gegen die im
Curriculum festgelegten Budgets pruefen.

#### Scenario: Budget ueberschritten
- **WHEN** die Summe der Theorie-Einheiten das festgelegte Budget uebersteigt
- **THEN** schlaegt die Pruefung fehl und nennt Ist- und Sollwert

### Requirement: Voraussetzungsgraph ist gueltig
Die Pruefung SHALL sicherstellen, dass Voraussetzungen nur auf existierende Themen
zeigen, dass keine Zyklen bestehen und dass jede Voraussetzung frueher unterrichtet wird
als das Thema, das sie voraussetzt.

#### Scenario: Vorwaertsreferenz durch Umplanung
- **WHEN** ein Thema so verschoben wird, dass eine seiner Voraussetzungen danach liegt
- **THEN** schlaegt die Pruefung fehl und nennt beide Themen mit ihren
  Unterrichtsnummern

#### Scenario: Zyklische Voraussetzung
- **WHEN** zwei Themen sich gegenseitig voraussetzen
- **THEN** schlaegt die Pruefung fehl und nennt den Zyklus

### Requirement: Slot-Belegung ist eindeutig und lueckenlos
Die Pruefung SHALL sicherstellen, dass je Unterricht hoechstens ein Theorie-Thema und
hoechstens ein Praxis-Thema liegt und dass zwischen dem ersten und dem letzten belegten
Unterricht keine Luecke bleibt.

#### Scenario: Zwei Theoriethemen im selben Unterricht
- **WHEN** zwei Themen mit Art Theorie dieselbe Unterrichtsnummer tragen
- **THEN** schlaegt die Pruefung fehl und nennt beide Themen

#### Scenario: Unterricht ohne Thema
- **WHEN** eine Unterrichtsnummer innerhalb der belegten Spanne kein Thema traegt
- **THEN** schlaegt die Pruefung fehl und nennt die Nummer

### Requirement: Pflichtabschnitte der Lernressource sind vorhanden
Die Pruefung SHALL sicherstellen, dass jede Lernressource eines fertigen Themas die
Pflichtabschnitte
`Learning outcomes`, `Decisions`, `Pitfalls` und `Terminology` enthaelt und dass keiner
davon leer ist. Eine ausdrueckliche Nullaussage SHALL als erfuellt gelten.

#### Scenario: Abschnitt fehlt
- **WHEN** eine Lernressource keinen Abschnitt `Decisions` enthaelt
- **THEN** schlaegt die Pruefung fehl und nennt Datei und fehlenden Abschnitt

#### Scenario: Ausdrueckliche Nullaussage
- **WHEN** ein Pflichtabschnitt nur eine ausdrueckliche Nullaussage enthaelt
- **THEN** gilt die Pruefung als erfuellt

### Requirement: Lernziele und Pruefungsfragen sind gekoppelt
Die Pruefung SHALL sicherstellen, dass jedes Lernziel einer Lernressource eines fertigen
Themas mindestens
eine zugehoerige Pruefungsfrage hat und dass jede Pruefungsfrage auf ein existierendes
Lernziel verweist.

#### Scenario: Lernziel ohne Frage
- **WHEN** ein Lernziel ergaenzt wird, ohne eine Frage nachzuziehen
- **THEN** schlaegt die Pruefung fehl und nennt das Lernziel

#### Scenario: Frage ohne Lernziel
- **WHEN** eine Pruefungsfrage auf ein Lernziel verweist, das es nicht gibt
- **THEN** schlaegt die Pruefung fehl und nennt die Frage

### Requirement: Bilder tragen eine Herkunftsklasse
Die Pruefung SHALL sicherstellen, dass jedes eingebundene Bild einer Lernressource genau
eine Herkunftsklasse traegt. Zulaessig SHALL sein: eigenes Werk, freie Lizenz oder
ungeklaert. Bei freier Lizenz MUST Lizenzname und Quelladresse angegeben sein.

#### Scenario: Bild ohne Herkunftsangabe
- **WHEN** ein Bild ohne Herkunftsklasse eingebunden wird
- **THEN** schlaegt die Pruefung fehl und nennt Datei und Zeile

#### Scenario: Freie Lizenz ohne Quelle
- **WHEN** ein Bild als frei lizenziert gekennzeichnet ist, aber Lizenzname oder
  Quelladresse fehlt
- **THEN** schlaegt die Pruefung fehl

### Requirement: Modulskelett ist einheitlich
Die Pruefung SHALL sicherstellen, dass jedes Modulverzeichnis eines fertigen Themas die
Dateien fuer Inhalt, Aufgaben und Pruefungsfragen enthaelt. Die Aufgabendatei MAY
inhaltsleer sein. Fuer fertige Themen der Art Praxis SHALL mindestens eine
Pruefungsfrage vorhanden sein.

#### Scenario: Datei fehlt im Modul
- **WHEN** ein Modulverzeichnis keine Aufgabendatei enthaelt
- **THEN** schlaegt die Pruefung fehl und nennt das Modul

#### Scenario: Praxisthema ohne Pruefungsfrage
- **WHEN** ein Thema der Art Praxis keine Pruefungsfrage hat
- **THEN** schlaegt die Pruefung fehl

### Requirement: Die Pruefung ist Pflichtschritt der Pipeline
Die Pruefung SHALL bei jeder Aenderung automatisch laufen. Ein Fehlschlag MUST die
Veroeffentlichung verhindern, mit Ausnahme der Rechteklaerung, die gesondert geregelt
ist.

#### Scenario: Fehlerhafte Aenderung wird eingebracht
- **WHEN** eine Aenderung eine der Pruefungen verletzt
- **THEN** bricht der Build ab und die veroeffentlichte Site bleibt auf dem letzten
  gueltigen Stand
