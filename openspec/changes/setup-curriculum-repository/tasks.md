# Tasks: Curriculum-Repository und Publikationsweg aufsetzen

> Werkzeugsprache: **Python** (offene Frage aus `design.md` entschieden am 2026-09-07).
> PyYAML als einzige Fremdabhängigkeit, Ausführung in Actions über `setup-python`.
> `klassen-setup` bleibt Bash (P9).
>
> Während der Umsetzung entschieden (2026-09-07): Themen tragen
> `status: planned | ready` (Default `planned`). Bijektion, Pflichtabschnitte,
> Outcome-Kopplung und Modulskelett greifen nur für `ready`; verwaiste Dateien und
> unbekannte Themen-IDs fallen immer auf. Design P1/P2 und die Specs
> `curriculum-model` und `curriculum-validation` sind nachgezogen.
>
> Stand 2026-09-07: `klassen-setup` und `student-project-template` liegen als
> lokale Repositories neben `curriculum-syp3` (je ein Commit, kein Remote).
> Alles, was GitHub verändert — Repos anlegen, pushen, Pages aktivieren,
> Hinweis im bestehenden Fragenkatalog — steht noch aus und ist bewusst nicht
> ungefragt ausgeführt worden.

## 1. Repository-Gerüst

- [x] 1.1 Verzeichnisse `modules/`, `tools/`, `templates/`, `.github/workflows/` anlegen; Prüfung: `ls` zeigt alle vier, `git status` führt sie (Platzhalterdatei je leerem Verzeichnis)
- [x] 1.2 `README.adoc` mit Zweck, Layout aus P6, Verweis auf `curriculum.yaml` als einzige Strukturwahrheit und auf die Zuständigkeitsregel der beiden Fragenkataloge (P8); Prüfung: Datei rendert mit `local-convert.sh` fehlerfrei
- [x] 1.3 Python-Werkzeugbasis: `tools/requirements.txt` (PyYAML), `tools/README.adoc` mit Aufrufkonventionen; Prüfung: `pip install -r tools/requirements.txt` läuft in frischem venv durch
- [x] 1.4 Gemeinsames Lademodul `tools/curriculum.py` (liest `curriculum.yaml`, leitet Modulpfade aus der ID ab, meldet fehlende Pflichtfelder mit Zeilenangabe); Prüfung: `python -c "import tools.curriculum as c; print(len(c.load().topics))"` gibt 54 aus

## 2. CI-Check `tools/check-curriculum.py` (P2)

