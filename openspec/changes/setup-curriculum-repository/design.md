# Design: Curriculum-Repository und Publikationsweg

## Context

Motivation siehe `proposal.md` — Why. Inhaltliche Vorgaben (UE-Budget, Blöcke, Sequenz)
stammen aus `../define-syp3-curriculum/design.md`.

Ausgangslage:

- **Der Zielstack läuft bereits.** Der Fragenkatalog
  (`htl-leonding-college.github.io/fragenkatalog`, im Besitz des Lehrenden, öffentlich
  zur Mitbenutzung) fährt AsciiDoc → Asciidoctor → GitHub Actions → gh-pages inklusive
  revealjs, mit `config.sh`, `local-convert.sh` und `publish.sh`. Das ist exakt die
  Pipeline, die im Unterricht (U6/U7) gelehrt werden soll.
- **Tags stecken im Überschriftentext** (`=== 1.5. .gitignore Foundation`,
  `=== 8.1. What is Quarkus? (Advanced)`) und sind damit nicht abfragbar.
- **Der Katalog ist technologieorientiert gewachsen** (Git 19, Docker/Compose 22,
  Kubernetes 6, Shell/Netzwerke 12, Asciidoctor 14, UML 5, Java 1, Quarkus 2,
  Agentic Programming 1, GitHub Classroom 2). Die gesamte Theorieseite des neuen
  Curriculums — Governance, Vorgehensmodelle, SDD — hat **null** Fragen.
- **Publikation ist zweigleisig**: Hugo-Site auf dem Schulwebspace für Lernressourcen,
  AsciiDoc auf GitHub Pages für Mitschriften.
- **Versionierung erfolgt heute über Repositories je Jahr und Klasse**
  (`2526-3bhif-syp-lecture-notes`).
- **Bewertungsmodell**: Übungsaufgaben werden zu Hause gelöst, der Nachweis erfolgt über
  mündliche Prüfungen. Lösungen zu verbergen ist sinnlos, da Agenten sie ohnehin erzeugen.

## Goals / Non-Goals

**Goals:**

- Die Stoffstruktur so ablegen, dass sie abfragbar, prüfbar und ableitbar ist
- Doppelpflege zwischen Struktur, Navigation, Mindmap und Fragenkatalog beseitigen
- Ein Modulformat, in dem Inhalt, Aufgabe, Lösung und Prüfungsfrage zusammenliegen
- Den vorhandenen, im Unterricht gelehrten Publikationsstack beibehalten
- Altbestand (Hugo) unangetastet lassen

**Non-Goals:**

- Kein neues Content-Management-System, kein Wiki, keine Datenbank
- Keine Sichtbarkeitstrennung zwischen Aufgaben und Lösungen
- Keine Ablösung der Hugo-Site in diesem Change
- Keine inhaltliche Erstellung der Lernressourcen

## Decisions

### P1 — Struktur als Daten, Inhalt als AsciiDoc, gekoppelt über IDs

`curriculum.yaml` ist die einzige Wahrheit für Struktur. Die Lernressource trägt genau
ein Attribut: ihre `:topic-id:`.

```yaml
# curriculum.yaml
meta:
  jahrgang: jg3
  gegenstand: SYP
  unterrichte: 30
  ue_je_unterricht: 3
  budget:
    theorie: 25
    praxis: 50

topics:
  - id: sdd-openspec
    title: Spec-Driven Development with openspec
    block: vorgehen           # governance | vorgehen | modellierung | werkzeuge
    kind: theorie             # theorie | praxis
    ue: 5
    lesson: 8                 # Nummer des Unterrichts
    taught_in: jg3
    prerequisite_for: jg4     # ersetzt Foundation / Advanced
    requires: [git-basics, ai-basics]
    resources:
      - modules/sdd-openspec/index.adoc
    questions:
      - modules/sdd-openspec/questions.adoc
```

```adoc
// modules/sdd-openspec/index.adoc
= Spec-Driven Development with openspec
:topic-id: sdd-openspec

...Inhalt...
```

*Begründung:* Reine Attribute in den `.adoc` (Variante 1) erlauben keine Planung von
Themen, für die noch keine Ressource existiert, und keine Gesamtsicht ohne Scan. Eine
reine `curriculum.yaml` (Variante 2) driftet gegen den Inhalt. Die Kopplung über IDs plus
CI-Check verbindet beide Vorteile und macht Drift zum Build-Fehler.

