## Purpose

Koppelt Curriculum-Modell und Lernressourcen durch automatisierte Prüfungen, sodass
Abweichungen beim Build auffallen statt im Unterrichtsjahr.

## ADDED Requirements

### Requirement: Bijektion zwischen Modell und Lernressourcen
Die Prüfung SHALL sicherstellen, dass jedes fertige Thema mindestens eine existierende
Lernressource hat und jede Lernressource genau einem Thema zugeordnet ist. Für geplante
Themen SHALL keine Lernressource verlangt werden.

#### Scenario: Fertiges Thema ohne Datei
- **WHEN** ein als fertig gekennzeichnetes Thema eine Ressource nennt, die im Dateisystem
  fehlt
- **THEN** schlägt die Prüfung fehl und nennt Thema und erwarteten Pfad

#### Scenario: Geplantes Thema ohne Datei
- **WHEN** ein geplantes Thema noch keine Lernressource hat
- **THEN** schlägt die Prüfung nicht fehl

#### Scenario: Verwaiste Lernressource
- **WHEN** eine Datei unter `modules/` keinem Thema zugeordnet ist
- **THEN** schlägt die Prüfung fehl und nennt die Datei

### Requirement: Unterrichtseinheiten-Budget wird eingehalten
Die Prüfung SHALL die Summe der Unterrichtseinheiten je Art und je Block gegen die im
Curriculum festgelegten Budgets prüfen.

#### Scenario: Budget überschritten
- **WHEN** die Summe der Theorie-Einheiten das festgelegte Budget übersteigt
- **THEN** schlägt die Prüfung fehl und nennt Ist- und Sollwert

### Requirement: Voraussetzungsgraph ist gültig
Die Prüfung SHALL sicherstellen, dass Voraussetzungen nur auf existierende Themen
zeigen, dass keine Zyklen bestehen und dass jede Voraussetzung früher unterrichtet wird
als das Thema, das sie voraussetzt.

#### Scenario: Vorwärtsreferenz durch Umplanung
- **WHEN** ein Thema so verschoben wird, dass eine seiner Voraussetzungen danach liegt
- **THEN** schlägt die Prüfung fehl und nennt beide Themen mit ihren
  Unterrichtsnummern

#### Scenario: Zyklische Voraussetzung
- **WHEN** zwei Themen sich gegenseitig voraussetzen
- **THEN** schlägt die Prüfung fehl und nennt den Zyklus

### Requirement: Slot-Belegung ist eindeutig und lückenlos
Die Prüfung SHALL sicherstellen, dass je Unterricht höchstens ein Theorie-Thema und
höchstens ein Praxis-Thema liegt und dass zwischen dem ersten und dem letzten belegten
Unterricht keine Lücke bleibt.

#### Scenario: Zwei Theoriethemen im selben Unterricht
- **WHEN** zwei Themen mit Art Theorie dieselbe Unterrichtsnummer tragen
- **THEN** schlägt die Prüfung fehl und nennt beide Themen

#### Scenario: Unterricht ohne Thema
- **WHEN** eine Unterrichtsnummer innerhalb der belegten Spanne kein Thema trägt
- **THEN** schlägt die Prüfung fehl und nennt die Nummer

### Requirement: Pflichtabschnitte der Lernressource sind vorhanden
Die Prüfung SHALL sicherstellen, dass jede Lernressource eines fertigen Themas die
Pflichtabschnitte
`Learning outcomes`, `Decisions`, `Pitfalls` und `Terminology` enthält und dass keiner
davon leer ist. Eine ausdrückliche Nullaussage SHALL als erfüllt gelten.

#### Scenario: Abschnitt fehlt
- **WHEN** eine Lernressource keinen Abschnitt `Decisions` enthält
- **THEN** schlägt die Prüfung fehl und nennt Datei und fehlenden Abschnitt

#### Scenario: Ausdrückliche Nullaussage
- **WHEN** ein Pflichtabschnitt nur eine ausdrückliche Nullaussage enthält
- **THEN** gilt die Prüfung als erfüllt

### Requirement: Lernziele und Prüfungsfragen sind gekoppelt
Die Prüfung SHALL sicherstellen, dass jedes Lernziel einer Lernressource eines fertigen
Themas mindestens
eine zugehörige Prüfungsfrage hat und dass jede Prüfungsfrage auf ein existierendes
Lernziel verweist.

#### Scenario: Lernziel ohne Frage
- **WHEN** ein Lernziel ergänzt wird, ohne eine Frage nachzuziehen
- **THEN** schlägt die Prüfung fehl und nennt das Lernziel

#### Scenario: Frage ohne Lernziel
- **WHEN** eine Prüfungsfrage auf ein Lernziel verweist, das es nicht gibt
- **THEN** schlägt die Prüfung fehl und nennt die Frage

### Requirement: Bilder tragen eine Herkunftsklasse
Die Prüfung SHALL sicherstellen, dass jedes eingebundene Bild einer Lernressource genau
eine Herkunftsklasse trägt. Zulässig SHALL sein: eigenes Werk, freie Lizenz oder
ungeklärt. Bei freier Lizenz MUST Lizenzname und Quelladresse angegeben sein.

#### Scenario: Bild ohne Herkunftsangabe
- **WHEN** ein Bild ohne Herkunftsklasse eingebunden wird
- **THEN** schlägt die Prüfung fehl und nennt Datei und Zeile

#### Scenario: Freie Lizenz ohne Quelle
- **WHEN** ein Bild als frei lizenziert gekennzeichnet ist, aber Lizenzname oder
  Quelladresse fehlt
- **THEN** schlägt die Prüfung fehl

### Requirement: Modulskelett ist einheitlich
Die Prüfung SHALL sicherstellen, dass jedes Modulverzeichnis eines fertigen Themas die
Dateien für Inhalt, Aufgaben und Prüfungsfragen enthält. Die Aufgabendatei MAY
inhaltsleer sein. Für fertige Themen der Art Praxis SHALL mindestens eine
Prüfungsfrage vorhanden sein.

#### Scenario: Datei fehlt im Modul
- **WHEN** ein Modulverzeichnis keine Aufgabendatei enthält
- **THEN** schlägt die Prüfung fehl und nennt das Modul

#### Scenario: Praxisthema ohne Prüfungsfrage
- **WHEN** ein Thema der Art Praxis keine Prüfungsfrage hat
- **THEN** schlägt die Prüfung fehl

### Requirement: Die Prüfung ist Pflichtschritt der Pipeline
Die Prüfung SHALL bei jeder Änderung automatisch laufen. Ein Fehlschlag MUST die
Veröffentlichung verhindern, mit Ausnahme der Rechteklärung, die gesondert geregelt
ist.

#### Scenario: Fehlerhafte Änderung wird eingebracht
- **WHEN** eine Änderung eine der Prüfungen verletzt
- **THEN** bricht der Build ab und die veröffentlichte Site bleibt auf dem letzten
  gültigen Stand
