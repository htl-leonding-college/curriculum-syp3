## Purpose

Baut einen Fragenkatalog auf, der aus den Prüfungsfragen der Module erzeugt wird und
nach den Merkmalen des Curriculum-Modells sortierbar ist, ohne den bestehenden Katalog
anzutasten.

## ADDED Requirements

### Requirement: Der Katalog wird erzeugt, nicht gepflegt
Der Fragenkatalog SHALL aus den Fragendateien der Module erzeugt werden. Fragen MUST NOT
außerhalb ihres Moduls gepflegt werden.

#### Scenario: Frage wird ergänzt
- **WHEN** eine Prüfungsfrage in einem Modul ergänzt wird
- **THEN** erscheint sie beim nächsten Build im Katalog, ohne dass der Katalog bearbeitet
  wird

### Requirement: Fragen sind nach den Merkmalen des Modells sortierbar
Der Katalog SHALL Sortierung und Filterung nach Block, unterrichtendem Jahrgang,
voraussetzendem Jahrgang und Thema erlauben. Diese Merkmale MUST aus dem Modell stammen
und MUST NOT im Überschriften- oder Fließtext kodiert sein.

#### Scenario: Fragen für eine Jahrgangsvoraussetzung
- **WHEN** alle Fragen gesucht werden, die für den nächsten Jahrgang vorausgesetzt sind
- **THEN** liefert der Katalog sie, ohne dass Überschriften umbenannt werden mussten

### Requirement: Der bestehende Katalog bleibt unverändert
Der vorhandene, öffentlich genutzte Fragenkatalog SHALL unverändert und erreichbar
bleiben. Seine Adressen und Sprungmarken MUST stabil bleiben.

#### Scenario: Kollege verwendet den bestehenden Katalog
- **WHEN** ein Kollege einen Link auf den bestehenden Katalog verwendet
- **THEN** funktioniert er unverändert

### Requirement: Übernommene Fragen werden einem Modul zugeordnet
Fragen aus dem bestehenden Katalog MAY übernommen werden. Beim Übernehmen SHALL jede
Frage genau einem Modul zugeordnet werden.

#### Scenario: Übernahme ohne Zuordnung
- **WHEN** eine übernommene Frage keinem Modul zugeordnet ist
- **THEN** erscheint sie nicht im erzeugten Katalog und fällt bei der Prüfung auf

### Requirement: Die Zuständigkeit beider Kataloge ist festgelegt
Solange beide Kataloge bestehen, SHALL festgelegt sein, welcher für welchen Gegenstand
und Jahrgang maßgeblich ist. Beide Einstiegsseiten SHALL auf den jeweils anderen
Katalog hinweisen.

#### Scenario: Schüler sucht die maßgebliche Fragenliste
- **WHEN** ein Schüler des betroffenen Jahrgangs eine der beiden Einstiegsseiten öffnet
- **THEN** erkennt er, welcher Katalog für ihn maßgeblich ist
