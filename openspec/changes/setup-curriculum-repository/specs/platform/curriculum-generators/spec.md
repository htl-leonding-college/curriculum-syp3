## Purpose

Leitet alle wiederkehrenden Darstellungen der Stoffstruktur maschinell aus dem
Curriculum-Modell ab, damit Navigation, Uebersichten und Tags nicht parallel gepflegt
werden muessen.

## ADDED Requirements

### Requirement: Stoffstruktur wird als Diagramm erzeugt
Aus dem Modell SHALL eine Darstellung der Stoffstruktur erzeugt werden, die Bloecke und
Themen in ihrer Zuordnung zeigt.

#### Scenario: Thema wird ergaenzt
- **WHEN** ein Thema im Modell ergaenzt wird
- **THEN** enthaelt die erzeugte Darstellung beim naechsten Build den neuen Knoten

### Requirement: Website-Navigation wird erzeugt
Die Navigation der veroeffentlichten Site SHALL aus dem Modell erzeugt werden und die
Reihenfolge der Unterrichte widerspiegeln.

#### Scenario: Thema wird verschoben
- **WHEN** die Unterrichtsnummer eines Themas geaendert wird
- **THEN** aendert sich die Reihenfolge in der Navigation ohne Handarbeit

### Requirement: Uebersicht der Unterrichtseinheiten wird erzeugt
Aus dem Modell SHALL eine Uebersicht der Unterrichtseinheiten je Block und je Art
erzeugt werden.

#### Scenario: Umfang wird geaendert
- **WHEN** die UE-Zahl eines Themas geaendert wird
- **THEN** zeigt die erzeugte Uebersicht die neuen Summen

### Requirement: Fragenkatalog-Tags werden erzeugt
Die Zuordnungsmerkmale des Fragenkatalogs — Block, unterrichtender Jahrgang und
voraussetzender Jahrgang — SHALL aus dem Modell erzeugt werden und MUST NOT im Text der
Fragen kodiert sein.

#### Scenario: Jahrgangszuordnung aendert sich
- **WHEN** ein Thema einem anderen Jahrgang zugeordnet wird
- **THEN** aendern sich die Tags aller zugehoerigen Fragen ohne Handarbeit

### Requirement: Erzeugte Artefakte werden nicht von Hand bearbeitet
Erzeugte Artefakte SHALL als solche erkennbar sein. Eine Handaenderung MUST beim
naechsten Build verworfen werden.

#### Scenario: Handaenderung an erzeugter Datei
- **WHEN** eine erzeugte Datei von Hand geaendert wird
- **THEN** ueberschreibt der naechste Generatorlauf die Aenderung
