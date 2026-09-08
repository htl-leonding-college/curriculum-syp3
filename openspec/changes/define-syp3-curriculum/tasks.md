# Tasks: Curriculum SYP 3. Jahrgang definieren

> Offene Fragen aus `design.md` sind durch `curriculum.yaml` beantwortet:
> Schätzverfahren entfallen (`governance-estimation-hygiene`, U15), die AI-UE sind auf
> sieben Praxisthemen aufgeteilt (U8, U9, U17, U18, U23, U24 plus openspec-Praxis U10),
> revealjs liegt in U22 vor dem dritten Meilenstein-Review. Aufgabe 5.1 zieht den
> Abschnitt "Open Questions" entsprechend nach.
>
> Nicht in diesem Change: Ausarbeitung der Lernressourcen (eigener Change) sowie
> Werkzeuge, Pipeline und Repository-Aufbau (`setup-curriculum-repository`).

## 1. Stoffstruktur gegen die Specs abgleichen

- [x] 1.1 Abdeckungstabelle Requirement -> `topic-id` für alle acht Capabilities erstellen und als `coverage.md` im Change ablegen; Prüfung: jedes Requirement der acht Spec-Dateien nennt mindestens ein Topic, und jedes der 54 Topics trägt mindestens ein Requirement
- [x] 1.2 Lücken aus 1.1 schließen: fehlende Topics ergänzen oder das betroffene Requirement anpassen; Prüfung: zweiter Lauf der Tabelle ohne offene Zeile
- [x] 1.3 Budget gegen den Jahresrahmen prüfen: 26 UE Theorie / 56 UE Praxis, Blocksummen 9/10/5/2; Prüfung: von Hand gerechnete Summen stimmen mit `meta.budget` und `meta.budget_je_block` überein (später maschinell durch Prüfung 2 des CI-Checks)
- [x] 1.4 Eröffnungssequenz U1-U10 aus `design.md` Zeile für Zeile gegen `curriculum.yaml` prüfen; Prüfung: Theorie- und Praxisslot jedes Unterrichts entsprechen der Tabelle, Hausübungen (Projektantrag nach U3, Projektauftrag nach U6, Baseline-specs nach U10) sind zugeordnet
- [x] 1.5 Reservezone U26-U30 prüfen: minikube in der Reserve, U29/U30 und die Theorieslots von U27/U28 frei (D9); Prüfung: kein Kerninhalt liegt hinter U25

## 2. Governance-Vorlagen (D2, P12)

- [x] 2.1 Vorlage Projektantrag mit der Feldstruktur des DA-Antrags und zweisprachigen Feldbezeichnern (`Ausgangslage / Initial situation` usw.); Prüfung: jedes Feld des DA-Antrags kommt genau einmal vor
- [x] 2.2 Vorlage Projektauftrag samt Einfrier-Regel und optionalem `baseline-v1`-Tag; Prüfung: Vorlage benennt, was eingefroren wird und woran später beurteilt wird
- [x] 2.3 Vorlage Meilensteinplan als PlantUML-Gantt mit Termin, Ergebnis und Spalte "Verantwortlich / Responsible"; Prüfung: Plan rendert und enthält je Meilenstein ein prüfbares Ergebnis
- [x] 2.4 Vorlage Abnahmeprotokoll (Abnahmekriterien, Ist-Stand, Restpunkte); Prüfung: Kriterien verweisen auf den eingefrorenen Projektauftrag, nicht auf den Endstand
- [x] 2.5 Zuordnungstabelle Antragsfeld -> openspec-Artefakt aus D2 als eigenständiges Material für die Brücken-Themen (U11/U12) ausformulieren; Prüfung: jede Zeile nennt Feld, Artefakt und den Nachweis, an dem der Fortschritt sichtbar wird
- [x] 2.6 Vorlagen an `setup-curriculum-repository` Aufgabe 8.2 übergeben; Prüfung: dort eingebunden und im Vorlagen-Repository sichtbar

## 3. Lernumgebung vorbereiten (D7)

- [x] 3.1 Hardware-Checkliste erstellen: RAM >= 8 GB (16 empfohlen), Partition >= 100 GB, Virtualisierung im BIOS, SATA-Modus AHCI, Secure Boot, Windows-Schnellstart aus, BitLocker-Recovery-Key vorher gesichert; Prüfung: Liste deckt jeden Punkt aus D7 ab und ist vor U1 verteilbar
- [x] 3.2 Ablauf Live-USB mit Persistenz -> Installationstest -> Partitionierung beschreiben; Prüfung: der Hardwaretest steht vor jedem Schritt, der die Platte verändert
- [x] 3.3 Abgrenzung zu WSL2 schriftlich festhalten (kein Fallback, erbt die Windows-Fehlkonfiguration); Prüfung: Begründung steht dort, wo Schüler nach WSL2 fragen werden
- [x] 3.4 Verweis auf `klassen-setup` statt eigener Werkzeugliste; Prüfung: die Lernumgebungs-Unterlage nennt kein Werkzeug, das nicht in `versions.env` gepinnt ist

## 4. Abstimmung und Quellenlage

- [ ] 4.1 Verschiebung von Deployment-Diagramm und Kubernetes-Vertiefung in den 4. Jahrgang mit den dort Unterrichtenden abstimmen; Prüfung: Zusage oder Ablehnung im Change vermerkt, bei Ablehnung Rücknahme in `curriculum.yaml` und Budget
- [ ] 4.2 JDK-Version für `versions.env` mit 4./5. Jahrgang abstimmen und an `setup-curriculum-repository` Aufgabe 7.3 melden; Prüfung: eine Version, die in allen drei Jahrgängen gilt
- [x] 4.3 Materialbestand je Topic sichten (Manz-Kapitel, PUMA-Kreativitätstechniken, PUMA-Nutzwertanalyse, UML Uni Heidelberg, `01.Vorgehensmodelle.key`) und in `coverage.md` je Topic als Quelle vermerken; Prüfung: jedes Governance- und Modellierungs-Topic nennt seine Quelle oder ausdrücklich keine
- [x] 4.4 Nutzungsregel für das Manz-Schulbuch aus D11 an sichtbarer Stelle festhalten: eigene Formulierung, eigene Gliederung, keine Abbildungen, keine Weitergabe der PDF-Kapitel; Prüfung: Regel steht im `README.adoc` des Curriculum-Repositorys neben der Bildherkunfts-Regel

## 5. Abschluss

- [x] 5.1 Abschnitt "Open Questions" in `design.md` auf den Stand der yaml bringen (Schätzverfahren entschieden, AI-Aufteilung entschieden, revealjs auf U22 gelegt); Prüfung: keine Frage bleibt ohne Entscheidung oder Vertagungsgrund
- [x] 5.2 Übergabe an den Autoren-Change: Reihenfolge der zu schreibenden Module aus der Eröffnungssequenz ableiten (U1-U10 zuerst); Prüfung: Liste liegt vor und beginnt mit den Topics, die vor Schulbeginn fertig sein müssen
