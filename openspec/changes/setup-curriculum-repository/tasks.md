# Tasks: Curriculum-Repository und Publikationsweg aufsetzen

> Werkzeugsprache: **Python** (offene Frage aus `design.md` entschieden am 2026-09-07).
> PyYAML als einzige Fremdabhaengigkeit, Ausfuehrung in Actions ueber `setup-python`.
> `klassen-setup` bleibt Bash (P9).
>
> Waehrend der Umsetzung entschieden (2026-09-07): Themen tragen
> `status: planned | ready` (Default `planned`). Bijektion, Pflichtabschnitte,
> Outcome-Kopplung und Modulskelett greifen nur fuer `ready`; verwaiste Dateien und
> unbekannte Themen-IDs fallen immer auf. Design P1/P2 und die Specs
> `curriculum-model` und `curriculum-validation` sind nachgezogen.
>
> Stand 2026-09-07: `klassen-setup` und `student-project-template` liegen als
> lokale Repositories neben `curriculum-syp3` (je ein Commit, kein Remote).
> Alles, was GitHub veraendert — Repos anlegen, pushen, Pages aktivieren,
> Hinweis im bestehenden Fragenkatalog — steht noch aus und ist bewusst nicht
> ungefragt ausgefuehrt worden.

## 1. Repository-Geruest

- [x] 1.1 Verzeichnisse `modules/`, `tools/`, `templates/`, `.github/workflows/` anlegen; Pruefung: `ls` zeigt alle vier, `git status` fuehrt sie (Platzhalterdatei je leerem Verzeichnis)
- [x] 1.2 `README.adoc` mit Zweck, Layout aus P6, Verweis auf `curriculum.yaml` als einzige Strukturwahrheit und auf die Zustaendigkeitsregel der beiden Fragenkataloge (P8); Pruefung: Datei rendert mit `local-convert.sh` fehlerfrei
- [x] 1.3 Python-Werkzeugbasis: `tools/requirements.txt` (PyYAML), `tools/README.adoc` mit Aufrufkonventionen; Pruefung: `pip install -r tools/requirements.txt` laeuft in frischem venv durch
- [x] 1.4 Gemeinsames Lademodul `tools/curriculum.py` (liest `curriculum.yaml`, leitet Modulpfade aus der ID ab, meldet fehlende Pflichtfelder mit Zeilenangabe); Pruefung: `python -c "import tools.curriculum as c; print(len(c.load().topics))"` gibt 54 aus

## 2. CI-Check `tools/check-curriculum.py` (P2)