- [x] 2.1 Grundgerüst mit Prüfungsregistry, Sammel-Reporting (Datei, Zeile, Ist/Soll) und Exit-Code != 0 bei mindestens einem Fehler; Prüfung: Lauf auf einem manipulierten Fixture endet mit Exit-Code 1 und listet alle Fehler, nicht nur den ersten
- [x] 2.2 Prüfung 1 Bijektion: jedes Topic hat `index.adoc`, jede `.adoc` unter `modules/` trägt eine in der yaml bekannte `:topic-id:`; Prüfung: Fixture mit fehlender Datei und Fixture mit verwaister Datei schlagen je mit dem erwarteten Text fehl
- [x] 2.3 Prüfung 2 Budget: Summe `ue` je `kind` gegen `meta.budget` (26/56) und je Block gegen `meta.budget_je_block`; Prüfung: Fixture mit einem Theorie-Topic zu viel nennt Ist- und Sollwert
- [x] 2.4 Prüfung 3 Graph: `requires` zeigt nur auf existierende IDs, keine Zyklen, keine Vorwärtsreferenz über `lesson` bzw. `taught_in`; Prüfung: Fixtures für unbekannte ID, Zweierzyklus und verschobene Voraussetzung schlagen fehl und nennen beide Topics mit Unterrichtsnummer
- [x] 2.5 Prüfung 4 Vollständigkeit: `taught_in` und `prerequisite_for` je Topic gesetzt, jedes Topic mit `kind: praxis` hat mindestens eine Frage; Prüfung: Praxis-Fixture ohne Frage schlägt fehl, Theorie-Fixture ohne Frage nicht
- [x] 2.6 Prüfung 5 Slot-Belegung: je `lesson` höchstens ein Theorie- und ein Praxis-Topic, keine Lücke zwischen Unterricht 1 und dem letzten belegten; Prüfung: Doppelbelegung und Lücke schlagen je mit Nummernangabe fehl
- [x] 2.7 Prüfung 6 Pflichtabschnitte: `== Learning outcomes`, `== Decisions`, `== Pitfalls`, `== Terminology` vorhanden und nicht leer, ausdrückliche Nullaussage gilt als erfüllt; Prüfung: Fixture ohne `Decisions` schlägt fehl, Fixture mit "None specific to this topic." besteht
- [x] 2.8 Prüfung 7 Outcome-Kopplung: jedes Learning outcome hat >= 1 Frage in `questions.adoc`, jede Frage verweist auf ein existierendes Outcome; Prüfung: beide Richtungen als Fixture rot
- [x] 2.9 Prüfung 8 Bildherkunft: jedes `image::` unter `modules/` trägt genau eine Klasse `own | free | unclear`, `free` verlangt Lizenzname und URL; Prüfung: Bild ohne Klasse und `free` ohne Quelle schlagen mit Datei und Zeile fehl
- [x] 2.10 Prüfung 9 Modulskelett: jedes Modulverzeichnis enthält `index.adoc`, `exercises.adoc`, `questions.adoc`; `exercises.adoc` darf inhaltsleer sein; Prüfung: Modul ohne Aufgabendatei schlägt fehl, Modul mit leerer Aufgabendatei besteht
- [x] 2.11 Zusatzprüfung Strukturattribute: `.adoc` unter `modules/` trägt außer `:topic-id:` kein Attribut mit UE-Zahl, Block, Jahrgang oder Voraussetzung; Prüfung: Fixture mit `:ue: 2` schlägt fehl und nennt Datei und Attribut
- [x] 2.12 Fixture-Testsuite unter `tools/tests/` mit je einem roten und einem grünen Fall pro Prüfung; Prüfung: `python -m pytest tools/tests` grün, jede der neun Prüfungen mindestens einmal abgedeckt
- [x] 2.13 Lauf gegen den echten Stand: `python tools/check-curriculum.py` meldet ausschließlich noch nicht angelegte Module und keinen Strukturfehler; Befund im Continuation-Dokument festhalten

## 3. Generatoren (P3)

- [x] 3.1 `tools/gen-mindmap.py`: `curriculum.yaml` -> `@startmindmap` je Block und Topic; Prüfung: neues Topic im Fixture erscheint nach dem Lauf als Knoten
- [x] 3.2 `tools/gen-nav.py`: Navigation in Unterrichtsreihenfolge, verlinkt `assignment_template` wo gesetzt; Prüfung: geänderte `lesson` ändert die Reihenfolge ohne Handarbeit
- [x] 3.3 `tools/gen-ue-overview.py`: UE-Übersicht je Block und je Art mit Summen; Prüfung: Ausgabe stimmt mit den Budgettabellen aus `define-syp3-curriculum/design.md` überein
- [x] 3.4 `tools/gen-questions.py`: Sammellauf über alle `questions.adoc`, Tags `block`, `taught_in`, `prerequisite_for`, `topic` aus dem Modell; Prüfung: erzeugter Katalog enthält keine Tags aus Überschriftentext
- [x] 3.5 Erzeugte Artefakte nach `build/` schreiben, jede Datei mit Kopfzeile "GENERATED — do not edit"; Prüfung: `build/` ist in `.gitignore` bzw. als generiert gekennzeichnet
- [x] 3.6 Erzeugte Artefakte bleiben unversioniert: Generatoren schreiben ausschließlich nach `build/` (in `.gitignore`) und laufen bei jedem Build vor asciidoctor; Prüfung: `test_repo_layout.py` fällt rot, sobald eine Datei mit GENERATED-Kopf im Versionsstand liegt oder `build/` nicht ignoriert wird — ein `git diff`-Vergleich entfällt damit, weil eine Handänderung an `build/` den nächsten Lauf ohnehin nicht überlebt

