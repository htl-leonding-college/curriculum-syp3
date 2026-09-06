# Curriculum-Repository und Publikationsweg aufsetzen

## Why

Die Stoffstruktur ist heute in Prosa kodiert: Im Fragenkatalog stehen die Tags im
Überschriftentext (`=== 1.5. .gitignore Foundation`), die Zuordnung von Themen zu
Jahrgängen existiert nur im Kopf des Lehrenden, und UE-Budgets werden von Hand
fortgeschrieben. Damit lässt sich nichts abfragen, nichts prüfen und nichts ableiten —
ein Umbau der Tags auf Jahrgangs-Voraussetzungen wäre eine Handeditierung von ~84
Überschriften und beim zweiten Mal nicht mehr durchführbar. Der bestehende Katalog
bleibt deshalb unangetastet; die Struktur wird stattdessen von Grund auf als Daten
angelegt.

Gleichzeitig entstehen für `define-syp3-curriculum` neue Lernressourcen auf Englisch, die
einen Ort brauchen: mit prüfbarer Struktur, mit Übungsaufgaben und Lösungen, und mit
einem Publikationsweg, der zu dem passt, was im Unterricht gelehrt wird.

Die naheliegende Antwort „LLM-Wiki" löst das nicht — ein Wiki hätte denselben Defekt
(Struktur in Prosa), zusätzlich eine zweite Wahrheitsquelle und keine Versionierung über
Jahrgänge hinweg.

## What Changes

- **Struktur wird zu Daten.** Eine `curriculum.yaml` ist die einzige Wahrheit für
  Themen, Blöcke, UE-Zahlen, Jahrgangszuordnung und Voraussetzungen. Die AsciiDoc-Dateien
  tragen ausschließlich ihre `:topic-id:` — keine weiteren Strukturangaben, sonst
  entstehen wieder zwei Wahrheiten.
- **Ein CI-Check koppelt beides.** Er prüft Bijektion (jedes Thema hat eine Ressource
  und umgekehrt), UE-Budget gegen die Vorgaben aus `define-syp3-curriculum`,
  Voraussetzungsgraph (existierende IDs, keine Zyklen, keine Vorwärtsreferenzen) und
  Vollständigkeit der Pflichtfelder. Ohne diesen Check wäre die zentrale Strukturdatei
  nur zusätzliche Handarbeit.
- **Generatoren statt Doppelpflege**: PlantUML-Mindmap der Stoffstruktur,
  Website-Navigation und Fragenkatalog-Tags werden aus `curriculum.yaml` erzeugt.
- **Einheitliches Modulformat** je Thema: `index.adoc` (Inhalt), `exercises.adoc`
  (Aufgaben mit `[%collapsible]` Lösungen), `questions.adoc` (mündliche Prüfungsfragen).
- **Lösungen werden mitgeliefert, nicht verborgen.** Der Leistungsnachweis ist die
  mündliche Prüfung über die Aufgabe, nicht die Abgabe. Kein zeitgesteuertes
  Freischalten, keine Sichtbarkeitstrennung, keine getrennten Branches für Lösungen —
  Branches bleiben dem Assignment-Muster in „classroom 50" vorbehalten
  (`main` / `solution`).
- **Ein Repository pro Jahrgang**, Publikation über den bestehenden Stack
  (AsciiDoc → Asciidoctor → GitHub Actions → gh-pages, revealjs für Präsentationen).
  **Antora wird verworfen** — Versionierung ist durch Repos je Jahrgang bereits gedeckt,
  und der eigene Stack soll dem entsprechen, was im Unterricht gelehrt wird. Die
  Entscheidung ist umkehrbar: AsciiDoc-Inhalt ist portabel.
