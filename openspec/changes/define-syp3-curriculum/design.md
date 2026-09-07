# Design: Curriculum SYP 3. Jahrgang

## Context

Motivation siehe `proposal.md` — Why.

Randbedingungen, die den Entwurf bestimmen:

- **30 Unterrichte à 3 UE**, Standardaufteilung 1 UE Theorie + 2 UE Praxis.
  Erfahrungsgemäß fallen ~5 Termine durch externe Veranstaltungen aus.
- **Governance ist gesetzt.** Projektantrag, Projektauftrag und Meilensteinplan sind in
  allen drei Projektformen (Jahresprojekt 3. Jg, zweijähriges Projekt 4./5. Jg,
  Diplomarbeit) verpflichtend. Der DA-Antrag verlangt zusätzlich eine Aufwandsschätzung
  in Stunden und eine Zuordnung „Verantwortlich" je Schüler.
- **Der DA-Antrag ist vorgehensmodell-neutral.** Er fragt nach Ausgangslage, Zielsetzung,
  Untersuchungsanliegen, geplantem Ergebnis, Meilensteinen und Terminen — nirgends nach
  Sprints, Phasen oder Iterationen.
- **Projektarbeit findet zu Hause statt.** Im Unterricht bleiben ~7 UE für Reviews und
  Hilfestellung.
- **Heterogene Geräte**: überwiegend Windows-Laptops, einzelne Macs.
- Quellenlage: Manz-Schulbuch (nur Textinhalte, keine Abbildungen), PUMA-Material zu
  Kreativitätstechniken und Nutzwertanalyse, UML-Skripten Uni Heidelberg,
  eigene Keynote zu Vorgehensmodellen.

## Goals / Non-Goals

**Goals:**

- Ein Curriculum, das die reale Arbeitsweise (spec-driven mit AI-Agenten) abbildet, ohne
  die für Diplomarbeit und Berufspraxis nötige Governance-Kompetenz zu verlieren
- Eine Unterrichtssequenz, die durch die Werkzeugabhängigkeiten begründet ist, nicht durch
  die Kapitelreihenfolge eines Lehrbuchs
- Ein Jahresrahmen, der Terminausfälle verkraftet, ohne dass Kerninhalte entfallen
- Eine einheitliche, vom Lehrenden beherrschte Lernumgebung

**Non-Goals:**

- Kein Ersatz der Governance-Artefakte durch openspec-Artefakte — sie koexistieren
- Keine Bindung des Curriculums an ein bestimmtes Tool; openspec ist die aktuelle Instanz
  eines Prinzips, nicht der Lerngegenstand selbst
- Keine vollständige UML-Ausbildung; Überblicksniveau genügt für das 3. Jg
- Keine Werkzeugvorgabe für die Schüler jenseits von Ubuntu-LTS bzw. macOS

## Decisions

### D1 — Zweiteilung Governance / Durchführung

Governance (außen, eingefroren, verpflichtend) wird von der Durchführung (innen, frei
wählbar) getrennt. Klassisches Projektmanagement ist damit kein „Vorgehensmodell", das mit
SDD konkurriert, sondern eine eigene Ebene.

```plantuml
@startuml
skinparam monochrome true
skinparam shadowing false
rectangle "GOVERNANCE (aussen, eingefroren)\nProjektauftrag, Ziele, Stakeholder,\nMeilensteinplan, Abnahme, Dokumentation" as G
rectangle "DURCHFUEHRUNG (innen, frei)\nfrueher: Scrum\njetzt: SDD / openspec" as D
G -down-> D : setzt Rahmen
D -up-> G : liefert Nachweise
@enduml
```

*Alternative:* SDD als Ersatz für klassisches PM lehren. Verworfen — die Governance ist
formal vorgeschrieben und wäre im 4./5. Jg nachzuholen.

*Alternative:* Bei Scrum bleiben. Verworfen — Story Points und Velocity setzen eine
Schätz- und Taktökonomie voraus, die durch Agenteneinsatz und Schuljahresrhythmus nicht
mehr trägt.

