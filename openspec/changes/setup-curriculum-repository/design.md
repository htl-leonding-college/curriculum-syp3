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
  - id: sdd-why-specs
    title: Why specifications instead of a requirements document
    block: vorgehen           # governance | vorgehen | modellierung | werkzeuge
    theme: Spec-driven development   # optional, Strang innerhalb des Blocks
    kind: theorie             # theorie | praxis
    ue: 1                     # 1 UE Theorie bzw. 2 UE Praxis = ein Unterricht
    lesson: 8                 # Nummer des Unterrichts
    taught_in: jg3
    prerequisite_for: jg4     # ersetzt Foundation / Advanced
    requires: [git-basics, ai-prompting]
    status: ready             # planned (Default) | ready
    assignment_template: htl-leonding-example/jg03-syp-sdd-why-specs   # optional
```

```adoc
// modules/sdd-why-specs/index.adoc
= Why specifications instead of a requirements document
:topic-id: sdd-why-specs

...Inhalt...
```

**Dateipfade werden abgeleitet, nicht eingetragen.** Aus der ID folgt:

```
modules/<id>/index.adoc        Lerninhalt
modules/<id>/exercises.adoc    Aufgaben
modules/<id>/questions.adoc    Prüfungsfragen
modules/<id>/images/           Bilder des Moduls
```

Eine Pfadliste in der yaml wäre eine zweite Wahrheit über etwas, das die Konvention
bereits festlegt — und bei rund 50 Themen eine Fehlerquelle ohne Gegenwert. Prüft der
CI-Check die Bijektion (P2, Prüfung 1), rechnet er die Pfade aus der ID aus.

`status` unterscheidet geplante von fertigen Themen. Default ist `planned`: Das Thema
ist im Modell vorhanden, erscheint in Jahresplanung, Mindmap und UE-Übersicht als offen
und wird noch nicht gegen eine Lernressource geprüft. Erst `ready` macht das Modul zum
Vertragsgegenstand — dann greifen Bijektion, Pflichtabschnitte, Outcome-Kopplung und
Modulskelett hart. Ohne diese Unterscheidung stünden die beiden Anforderungen des
Modells gegeneinander: Themen sollen planbar sein, bevor ihre Ressource existiert, und
zugleich soll jedes Thema eine Ressource haben. Der Bruch träfe genau den Anfangszustand
— 54 geplante Themen, kein Modul — und hätte die Veröffentlichung blockiert, bis alle
Module geschrieben sind.

*Regel, an der die Entscheidung hängt:* `ready` wird gesetzt, wenn das Modul fertig ist,
nicht wenn es angelegt wird. Ein Modulverzeichnis zu einem `planned`-Thema ist erlaubt
und wird als Entwurf behandelt; verwaiste Dateien und unbekannte Themen-IDs fallen
weiterhin hart auf.

`assignment_template` ist optional und trägt die Zuordnung eines Moduls zu seiner
Übungsangabe (P13). Nur dadurch kann die generierte Navigation die Angabe verlinken und
der Check prüfen, ob das Repository existiert; ohne das Feld liegt die Zuordnung wieder
nur im Kopf.

*Begründung:* Reine Attribute in den `.adoc` (Variante 1) erlauben keine Planung von
Themen, für die noch keine Ressource existiert, und keine Gesamtsicht ohne Scan. Eine
reine `curriculum.yaml` (Variante 2) driftet gegen den Inhalt. Die Kopplung über IDs plus
CI-Check verbindet beide Vorteile und macht Drift zum Build-Fehler.

*Regel, an der die Entscheidung hängt:* Strukturdaten stehen **ausschließlich** in
`curriculum.yaml`. Sobald UE-Zahlen oder Tags zusätzlich im AsciiDoc auftauchen, sind
zwei Wahrheiten zurück.

**Granularität: ein Topic ist ein Unterricht.**

Ein Topic umfasst genau das, was in einem Slot behandelt wird — 1 UE Theorie oder 2 UE
Praxis. Für den Jahresrahmen aus `define-syp3-curriculum` (30 Unterrichte, 25 UE Theorie /
50 UE Praxis) ergibt das rund 48 Topics.

```
GROB (Blockebene, ~13 Topics)        FEIN (ein Unterricht, ~48 Topics)

  git-toolchain    ue: 14              git-basics        ue: 2  lesson: 2
  governance       ue:  8              git-branching     ue: 2  lesson: 3
  ai               ue: 15              git-pullrequests  ue: 2  lesson: 4
  ...                                  git-conflicts     ue: 2  lesson: 5
                                       asciidoctor       ue: 2  lesson: 6
                                       gh-actions-pages  ue: 2  lesson: 7
                                       ...

  index.adoc: 10-20 Seiten             index.adoc: 1-2 Seiten
