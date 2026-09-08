## Purpose

Bringt die Lernressourcen automatisch als öffentliche Website ins Netz und regelt das
Nebeneinander von automatischer Veröffentlichung, manuellem Ausrollen auf den
Schulwebspace und der bestehenden Altsite.

## ADDED Requirements

### Requirement: Veröffentlichung erfolgt automatisch aus dem Repository
Eine Änderung an den Lernressourcen SHALL nach dem Einbringen ohne weitere Handgriffe
als Website veröffentlicht werden.

#### Scenario: Änderung wird eingebracht
- **WHEN** eine gültige Änderung in den Hauptstand gelangt
- **THEN** ist die veröffentlichte Site nach dem Build auf diesem Stand

#### Scenario: Ungültige Änderung
- **WHEN** eine Änderung die Curriculum-Prüfung verletzt
- **THEN** wird nicht veröffentlicht und der letzte gültige Stand bleibt online

### Requirement: Ungeklärte Bildrechte werden gemeldet, blockieren aber nicht
Bilder mit ungeklärter Rechtelage SHALL in einem eigenen, deutlich sichtbaren
Prüfschritt gemeldet werden. Dieser Schritt MUST NOT die Veröffentlichung verhindern.

#### Scenario: Modul mit ungeklärtem Bild
- **WHEN** ein Modul ein Bild mit ungeklärter Rechtelage enthält
- **THEN** meldet der Rechte-Prüfschritt es mit Datei und Zeile, und die übrigen Module
  werden trotzdem veröffentlicht

### Requirement: Präsentationsausgabe aus derselben Quelle
Aus den Lernressourcen SHALL sich eine Präsentationsansicht erzeugen lassen, ohne die
Inhalte ein zweites Mal zu pflegen.

#### Scenario: Inhalt ändert sich
- **WHEN** ein Modultext geändert wird
- **THEN** ändert sich die Präsentationsansicht mit, ohne separate Bearbeitung

### Requirement: Ausrollen auf fremde Infrastruktur erfolgt manuell
Das Ausrollen auf den Schulwebspace SHALL manuell und lokal auslösbar sein. Zugangsdaten
für fremde Infrastruktur MUST NOT in der Automatisierung hinterlegt werden.

#### Scenario: Ausrollen auf den Schulwebspace
- **WHEN** die Site zusätzlich auf dem Schulwebspace bereitstehen soll
- **THEN** geschieht das über einen lokal ausgeführten Schritt, ohne Zugangsdaten im
  Automatisierungssystem

### Requirement: Die bestehende Altsite bleibt erreichbar
Die vorhandene Website auf dem Schulwebspace SHALL unverändert erreichbar bleiben. Die
neue Site SHALL daneben entstehen.

#### Scenario: Zugriff auf Altbestand
- **WHEN** ein Link auf Inhalte früherer Projekte aufgerufen wird
- **THEN** funktioniert er unverändert