- [x] 2.1 Grundgeruest mit Pruefungsregistry, Sammel-Reporting (Datei, Zeile, Ist/Soll) und Exit-Code != 0 bei mindestens einem Fehler; Pruefung: Lauf auf einem manipulierten Fixture endet mit Exit-Code 1 und listet alle Fehler, nicht nur den ersten
- [x] 2.2 Pruefung 1 Bijektion: jedes Topic hat `index.adoc`, jede `.adoc` unter `modules/` traegt eine in der yaml bekannte `:topic-id:`; Pruefung: Fixture mit fehlender Datei und Fixture mit verwaister Datei schlagen je mit dem erwarteten Text fehl
- [x] 2.3 Pruefung 2 Budget: Summe `ue` je `kind` gegen `meta.budget` (26/56) und je Block gegen `meta.budget_je_block`; Pruefung: Fixture mit einem Theorie-Topic zu viel nennt Ist- und Sollwert
- [x] 2.4 Pruefung 3 Graph: `requires` zeigt nur auf existierende IDs, keine Zyklen, keine Vorwaertsreferenz ueber `lesson` bzw. `taught_in`; Pruefung: Fixtures fuer unbekannte ID, Zweierzyklus und verschobene Voraussetzung schlagen fehl und nennen beide Topics mit Unterrichtsnummer
- [x] 2.5 Pruefung 4 Vollstaendigkeit: `taught_in` und `prerequisite_for` je Topic gesetzt, jedes Topic mit `kind: praxis` hat mindestens eine Frage; Pruefung: Praxis-Fixture ohne Frage schlaegt fehl, Theorie-Fixture ohne Frage nicht
- [x] 2.6 Pruefung 5 Slot-Belegung: je `lesson` hoechstens ein Theorie- und ein Praxis-Topic, keine Luecke zwischen Unterricht 1 und dem letzten belegten; Pruefung: Doppelbelegung und Luecke schlagen je mit Nummernangabe fehl
- [x] 2.7 Pruefung 6 Pflichtabschnitte: `== Learning outcomes`, `== Decisions`, `== Pitfalls`, `== Terminology` vorhanden und nicht leer, ausdrueckliche Nullaussage gilt als erfuellt; Pruefung: Fixture ohne `Decisions` schlaegt fehl, Fixture mit "None specific to this topic." besteht
- [x] 2.8 Pruefung 7 Outcome-Kopplung: jedes Learning outcome hat >= 1 Frage in `questions.adoc`, jede Frage verweist auf ein existierendes Outcome; Pruefung: beide Richtungen als Fixture rot
- [x] 2.9 Pruefung 8 Bildherkunft: jedes `image::` unter `modules/` traegt genau eine Klasse `own | free | unclear`, `free` verlangt Lizenzname und URL; Pruefung: Bild ohne Klasse und `free` ohne Quelle schlagen mit Datei und Zeile fehl
- [x] 2.10 Pruefung 9 Modulskelett: jedes Modulverzeichnis enthaelt `index.adoc`, `exercises.adoc`, `questions.adoc`; `exercises.adoc` darf inhaltsleer sein; Pruefung: Modul ohne Aufgabendatei schlaegt fehl, Modul mit leerer Aufgabendatei besteht
- [x] 2.11 Zusatzpruefung Strukturattribute: `.adoc` unter `modules/` traegt ausser `:topic-id:` kein Attribut mit UE-Zahl, Block, Jahrgang oder Voraussetzung; Pruefung: Fixture mit `:ue: 2` schlaegt fehl und nennt Datei und Attribut
- [x] 2.12 Fixture-Testsuite unter `tools/tests/` mit je einem roten und einem gruenen Fall pro Pruefung; Pruefung: `python -m pytest tools/tests` gruen, jede der neun Pruefungen mindestens einmal abgedeckt
- [x] 2.13 Lauf gegen den echten Stand: `python tools/check-curriculum.py` meldet ausschliesslich noch nicht angelegte Module und keinen Strukturfehler; Befund im Continuation-Dokument festhalten

## 3. Generatoren (P3)

- [x] 3.1 `tools/gen-mindmap.py`: `curriculum.yaml` -> `@startmindmap` je Block und Topic; Pruefung: neues Topic im Fixture erscheint nach dem Lauf als Knoten
- [x] 3.2 `tools/gen-nav.py`: Navigation in Unterrichtsreihenfolge, verlinkt `assignment_template` wo gesetzt; Pruefung: geaenderte `lesson` aendert die Reihenfolge ohne Handarbeit
- [x] 3.3 `tools/gen-ue-overview.py`: UE-Uebersicht je Block und je Art mit Summen; Pruefung: Ausgabe stimmt mit den Budgettabellen aus `define-syp3-curriculum/design.md` ueberein
- [x] 3.4 `tools/gen-questions.py`: Sammellauf ueber alle `questions.adoc`, Tags `block`, `taught_in`, `prerequisite_for`, `topic` aus dem Modell; Pruefung: erzeugter Katalog enthaelt keine Tags aus Ueberschriftentext
- [x] 3.5 Erzeugte Artefakte nach `build/` schreiben, jede Datei mit Kopfzeile "GENERATED — do not edit"; Pruefung: `build/` ist in `.gitignore` bzw. als generiert gekennzeichnet
- [x] 3.6 Erzeugte Artefakte bleiben unversioniert: Generatoren schreiben ausschliesslich nach `build/` (in `.gitignore`) und laufen bei jedem Build vor asciidoctor; Pruefung: `test_repo_layout.py` faellt rot, sobald eine Datei mit GENERATED-Kopf im Versionsstand liegt oder `build/` nicht ignoriert wird — ein `git diff`-Vergleich entfaellt damit, weil eine Handaenderung an `build/` den naechsten Lauf ohnehin nicht ueberlebt

## 4. Modulformat und Skelett (P4)

