## Purpose

Stellt für alle Schüler eine einheitliche, vom Lehrenden beherrschte Arbeitsumgebung
her, damit Fehler aus unterschiedlich konfigurierten Geräten als Fehlerklasse
verschwinden.

## ADDED Requirements

### Requirement: Einheitliche Lernumgebung
Der Unterricht SHALL auf einer Linux-Langzeitversion als eigenständige Installation oder
auf macOS stattfinden. Eine Umgebung, die auf einer bestehenden Windows-Installation
aufsetzt, MUST NOT als gleichwertig gelten.

#### Scenario: Fehler tritt nur bei einem Schüler auf
- **WHEN** ein Arbeitsschritt bei einzelnen Geräten scheitert
- **THEN** ist die Umgebung als Ursache ausgeschlossen, weil alle dieselbe verwenden

### Requirement: Die Installation wird risikoarm vorbereitet
Vor jeder Veränderung an der Partitionierung SHALL nachgewiesen sein, dass das Gerät
das Zielsystem startet. Die Wiederherstellungsschlüssel bestehender
Festplattenverschlüsselung MUST vorher gesichert sein.

#### Scenario: Gerät startet das Zielsystem nicht
- **WHEN** ein Gerät den Probestart nicht besteht
- **THEN** wird die Partitionierung nicht durchgeführt, und der Schüler arbeitet
  übergangsweise vom Wechselmedium

#### Scenario: Verschlüsselung fordert den Wiederherstellungsschlüssel
- **WHEN** das Gerät nach der Änderung den Schlüssel verlangt
- **THEN** liegt er gesichert vor, und kein Datenverlust entsteht

### Requirement: Hardware-Voraussetzungen sind vorab geprüft
Vor der Einrichtung SHALL geprüft sein, dass Arbeitsspeicher, freier Plattenplatz und
die Virtualisierungsfähigkeit des Geräts für den gesamten Jahresstoff ausreichen.

#### Scenario: Container-Block beginnt
- **WHEN** der Unterricht Container einführt
- **THEN** erfüllen die Geräte die Voraussetzungen, weil sie zu Jahresbeginn geprüft
  wurden

### Requirement: Der Werkzeugstand ist klassenweit reproduzierbar
Die Werkzeugausstattung SHALL über ein versioniertes, wiederholbares Verfahren
hergestellt werden. Eine Einrichtung von Hand nach mündlicher Anleitung MUST NOT die
Grundlage sein.

#### Scenario: Gerät muss neu aufgesetzt werden
- **WHEN** ein Schüler sein System neu installiert
- **THEN** stellt er den verbindlichen Werkzeugstand ohne Nachfragen wieder her

### Requirement: Die Lernumgebung ist Anknüpfungspunkt für späteren Stoff
Der Schüler SHALL erklären können, dass die reproduzierbare Einrichtung dasselbe
Prinzip verfolgt wie die später behandelte Containerisierung.

#### Scenario: Übergang zum Container-Block
- **WHEN** der Unterricht von der Einrichtung zum Container übergeht
- **THEN** erkennt der Schüler die Beschreibung einer Umgebung als Text als das
  gemeinsame Prinzip
