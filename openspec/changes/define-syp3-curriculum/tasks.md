# Tasks: Curriculum SYP 3. Jahrgang definieren

> Offene Fragen aus `design.md` sind durch `curriculum.yaml` beantwortet:
> Schaetzverfahren entfallen (`governance-estimation-hygiene`, U15), die AI-UE sind auf
> sieben Praxisthemen aufgeteilt (U8, U9, U17, U18, U23, U24 plus openspec-Praxis U10),
> revealjs liegt in U22 vor dem dritten Meilenstein-Review. Aufgabe 5.1 zieht den
> Abschnitt "Open Questions" entsprechend nach.
>
> Nicht in diesem Change: Ausarbeitung der Lernressourcen (eigener Change) sowie
> Werkzeuge, Pipeline und Repository-Aufbau (`setup-curriculum-repository`).

## 1. Stoffstruktur gegen die Specs abgleichen

- [ ] 1.1 Abdeckungstabelle Requirement -> `topic-id` fuer alle acht Capabilities erstellen und als `coverage.md` im Change ablegen; Pruefung: jedes Requirement der acht Spec-Dateien nennt mindestens ein Topic, und jedes der 54 Topics traegt mindestens ein Requirement
- [ ] 1.2 Luecken aus 1.1 schliessen: fehlende Topics ergaenzen oder das betroffene Requirement anpassen; Pruefung: zweiter Lauf der Tabelle ohne offene Zeile
- [ ] 1.3 Budget gegen den Jahresrahmen pruefen: 26 UE Theorie / 56 UE Praxis, Blocksummen 9/10/5/2; Pruefung: von Hand gerechnete Summen stimmen mit `meta.budget` und `meta.budget_je_block` ueberein (spaeter maschinell durch Pruefung 2 des CI-Checks)
- [ ] 1.4 Eroeffnungssequenz U1-U10 aus `design.md` Zeile fuer Zeile gegen `curriculum.yaml` pruefen; Pruefung: Theorie- und Praxisslot jedes Unterrichts entsprechen der Tabelle, Hausuebungen (Projektantrag nach U3, Projektauftrag nach U6, Baseline-specs nach U10) sind zugeordnet
- [ ] 1.5 Reservezone U26-U30 pruefen: minikube in der Reserve, U29/U30 und die Theorieslots von U27/U28 frei (D9); Pruefung: kein Kerninhalt liegt hinter U25

## 2. Governance-Vorlagen (D2, P12)

- [ ] 2.1 Vorlage Projektantrag mit der Feldstruktur des DA-Antrags und zweisprachigen Feldbezeichnern (`Ausgangslage / Initial situation` usw.); Pruefung: jedes Feld des DA-Antrags kommt genau einmal vor
- [ ] 2.2 Vorlage Projektauftrag samt Einfrier-Regel und optionalem `baseline-v1`-Tag; Pruefung: Vorlage benennt, was eingefroren wird und woran spaeter beurteilt wird
- [ ] 2.3 Vorlage Meilensteinplan als PlantUML-Gantt mit Termin, Ergebnis und Spalte "Verantwortlich / Responsible"; Pruefung: Plan rendert und enthaelt je Meilenstein ein pruefbares Ergebnis
- [ ] 2.4 Vorlage Abnahmeprotokoll (Abnahmekriterien, Ist-Stand, Restpunkte); Pruefung: Kriterien verweisen auf den eingefrorenen Projektauftrag, nicht auf den Endstand
- [ ] 2.5 Zuordnungstabelle Antragsfeld -> openspec-Artefakt aus D2 als eigenstaendiges Material fuer die Bruecken-Themen (U11/U12) ausformulieren; Pruefung: jede Zeile nennt Feld, Artefakt und den Nachweis, an dem der Fortschritt sichtbar wird
- [ ] 2.6 Vorlagen an `setup-curriculum-repository` Aufgabe 8.2 uebergeben; Pruefung: dort eingebunden und im Vorlagen-Repository sichtbar

## 3. Lernumgebung vorbereiten (D7)

- [ ] 3.1 Hardware-Checkliste erstellen: RAM >= 8 GB (16 empfohlen), Partition >= 100 GB, Virtualisierung im BIOS, SATA-Modus AHCI, Secure Boot, Windows-Schnellstart aus, BitLocker-Recovery-Key vorher gesichert; Pruefung: Liste deckt jeden Punkt aus D7 ab und ist vor U1 verteilbar
- [ ] 3.2 Ablauf Live-USB mit Persistenz -> Installationstest -> Partitionierung beschreiben; Pruefung: der Hardwaretest steht vor jedem Schritt, der die Platte veraendert
- [ ] 3.3 Abgrenzung zu WSL2 schriftlich festhalten (kein Fallback, erbt die Windows-Fehlkonfiguration); Pruefung: Begruendung steht dort, wo Schueler nach WSL2 fragen werden
- [ ] 3.4 Verweis auf `klassen-setup` statt eigener Werkzeugliste; Pruefung: die Lernumgebungs-Unterlage nennt kein Werkzeug, das nicht in `versions.env` gepinnt ist

## 4. Abstimmung und Quellenlage

- [ ] 4.1 Verschiebung von Deployment-Diagramm und Kubernetes-Vertiefung in den 4. Jahrgang mit den dort Unterrichtenden abstimmen; Pruefung: Zusage oder Ablehnung im Change vermerkt, bei Ablehnung Ruecknahme in `curriculum.yaml` und Budget
- [ ] 4.2 JDK-Version fuer `versions.env` mit 4./5. Jahrgang abstimmen und an `setup-curriculum-repository` Aufgabe 7.3 melden; Pruefung: eine Version, die in allen drei Jahrgaengen gilt
- [ ] 4.3 Materialbestand je Topic sichten (Manz-Kapitel, PUMA-Kreativitaetstechniken, PUMA-Nutzwertanalyse, UML Uni Heidelberg, `01.Vorgehensmodelle.key`) und in `coverage.md` je Topic als Quelle vermerken; Pruefung: jedes Governance- und Modellierungs-Topic nennt seine Quelle oder ausdruecklich keine
- [ ] 4.4 Nutzungsregel fuer das Manz-Schulbuch aus D11 an sichtbarer Stelle festhalten: eigene Formulierung, eigene Gliederung, keine Abbildungen, keine Weitergabe der PDF-Kapitel; Pruefung: Regel steht im `README.adoc` des Curriculum-Repositorys neben der Bildherkunfts-Regel

## 5. Abschluss

- [ ] 5.1 Abschnitt "Open Questions" in `design.md` auf den Stand der yaml bringen (Schaetzverfahren entschieden, AI-Aufteilung entschieden, revealjs auf U22 gelegt); Pruefung: keine Frage bleibt ohne Entscheidung oder Vertagungsgrund
- [ ] 5.2 Uebergabe an den Autoren-Change: Reihenfolge der zu schreibenden Module aus der Eroeffnungssequenz ableiten (U1-U10 zuerst); Pruefung: Liste liegt vor und beginnt mit den Topics, die vor Schulbeginn fertig sein muessen
