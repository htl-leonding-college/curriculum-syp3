## Purpose

Legt fest, wie ein Lernmodul aufgebaut ist — Dateien, Pflichtabschnitte, Aufgaben,
Prüfungsfragen, Diagramme und Sprache — damit rund 48 Module einander gleichen und
maschinell prüfbar bleiben.

## ADDED Requirements

### Requirement: Ein Modul besteht aus Inhalt, Aufgaben und Prüfungsfragen
Jedes Modul SHALL aus einer Inhaltsdatei, einer Aufgabendatei und einer Fragendatei
bestehen, die im selben Verzeichnis liegen. Bilder eines Moduls SHALL in einem
Unterverzeichnis dieses Moduls liegen.

#### Scenario: Neues Modul wird angelegt
- **WHEN** ein Modul angelegt wird
- **THEN** entstehen alle drei Dateien, auch wenn die Aufgabendatei zunächst leer bleibt

### Requirement: Die Inhaltsdatei hat eine feste Abschnittsfolge
Die Inhaltsdatei SHALL die Abschnitte `Learning outcomes`, den fachlichen Teil,
`Decisions`, `Pitfalls`, `Terminology` und weiterführende Quellen in dieser Reihenfolge
enthalten. `Learning outcomes`, `Decisions`, `Pitfalls` und `Terminology` SHALL
verpflichtend sein.

#### Scenario: Leser sucht die verbindliche Festlegung
- **WHEN** ein Schüler wissen will, welche Vorgabe für dieses Thema in diesem Jahrgang
  gilt
- **THEN** steht sie im Abschnitt `Decisions` und nicht verstreut im Fließtext

### Requirement: Eine ausdrückliche Nullaussage erfüllt einen Pflichtabschnitt
Ein Pflichtabschnitt ohne Inhalt SHALL eine ausdrückliche Nullaussage tragen. Ein
Weglassen des Abschnitts MUST NOT zulässig sein.

#### Scenario: Thema ohne eigene Festlegung
- **WHEN** ein Thema keine eigene Festlegung kennt
- **THEN** enthält `Decisions` eine ausdrückliche Nullaussage, und das ist vom
  Vergessen unterscheidbar

### Requirement: Lernziele korrespondieren mit Prüfungsfragen
Die Lernziele eines Moduls SHALL angeben, was nach dem Modul gekonnt werden muss. Jedes
Lernziel SHALL mindestens eine Prüfungsfrage in der Fragendatei haben, und jede
Prüfungsfrage SHALL einem Lernziel zugeordnet sein.

#### Scenario: Schüler bereitet die mündliche Prüfung vor
- **WHEN** ein Schüler wissen will, woran er gemessen wird
- **THEN** findet er zu jedem Lernziel die zugehörigen Prüfungsfragen im Modul

### Requirement: Aufgaben tragen eine Art, Lösungen sind freiwillig
Jede Aufgabe SHALL als übungsartige Aufgabe oder als Aufgabe am eigenen Projekt
gekennzeichnet sein. Eine mitgelieferte Lösung und ein Bewertungsraster SHALL zulässig,
aber MUST NOT verpflichtend sein. Mitgelieferte Lösungen SHALL im selben Dokument
stehen und MUST NOT zeitgesteuert freigeschaltet oder in einen anderen Zweig ausgelagert
werden.

#### Scenario: Aufgabe am eigenen Projekt
- **WHEN** eine Aufgabe sich auf das Projekt des Teams bezieht
- **THEN** ist sie entsprechend gekennzeichnet, und es wird keine Musterlösung erwartet

#### Scenario: Schüler sucht die Lösung
- **WHEN** eine Lösung mitgeliefert ist
- **THEN** ist sie im selben Dokument aufklappbar erreichbar, ohne Freischaltung

### Requirement: Diagramme werden bevorzugt als Quelltext geführt
Diagramme SHALL bevorzugt als Diagramm-Quelltext im Dokument stehen. Ein Bild SHALL nur
verwendet werden, wo eine Quelltextdarstellung nicht trägt. Zu einem selbst erstellten
Bild SHALL die bearbeitbare Quelldatei im Modul mitgeführt werden.

#### Scenario: Diagramm wird geändert
- **WHEN** ein als Quelltext geführtes Diagramm geändert wird
- **THEN** ist die Änderung im Versionsvergleich lesbar und braucht kein weiteres
  Werkzeug

#### Scenario: Eigene Zeichnung wird eingebunden
- **WHEN** eine selbst erstellte Zeichnung als Bild eingebunden wird
- **THEN** liegt ihre bearbeitbare Quelldatei daneben, damit sie änderbar bleibt

### Requirement: Jedes Bild trägt seine Herkunft
Jedes eingebundene Bild SHALL beim Einfügen mit seiner Herkunft gekennzeichnet werden:
eigenes Werk, freie Lizenz mit Lizenzname und Quelladresse, oder ungeklärt.

#### Scenario: Bild aus einer fremden Quelle
- **WHEN** ein gefundenes Bild eingebunden wird, dessen Rechte nicht geprüft sind
- **THEN** wird es als ungeklärt gekennzeichnet und bleibt auffindbar

#### Scenario: Spätere Rechtebereinigung
- **WHEN** die Rechtelage geklärt ist und bestimmte Bilder entfernt werden müssen
- **THEN** sind die betroffenen Bilder über ihre Herkunftsangabe auffindbar, ohne alle
  Module durchzusehen

### Requirement: Sprache ist Englisch mit zweisprachigem Governance-Wortschatz
Lernressourcen SHALL auf Englisch verfasst sein. Fachbegriffe der Projekt-Governance
SHALL zusätzlich in ihrer deutschen Form geführt werden, weil die zugehörigen
Formulare deutsch sind. Jedes Modul SHALL einen Begriffsabschnitt mit deutsch/englischen
Paaren enthalten.

#### Scenario: Schüler füllt später ein deutsches Formular aus
- **WHEN** ein Schüler im höheren Jahrgang einen Antrag mit deutschen Feldnamen
  ausfüllt
- **THEN** sind ihm die deutschen Begriffe aus dem Unterricht geläufig

### Requirement: Module enthalten keinen Unterrichtsverlauf
Eine Lernressource SHALL vorbereitet, stabil und unabhängig von einer einzelnen Klasse
sein. Klassenbezogene Aufzeichnungen über Termine, Fortschritt oder Abschweifungen
MUST NOT in den Modulen abgelegt werden.

#### Scenario: Zweite Klasse im selben Jahrgang
- **WHEN** dasselbe Modul in einer weiteren Klasse verwendet wird
- **THEN** ist es unverändert verwendbar und enthält nichts, was nur für die erste
  Klasse galt

#### Scenario: Wiederverwendung im Folgejahr
- **WHEN** das Modul im nächsten Schuljahr verwendet wird
- **THEN** enthält es keine Spuren des Vorjahresverlaufs