```

*Begründung:* Der Detaillierungsgrad einer Lernressource muss dann nicht als Konvention
festgelegt werden („höchstens N Seiten") — er folgt aus dem Zuschnitt. Ein `index.adoc`
enthält, was in seinem Slot vorgetragen wird, und ist fertig, wenn der Slot voll ist.
Konventionen dieser Art werden erfahrungsgemäß nicht eingehalten; eine Struktur, aus der
sich der Umfang ergibt, braucht keine Disziplin.

*Zweitwirkung:* Grobe Topics machen `requires:` trivial („git-toolchain vor allem
anderen"), die Vorwärtsreferenzprüfung wirkungslos und die Fragenkatalog-Zuordnung
ungenau. Erst feine IDs erzeugen eine echte Voraussetzungskette
(`asciidoctor` vor `gh-actions-pages`).

*Preis:* rund 48 Verzeichnisse statt rund 13. Die Textmenge ist dieselbe, nur anders
geschnitten; die Verzeichnismenge tragen die Generatoren aus P3, nicht der Autor.

*Folge:* `lesson:` zusammen mit `kind:` adressiert einen konkreten Slot. Damit wird der
Jahresplan selbst maschinell prüfbar, nicht nur das UE-Budget (P2, Prüfung 5).

### P2 — Der CI-Check ist der Vertrag

Ohne ihn ist P1 nur eine zusätzliche Datei. Geprüft wird:

```
1  BIJEKTION
     jedes topic mit status: ready hat >= 1 resource, und die Datei
     existiert
     jede .adoc unter modules/ hat eine topic-id, die in der yaml steht
     (auch für status: planned — verwaiste Dateien fallen immer auf)

2  BUDGET
     Summe ue je kind      gegen meta.budget (25 Theorie / 50 Praxis)
     Summe ue je block     gegen die Tabelle in
                           define-syp3-curriculum/design.md

3  GRAPH
     requires zeigt nur auf existierende ids
     keine Zyklen
     keine Vorwärtsreferenz: jede Voraussetzung liegt in einem
     früheren lesson bzw. einem früheren taught_in

4  VOLLSTÄNDIGKEIT
     jedes topic hat taught_in und prerequisite_for
     jedes topic mit kind: praxis und status: ready hat >= 1 question

5  SLOT-BELEGUNG
     je lesson höchstens 1 topic mit kind: theorie
     je lesson höchstens 1 topic mit kind: praxis
     keine Lücke zwischen lesson 1 und der letzten belegten

6  PFLICHTABSCHNITTE   (nur status: ready)
     index.adoc enthält  == Learning outcomes
                          == Decisions
                          == Pitfalls
                          == Terminology
     jeder Abschnitt ist nicht leer; eine ausdrückliche Nullaussage
     ("None specific to this topic.") gilt als erfüllt

7  OUTCOME-KOPPLUNG
     jedes Learning outcome hat >= 1 Frage in questions.adoc
     jede Frage verweist auf ein existierendes Outcome

8  BILDHERKUNFT
     jedes image:: unter modules/ trägt eine Herkunftsklasse
       own | free | unclear
     free verlangt Lizenzname und URL
     Klasse unclear läuft in den Job rights-check (P11)

9  MODULSKELETT      (nur status: ready)
     jedes Modulverzeichnis enthält index.adoc, exercises.adoc
     und questions.adoc
     exercises.adoc darf inhaltsleer sein
