## Purpose

Stellt fuer alle Schueler eine einheitliche, vom Lehrenden beherrschte Arbeitsumgebung
her, damit Fehler aus unterschiedlich konfigurierten Geraeten als Fehlerklasse
verschwinden.

## ADDED Requirements

### Requirement: Einheitliche Lernumgebung
Der Unterricht SHALL auf einer Linux-Langzeitversion als eigenstaendige Installation oder
auf macOS stattfinden. Eine Umgebung, die auf einer bestehenden Windows-Installation
aufsetzt, MUST NOT als gleichwertig gelten.

#### Scenario: Fehler tritt nur bei einem Schueler auf
- **WHEN** ein Arbeitsschritt bei einzelnen Geraeten scheitert
- **THEN** ist die Umgebung als Ursache ausgeschlossen, weil alle dieselbe verwenden

### Requirement: Die Installation wird risikoarm vorbereitet
Vor jeder Veraenderung an der Partitionierung SHALL nachgewiesen sein, dass das Geraet
das Zielsystem startet. Die Wiederherstellungsschluessel bestehender
Festplattenverschluesselung MUST vorher gesichert sein.

#### Scenario: Geraet startet das Zielsystem nicht
- **WHEN** ein Geraet den Probestart nicht besteht
- **THEN** wird die Partitionierung nicht durchgefuehrt, und der Schueler arbeitet
  uebergangsweise vom Wechselmedium

#### Scenario: Verschluesselung fordert den Wiederherstellungsschluessel
- **WHEN** das Geraet nach der Aenderung den Schluessel verlangt
- **THEN** liegt er gesichert vor, und kein Datenverlust entsteht

### Requirement: Hardware-Voraussetzungen sind vorab geprueft
Vor der Einrichtung SHALL geprueft sein, dass Arbeitsspeicher, freier Plattenplatz und
die Virtualisierungsfaehigkeit des Geraets fuer den gesamten Jahresstoff ausreichen.

#### Scenario: Container-Block beginnt
- **WHEN** der Unterricht Container einfuehrt
- **THEN** erfuellen die Geraete die Voraussetzungen, weil sie zu Jahresbeginn geprueft
  wurden

### Requirement: Der Werkzeugstand ist klassenweit reproduzierbar
Die Werkzeugausstattung SHALL ueber ein versioniertes, wiederholbares Verfahren
hergestellt werden. Eine Einrichtung von Hand nach muendlicher Anleitung MUST NOT die
Grundlage sein.

#### Scenario: Geraet muss neu aufgesetzt werden
- **WHEN** ein Schueler sein System neu installiert
- **THEN** stellt er den verbindlichen Werkzeugstand ohne Nachfragen wieder her

### Requirement: Die Lernumgebung ist Anknuepfungspunkt fuer spaeteren Stoff
Der Schueler SHALL erklaeren koennen, dass die reproduzierbare Einrichtung dasselbe
Prinzip verfolgt wie die spaeter behandelte Containerisierung.

#### Scenario: Uebergang zum Container-Block
- **WHEN** der Unterricht von der Einrichtung zum Container uebergeht
- **THEN** erkennt der Schueler die Beschreibung einer Umgebung als Text als das
  gemeinsame Prinzip