## 4. Modulformat und Skelett (P4)

- [x] 4.1 `templates/module/` mit `index.adoc` (feste Abschnittsfolge inkl. Pflichtabschnitte), `exercises.adoc` (Kennzeichnung `drill|project`, Lösung als `[%collapsible]`), `questions.adoc` (Verweis auf Outcome-ID); Prüfung: aus der Vorlage erzeugtes Modul besteht die Prüfungen 6, 7, 9
- [x] 4.2 `tools/new-module.py <topic-id>`: legt Verzeichnis, drei Dateien und `images/` aus Vorlage und yaml-Daten an; Prüfung: Aufruf für ein Topic ohne Modul erzeugt ein Skelett, das `check-curriculum.py` nur wegen fehlender Inhalte, nicht wegen Struktur bemängelt
- [x] 4.3 Modulskelette für `git-basics` und `sdd-openspec-artifacts` (so heißt das Thema im Modell) anlegen (Einführungsplan Schritt 3); Prüfung: beide Module bestehen alle neun Prüfungen mit ausdrücklichen Nullaussagen, wo noch nichts feststeht
- [x] 4.4 Autorenleitfaden `templates/module/README.adoc`: Abschnittszweck, Nullaussage, Aufgabenarten, PlantUML-Default, Bildherkunft, Terminology-Paare; Prüfung: Leitfaden nennt jede der neun CI-Prüfungen mit der Stelle, an der sie greift

## 5. Pipeline und Publikation (P7, P11)

- [x] 5.1 Containerisiertes asciidoctor-Image um `asciidoctor-diagram` und Graphviz ergänzen, `local-convert.sh` übernehmen und anpassen; Prüfung: ein Modul mit PlantUML-Block rendert lokal ohne lokale Ruby-Installation
- [x] 5.2 Workflow `build`: `check-curriculum.py` -> Generatoren -> asciidoctor -> Deploy auf `gh-pages`; Prüfung: Push auf `main` veröffentlicht, roter Check verhindert das Deploy und die Site bleibt auf dem letzten gültigen Stand
- [x] 5.3 Eigener Job `rights-check`: fällt rot bei `unclear > 0`, listet Datei und Zeile, blockiert das Deploy nicht; Prüfung: Modul mit `unclear`-Bild wird veröffentlicht und der Job meldet es rot
- [x] 5.4 revealjs-Ausgabe aus derselben Quelle erzeugen; Prüfung: Änderung an einem Modultext erscheint ohne zweite Bearbeitung in der Präsentationsansicht
- [ ] 5.5 `publish.sh` für rsync auf den Schulwebspace, lokal ausführbar, keine Zugangsdaten in Actions-Secrets; Prüfung: Lauf legt die Site parallel zur bestehenden Hugo-Site ab, ein Altlink bleibt erreichbar
- [x] 5.6 GitHub Pages für `htl-leonding-college/curriculum-syp3` aktivieren und Einstiegsseite verlinken (Altsite, bestehender Fragenkatalog); Prüfung: öffentliche URL liefert die Site ohne Anmeldung

## 6. Fragenkatalog (P8)

- [x] 6.1 Katalogseite aus `gen-questions.py` veröffentlichen, sortier- und filterbar nach Block, unterrichtendem Jahrgang, voraussetzendem Jahrgang und Thema; Prüfung: Abfrage "alle Fragen mit `prerequisite_for: jg4`" liefert die erwartete Menge
- [ ] 6.2 Übernahme geeigneter Fragen aus dem bestehenden Katalog, je Frage genau ein Modul; Prüfung: nicht zugeordnete Fragen erscheinen nicht im erzeugten Katalog und fallen bei Prüfung 7 auf
- [ ] 6.3 Zuständigkeitshinweis auf beiden Einstiegsseiten (neuer Katalog maßgeblich für SYP 3. Jg ab 2026/27, bestehender bleibt Archiv); Prüfung: bestehende URLs und Anker des alten Katalogs sind unverändert erreichbar

## 7. Repository `klassen-setup` (P9)