```

*Wirkung von Prüfung 3:* Wird ein Thema verschoben und rutscht dadurch eine Voraussetzung
nach hinten, schlägt der Build an — nicht der Unterricht im März.

*Wirkung von Prüfung 2:* Die Budget-Tabellen aus `define-syp3-curriculum` werden zur
maschinell geprüften Vorgabe statt zur Dokumentation, die veraltet.

*Wirkung von Prüfung 5:* Der Jahresplan ist nicht mehr nur eine Summe, sondern eine
Belegung. Ein Thema ohne Slot oder zwei Theoriethemen im selben Unterricht fallen beim
Build auf, nicht im Unterrichtsjahr.

*Wirkung von Prüfung 7:* Sie macht aus P4 („Prüfungsfragen werden mitgeliefert") einen
Vertrag statt einer Absicht. Die Schüler sehen vorab, woran gemessen wird, und ein neu
formuliertes Lernziel ohne zugehörige Frage blockiert den Build.

*Nicht geprüft wird* der Inhalt der Aufgaben: weder `.Solution` noch ein Kriterienblock
sind Pflicht (P4). Der Vertrag betrifft Struktur und Herkunft, nicht Vollständigkeit der
Didaktik.

### P3 — Generatoren statt Doppelpflege

```
curriculum.yaml
   |
   +--> PlantUML-Mindmap der Stoffstruktur   (@startmindmap)
   +--> Navigation der Website
   +--> Fragenkatalog-Tags
   +--> UE-Übersicht je Block
```

Alle Ausgaben sind generierte Artefakte und werden nicht von Hand bearbeitet. Sie liegen
ausschließlich unter `build/` — dem ignorierten Bauverzeichnis — und werden bei jedem
Build neu geschrieben; damit ist eine Handänderung beim nächsten Lauf verworfen, ohne
dass erzeugte Dateien im Versionsstand mitgeführt werden müssen. Ein Test hält fest,
dass keine Datei mit GENERATED-Kopf versioniert ist.

### P4 — Modulformat: Inhalt, Aufgabe, Lösung und Prüfungsfrage liegen zusammen

```
modules/<topic-id>/
  index.adoc        Lerninhalt          (:topic-id:)
  exercises.adoc    Aufgaben + Lösungen als [%collapsible]
  questions.adoc    mündliche Prüfungsfragen
```

*Begründung:* Wenn die Lösung ohnehin verfügbar ist — mitgeliefert oder vom Agenten
erzeugt —, ist die Übungsaufgabe kein Leistungsnachweis mehr, sondern ein Lernanlass.
Der Nachweis ist die mündliche Prüfung. Damit der Wert im Durcharbeiten entsteht und
nicht im Abliefern, wird **jede Aufgabe mit ihren Prüfungsfragen ausgeliefert**.

*Nebeneffekt:* Diese Prüfungsfragen sind das Rohmaterial für den Fragenkatalog. Er wächst
aus den Modulen, statt separat gepflegt zu werden — auch für die Theorieseite, die heute
keine Fragen hat.

```
Übungsaufgabe --> Lösung --> Prüfungsfragen --> Fragenkatalog
      |                              |
      +------ ein Modul, eine topic-id ------+
```

**Abschnittsfolge von `index.adoc`.** Bei rund 48 Modulen (P1) entscheidet eine feste
Gliederung darüber, ob sie einander gleichen. Ohne sie driften sie, und `questions.adoc`
hängt an nichts.

```adoc
= Branching in git
:topic-id: git-branching

== Learning outcomes     PFLICHT  was danach gekonnt werden muss;
                                  korrespondiert 1:1 mit questions.adoc

== <Stoff>                        frei viele Abschnitte, Stichpunkte
== <Stoff>                        und Diagramme, ~1-2 Seiten

== Decisions             PFLICHT  was BEI UNS gilt: no-flow, kein rebase
                                  auf main, Ubuntu statt WSL2

== Pitfalls              PFLICHT  was erfahrungsgemäß schiefgeht

== Terminology           PFLICHT  dt./engl. Begriffspaare (P12)