- [x] 4.1 `templates/module/` mit `index.adoc` (feste Abschnittsfolge inkl. Pflichtabschnitte), `exercises.adoc` (Kennzeichnung `drill|project`, Loesung als `[%collapsible]`), `questions.adoc` (Verweis auf Outcome-ID); Pruefung: aus der Vorlage erzeugtes Modul besteht die Pruefungen 6, 7, 9
- [x] 4.2 `tools/new-module.py <topic-id>`: legt Verzeichnis, drei Dateien und `images/` aus Vorlage und yaml-Daten an; Pruefung: Aufruf fuer ein Topic ohne Modul erzeugt ein Skelett, das `check-curriculum.py` nur wegen fehlender Inhalte, nicht wegen Struktur bemaengelt
- [x] 4.3 Modulskelette fuer `git-basics` und `sdd-openspec-artifacts` (so heisst das Thema im Modell) anlegen (Einfuehrungsplan Schritt 3); Pruefung: beide Module bestehen alle neun Pruefungen mit ausdruecklichen Nullaussagen, wo noch nichts feststeht
- [x] 4.4 Autorenleitfaden `templates/module/README.adoc`: Abschnittszweck, Nullaussage, Aufgabenarten, PlantUML-Default, Bildherkunft, Terminology-Paare; Pruefung: Leitfaden nennt jede der neun CI-Pruefungen mit der Stelle, an der sie greift

## 5. Pipeline und Publikation (P7, P11)

- [x] 5.1 Containerisiertes asciidoctor-Image um `asciidoctor-diagram` und Graphviz ergaenzen, `local-convert.sh` uebernehmen und anpassen; Pruefung: ein Modul mit PlantUML-Block rendert lokal ohne lokale Ruby-Installation
- [x] 5.2 Workflow `build`: `check-curriculum.py` -> Generatoren -> asciidoctor -> Deploy auf `gh-pages`; Pruefung: Push auf `main` veroeffentlicht, roter Check verhindert das Deploy und die Site bleibt auf dem letzten gueltigen Stand
- [x] 5.3 Eigener Job `rights-check`: faellt rot bei `unclear > 0`, listet Datei und Zeile, blockiert das Deploy nicht; Pruefung: Modul mit `unclear`-Bild wird veroeffentlicht und der Job meldet es rot
- [x] 5.4 revealjs-Ausgabe aus derselben Quelle erzeugen; Pruefung: Aenderung an einem Modultext erscheint ohne zweite Bearbeitung in der Praesentationsansicht
- [ ] 5.5 `publish.sh` fuer rsync auf den Schulwebspace, lokal ausfuehrbar, keine Zugangsdaten in Actions-Secrets; Pruefung: Lauf legt die Site parallel zur bestehenden Hugo-Site ab, ein Altlink bleibt erreichbar
- [x] 5.6 GitHub Pages fuer `htl-leonding-college/curriculum-syp3` aktivieren und Einstiegsseite verlinken (Altsite, bestehender Fragenkatalog); Pruefung: oeffentliche URL liefert die Site ohne Anmeldung

## 6. Fragenkatalog (P8)

- [x] 6.1 Katalogseite aus `gen-questions.py` veroeffentlichen, sortier- und filterbar nach Block, unterrichtendem Jahrgang, voraussetzendem Jahrgang und Thema; Pruefung: Abfrage "alle Fragen mit `prerequisite_for: jg4`" liefert die erwartete Menge
- [ ] 6.2 Uebernahme geeigneter Fragen aus dem bestehenden Katalog, je Frage genau ein Modul; Pruefung: nicht zugeordnete Fragen erscheinen nicht im erzeugten Katalog und fallen bei Pruefung 7 auf
- [ ] 6.3 Zustaendigkeitshinweis auf beiden Einstiegsseiten (neuer Katalog massgeblich fuer SYP 3. Jg ab 2026/27, bestehender bleibt Archiv); Pruefung: bestehende URLs und Anker des alten Katalogs sind unveraendert erreichbar

## 7. Repository `klassen-setup` (P9)

