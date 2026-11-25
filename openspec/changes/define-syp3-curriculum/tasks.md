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
- [x] 3.2 Ablauf Checkliste -> Recovery-Key sichern -> Partitionierung beschreiben; Prüfung: jeder vorab prüfbare Punkt steht vor dem ersten Schritt, der die Platte verändert (Nachtrag 2026-09-27: der vorgeschaltete Live-USB-Test ist entfallen, siehe D7)
- [x] 3.3 Abgrenzung zu WSL2 schriftlich festhalten (kein Fallback, erbt die Windows-Fehlkonfiguration); Prüfung: Begründung steht dort, wo Schüler nach WSL2 fragen werden
- [x] 3.4 Verweis auf `klassen-setup` statt eigener Werkzeugliste; Prüfung: die Lernumgebungs-Unterlage nennt kein Werkzeug, das nicht in `versions.env` gepinnt ist

## 4. Abstimmung und Quellenlage

- [ ] 4.1 Verschiebung der Kubernetes-Vertiefung in den 4. Jahrgang mit den dort Unterrichtenden abstimmen (das Deployment-Diagramm bleibt seit 2026-11-25 im 3. Jg, D13); Prüfung: Zusage oder Ablehnung im Change vermerkt, bei Ablehnung Rücknahme in `curriculum.yaml` und Budget
- [ ] 4.2 JDK-Version für `versions.env` mit 4./5. Jahrgang abstimmen und an `setup-curriculum-repository` Aufgabe 7.3 melden; Prüfung: eine Version, die in allen drei Jahrgängen gilt
- [x] 4.3 Materialbestand je Topic sichten (Manz-Kapitel, PUMA-Kreativitätstechniken, PUMA-Nutzwertanalyse, UML Uni Heidelberg, `01.Vorgehensmodelle.key`) und in `coverage.md` je Topic als Quelle vermerken; Prüfung: jedes Governance- und Modellierungs-Topic nennt seine Quelle oder ausdrücklich keine
- [x] 4.4 Nutzungsregel für das Manz-Schulbuch aus D11 an sichtbarer Stelle festhalten: eigene Formulierung, eigene Gliederung, keine Abbildungen, keine Weitergabe der PDF-Kapitel; Prüfung: Regel steht im `README.adoc` des Curriculum-Repositorys neben der Bildherkunfts-Regel

## 5. Abschluss

- [x] 5.1 Abschnitt "Open Questions" in `design.md` auf den Stand der yaml bringen (Schätzverfahren entschieden, AI-Aufteilung entschieden, revealjs auf U22 gelegt); Prüfung: keine Frage bleibt ohne Entscheidung oder Vertagungsgrund
- [x] 5.2 Übergabe an den Autoren-Change: Reihenfolge der zu schreibenden Module aus der Eröffnungssequenz ableiten (U1-U10 zuerst); Prüfung: Liste liegt vor und beginnt mit den Topics, die vor Schulbeginn fertig sein müssen

## 6. Nachtrag 2026-11-25: Vorgehensmodelle und UML (D12-D14)

- [x] 6.1 `curriculum.yaml` umstellen: `uml-class-object` auf L22, `uml-use-case` auf L23, `uml-activity` wird `uml-activity-state` (L24), `uml-state-overview` wird `uml-architecture` (L25), `requires` nachziehen (`uml-use-case` setzt `process-scrum` voraus); Prüfung: `tools/check-curriculum.py` ohne Befund, Budget unverändert
- [x] 6.2 `coverage.md` auf die neuen Requirements von `uml-basics` und `vorgehen-sdd` und die umbenannten Topics bringen; Prüfung: jedes Requirement nennt ein Topic, jedes Topic trägt ein Requirement
- [ ] 6.3 Modul `sdd-principle-not-tool` (L18) nach D14 schreiben; Prüfung: Tabelle Prinzip/Werkzeug mit mindestens zwei Werkzeugen, die Übung „openspec gibt es morgen nicht mehr", Überleitung zu L19
- [ ] 6.4 Module `process-waterfall` (L19) und `process-scrum` (L20) aus den Folien nach D12 auf Englisch schreiben; Prüfung: jede Folie außer 1, 5 und 41 ist einem Abschnitt zugeordnet, kein Bild mit deutschem Text
- [ ] 6.5 Bilder mit deutschem Text nachzeichnen (Folien 4, 7, 11, 14); die Mindmaps nach den Freeplane-Dateien in `assets/freeplane/` als `@startmindmap`; Prüfung: Diagramme rendern, Inhalt stimmt mit dem Original überein
- [ ] 6.6 Herkunftsklasse `quoted` in P11 (`setup-curriculum-repository`) und `tools/rights-report.py` ergänzen, dekorative Bilder nur in Moodle; Prüfung: der Report zählt `quoted` getrennt, kein dekoratives fremdes Bild im Site-Build
- [ ] 6.7 Module `uml-overview` (L21, WBS nach UML 2.5), `uml-class-object` (L22, DOM), `uml-use-case` (L23), `uml-activity-state` (L24), `uml-architecture` (L25) nach D13 schreiben; Prüfung: nur die Notationselemente aus der Tabelle in D13, alle Diagramme als PlantUML, kein Projektthema als Beispiel