== Further reading                Manz-Kapitel, Links, Uni-Heidelberg-Skript
```

*Begründung für `Decisions`:* Das ist der Abschnitt, den kein Sprachmodell erzeugen kann.
Erklärtext ist keine knappe Ware mehr — jeder Schüler kann sich eine beliebig lange
Erklärung generieren lassen. Was der Agent nicht weiß, ist, was in diesem Jahrgang gilt,
was geprüft wird und welche Entscheidung hier getroffen wurde. Bisher steckte das
implizit im Vortrag und ging beim Nachlesen verloren.

*Füllfloskel-Risiko:* Pflichtabschnitte erzeugen Leerlauf in Modulen, wo es nichts zu
entscheiden gibt. Deshalb ist eine ausdrückliche Nullaussage erlaubt und gilt als
erfüllt:

```adoc
== Decisions

None specific to this topic.
```

Das ist eine bewusste Aussage statt eines vergessenen Abschnitts und hält Prüfung 6
trivial.

**Aufgabenarten in `exercises.adoc`.** Nicht jede Aufgabe hat eine Musterlösung.

```
DRILL                              PROJECT
generisch, wiederholbar            am eigenen Projekt
"erzeuge einen Merge-Konflikt      "erstellt die Nutzwertanalyse für
 und löse ihn auf"                  eure drei Projektideen"

Musterlösung möglich               Musterlösung existiert nicht
```

`kind=drill|project` ist eine **Kennzeichnung, kein CI-Zwang**. Weder `.Solution` noch ein
Kriterienblock sind verpflichtend; die Aufgabenzahl je Modul ist frei, `exercises.adoc`
darf inhaltsleer sein (Prüfung 9). Die Kennzeichnung dient zwei Zwecken: Die Schüler
erkennen, welche Aufgabe Teil ihrer Projektarbeit ist, und die Jahresplanung zeigt,
welcher Unterricht das Projekt vorantreibt.

*Verhältnis zu P5:* Verbergen bleibt kein Prinzip. Mitliefern ist aber keine Pflicht —
bei `project`-Aufgaben gibt es nichts mitzuliefern, weil die Lösung das Projekt des Teams
ist.

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
    check-curriculum.*              CI-Prüfungen aus P2
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
        +-- GitHub Actions --> gh-pages          (primär, automatisch)
        |
        +-- publish.sh (lokal) --> Schulwebspace (optional, manuell)

   Hugo-Site auf dem Schulwebspace: bleibt unverändert bestehen
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
        |  Sammellauf über curriculum.yaml
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

### P10 — Das Modul ist vorbereitet und klassenunabhängig, der Verlauf bleibt außerhalb

Bisher war die Lernressource ein einziges Dokument, das im Unterricht live mitgeschrieben
wurde und nach Datum gegliedert war (`2526-3bhif-syp-lecture-notes` und die
Vorgängerjahrgänge: 20–31 Kapitel, je ein Unterrichtstermin). Dieses Dokument leistete
drei Dinge gleichzeitig.

```
1  Stoff erklären          --> gehört ins Modul    (stabil, mehrjährig)
2  Verlauf protokollieren  --> klassenspezifisch   (flüchtig)
3  Spontanes festhalten    --> flüchtig, manches später wertvoll
```

Nur (1) gehört ins Curriculum-Repository. `modules/<topic-id>/index.adoc` ist jahrgangs-
weit und mehrjährig gültig; wird darin live mitgeschrieben, steht Klassenspezifisches in
der gemeinsamen Quelle, überschreibt die nächste Klasse den Verlauf der vorigen, und der
Text ist im Folgejahr mit den Zufällen des Vorjahres durchsetzt.

```
   BISHER: eine Achse -- ZEIT        NEU: eine Achse -- THEMA

   2025-09-16                        modules/git-basics/
     Static Site Generators            index.adoc, exercises.adoc,
     Types of Branches                 questions.adoc
   2025-09-23                        modules/git-branching/
     Fork, Pull Request                ...
