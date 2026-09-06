## Purpose

Baut einen Fragenkatalog auf, der aus den Pruefungsfragen der Module erzeugt wird und
nach den Merkmalen des Curriculum-Modells sortierbar ist, ohne den bestehenden Katalog
anzutasten.

## ADDED Requirements

### Requirement: Der Katalog wird erzeugt, nicht gepflegt
Der Fragenkatalog SHALL aus den Fragendateien der Module erzeugt werden. Fragen MUST NOT
ausserhalb ihres Moduls gepflegt werden.

#### Scenario: Frage wird ergaenzt
- **WHEN** eine Pruefungsfrage in einem Modul ergaenzt wird
- **THEN** erscheint sie beim naechsten Build im Katalog, ohne dass der Katalog bearbeitet
  wird

### Requirement: Fragen sind nach den Merkmalen des Modells sortierbar
Der Katalog SHALL Sortierung und Filterung nach Block, unterrichtendem Jahrgang,
voraussetzendem Jahrgang und Thema erlauben. Diese Merkmale MUST aus dem Modell stammen
und MUST NOT im Ueberschriften- oder Fliesstext kodiert sein.

#### Scenario: Fragen fuer eine Jahrgangsvoraussetzung
- **WHEN** alle Fragen gesucht werden, die fuer den naechsten Jahrgang vorausgesetzt sind
- **THEN** liefert der Katalog sie, ohne dass Ueberschriften umbenannt werden mussten

### Requirement: Der bestehende Katalog bleibt unveraendert
Der vorhandene, oeffentlich genutzte Fragenkatalog SHALL unveraendert und erreichbar
bleiben. Seine Adressen und Sprungmarken MUST stabil bleiben.

#### Scenario: Kollege verwendet den bestehenden Katalog
- **WHEN** ein Kollege einen Link auf den bestehenden Katalog verwendet
- **THEN** funktioniert er unveraendert

### Requirement: Uebernommene Fragen werden einem Modul zugeordnet
Fragen aus dem bestehenden Katalog MAY uebernommen werden. Beim Uebernehmen SHALL jede
Frage genau einem Modul zugeordnet werden.

#### Scenario: Uebernahme ohne Zuordnung
- **WHEN** eine uebernommene Frage keinem Modul zugeordnet ist
- **THEN** erscheint sie nicht im erzeugten Katalog und faellt bei der Pruefung auf

### Requirement: Die Zustaendigkeit beider Kataloge ist festgelegt
Solange beide Kataloge bestehen, SHALL festgelegt sein, welcher fuer welchen Gegenstand
und Jahrgang massgeblich ist. Beide Einstiegsseiten SHALL auf den jeweils anderen
Katalog hinweisen.

#### Scenario: Schueler sucht die massgebliche Fragenliste
- **WHEN** ein Schueler des betroffenen Jahrgangs eine der beiden Einstiegsseiten oeffnet
- **THEN** erkennt er, welcher Katalog fuer ihn massgeblich ist