- [ ] 7.1 Repository `htl-leonding-college/klassen-setup` public anlegen mit `README.adoc`; Prüfung: `git clone` ohne Anmeldung möglich
- [x] 7.2 `setup-tools.sh` mit OS-Weiche (`apt`/`brew`), einer Werkzeugliste, Idempotenzprüfung je Schritt; Werkzeuge: JetBrains Toolbox, SDKMAN (JDK/Maven/Gradle), Docker, kubectl, minikube, zsh + powerlevel10k; Prüfung: zweiter Lauf auf eingerichtetem Gerät ändert nichts und meldet den Zustand als hergestellt
- [ ] 7.3 `versions.env` mit gepinnten Versionen; JDK-Version nach Abstimmung mit 4./5. Jahrgang eintragen (offene Frage aus `design.md`); Prüfung: Änderung einer Version wirkt sich ohne weitere Stelle im Script aus
- [x] 7.4 `setup-identity.sh` interaktiv und einmalig (git user.name/user.email, SSH-Key, `gh auth`), keine Zugangsdaten im Repository; Prüfung: Lauf von `setup-tools.sh` danach lässt Name, Schlüssel und Anmeldungen unangetastet
- [x] 7.5 Bootstrap-Anleitung ohne `curl … | bash`: herunterladen, lesen, ausführen; Prüfung: `README.adoc` führt den Weg mit lesbarem Zwischenschritt und begründet ihn
- [ ] 7.6 Vollständiger Durchlauf auf frisch installiertem Ubuntu 26.04 LTS und auf macOS vor U1 (Einführungsplan 5a); Prüfung: beide Läufe protokolliert, Abbruch mitten im Lauf und Fortsetzung einmal bewusst getestet
- [ ] 7.7 git-Tag für das Schuljahr 2026/27 setzen; Prüfung: Tag zeigt auf den erprobten Stand aus 7.6

## 8. Vorlage für Schülerprojekte (P6, P13)

- [x] 8.1 (lokal angelegt, Remote steht aus) `htl-leonding-college/student-project-template`: openspec-Scaffold, `docs/` als AsciiDoc, CI nach Muster 5.2; Prüfung: aus der Vorlage erzeugtes Repo baut beim ersten Push eine Pages-Site
- [x] 8.2 Governance-Vorlagen aus `define-syp3-curriculum` (Projektantrag, Projektauftrag, Meilensteinplan, Abnahme) mit zweisprachigen Feldbezeichnern einbinden; Prüfung: Vorlage enthält die Feldstruktur des DA-Antrags in beiden Sprachen
- [x] 8.3 `baseline-v1`-Tag als dokumentierten Schritt aufnehmen (D2, optional); Prüfung: `README` beschreibt, wie die eingefrorene Spec-Menge markiert und später als `git diff` gelesen wird

## 9. Ablage der Übungsangaben (P13)

- [ ] 9.1 Erste Übungsangabe `htl-leonding-example/jg03-syp-git-basics` nach Namensschema anlegen (public, Startercode, `solution`-Branch per PR); Prüfung: Repo folgt `jg03-syp-<topic-id>` und ist ohne Anmeldung lesbar
- [ ] 9.2 `assignment_template` in `curriculum.yaml` für dieses Topic eintragen und den Check um "genanntes Template-Repository existiert" erweitern; Prüfung: falscher Repositoryname lässt den Check rot werden
- [x] 9.3 Ablageregel für Prüfungsangaben dokumentieren (privat in der Jahresorganisation, nach Durchführung öffentlich als `<jahr>-exam-<thema>`); Prüfung: Regel steht im `README.adoc` neben der Übungsangaben-Regel

## 10. Abnahme des Changes

- [x] 10.1 Gesamtlauf: `check-curriculum.py` grün, Generatoren aktuell, Build veröffentlicht, `rights-check` mit bekanntem Stand; Prüfung: ein Durchlauf der Pipeline auf `main` ohne manuellen Eingriff
- [x] 10.2 Verbleibende offene Fragen aus `design.md` nachziehen oder ausdrücklich vertagen (Pflichtfragen für Theoriethemen, Zeitpunkt der Hugo-Ablösung); Prüfung: jede offene Frage trägt Entscheidung oder Vertagungsgrund