- **Neuer Fragenkatalog statt Umbau des bestehenden.** Der vorhandene Katalog bleibt
  unangetastet, öffentlich und weiterhin von anderen Lehrenden nutzbar; seine URLs
  bleiben stabil. Der neue Katalog wird von Beginn an aus den `questions.adoc` der Module
  generiert — das Zielbild wird damit zum Startzustand, weil keine Altstruktur zu
  bewahren ist. Inhalte des alten Katalogs dürfen frei übernommen werden (eigenes Werk),
  werden dabei aber einem Modul zugeordnet.
- **Klassen-Setup als eigenes Repository `klassen-setup`**, getrennt nach
  `setup-tools.sh` (idempotent, unbeaufsichtigt) und `setup-identity.sh` (interaktiv,
  personenbezogen). Bash mit einer Betriebssystem-Weiche statt zweier Scripts, SDKMAN für
  JDK/Maven/Gradle statt Einzelinstallation mit manuellem `JAVA_HOME`, gepinnte Versionen
  in `versions.env`.
- **Hugo-Site bleibt vorerst unangetastet.** Sie enthält Altdaten früherer Projekte, die
  erhalten bleiben sollen. Die neue Site entsteht parallel; über eine Ablösung wird später
  entschieden.

## Capabilities

### New Capabilities

- `platform/curriculum-model`: Schema und Semantik von `curriculum.yaml`, ID-Vergabe,
  Kopplung zu den Lernressourcen über `:topic-id:`
- `platform/curriculum-validation`: CI-Prüfungen auf Bijektion, UE-Budget,
  Voraussetzungsgraph und Pflichtfelder
- `platform/curriculum-generators`: Ableitung von PlantUML-Mindmap, Navigation und
  Fragenkatalog-Tags aus dem Modell
- `platform/learning-resource-format`: Aufbau eines Moduls, Aufgaben- und Lösungsmodell,
  Prüfungsfragen je Thema
- `platform/publication`: Build-Pipeline nach gh-pages, revealjs-Ausgabe, optionales
  Ausrollen auf den Schulwebspace, Koexistenz mit der bestehenden Hugo-Site
- `platform/question-catalogue`: Aufbau eines aus den Modulen generierten Fragenkatalogs,
  Abgrenzung zum bestehenden Katalog
- `platform/class-setup`: reproduzierbare Lernumgebung über `klassen-setup`, Idempotenz,
  Betriebssystem-Weiche, Versionspinning, Trennung von Toolchain und Identität

### Modified Capabilities

Keine — unter `openspec/specs/` existieren noch keine Capabilities.

## Impact

- **Repository `curriculum-syp3`**: neue Verzeichnisse `modules/`, `tools/`,
  `templates/`, `.github/workflows/`, neue Datei `curriculum.yaml`.
- **Repository `fragenkatalog`** (eigenständig, öffentlich): **keine Änderung.** Es
  bleibt als Bestand erhalten; der neue Katalog entsteht daneben.
- **`define-syp3-curriculum`**: Die UE-Budget-Tabellen in dessen `design.md` werden zur
  maschinell geprüften Vorgabe statt zur Dokumentation, die veraltet.
- **Schulwebspace** (`edufs.edu.htl-leonding.ac.at/~t.stuetz/`): Hugo-Site bleibt
  bestehen; optionales `publish.sh` für die neue Site, um keine Schul-Credentials in
  GitHub-Actions-Secrets ablegen zu müssen.
- **Neues Repository `klassen-setup`** (öffentlich): Setup-Scripts, `versions.env`,
  git-Tag je Schuljahr. Wird vor U1 auf frischem Ubuntu und auf macOS getestet.
- **4./5. Jahrgang**: Modell und Werkzeuge sind wiederverwendbar; die Entscheidung
  „ein Repository pro Jahrgang" ist dort erneut zu treffen.
- **Nicht im Umfang**: Inhaltliche Erstellung der Lernressourcen, Ablösung der
  Hugo-Site, jede Änderung am bestehenden Fragenkatalog, Moodle-Anbindung,
  „classroom 50"-Konfiguration.