### D2 — `specs/` ersetzt das Pflichtenheft, der Projektauftrag bleibt Beurteilungsanker

Das Pflichtenheft entfällt. Der Soll-Zustand wird als `specs/<capability>/spec.md`
formuliert und durch `changes/` fortgeschrieben. Beurteilt wird gegen den eingefrorenen
Projektauftrag, gebaut wird gegen die specs.

| Antragsfeld (DA / Projektauftrag) | openspec-Artefakt |
|---|---|
| Ausgangslage | `openspec/config.yaml` → `context:` |
| Zielsetzung | Menge der `specs/` (Capabilities) |
| Individuelle Themenstellung je Schüler | Zuschnitt der `changes/` je Schüler |
| Untersuchungsanliegen | `proposal.md` → Why / offene Fragen |
| Geplantes Ergebnis | `spec.md` → Requirements + Scenarios |
| Meilenstein + Datum | Change archiviert bis Datum |
| Spalte „Verantwortlich" | Change-Ownership + git-Historie |
| Projektfortschritt | `openspec list` / `openspec status` |

*Begründung:* Ohne fixierten Vergleichspunkt könnte ein Team die specs unterwegs an das
anpassen, was fertig geworden ist, und wäre per Definition vollständig. Die Differenz
zwischen Projektauftrag und Endstand wird durch `changes/archive/` sichtbar und ist selbst
Lerngegenstand (Scope-Management).

*Optional:* Initiale Spec-Menge per git-Tag (`baseline-v1`) markieren — das „Pflichtenheft"
ist dann ein `git diff` entfernt.

*Formstruktur:* Die Governance-Artefakte des 3. Jahrgangs folgen der Feldstruktur des
DA-Antrags, damit die Schüler im 5. Jahrgang ein bekanntes Formular ausfüllen. Die
Feldbezeichner der Vorlage sind zweisprachig:

```adoc
== Ausgangslage / Initial situation
== Untersuchungsanliegen / Research objective
== Geplantes Ergebnis / Planned deliverable
```

Das Formular ist deutsch, die Unterrichtssprache englisch; Governance-Fachbegriffe werden
deshalb durchgehend in beiden Sprachen geführt. Begründung und Regelwerk in
`../setup-curriculum-repository/design.md` — P12.

### D3 — Vorgehensmodelle als drei Taktfrequenzen desselben Musters

Wasserfall, Scrum und SDD werden nicht als konkurrierende Schulen gelehrt, sondern als
Instanzen eines invarianten Musters (Ziel klären → Scope abgrenzen → Anforderung präzise
formulieren → bauen → verifizieren → Änderung kontrolliert einbringen) mit
unterschiedlichem Takt: Monate / Wochen / Minuten.

*Begründung:* Erlaubt es, Wasserfall und Scrum ehrlich kurz zu halten (je 1–2 UE), ohne den
Schülern das Vokabular zu nehmen, das sie in Diplomarbeit und Betrieb brauchen. Macht SDD
begründbar statt behauptet.

### D4 — UML von 8 UE auf 5 UE

Bleiben: Use-Case-, Klassen- (inkl. Objekt-) und Aktivitätsdiagramm. Zustandsdiagramm nur
im Überblick. Deployment-Diagramm wandert in den 4. Jg, wo es inhaltlich zum
Kubernetes-Block gehört. Darstellung durchgängig PlantUML.

*Trade-off:* Finanziert den neuen Brücken-Block. Objektdiagramm kostet neben dem
Klassendiagramm fast nichts; Zustandsdiagramme sind in 3.-Jg-Projekten selten tragend.

### D5 — Schätz-Hygiene statt Schätzverfahren

Function Points, COCOMO und Planning Poker entfallen. Stattdessen 1 UE: Zerlegen schlägt
Schätzen, Bandbreite statt Punktwert (Drei-Punkt), Schätzung ≠ Zusage ≠ Zielvorgabe,
Planning Fallacy, verschobene Unsicherheit bei Agenteneinsatz. Kalibrierung läuft gratis
über die Meilenstein-Reviews (geschätzt vs. tatsächlich).

