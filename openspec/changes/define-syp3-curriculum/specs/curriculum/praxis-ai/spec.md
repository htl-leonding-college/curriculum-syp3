## Purpose

Vermittelt den beruflich tragfähigen Umgang mit KI-Agenten in der Softwareentwicklung —
vom Formulieren einer Aufgabe über die Steuerung des Arbeitsumfelds bis zur Verantwortung
für das Ergebnis.

## ADDED Requirements

### Requirement: Grundlagen und Aufgabenformulierung
Der Schüler SHALL eine Aufgabe so formulieren können, dass Ziel, Randbedingungen und
erwartete Form des Ergebnisses darin stehen, und die Auswirkung präziserer Formulierung
auf das Ergebnis beurteilen können.

#### Scenario: Unbrauchbares Ergebnis
- **WHEN** ein Ergebnis nicht brauchbar ist
- **THEN** verbessert der Schüler zuerst die Aufgabenstellung, statt dasselbe erneut zu
  versuchen

### Requirement: Kontext bewusst bereitstellen
Der Schüler SHALL beurteilen können, welche Angaben ein Agent für eine Aufgabe
braucht, und diesen Kontext gezielt bereitstellen statt vollständig oder zufällig.

#### Scenario: Aufgabe in einem größeren Projekt
- **WHEN** eine Aufgabe nur einen Teil des Projekts betrifft
- **THEN** stellt der Schüler die dafür nötigen Teile bereit und begründet die Auswahl

### Requirement: Arbeit über eine Sitzungsgrenze hinweg fortsetzen
Der Schüler SHALL den Stand einer längeren Arbeit so festhalten können, dass sie in
einer neuen Sitzung ohne Wiederholung der Vorgeschichte fortgesetzt werden kann.

#### Scenario: Arbeit wird unterbrochen
- **WHEN** eine Arbeit über mehrere Tage läuft
- **THEN** genügt der festgehaltene Stand, um ohne Rückfragen fortzusetzen

### Requirement: Das Arbeitsumfeld des Agenten gestalten
Der Schüler SHALL beschreiben können, wie Werkzeuge, Zugriffsrechte und verbindliche
Vorgaben das Ergebnis eines Agenten beeinflussen, und diese Rahmenbedingungen für sein
Projekt festlegen.

#### Scenario: Wiederkehrende Vorgabe
- **WHEN** dieselbe Vorgabe in jeder Sitzung wiederholt werden müsste
- **THEN** legt der Schüler sie dauerhaft im Projekt ab, statt sie jedes Mal zu nennen

### Requirement: Wiederholende Abläufe erkennen und begrenzen
Der Schüler SHALL einen sich wiederholenden Arbeitsablauf einrichten und ein
Abbruchkriterium dafür angeben können.

#### Scenario: Ablauf kommt nicht zum Ende
- **WHEN** ein wiederholender Ablauf sein Ziel nicht erreicht
- **THEN** bricht er anhand des festgelegten Kriteriums ab, statt endlos zu laufen

### Requirement: Verantwortung für das Ergebnis bleibt beim Schüler
Der Schüler SHALL von einem Agenten erzeugte Ergebnisse prüfen, bevor er sie übernimmt,
und für jede übernommene Stelle erklären können, was sie tut und warum sie so
aussieht.

#### Scenario: Mündliche Prüfung über eigenen Projektcode
- **WHEN** der Schüler zu einer Stelle seines Projekts befragt wird
- **THEN** erklärt er Zweck und Funktionsweise, unabhängig davon, wer oder was sie
  erzeugt hat

#### Scenario: Ergebnis wirkt plausibel, ist aber falsch
- **WHEN** ein erzeugtes Ergebnis überzeugend aussieht
- **THEN** prüft der Schüler es gegen die Anforderung, bevor er es übernimmt