- [ ] 7.1 Repository `htl-leonding-college/klassen-setup` public anlegen mit `README.adoc`; Pruefung: `git clone` ohne Anmeldung moeglich
- [x] 7.2 `setup-tools.sh` mit OS-Weiche (`apt`/`brew`), einer Werkzeugliste, Idempotenzpruefung je Schritt; Werkzeuge: JetBrains Toolbox, SDKMAN (JDK/Maven/Gradle), Docker, kubectl, minikube, zsh + powerlevel10k; Pruefung: zweiter Lauf auf eingerichtetem Geraet aendert nichts und meldet den Zustand als hergestellt
- [ ] 7.3 `versions.env` mit gepinnten Versionen; JDK-Version nach Abstimmung mit 4./5. Jahrgang eintragen (offene Frage aus `design.md`); Pruefung: Aenderung einer Version wirkt sich ohne weitere Stelle im Script aus
- [x] 7.4 `setup-identity.sh` interaktiv und einmalig (git user.name/user.email, SSH-Key, `gh auth`), keine Zugangsdaten im Repository; Pruefung: Lauf von `setup-tools.sh` danach laesst Name, Schluessel und Anmeldungen unangetastet
- [x] 7.5 Bootstrap-Anleitung ohne `curl … | bash`: herunterladen, lesen, ausfuehren; Pruefung: `README.adoc` fuehrt den Weg mit lesbarem Zwischenschritt und begruendet ihn
- [ ] 7.6 Vollstaendiger Durchlauf auf frisch installiertem Ubuntu 26.04 LTS und auf macOS vor U1 (Einfuehrungsplan 5a); Pruefung: beide Laeufe protokolliert, Abbruch mitten im Lauf und Fortsetzung einmal bewusst getestet
- [ ] 7.7 git-Tag fuer das Schuljahr 2026/27 setzen; Pruefung: Tag zeigt auf den erprobten Stand aus 7.6

## 8. Vorlage fuer Schuelerprojekte (P6, P13)

- [x] 8.1 (lokal angelegt, Remote steht aus) `htl-leonding-college/student-project-template`: openspec-Scaffold, `docs/` als AsciiDoc, CI nach Muster 5.2; Pruefung: aus der Vorlage erzeugtes Repo baut beim ersten Push eine Pages-Site
- [x] 8.2 Governance-Vorlagen aus `define-syp3-curriculum` (Projektantrag, Projektauftrag, Meilensteinplan, Abnahme) mit zweisprachigen Feldbezeichnern einbinden; Pruefung: Vorlage enthaelt die Feldstruktur des DA-Antrags in beiden Sprachen
- [x] 8.3 `baseline-v1`-Tag als dokumentierten Schritt aufnehmen (D2, optional); Pruefung: `README` beschreibt, wie die eingefrorene Spec-Menge markiert und spaeter als `git diff` gelesen wird

## 9. Ablage der Uebungsangaben (P13)

- [ ] 9.1 Erste Uebungsangabe `htl-leonding-example/jg03-syp-git-basics` nach Namensschema anlegen (public, Startercode, `solution`-Branch per PR); Pruefung: Repo folgt `jg03-syp-<topic-id>` und ist ohne Anmeldung lesbar
- [ ] 9.2 `assignment_template` in `curriculum.yaml` fuer dieses Topic eintragen und den Check um "genanntes Template-Repository existiert" erweitern; Pruefung: falscher Repositoryname laesst den Check rot werden
- [ ] 9.3 Ablageregel fuer Pruefungsangaben dokumentieren (privat in der Jahresorganisation, nach Durchfuehrung oeffentlich als `<jahr>-exam-<thema>`); Pruefung: Regel steht im `README.adoc` neben der Uebungsangaben-Regel

## 10. Abnahme des Changes

- [ ] 10.1 Gesamtlauf: `check-curriculum.py` gruen, Generatoren aktuell, Build veroeffentlicht, `rights-check` mit bekanntem Stand; Pruefung: ein Durchlauf der Pipeline auf `main` ohne manuellen Eingriff
- [ ] 10.2 Verbleibende offene Fragen aus `design.md` nachziehen oder ausdruecklich vertagen (Pflichtfragen fuer Theoriethemen, Zeitpunkt der Hugo-Abloesung); Pruefung: jede offene Frage traegt Entscheidung oder Vertagungsgrund