*Begründung:* Parametrische Verfahren brauchen Kalibrierungsdaten, die Schüler nicht haben;
Velocity braucht stabile Sprints, die es im Schuljahr nicht gibt. Alle klassischen Verfahren
schätzen im Kern Implementierungsaufwand — genau den Posten, der durch Agenteneinsatz
geschrumpft ist. Verbleibende Unsicherheit liegt im Spezifizieren, Reviewen, Integrieren.

*Restrisiko:* Fragenkatalog und Manz-Buch nennen die Verfahren. Abgedeckt durch 10 Minuten
Namenskenntnis und Einordnung, keine Anwendungskompetenz.

### D6 — Kreativitätstechniken und Nutzwertanalyse als Paar

Divergieren (U3) und Konvergieren (U4) werden gekoppelt und jeweils sofort angewendet.
6-3-5 Brainwriting als die eine real durchgeführte Technik: erzeugt schriftliche Ergebnisse
(direkt Rohmaterial für die Projektanträge), alle beteiligen sich, ist durch Konstruktion
zeitgeboxt. Weitere Techniken nur benannt und eingeordnet.

Die Nutzwertanalyse macht die Projektauswahl kriterienbasiert und nachvollziehbar statt
willkürlich; die Schüler legen Kriterien und Gewichte selbst fest.

*Alternative:* Kreativitätstechniken in einen Praxis-Slot. Verworfen — Ideenfindung braucht
keinen Rechner, und die Praxis-Slots am Jahresanfang sind mit git belegt, das auf dem
kritischen Pfad liegt.

### D7 — Lernumgebung: Ubuntu-Partition oder macOS, kein WSL2

Ubuntu 26.04 LTS als Dual-Boot-Partition (≥ 100 GB) oder macOS. Ein klassenweites Setup
mit `apt`- und `brew`-Zweig etabliert den Standard; Aufbau und Ablage sind in
`../setup-curriculum-repository/design.md` — P9 entschieden (eigenes Repository
`klassen-setup`).

*Begründung:* Der Gewinn ist Umgebungsisolation, nicht Didaktik — eine saubere, einheitliche
Partition gegenüber N unterschiedlich verkonfigurierten Windows-Installationen. „Works on my
machine" verschwindet als Fehlerklasse.

*Alternative:* WSL2. Verworfen — WSL2 sitzt auf Windows und erbt dessen Fehlkonfiguration
(BIOS-Virtualisierung, Hyper-V-Features, Antivirus). Bei kaputtem Windows kein Fallback.

*Überbrückung* statt Fallback: Ubuntu-Live-USB mit Persistenz. Bootet unabhängig vom
Windows-Zustand, braucht keine Partitionsänderung und beweist vorab, dass die Hardware
Linux bootet.

Ergänzungen zur Installationsanleitung: BitLocker-Recovery-Key **vorher** sichern,
Windows-Schnellstart deaktivieren, SATA-Modus auf AHCI prüfen (Intel RST), Secure Boot
beachten, Partition ≥ 100 GB, RAM ≥ 8 GB (16 empfohlen), Virtualisierung im BIOS aktivieren.

### D8 — asciidoctor, GitHub Actions und Pages in den git-Block integrieren

```
git I-IV               8 UE   Repo/Commit/Push, Branch/Merge, PR/Review, Konflikte
asciidoctor            2 UE   Syntax, Struktur, PlantUML-Einbindung
gh-actions + gh-pages  2 UE   Pipeline adoc -> HTML -> Pages
revealjs               2 UE   just-in-time vor der ersten Praesentation
```

*Begründung:* CI ohne Anwendungsfall bleibt abstrakt; „mein `.adoc` wird beim Push zur
Website" ist die kleinste sinnvolle Pipeline. Projektdokumentation fällt als Nebenprodukt
ab, statt am Jahresende zu entstehen. `ubuntu-latest` wird zur neutralen Instanz zwischen
Linux- und macOS-Geräten (Case-Sensitivity, Architektur).

### D9 — Reserve am Ende, gefüllt mit dem verzichtbarsten Inhalt