```

**Entscheidung:** Das Repository trägt kein Journal. Der Unterrichtsverlauf — welche
Klasse wie weit gekommen ist — wird außerhalb geführt. Damit bleibt das Modul
vorbereitbar, und der Detaillierungsgrad aus P1/P4 ist haltbar.

*Verworfen:* `journal/<klasse>/<datum>.adoc` im Repository mit `:covered:`-Attributen und
generierter Fortschrittsübersicht. Technisch reizvoll, aber eine Struktur, die niemand
gefordert hat; der Verlauf ist ohnehin nur für den Lehrenden relevant und braucht keine
Versionierung neben dem Stoff.

*Konsequenz für die Schüler:* Nachgelesen wird das vorbereitete Modul, nicht das
Unterrichtsprotokoll. Der Text muss deshalb ohne den Vortrag verständlich sein.

### P11 — Diagramme: PlantUML als Default, Bilder mit Herkunftsklasse

In den bestehenden Lecture Notes sind alle Diagramme exportierte Bilder ohne Quelltext,
bei 15–25 % Anteil am Material. Inhaltlich ist davon fast alles PlantUML-fähig —
Git-Workflows, V-Modell, Scrum-Framework, Kubernetes-Architektur, Docker-Volumes, UML.

```
@startuml      alle UML-Typen, component, deployment
@startmindmap  Stoffstruktur
@startwbs      Projektstrukturplan
@startgantt    Meilensteinplan   <-- unmittelbar Governance-Stoff
@startsalt     UI-Skizzen
@startjson     Datenstrukturen
```

**Regel:**

```
PlantUML ist Default, inline im .adoc, kein separates File.
Bild nur, wo PlantUML nicht trägt.
Bilder liegen beim Modul:   modules/<topic-id>/images/
Keynote-Quelle liegt daneben (.key), sonst ist der Export tot.
Screenshots tragen die Werkzeugversion im Dateinamen.
```

Ein PlantUML-Block ist diffbar, im Review lesbar, stilistisch einheitlich, überlebt eine
Überarbeitung und ist selbst Lehrmittel — PlantUML wird laut `define-syp3-curriculum`
(D4) ohnehin unterrichtet. Ein PNG ist ein Binärklotz, dessen Quelle auf dem Rechner des
Lehrenden liegt: genau die Drift, die P1 für Strukturdaten abgeschafft hat, nur für
Bilder.

*Echte Grenzen von PlantUML:* Git-Commit-Graphen (Punktnetz aus Branches und Merges),
Screenshots realer Oberflächen (GitHub-PR, IntelliJ) und freie konzeptuelle Skizzen. Dort
sind Bilder ausdrücklich erwünscht — ein vorhandenes gutes Bild neu zu zeichnen ist
Verschwendung.

**Herkunft ist Pflichtfeld, nicht Bildverzicht.** Drei Klassen:

```adoc
.Zielkreuz (own)
image::zielkreuz.png[Zielkreuz,500]

