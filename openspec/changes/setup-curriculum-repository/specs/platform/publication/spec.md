## Purpose

Bringt die Lernressourcen automatisch als oeffentliche Website ins Netz und regelt das
Nebeneinander von automatischer Veroeffentlichung, manuellem Ausrollen auf den
Schulwebspace und der bestehenden Altsite.

## ADDED Requirements

### Requirement: Veroeffentlichung erfolgt automatisch aus dem Repository
Eine Aenderung an den Lernressourcen SHALL nach dem Einbringen ohne weitere Handgriffe
als Website veroeffentlicht werden.

#### Scenario: Aenderung wird eingebracht
- **WHEN** eine gueltige Aenderung in den Hauptstand gelangt
- **THEN** ist die veroeffentlichte Site nach dem Build auf diesem Stand

#### Scenario: Ungueltige Aenderung
- **WHEN** eine Aenderung die Curriculum-Pruefung verletzt
- **THEN** wird nicht veroeffentlicht und der letzte gueltige Stand bleibt online

### Requirement: Ungeklaerte Bildrechte werden gemeldet, blockieren aber nicht
Bilder mit ungeklaerter Rechtelage SHALL in einem eigenen, deutlich sichtbaren
Pruefschritt gemeldet werden. Dieser Schritt MUST NOT die Veroeffentlichung verhindern.

#### Scenario: Modul mit ungeklaertem Bild
- **WHEN** ein Modul ein Bild mit ungeklaerter Rechtelage enthaelt
- **THEN** meldet der Rechte-Pruefschritt es mit Datei und Zeile, und die uebrigen Module
  werden trotzdem veroeffentlicht

### Requirement: Praesentationsausgabe aus derselben Quelle
Aus den Lernressourcen SHALL sich eine Praesentationsansicht erzeugen lassen, ohne die
Inhalte ein zweites Mal zu pflegen.

#### Scenario: Inhalt aendert sich
- **WHEN** ein Modultext geaendert wird
- **THEN** aendert sich die Praesentationsansicht mit, ohne separate Bearbeitung

### Requirement: Ausrollen auf fremde Infrastruktur erfolgt manuell
Das Ausrollen auf den Schulwebspace SHALL manuell und lokal ausloesbar sein. Zugangsdaten
fuer fremde Infrastruktur MUST NOT in der Automatisierung hinterlegt werden.

#### Scenario: Ausrollen auf den Schulwebspace
- **WHEN** die Site zusaetzlich auf dem Schulwebspace bereitstehen soll
- **THEN** geschieht das ueber einen lokal ausgefuehrten Schritt, ohne Zugangsdaten im
  Automatisierungssystem

### Requirement: Die bestehende Altsite bleibt erreichbar
Die vorhandene Website auf dem Schulwebspace SHALL unveraendert erreichbar bleiben. Die
neue Site SHALL daneben entstehen.

#### Scenario: Zugriff auf Altbestand
- **WHEN** ein Link auf Inhalte frueherer Projekte aufgerufen wird
- **THEN** funktioniert er unveraendert