U26–U30 sind Reserve und tragen minikube. Fallen Termine aus, entfällt automatisch das
Entbehrlichste; Kerninhalte bleiben unberührt. Kubernetes wird im 4. Jg ohnehin vertieft
(dort Deployment in echte Cloud, im 3. Jg nur minikube lokal).

*Alternative:* Reserve gleichmäßig verteilen. Verworfen — dann trifft ein Ausfall zufälligen
Stoff statt des geplant Entbehrlichen.

### D10 — Sequenz folgt der Werkzeugkette

```
git  -->  AI-Grundlagen  -->  openspec  -->  specs statt Pflichtenheft
```

Der Projektstart ist nicht durch die Theorie begrenzt, sondern durch die Werkzeugverfügbarkeit.
Die Lücke zwischen Projektauftrag (HÜ nach U6) und Baseline-specs (HÜ nach U10) füllt sich
mit genau der Theorie, die erklärt, *warum* jetzt specs statt Pflichtenheft kommen.

Die tiefen AI-Themen (Harness Engineering, Loops, agentische Muster) liegen bewusst nach U10,
wenn die Schüler AI bereits am eigenen Projekt einsetzen.

### D11 — Nutzung des Manz-Schulbuchs

Recherchestand 2026-09-06, keine Rechtsberatung. Die Schulgebrauchs-Ausnahme des § 42
Abs 6 UrhG nimmt Werke aus, die ihrer Beschaffenheit und Bezeichnung nach für den
Unterrichtsgebrauch bestimmt sind. Ein Schulbuch ist genau das — die Ausnahme greift
also **nicht**, auch nicht auf Papier und auch nicht in Klassenstärke. § 42g (digitale
Nutzung) enthält dieselbe Ausnahme und deckt ohnehin nur einen abgegrenzten
Teilnehmerkreis, nicht das offene Netz.

Gleichzeitig sind Fakten und Erkenntnisse nie geschützt, nur ihre konkrete sprachliche
Darstellung.

```
ZULAESSIG                                UNZULAESSIG
Inhalte in eigener Formulierung          Seitenkopien, Scans, PDF-Kapitel weitergeben
eigene Gliederung des Stoffs             Kapitelgliederung 1:1 uebernehmen (§ 6)
Zitat mit Belegfunktion und Quelle       Abbildungen uebernehmen
Verweis auf das Buch als Quelle          Verteilung an die Klasse, auch digital
```

*Folge fuer das Curriculum:* Das Buch bleibt inhaltliche Quelle. Die Gliederung folgt
ohnehin der Werkzeugkette (D10) und nicht der Kapitelfolge des Buchs, wodurch die
Sammelwerksfrage aus § 6 gar nicht erst entsteht. Die vorhandenen PDF-Kapitel dienen der
eigenen Vorbereitung und werden nicht verteilt.

*Verweis:* Die entsprechende Regelung für Bilder auf der öffentlichen Site steht in
`../setup-curriculum-repository/design.md` — P11.

## Jahresrahmen

```
30 Unterrichte x 3 UE = 90 UE geplant
   U1      Einfuehrung                            3 UE  =  1 T /  2 P
   U2-U25  Kernbetrieb                           72 UE  = 24 T / 48 P
   U26-U30 Reserve / Ausfallpuffer               15 UE  (davon 7 UE belegt)
```

Ein Unterricht besteht aus einem Theorieslot (1 UE) und einem Praxisslot (2 UE); ein
Thema fuellt genau einen Slot (`setup-curriculum-repository` — P1). Alle UE-Zahlen sind
daher Vielfache dieser Slotgroesse. **Verbindlich ist `curriculum.yaml`**; die Tabellen
hier sind die Vorgabe, gegen die der CI-Check prueft (P2, Pruefung 2).

**Theorie 26 UE = 26 Themen**

