## Purpose

Leitet alle wiederkehrenden Darstellungen der Stoffstruktur maschinell aus dem
Curriculum-Modell ab, damit Navigation, Übersichten und Tags nicht parallel gepflegt
werden müssen.

## ADDED Requirements

### Requirement: Stoffstruktur wird als Diagramm erzeugt
Aus dem Modell SHALL eine Darstellung der Stoffstruktur erzeugt werden, die Blöcke und
Themen in ihrer Zuordnung zeigt.

#### Scenario: Thema wird ergänzt
- **WHEN** ein Thema im Modell ergänzt wird
- **THEN** enthält die erzeugte Darstellung beim nächsten Build den neuen Knoten

### Requirement: Website-Navigation wird erzeugt
Die Navigation der veröffentlichten Site SHALL aus dem Modell erzeugt werden und die
Reihenfolge der Unterrichte widerspiegeln.

#### Scenario: Thema wird verschoben
- **WHEN** die Unterrichtsnummer eines Themas geändert wird
- **THEN** ändert sich die Reihenfolge in der Navigation ohne Handarbeit

### Requirement: Übersicht der Unterrichtseinheiten wird erzeugt
Aus dem Modell SHALL eine Übersicht der Unterrichtseinheiten je Block und je Art
erzeugt werden.

#### Scenario: Umfang wird geändert
- **WHEN** die UE-Zahl eines Themas geändert wird
- **THEN** zeigt die erzeugte Übersicht die neuen Summen

### Requirement: Fragenkatalog-Tags werden erzeugt
Die Zuordnungsmerkmale des Fragenkatalogs — Block, unterrichtender Jahrgang und
voraussetzender Jahrgang — SHALL aus dem Modell erzeugt werden und MUST NOT im Text der
Fragen kodiert sein.

#### Scenario: Jahrgangszuordnung ändert sich
- **WHEN** ein Thema einem anderen Jahrgang zugeordnet wird
- **THEN** ändern sich die Tags aller zugehörigen Fragen ohne Handarbeit

### Requirement: Erzeugte Artefakte werden nicht von Hand bearbeitet
Erzeugte Artefakte SHALL als solche erkennbar sein. Eine Handänderung MUST beim
nächsten Build verworfen werden.

#### Scenario: Handänderung an erzeugter Datei
- **WHEN** eine erzeugte Datei von Hand geändert wird
- **THEN** überschreibt der nächste Generatorlauf die Änderung