*Regel, an der die Entscheidung hängt:* Strukturdaten stehen **ausschließlich** in
`curriculum.yaml`. Sobald UE-Zahlen oder Tags zusätzlich im AsciiDoc auftauchen, sind
zwei Wahrheiten zurück.

### P2 — Der CI-Check ist der Vertrag

Ohne ihn ist P1 nur eine zusätzliche Datei. Geprüft wird:

```
1  BIJEKTION
     jedes topic hat >= 1 resource, und die Datei existiert
     jede .adoc unter modules/ hat eine topic-id, die in der yaml steht

2  BUDGET
     Summe ue je kind      gegen meta.budget (25 Theorie / 50 Praxis)
     Summe ue je block     gegen die Tabelle in
                           define-syp3-curriculum/design.md

3  GRAPH
     requires zeigt nur auf existierende ids
     keine Zyklen
     keine Vorwaertsreferenz: jede Voraussetzung liegt in einem
     frueheren lesson bzw. einem frueheren taught_in

4  VOLLSTAENDIGKEIT
     jedes topic hat taught_in und prerequisite_for
     jedes topic mit kind: praxis hat >= 1 question
```

*Wirkung von Prüfung 3:* Wird ein Thema verschoben und rutscht dadurch eine Voraussetzung
nach hinten, schlägt der Build an — nicht der Unterricht im März.

*Wirkung von Prüfung 2:* Die Budget-Tabellen aus `define-syp3-curriculum` werden zur
maschinell geprüften Vorgabe statt zur Dokumentation, die veraltet.

### P3 — Generatoren statt Doppelpflege

```
curriculum.yaml
   |
   +--> PlantUML-Mindmap der Stoffstruktur   (@startmindmap)
   +--> Navigation der Website
   +--> Fragenkatalog-Tags
   +--> UE-Uebersicht je Block
```

Alle Ausgaben sind generierte Artefakte und werden nicht von Hand bearbeitet.

### P4 — Modulformat: Inhalt, Aufgabe, Lösung und Prüfungsfrage liegen zusammen

```
modules/<topic-id>/
  index.adoc        Lerninhalt          (:topic-id:)
  exercises.adoc    Aufgaben + Loesungen als [%collapsible]
  questions.adoc    muendliche Pruefungsfragen
```

*Begründung:* Wenn die Lösung ohnehin verfügbar ist — mitgeliefert oder vom Agenten
erzeugt —, ist die Übungsaufgabe kein Leistungsnachweis mehr, sondern ein Lernanlass.
Der Nachweis ist die mündliche Prüfung. Damit der Wert im Durcharbeiten entsteht und
nicht im Abliefern, wird **jede Aufgabe mit ihren Prüfungsfragen ausgeliefert**.

*Nebeneffekt:* Diese Prüfungsfragen sind das Rohmaterial für den Fragenkatalog. Er wächst
aus den Modulen, statt separat gepflegt zu werden — auch für die Theorieseite, die heute
keine Fragen hat.

```
Uebungsaufgabe --> Loesung --> Pruefungsfragen --> Fragenkatalog
      |                              |
      +------ ein Modul, eine topic-id ------+
```

### P5 — Kein Freischalten, keine Lösungs-Branches in Lernressourcen

`[%collapsible]` — dasselbe Muster, das der Fragenkatalog bereits verwendet.