| Block | UE | Inhalt |
|---|---|---|
| `governance` | 9 | Projektbegriff, Ausgangslage, Kreativitätstechniken, Nutzwertanalyse, Stakeholder, Zielsetzung, Projektauftrag, Schätz-Hygiene, Meilensteinplanung, Abnahme (8) + Leistungsfeststellung in der Reserve (1) |
| `vorgehen` | 10 | Vorgehensmodelle-Überblick, Wasserfall, Scrum (3) + SDD / openspec vertieft (5) + Brücke Governance ↔ SDD (2) |
| `modellierung` | 5 | UML: Überblick, Use-Case, Klassen/Objekt, Aktivität, Zustand im Überblick |
| `werkzeuge` | 2 | Kursüberblick U1 (1) + Was ist Software-Engineering (1) |

**Praxis 56 UE = 28 Themen à 2 UE**

| Block | UE | Inhalt |
|---|---|---|
| Lernumgebung | 2 | Einrichtung in U1 |
| git + asciidoctor + gh-actions/Pages + revealjs | 14 | 7 Themen |
| AI inkl. openspec-Praxis | 14 | 7 Themen; die openspec-Praxis (U10) war in der ersten Fassung ohne Budgetposten |
| Docker (inkl. Multi-Arch) | 8 | 4 Themen |
| docker compose | 6 | 3 Themen |
| Meilenstein-Reviews | 6 | 3 Themen |
| minikube *(Reserve-Zone)* | 6 | 3 Themen |

*Abweichung gegenüber der ersten Fassung:* AI 15 → 14 UE und Reviews 7 → 6 UE. Beide
Zahlen waren ungerade und passen nicht in ein Raster aus Zwei-UE-Slots. Die frei
gewordene UE deckt den openspec-Praxisslot mit ab.

*Ungenutzt:* U29 und U30 sowie die Theorieslots von U27 und U28 — 8 UE reiner Puffer
am Jahresende (D9).

## Eröffnungssequenz

```
U1   VORSTELLUNGSEINHEIT (3 UE)
     Ueberblick Stoffgebiet (PlantUML-Mindmap), Organisation, Bewertung,
     Werkzeugkette (warum Linux, warum git, warum Doku als Code),
     Linux: Live-USB-Test -> Installation -> setup.sh,
     Hardware-Checkliste (RAM, Platz, Virtualisierung, Recovery-Key)
     HUE: Live-USB testen, dann installieren

U    THEORIE (1 UE)                    PRAXIS (2 UE)                HUE
--   --------------------------------  ---------------------------  --------------
 2   Projektbegriff, Ausgangslage      git I  (+30 min Trouble-      --
                                       shooting Setup)
 3   Kreativitaetstechniken (6-3-5)    git II: branch, merge        Projektantrag
 4   Nutzwertanalyse -> Auswahl,       git III: PR, review          --
     Teambildung
 5   Stakeholder + Zielsetzung         git IV: conflicts, remotes   --
 6   Projektauftragsstruktur           asciidoctor Grundlagen       Projektauftrag
 7   Vorgehensmodelle-Ueberblick       gh-actions -> gh-pages       --
 8   SDD: warum specs                  AI I: Grundlagen, Prompting  --
 9   BRUECKE Auftrag <-> specs         AI II: Kontext, Continuation --
10   Was ist Software-Engineering      openspec I+II                Baseline-specs
--------------------------------------------------------------------------------
     ab U11: Projekt laeuft, restliche Theorie just-in-time
```

Der Projektantrag wird als `.adoc` im eigenen Repo geschrieben — git-Praxis und
Governance-Hausübung fallen zusammen.

*Nachtrag 2026-09-07:* Der Theorieslot von U10 war in der ersten Fassung frei. Er traegt
jetzt `what-is-software-engineering`, weil das Theoriebudget (26 UE) sonst nicht aufgeht
und der Begriff genau dort hingehoert, wo die Schueler zum ersten Mal spezifizieren
statt zu programmieren.

## Stoffstruktur (Übersicht)

