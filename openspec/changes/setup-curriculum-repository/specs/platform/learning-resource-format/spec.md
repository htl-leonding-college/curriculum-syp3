## Purpose

Legt fest, wie ein Lernmodul aufgebaut ist — Dateien, Pflichtabschnitte, Aufgaben,
Pruefungsfragen, Diagramme und Sprache — damit rund 48 Module einander gleichen und
maschinell pruefbar bleiben.

## ADDED Requirements

### Requirement: Ein Modul besteht aus Inhalt, Aufgaben und Pruefungsfragen
Jedes Modul SHALL aus einer Inhaltsdatei, einer Aufgabendatei und einer Fragendatei
bestehen, die im selben Verzeichnis liegen. Bilder eines Moduls SHALL in einem
Unterverzeichnis dieses Moduls liegen.

#### Scenario: Neues Modul wird angelegt
- **WHEN** ein Modul angelegt wird
- **THEN** entstehen alle drei Dateien, auch wenn die Aufgabendatei zunaechst leer bleibt

### Requirement: Die Inhaltsdatei hat eine feste Abschnittsfolge
Die Inhaltsdatei SHALL die Abschnitte `Learning outcomes`, den fachlichen Teil,
`Decisions`, `Pitfalls`, `Terminology` und weiterfuehrende Quellen in dieser Reihenfolge
enthalten. `Learning outcomes`, `Decisions`, `Pitfalls` und `Terminology` SHALL
verpflichtend sein.

#### Scenario: Leser sucht die verbindliche Festlegung
- **WHEN** ein Schueler wissen will, welche Vorgabe fuer dieses Thema in diesem Jahrgang
  gilt
- **THEN** steht sie im Abschnitt `Decisions` und nicht verstreut im Fliesstext

### Requirement: Eine ausdrueckliche Nullaussage erfuellt einen Pflichtabschnitt
Ein Pflichtabschnitt ohne Inhalt SHALL eine ausdrueckliche Nullaussage tragen. Ein
Weglassen des Abschnitts MUST NOT zulaessig sein.

#### Scenario: Thema ohne eigene Festlegung
- **WHEN** ein Thema keine eigene Festlegung kennt
- **THEN** enthaelt `Decisions` eine ausdrueckliche Nullaussage, und das ist vom
  Vergessen unterscheidbar

### Requirement: Lernziele korrespondieren mit Pruefungsfragen
Die Lernziele eines Moduls SHALL angeben, was nach dem Modul gekonnt werden muss. Jedes
Lernziel SHALL mindestens eine Pruefungsfrage in der Fragendatei haben, und jede
Pruefungsfrage SHALL einem Lernziel zugeordnet sein.

#### Scenario: Schueler bereitet die muendliche Pruefung vor
- **WHEN** ein Schueler wissen will, woran er gemessen wird
- **THEN** findet er zu jedem Lernziel die zugehoerigen Pruefungsfragen im Modul

### Requirement: Aufgaben tragen eine Art, Loesungen sind freiwillig
Jede Aufgabe SHALL als uebungsartige Aufgabe oder als Aufgabe am eigenen Projekt
gekennzeichnet sein. Eine mitgelieferte Loesung und ein Bewertungsraster SHALL zulaessig,
aber MUST NOT verpflichtend sein. Mitgelieferte Loesungen SHALL im selben Dokument
stehen und MUST NOT zeitgesteuert freigeschaltet oder in einen anderen Zweig ausgelagert
werden.

#### Scenario: Aufgabe am eigenen Projekt
- **WHEN** eine Aufgabe sich auf das Projekt des Teams bezieht
- **THEN** ist sie entsprechend gekennzeichnet, und es wird keine Musterloesung erwartet

#### Scenario: Schueler sucht die Loesung
- **WHEN** eine Loesung mitgeliefert ist
- **THEN** ist sie im selben Dokument aufklappbar erreichbar, ohne Freischaltung

### Requirement: Diagramme werden bevorzugt als Quelltext gefuehrt
Diagramme SHALL bevorzugt als Diagramm-Quelltext im Dokument stehen. Ein Bild SHALL nur
verwendet werden, wo eine Quelltextdarstellung nicht traegt. Zu einem selbst erstellten
Bild SHALL die bearbeitbare Quelldatei im Modul mitgefuehrt werden.

#### Scenario: Diagramm wird geaendert
- **WHEN** ein als Quelltext gefuehrtes Diagramm geaendert wird
- **THEN** ist die Aenderung im Versionsvergleich lesbar und braucht kein weiteres
  Werkzeug

#### Scenario: Eigene Zeichnung wird eingebunden
- **WHEN** eine selbst erstellte Zeichnung als Bild eingebunden wird
- **THEN** liegt ihre bearbeitbare Quelldatei daneben, damit sie aenderbar bleibt

### Requirement: Jedes Bild traegt seine Herkunft
Jedes eingebundene Bild SHALL beim Einfuegen mit seiner Herkunft gekennzeichnet werden:
eigenes Werk, freie Lizenz mit Lizenzname und Quelladresse, oder ungeklaert.

#### Scenario: Bild aus einer fremden Quelle
- **WHEN** ein gefundenes Bild eingebunden wird, dessen Rechte nicht geprueft sind
- **THEN** wird es als ungeklaert gekennzeichnet und bleibt auffindbar

#### Scenario: Spaetere Rechtebereinigung
- **WHEN** die Rechtelage geklaert ist und bestimmte Bilder entfernt werden muessen
- **THEN** sind die betroffenen Bilder ueber ihre Herkunftsangabe auffindbar, ohne alle
  Module durchzusehen

### Requirement: Sprache ist Englisch mit zweisprachigem Governance-Wortschatz
Lernressourcen SHALL auf Englisch verfasst sein. Fachbegriffe der Projekt-Governance
SHALL zusaetzlich in ihrer deutschen Form gefuehrt werden, weil die zugehoerigen
Formulare deutsch sind. Jedes Modul SHALL einen Begriffsabschnitt mit deutsch/englischen
Paaren enthalten.

#### Scenario: Schueler fuellt spaeter ein deutsches Formular aus
- **WHEN** ein Schueler im hoeheren Jahrgang einen Antrag mit deutschen Feldnamen
  ausfuellt
- **THEN** sind ihm die deutschen Begriffe aus dem Unterricht gelaeufig

### Requirement: Module enthalten keinen Unterrichtsverlauf
Eine Lernressource SHALL vorbereitet, stabil und unabhaengig von einer einzelnen Klasse
sein. Klassenbezogene Aufzeichnungen ueber Termine, Fortschritt oder Abschweifungen
MUST NOT in den Modulen abgelegt werden.

#### Scenario: Zweite Klasse im selben Jahrgang
- **WHEN** dasselbe Modul in einer weiteren Klasse verwendet wird
- **THEN** ist es unveraendert verwendbar und enthaelt nichts, was nur fuer die erste
  Klasse galt

#### Scenario: Wiederverwendung im Folgejahr
- **WHEN** das Modul im naechsten Schuljahr verwendet wird
- **THEN** enthaelt es keine Spuren des Vorjahresverlaufs
