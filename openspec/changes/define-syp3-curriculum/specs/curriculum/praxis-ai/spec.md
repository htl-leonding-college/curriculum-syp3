## Purpose

Vermittelt den beruflich tragfaehigen Umgang mit KI-Agenten in der Softwareentwicklung —
vom Formulieren einer Aufgabe ueber die Steuerung des Arbeitsumfelds bis zur Verantwortung
fuer das Ergebnis.

## ADDED Requirements

### Requirement: Grundlagen und Aufgabenformulierung
Der Schueler SHALL eine Aufgabe so formulieren koennen, dass Ziel, Randbedingungen und
erwartete Form des Ergebnisses darin stehen, und die Auswirkung praeziserer Formulierung
auf das Ergebnis beurteilen koennen.

#### Scenario: Unbrauchbares Ergebnis
- **WHEN** ein Ergebnis nicht brauchbar ist
- **THEN** verbessert der Schueler zuerst die Aufgabenstellung, statt dasselbe erneut zu
  versuchen

### Requirement: Kontext bewusst bereitstellen
Der Schueler SHALL beurteilen koennen, welche Angaben ein Agent fuer eine Aufgabe
braucht, und diesen Kontext gezielt bereitstellen statt vollstaendig oder zufaellig.

#### Scenario: Aufgabe in einem groesseren Projekt
- **WHEN** eine Aufgabe nur einen Teil des Projekts betrifft
- **THEN** stellt der Schueler die dafuer noetigen Teile bereit und begruendet die Auswahl

### Requirement: Arbeit ueber eine Sitzungsgrenze hinweg fortsetzen
Der Schueler SHALL den Stand einer laengeren Arbeit so festhalten koennen, dass sie in
einer neuen Sitzung ohne Wiederholung der Vorgeschichte fortgesetzt werden kann.

#### Scenario: Arbeit wird unterbrochen
- **WHEN** eine Arbeit ueber mehrere Tage laeuft
- **THEN** genuegt der festgehaltene Stand, um ohne Rueckfragen fortzusetzen

### Requirement: Das Arbeitsumfeld des Agenten gestalten
Der Schueler SHALL beschreiben koennen, wie Werkzeuge, Zugriffsrechte und verbindliche
Vorgaben das Ergebnis eines Agenten beeinflussen, und diese Rahmenbedingungen fuer sein
Projekt festlegen.

#### Scenario: Wiederkehrende Vorgabe
- **WHEN** dieselbe Vorgabe in jeder Sitzung wiederholt werden muesste
- **THEN** legt der Schueler sie dauerhaft im Projekt ab, statt sie jedes Mal zu nennen

### Requirement: Wiederholende Ablaeufe erkennen und begrenzen
Der Schueler SHALL einen sich wiederholenden Arbeitsablauf einrichten und ein
Abbruchkriterium dafuer angeben koennen.

#### Scenario: Ablauf kommt nicht zum Ende
- **WHEN** ein wiederholender Ablauf sein Ziel nicht erreicht
- **THEN** bricht er anhand des festgelegten Kriteriums ab, statt endlos zu laufen

### Requirement: Verantwortung fuer das Ergebnis bleibt beim Schueler
Der Schueler SHALL von einem Agenten erzeugte Ergebnisse pruefen, bevor er sie uebernimmt,
und fuer jede uebernommene Stelle erklaeren koennen, was sie tut und warum sie so
aussieht.

#### Scenario: Muendliche Pruefung ueber eigenen Projektcode
- **WHEN** der Schueler zu einer Stelle seines Projekts befragt wird
- **THEN** erklaert er Zweck und Funktionsweise, unabhaengig davon, wer oder was sie
  erzeugt hat

#### Scenario: Ergebnis wirkt plausibel, ist aber falsch
- **WHEN** ein erzeugtes Ergebnis ueberzeugend aussieht
- **THEN** prueft der Schueler es gegen die Anforderung, bevor er es uebernimmt