.Scrum framework (free: CC BY-SA 4.0, Scrum.org, https://…, retrieved 2026-09-10)
image::scrum-framework.png[Scrum framework,600]

.Kanban board (unclear: found via web search, rights not checked)
image::kanban.png[Kanban board,600]
```

*Begründung für die Erfassung zum Zeitpunkt des Einfügens:* Herkunft ist der einzige
Bestandteil, der sich nachträglich nicht beschaffen lässt. Bei 48 Modulen und
größenordnungsmäßig 100 Bildern ist in zwei Jahren nicht mehr feststellbar, welches PNG
woher kam; eine spätere Bereinigung würde zur Vollprüfung. Mit Feld ist sie ein `grep`.

**`unclear` blockiert nicht.**

```
Job "build"         baut und deployt        -> läuft auch bei unclear
Job "rights-check"  fällt rot bei unclear > 0, listet Datei und Zeile
```

*Begründung:* Ein hartes Fail würde die Veröffentlichung von 48 Modulen an einem einzigen
ungeklärten Bild aufhängen — mit der Folge, dass die Klasse `unclear` gemieden und das
Feld wertlos wird. Ehrlich zu sein muss die bequemere Option bleiben.

**Rechtliche Grundlage** (Recherchestand 2026-09-06, keine Rechtsberatung). Die
entscheidende Trennlinie ist nicht „Unterricht oder nicht", sondern **öffentlich oder
abgegrenzt**:

```
Moodle (Login, abgegrenzter Kursteilnehmerkreis)  -> § 42g UrhG greift
gh-pages / Schulwebspace (öffentlich)             -> § 42g UrhG greift NICHT
```

| Bestimmung | Inhalt | Folge für diese Site |
|---|---|---|
| § 42 Abs 6 | Vervielfältigung zum Schulgebrauch in Klassenstärke — **ausgenommen Werke, die ihrer Beschaffenheit und Bezeichnung nach für den Unterrichtsgebrauch bestimmt sind** | deckt Schulbücher nicht; deckt keine Web-Veröffentlichung |
| § 42g | digitale Nutzung für einen **abgegrenzten Kreis von Unterrichtsteilnehmern**, als Intranet-Regel gedacht | deckt Moodle, nicht das offene Netz; dieselbe Schulbuch-Ausnahme |
| § 42f | Zitat, ausdrücklich auch bei öffentlicher Zugänglichmachung — verlangt **Belegfunktion**, inneren Zusammenhang, verhältnismäßigen Umfang, Quellenangabe | einziger Weg für fremdes Material ohne Lizenz |
| § 6 | Sammelwerke: Auswahl und Anordnung sind schutzfähig, wenn eigentümlich | Gliederungen nicht 1:1 übernehmen |
| — | Fakten und Erkenntnisse sind nie geschützt, nur ihre konkrete sprachliche Darstellung | Inhalte in eigener Formulierung sind frei |

Zur Abgrenzung beim Bildzitat: Ein Bild, das den Text *illustriert*, ist kein Zitat. Ein
Bild, mit dem sich der Text erkennbar auseinandersetzt, kann eines sein.

```
"Grafik, weil sie Scrum gut zeigt"          -> Illustration, kein Zitat
"So stellt Quelle X den Ablauf dar; hier
 liegt der Review vor der Retro, während"  -> Belegfunktion, Zitat
```

Screenshots von Software-Oberflächen aus Piktogrammen, Menüs und Navigationselementen
gelten weithin als unkritisch und tragen im erklärenden Zusammenhang zusätzlich als
Bildzitat.

**Zwei Auswege, die nichts kosten:** ein Link auf eine frei zugängliche Seite ist keine
Vervielfältigung; und Material, das § 42g deckt, kann in Moodle statt auf der
öffentlichen Site liegen.

**Bewusst getragenes Restrisiko:** Bilder der Klasse `unclear` werden trotz ungeklärter
Rechtelage ausgeliefert. Eine vierte Klasse für Bildzitate und ein Ausschluss von
`unclear` aus der Auslieferung wurden erwogen und verworfen — die Herkunftsangabe macht
eine Bereinigung jederzeit möglich, und die Klassifikation soll die Arbeit nicht
verlangsamen.

Quellen: § 42, § 42f, § 42g und § 6 UrhG (jusline.at); „Urheberrecht und Schule",
Bildungsdirektion Tirol; Saferinternet.at; OGH-Judikatur zum Bildzitat (jusguide.at);
FAQ Copyright Universität Innsbruck.

### P12 — Sprache: Englisch, Governance-Begriffe zweisprachig

Unterrichtssprache und Lernressourcen sind Englisch. Der Governance-Block ist jedoch an
**deutsche Formulare** gebunden: Der Diplomarbeitsantrag fragt nach *Ausgangslage*,
*Untersuchungsanliegen*, *Geplantes Ergebnis*, *Verantwortlich*. Wer den Stoff nur als
*initial situation* und *research objective* gelernt hat, übersetzt im 5. Jahrgang unter
Prüfungsdruck zurück.

```
Governance    deutsche Begriffe sind der Lerngegenstand
Werkzeuge     englische Begriffe sind der Lerngegenstand
              (git, pull request, merge conflict, spec, capability)
Modellierung  gemischt (Anwendungsfalldiagramm / use case diagram)
```

**Entscheidung:** Modultext auf Englisch, plus Pflichtabschnitt `== Terminology` mit
deutsch/englischen Begriffspaaren (P4, Prüfung 6). In Governance-Modulen werden
Fachbegriffe durchgehend in beiden Sprachen geführt, nicht nur im Terminology-Abschnitt.

Die Vorlage für Projektantrag und Projektauftrag trägt zweisprachige Feldbezeichner:

```adoc
== Ausgangslage / Initial situation
== Untersuchungsanliegen / Research objective
== Geplantes Ergebnis / Planned deliverable
```

*Alternative:* Deutsche Begriffe nur in Klammern beim ersten Auftreten. Verworfen — im
Fließtext gehen sie beim Lernen unter, und der Terminology-Abschnitt liefert nebenbei die
Vokabelliste, die bei mündlichen Prüfungen fehlt.

*Alternative:* Governance-Module auf Deutsch, Rest Englisch. Verworfen — eine
zweisprachige Site ist inkonsistent, und die Unterrichtssprache ist Englisch.

*Folge für `define-syp3-curriculum`:* Zweisprachige Feldbezeichner ergeben nur Sinn, wenn
die Feldstruktur die des DA-Antrags ist. Damit ist die dortige offene Frage entschieden —
siehe D2.

### P13 — Ablage auf GitHub: drei Organisationen nach Lebensdauer

Der Account führt rund 77 Organisationen nach dem Muster `<jahr>-<klasse>-<gegenstand>`,
seit 2026/27 verkürzt auf `<jahr>-<klasse>`. Diese Organisationen sind jahresgebunden und
werden nach dem Schuljahr nicht mehr gepflegt. Daneben bestehen `htl-leonding-college`
(themenbezogenes Material: Fragenkatalog, diverse `*-lecture-notes`) und
`htl-leonding-example` (Angaben zu Übungen und Tests, rund 93 Repositories nach dem
Muster `jg<NN>-<gegenstand>-<thema>`).

Die Zuordnung folgt der Lebensdauer des Inhalts, nicht seiner Zugehörigkeit zu einer
Klasse:

```
htl-leonding-college/       mehrjährig, klassenunabhängig, public
  curriculum-syp3           Module, curriculum.yaml, Generatoren, Site
  student-project-template  Jahresprojekt-Gerüst: openspec, docs, CI
  klassen-setup             P9
  fragenkatalog             bestehend, unangetastet

htl-leonding-example/       Übungsangaben, public
  jg03-syp-<topic-id>       je Übung mit Startercode
  <Altbestand>              überwiegend privat, bleibt unverändert

<jahr>-<klasse>/            ein Schuljahr, eine Klasse, Classroom 50
  classroom50               Konfiguration und Roster
  <exam-templates>          privat
  <assignment-repos>        entstehen je Schüler
```

*Begründung gegen die Klassen-Organisation als Stoffablage:* `curriculum-syp3` ist per P6
jahrgangsweit und mehrjährig. Eine Organisation, die im Juli des Folgejahres nicht mehr
gepflegt wird, ist der falsche Ort dafür. `htl-leonding-college` trägt bereits den
Fragenkatalog, an den P8 den neuen Katalog koppelt.

**Classroom 50 als Randbedingung.** Das Werkzeug hat keinen eigenen Server; Klassenlisten,
Assignments und Ergebnisse liegen als Organisations- und Team-Mitgliedschaft, Repositories
und Konfigurationsdateien in GitHub. Daraus folgen zwei Regeln:

```
öffentliches Template    darf in einer FREMDEN Organisation liegen
privates Template        muss in DERSELBEN Organisation liegen wie das Classroom
```

Deshalb liegen Übungsangaben öffentlich in `htl-leonding-example` und sind über Jahre
und Klassen hinweg wiederverwendbar, ohne jährliche Kopie.

**Übungsangabe und Prüfungsangabe werden getrennt behandelt.**

| | Übung | Prüfung |
|---|---|---|
| Sichtbarkeit | public | privat |
| Ort | `htl-leonding-example` | Classroom-Organisation des Jahres |
| Begründung | Lösungen dürfen bekannt sein (P5); der Nachweis ist die mündliche Prüfung | die Angabe ist wertlos, wenn sie vorab lesbar ist |
| Zugriffssteuerung | keine | Freischaltung des Assignments in Classroom 50 |
| Wiederverwendung | über Jahre | keine — Angaben werden jährlich geändert |

Nach der Durchführung kann eine Prüfungsangabe öffentlich werden und als
`<jahr>-exam-<thema>` ins Archiv wandern; ab dann greift wieder die P5-Logik, und alte
Angaben sind Lernmaterial.

*Namensschema für Übungsangaben:* `jg03-syp-<topic-id>`. Der Jahrgangspräfix folgt dem
Bestand, der Gegenstand unterscheidet SYP von ITP mit denselben Themen, und die
`topic-id` ist stabil — eine fortlaufende Nummerierung würde genau dann brechen, wenn im
Jahresplan etwas verschoben wird, also im Fall, für den Prüfung 5 existiert.

*Sichtbarkeit von `curriculum-syp3`:* public. GitHub Pages liefert öffentliche
Repositories ohne weitere Voraussetzung aus; ein Pro-Status der Organisation wird erst
nötig, wenn ein privates Repository Pages liefern soll.

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
| Pflichtabschnitte (`Decisions`, `Pitfalls`, `Terminology`) erzeugen Füllfloskeln | Ausdrückliche Nullaussage ist erlaubt und erfüllt die Prüfung (P4); eine bewusste Leermeldung ist informativer als ein fehlender Abschnitt |
| Bilder der Klasse `unclear` gehen öffentlich live | Bewusst akzeptiert (P11): `rights-check` meldet sie rot und macht sie auffindbar, statt die Veröffentlichung zu blockieren; endgültige Klärung mit der Manz-Rechtsfrage |
| 48 Modulverzeichnisse statt 13 erhöhen den Pflegeaufwand | Textmenge unverändert, nur anders geschnitten (P1); Skelett und Navigation kommen aus den Generatoren (P3), Prüfung 9 hält die Struktur einheitlich |
| Prüfungsangaben liegen in der jahresgebundenen Classroom-Organisation und sind nicht wiederverwendbar | Bewusst (P13): Angaben werden ohnehin jährlich geändert; nach der Durchführung wandern sie öffentlich ins Archiv und bleiben als Lernmaterial erhalten |
| Übungsangaben sind öffentlich einsehbar, bevor die Klasse sie bearbeitet | Bewusst (P5/P13): Verbergen ist bei Agentenverfügbarkeit wirkungslos, der Nachweis ist die mündliche Prüfung |
| Unterrichtsverlauf ist im Repository nicht mehr nachvollziehbar | Bewusst (P10): Verlauf ist klassenspezifisch und wird außerhalb geführt; das Modul bleibt dafür mehrjährig gültig |

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

Stand 2026-09-07 nach der Umsetzung:

- ~~Sprache der Werkzeuge in `tools/`~~ **Python** mit PyYAML als einziger
  Fremdabhängigkeit; `klassen-setup` bleibt Bash (P9). Die Graphprüfungen (Zyklen,
  Vorwärtsreferenzen) sind in Bash mühsam und schlecht testbar, und Node würde
  `node_modules` in ein Repository ziehen, das sonst keinen Build-Schritt hat.
- ~~Wie das containerisierte asciidoctor-Image ergänzt wird~~ **Gar nicht.**
  `asciidoctor/docker-asciidoctor:1.83` bringt `asciidoctor-diagram`, PlantUML, Graphviz
  und `asciidoctor-revealjs` bereits mit; `local-convert.sh` und der Build-Job rufen
  dasselbe Image.
- **Offen:** JDK-Version — hängt am 4./5. Jahrgang. `versions.env` trägt `25.0.1-tem`
  als vorläufigen Wert mit TODO.
- **Vertagt:** Pflichtfragen auch für Theoriethemen (CI-Prüfung 4 ausweiten). Sinnvoll
  erst, wenn die Theorieseite des Katalogs eine Weile bestanden hat; heute tragen alle
  zwanzig fertigen Module ohnehin Fragen, Theorie wie Praxis.
- **Vertagt:** Zeitpunkt und Umfang der Hugo-Ablösung. Entscheidbar, sobald die neue
  Site ein Schuljahr im Einsatz war.