*Alternative:* zeitgesteuertes Freischalten wie in „classroom 50". Verworfen — das ist
Verbergen, und Verbergen ist bei Agentenverfügbarkeit wirkungslos. Was legitim bleibt,
ist ein didaktischer Anreiz („erst selbst versuchen"); dafür ist ein Klick die passende
Hürde, ohne Build-Komplexität.

*Alternative:* zwei Branches `instructions` / `solutions`. Verworfen für Lernressourcen —
die Zweige driften (jede Korrektur zweimal), beim Schreiben sieht man nie beides
nebeneinander, und ein Merge leakt die Lösung. **Im Assignment-Repo ist das Muster
richtig** (`main` = Starter, `solution` = Musterlösung per PR nachgereicht), weil das
Repository dem Schüler gehört.

### P6 — Ein Repository pro Jahrgang, bestehender Stack, kein Antora

```
curriculum-syp3/                    (public)
  curriculum.yaml
  modules/<topic-id>/               index.adoc, exercises.adoc, questions.adoc
  templates/student-project/        Vorlage: openspec, adoc, CI
  tools/
    check-curriculum.*              CI-Pruefungen aus P2
    gen-mindmap.*                   curriculum.yaml -> PlantUML
    gen-nav.*                       curriculum.yaml -> Navigation
  openspec/                         Planung
  continuations/
  .github/workflows/                adoc -> HTML -> gh-pages
  publish.sh                        optional: rsync auf Schulwebspace
```

Wiederholung im 4./5. Jg über Links auf die 3.-Jg-Site — kein Kopieren, keine Drift.

*Alternative:* **Antora**. Verworfen, mit drei Gründen:

1. Antoras Kernfeature ist „eine Site, mehrere Versionen". Dieser Bedarf ist durch
   Repositories je Jahrgang bereits gedeckt und funktioniert seit Jahren.
2. Der eigene Stack würde von dem abweichen, was unterrichtet wird. Der Fragenkatalog ist
   heute das Vorzeigesystem für genau die Pipeline aus U6/U7; diesen Gleichlauf für eine
   komfortablere Navigation aufzugeben, wäre ein schlechter Tausch.
3. Antora bringt konkrete Reibung: Content wird aus git-Refs gelesen, nicht aus dem
   Arbeitsverzeichnis (Änderungen erscheinen erst nach dem Commit); die
   Verzeichnisstruktur ist vorgeschrieben (`modules/ROOT/pages/`, `nav.adoc`,
   `antora.yml`) und passt nicht zum Layout oben; PlantUML läuft nur über eine Extension.

*Umkehrbarkeit:* Der Inhalt ist AsciiDoc. Eine spätere Migration verschiebt Verzeichnisse
und ergänzt ein Playbook, schreibt aber kein Dokument neu. Antora bleibt Zielbild für den
Fall, dass 3./4./5. Jahrgang zu einer Site verschmelzen sollen.

### P7 — Publikation: gh-pages primär, Schulwebspace optional, Hugo koexistiert

```
   curriculum-syp3 (GitHub)
        |
        +-- GitHub Actions --> gh-pages          (primaer, automatisch)
        |
        +-- publish.sh (lokal) --> Schulwebspace (optional, manuell)

   Hugo-Site auf dem Schulwebspace: bleibt unveraendert bestehen
```

*Begründung für `publish.sh` statt CI-Deployment auf den Schulserver:* SSH-Zugangsdaten
für fremde Infrastruktur in GitHub-Actions-Secrets abzulegen, ist technisch trivial, aber
organisatorisch fragwürdig. Das Muster existiert im Fragenkatalog bereits.

*Hugo:* Die Site enthält Altdaten früherer Projekte, die erhalten bleiben sollen. Die neue
Site entsteht parallel; eine Ablösung wird separat entschieden, wenn Inhalt vorliegt.

### P8 — Neuer Fragenkatalog, bestehender bleibt unangetastet

Der vorhandene Katalog (`htl-leonding-college.github.io/fragenkatalog`) wird **nicht**
migriert. Er bleibt öffentlich, unverändert und weiterhin von anderen Lehrenden nutzbar;
seine URLs und Anker bleiben stabil.

Der neue Katalog wird von Beginn an aus den `questions.adoc` der Module generiert:

```
modules/<topic-id>/questions.adoc
        |
        |  Sammellauf ueber curriculum.yaml
        v
   Fragenkatalog (generiert)
        sortierbar nach Block, Jahrgang, Voraussetzung, Technologie
        weil taught_in / prerequisite_for / block Daten sind
```

*Begründung:* Ohne Altstruktur, die bewahrt werden muss, entfällt der Zwischenschritt
über eine Attributmigration. Das Zielbild aus der vorherigen Fassung dieses Dokuments —
Generierung aus den Modulen — wird damit unmittelbar zum Startzustand. Der bisherige
Defekt (Tags stecken im Überschriftentext und sind nicht abfragbar) kann so gar nicht
erst entstehen: Die Tags stehen in `curriculum.yaml`, nicht im Fließtext.

*Wiederverwendung:* Die Inhalte des alten Katalogs sind eigenes Werk und dürfen
übernommen werden. Beim Übernehmen wird jede Frage einem Modul zugeordnet — das ist der
Arbeitsschritt, der aus einer Sammlung eine Struktur macht.

*Abgrenzung, die festgelegt werden muss:* Solange beide Kataloge existieren, überschneiden
sie sich inhaltlich (Git, Docker, Kubernetes, Shell, Asciidoctor, UML). Regel: Der neue
Katalog ist ab dem Schuljahr 2026/27 für SYP 3. Jahrgang maßgeblich; der bestehende bleibt
für die übrigen Themen und Gegenstände sowie als Archiv erhalten.

*Befund, der Aufwand erzeugt:* Die Theorieseite des Curriculums (Governance,
Vorgehensmodelle, SDD) hat im bestehenden Katalog null Fragen. Dieser Teil ist
Neuautorenschaft und entsteht ohnehin modulweise mit den Lernressourcen (P4).

### P9 — Klassen-Setup als eigenes Repository `klassen-setup`

Bash, nicht Ansible oder Nix: Ansible bringt eine Abhängigkeit ohne Gegenwert, Nix wäre für
einen 3. Jahrgang ein eigenes Projekt. Bash ist zugleich Lernstoff — Shell steht als
Voraussetzung im Curriculum, und `define-syp3-curriculum` (D7) nutzt das Script später als
Brücke zum Dockerfile.

```
klassen-setup/                       (eigenes Repo, public)
  setup-tools.sh      idempotent, unbeaufsichtigt, beliebig oft wiederholbar
                      JetBrains Toolbox, SDKMAN (JDK/Maven/Gradle),
                      Docker, kubectl, minikube, zsh + powerlevel10k
  setup-identity.sh   interaktiv, einmalig
                      git config user.name/user.email, SSH-Key, gh auth
  versions.env        gepinnte Werkzeugversionen
  README.adoc
```

**Idempotenz ist Pflicht, nicht Kür.** Der Lauf dauert realistisch 15+ Minuten über ein
Dutzend Fehlerquellen (Netz, apt-Lock, abgebrochener Download) und wird abbrechen. Jeder
Schritt prüft zuerst, ob das Werkzeug bereits vorhanden ist. Derselbe Begriff begegnet den
Schülern später bei Docker und Kubernetes wieder.

**Eine OS-Weiche, kein zweites Script.**

```bash
case "$(uname -s)" in
  Linux)  PKG=apt  ;;
  Darwin) PKG=brew ;;
esac
```

Die Werkzeugliste steht damit einmal da; nur das Installationsverb unterscheidet sich.
Getrennte Scripts je Betriebssystem driften.

**SDKMAN für den Java-Stack** statt Einzelinstallation:

| | Einzelinstallation | SDKMAN |
|---|---|---|
| JDK | apt/brew, `JAVA_HOME` von Hand | `sdk install java` |
| Maven | separates Paket | `sdk install maven <version>` |
| Gradle | separates Paket | `sdk install gradle` |
| `JAVA_HOME` | manuelle Umgebungsvariable | wird gesetzt |

Ein Mechanismus, identisch auf Ubuntu und macOS, Versionen pinbar, mehrere JDKs parallel.
Das manuell gesetzte `JAVA_HOME` — die häufigste Fehlerquelle der bisherigen Anleitung —
entfällt.

`asciidoctor` wird nicht lokal installiert: Es läuft containerisiert, wie im bestehenden
Fragenkatalog (`local-convert.sh`). Docker genügt.

**Trennung Toolchain / Identität.** `setup-tools.sh` ist reproduzierbar und
wiederholbar, `setup-identity.sh` ist personenbezogen und interaktiv. Vermischt entsteht
ein Script, das man nicht wiederholen kann. Keine Zugangsdaten im Repository.

*Alternative:* Ablage in `curriculum-syp3/tools/`. Verworfen — das Setup ist das Erste,
was die Schüler nach der Installation anfassen, also ihr erster echter `git clone`, und es
ist über Jahrgänge, Klassen und Kollegen hinweg wiederverwendbar.

*Bootstrap:* Auf frischem Ubuntu ist `git` nicht immer vorhanden. Bewusst **nicht**
`curl … | bash`, sondern herunterladen, lesen, ausführen — ein fremdes Script ungelesen mit
erhöhten Rechten laufen zu lassen, ist genau die Gewohnheit, die Informatikschülern nicht
antrainiert werden soll. Der Umweg ist der Lehrinhalt.

*Versionierung:* `versions.env` pinnt die Werkzeugversionen; je Schuljahr ein git-Tag.

## Risks / Trade-offs

| Risiko | Mitigation |
|---|---|
| `curriculum.yaml` und Inhalt driften auseinander | CI-Check P2 als Pflichtschritt in der Pipeline; ein roter Build blockiert die Veröffentlichung |
| Strukturangaben schleichen sich zusätzlich ins AsciiDoc ein | Prüfung: `.adoc` unter `modules/` darf außer `:topic-id:` keine Strukturattribute tragen |
| Die zentrale yaml wird zum Flaschenhals bei häufigen Änderungen | Sie enthält nur Struktur, nicht Inhalt; Änderungen sind selten und haben bewusst Fernwirkung |
| Werkzeuge in `tools/` verrotten, weil sie nur einmal gebraucht werden | Sie laufen bei jedem Push mit; ein defekter Generator fällt sofort auf |
| Zwei Fragenkataloge mit überlappendem Inhalt verwirren Schüler und Kollegen | Festgelegte Zuständigkeit (P8): neuer Katalog maßgeblich für SYP 3. Jg ab 2026/27, bestehender bleibt Archiv und Quelle für andere Gegenstände; Hinweis auf beiden Einstiegsseiten |
| Theorieseite bleibt ohne Fragen, weil Neuautorenschaft aufwendig ist | CI-Prüfung 4 verlangt Fragen je Praxisthema; für Theoriethemen bewusst zunächst optional |
| Zwei Sites (Hugo + Pages) verwirren Schüler | Übergangszeit begrenzen; Einstiegsseite verlinkt beide, bis über die Ablösung entschieden ist |
| Kein Freischalten → Schüler kopieren Lösungen | Bewusst akzeptiert: Nachweis ist die mündliche Prüfung, Prüfungsfragen werden mitgeliefert (P4) |
| `setup-tools.sh` bricht mitten im Lauf ab und blockiert den Praxisunterricht | Idempotenz als Pflichtanforderung (P9); zweiter Lauf setzt fort; 30 min Troubleshooting-Puffer in U2 |
| Gepinnte Werkzeugversionen veralten unbemerkt | `versions.env` an einer Stelle; jährlicher Durchgang vor Schulbeginn, git-Tag je Schuljahr |

## Einführungsplan

1. `curriculum.yaml` mit den Themen aus `define-syp3-curriculum/design.md` befüllen
   (Blöcke, UE, Sequenz U1–U10 sind dort bereits festgelegt)
2. `tools/check-curriculum.*` schreiben und in die Actions-Pipeline hängen — vor den
   ersten Lernressourcen, damit der Vertrag von Beginn an greift
3. Modulgerüst für die ersten Themen anlegen (`git-basics`, `sdd-openspec`)
4. Generatoren ergänzen (Mindmap, Navigation)
5. `templates/student-project/` aufbauen: openspec-Scaffold, AsciiDoc-Grundgerüst, CI
5a. Repository `klassen-setup` anlegen und vor U1 auf einer frischen Ubuntu-Installation
    sowie auf macOS durchtesten
6. Neuen Fragenkatalog aufbauen: Generatorlauf über die `questions.adoc`, Übernahme
   geeigneter Fragen aus dem bestehenden Katalog mit Modulzuordnung
7. Lernressourcen inhaltlich erstellen — eigener Change

## Open Questions

- Sprache der Werkzeuge in `tools/` (Python, Node oder Shell). Beeinflusst weder Modell
  noch Layout; entscheidbar bei der Umsetzung. Betrifft nicht `klassen-setup`, das
  bewusst Bash ist (P9).
- Welche JDK-Version gepinnt wird — abhängig davon, was die übrigen Gegenstände im
  4./5. Jahrgang verwenden.
- Ob `templates/student-project/` im selben Repository liegt oder ein eigenes
  Template-Repository wird — Letzteres wäre für „classroom 50" bequemer.
- Ob Theoriethemen ebenfalls Pflichtfragen bekommen (CI-Prüfung 4 ausweiten), sobald die
  Theorieseite des neuen Katalogs existiert.
- Ob der neue Katalog als eigener Bereich der Curriculum-Site publiziert wird oder als
  eigenes Repository mit eigener Adresse.
- Zeitpunkt und Umfang der Hugo-Ablösung.