```plantuml
@startmindmap
* SYP 3. Jahrgang
** Governance
*** Projektbegriff / Ausgangslage
*** Kreativitaetstechniken
*** Nutzwertanalyse
*** Stakeholder / Zielsetzung
*** Projektantrag / Projektauftrag
*** Schaetz-Hygiene
*** Meilensteinplanung / Abnahme
** Vorgehen
*** Wasserfall (Ueberblick)
*** Scrum (Ueberblick)
*** SDD / openspec
*** Bruecke Governance <-> SDD
** Modellierung
*** Use-Case-Diagramm
*** Klassen- / Objektdiagramm
*** Aktivitaetsdiagramm
*** Zustandsdiagramm (Ueberblick)
** Werkzeuge
*** Lernumgebung (Ubuntu / macOS, setup.sh)
*** git
*** asciidoctor / gh-actions / Pages
*** AI-Nutzung
*** Docker / compose
*** minikube
@endmindmap
```

## Risks / Trade-offs

| Risiko | Mitigation |
|---|---|
| Linux-Installation scheitert bei einzelnen Schülern und blockiert die Praxis ab U2 | Live-USB-Test **vor** dem Partitionieren; 30 min Troubleshooting-Puffer in U2; `setup.sh` reduziert Folgefehler; Recovery-Key-Pflicht in der Checkliste |
| specs driften mit dem Ist-Stand, Beurteilbarkeit geht verloren | Projektauftrag eingefroren als Beurteilungsanker; optionaler git-Tag `baseline-v1`; `changes/archive/` als Änderungsnachweis |
| openspec ist ein junges Tool und ändert sich | Prinzip (SDD) ist Lerngegenstand, Tool ist die aktuelle Instanz; Curriculum-Struktur benennt das Prinzip, nicht das Kommando |
| Fragenkatalog / Matura fragt klassische Schätzverfahren ab | 10 Minuten Namenskenntnis und Einordnung im Governance-Block |
| Apple Silicon erzeugt arm64-Images, die im 4. Jg beim Cloud-Deployment brechen | Multi-Arch im Docker-Block explizit behandeln; `ubuntu-latest` in CI als Schiedsrichter |
| macOS-Standarddateisystem ist case-insensitiv → „bei mir geht's"-Fehler in gemischten Teams | CI auf `ubuntu-latest` als verbindliche Instanz, ab U7 verfügbar |
| Governance-Artefakte als Hausübung → schwache Qualität | Struktur-UE unmittelbar davor; Review im folgenden Unterricht; Nutzwertanalyse macht Antragsqualität sichtbar |
| Terminausfälle fressen Kerninhalte | Reserve am Ende, gefüllt mit minikube (D9) |
| Praxis-Slots am Jahresanfang vollständig durch git belegt | Ideenfindung braucht keinen Rechner und läuft im Theorie-Slot (D6) |

## Einführungsplan

1. Threads 2–5 klären: Speicherformat der Stoffstruktur, Publikationswege, Rechtslage
   Schulbuch, Detaillierungsgrad der Lernressourcen
2. `specs/` je Capability aus `proposal.md` schreiben (Lernziele als prüfbare Requirements)
3. `tasks.md` ableiten: Erstellung der Lernressourcen auf Englisch, `setup.sh`,
   Vorlagen-Repository für Schülerprojekte
4. Fragenkatalog-Umbau als eigener Change

## Open Questions

Stand 2026-09-07: durch `curriculum.yaml` beantwortet.

- ~~Schätzverfahren doch aufnehmen?~~ **Nein.** `governance-estimation-hygiene` (U15)
  behandelt Schätz-Hygiene; Function Points, COCOMO und Planning Poker werden dort nur
  benannt und eingeordnet.
- ~~Feinaufteilung der AI-UE~~ **Entschieden:** sieben Praxisthemen — Grundlagen und
  Kontext vor der openspec-Praxis (U8, U9), Vertiefung danach (U11, U12, U23, U25),
  dazu `openspec-hands-on` in U10.
- ~~Zeitpunkt des revealjs-Blocks~~ **U22**, unmittelbar vor dem dritten
  Meilenstein-Review in U24.

Offen bleibt nur, was von außerhalb abhängt: die Abstimmung mit dem 4./5. Jahrgang über
Deployment-Diagramm, Kubernetes-Vertiefung und die gepinnte JDK-Version (Aufgaben 4.1
und 4.2).
