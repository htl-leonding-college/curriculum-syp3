# Continuation Prompt — Curriculum SYP 3. Jahrgang

**Stand:** 2026-09-07 · Planung beider Changes vollstaendig · Umsetzung von
`setup-curriculum-repository` bei **37/51 Aufgaben** · alles Lokale gebaut und gruen
**Repo:** `github.com/htl-leonding-college/curriculum-syp3` (public) — lokal 2 Commits vor `origin/main`

> Loest `2026-09-07-alle-threads-durch.md` ab. Die aelteren bleiben als Historie liegen.

---

## Einstieg

```
/opsx:apply setup-curriculum-repository
```

Der Kontext steht in `openspec/changes/*/{proposal,design,tasks}.md` und den Specs.
`curriculum.yaml` ist die Strukturwahrheit (54 Themen, U1–U28, alle `planned`).

---

## Was seit dem letzten Stand entstanden ist

```
curriculum-syp3/
  README.adoc                 Zweck, Layout, Katalog-Zustaendigkeit, Manz-Regel
  config.sh                   Image-Tag, Pfade, Webspace-Ziel
  local-convert.sh            Pruefung -> Generatoren -> asciidoctor -> revealjs
  publish.sh                  rsync auf den Schulwebspace (lokal, ohne Secrets)
  site/index.adoc             Landing Page (Mindmap, Navigation, UE-Uebersicht)
  tools/
    curriculum.py             Lademodul, Modulpfade aus der ID
    adoc.py                   Attribute, Abschnitte, Outcomes, Fragen, Bilder
    check-curriculum.py       Pruefungen 1-9 + Strukturattribut-Verbot
    gen-{mindmap,nav,ue-overview,questions}.py
    new-module.py             Skelett aus templates/module/
    rights-report.py          meldet unclear-Bilder, blockiert nicht
    tests/                    49 Tests, je Pruefung rot und gruen
  templates/module/           Vorlage + Autorenleitfaden
  modules/git-basics/, modules/sdd-openspec-artifacts/    Skelette
  .github/workflows/build.yml check | rights-check | build | deploy
```

Daneben, als eigene lokale Repositories ohne Remote:

```
../klassen-setup/                setup-tools.sh, setup-identity.sh,
                                 versions.env, README.adoc   (1 Commit)
../student-project-template/     openspec-Scaffold, docs/, CI (1 Commit)
```

## Zwei Entscheidungen aus der Umsetzung

1. **`status: planned | ready` je Thema** (Default `planned`). Ohne das Feld stehen zwei
   Spec-Anforderungen gegeneinander — jedes Thema braucht eine Ressource, Themen sollen
   aber vor ihrer Ressource planbar sein — und der Widerspruch trifft genau den
   Anfangszustand: 54 Themen, keine Module. Bijektion, Pflichtabschnitte,
   Outcome-Kopplung und Modulskelett greifen nur fuer `ready`; verwaiste Dateien und
   unbekannte IDs fallen immer auf. Design P1/P2 und beide Specs sind nachgezogen.
2. **Erzeugte Artefakte nur in `build/`** (ignoriert, bei jedem Build neu). Der geplante
   `git diff --exit-code`-Vergleich entfaellt damit; ein Test haelt fest, dass nichts mit
   GENERATED-Kopf versioniert ist.

Werkzeugsprache ist **Python** (PyYAML), `klassen-setup` bleibt **Bash**.

## Konventionen, die die Pruefung erwartet

```adoc
// index.adoc
== Learning outcomes
* [[lo-1]] Record a change as a commit

// questions.adoc
== What does a commit contain?
covers: lo-1

// Bild
.Scrum framework (free: CC BY-SA 4.0, https://…, retrieved 2026-09-10)
image::images/scrum.png[Scrum framework,600]
```

## Verifikation

```bash
python3 -m venv .venv && .venv/bin/pip install -r tools/requirements-dev.txt
.venv/bin/python tools/check-curriculum.py          # 54 Themen, 0 Befunde
.venv/bin/python -m pytest tools/tests -q           # 49 passed
PYTHON=.venv/bin/python ./local-convert.sh          # build/site/index.html
.venv/bin/python tools/check-curriculum.py --as-ready git-basics   # Skelett-Probelauf
```

Stand des Checks gegen das echte Modell: **0 Befunde**, 54 Themen `planned`, keine
Strukturfehler. Die Site baut durch, Mindmap als SVG, revealjs-Deck je Modul.

## Was aussteht

**Braucht GitHub — bewusst nicht ungefragt gemacht:**

- `main` pushen (2 Commits), Pages aktivieren, ersten Actions-Lauf pruefen (5.2, 5.3, 5.6)
- `htl-leonding-college/klassen-setup` und `student-project-template` anlegen und pushen
  (7.1, 8.1)
- `htl-leonding-example/jg03-syp-git-basics` anlegen, `assignment_template` eintragen,
  Check um "Repository existiert" erweitern (9.1, 9.2)
- Hinweis auf den jeweils anderen Katalog auf beiden Einstiegsseiten (6.3)

**Braucht Geraete oder Absprachen:**

- `setup-tools.sh` auf frischem Ubuntu 26.04 und auf macOS durchlaufen, danach git-Tag
  fuer 2026/27 (7.6, 7.7)
- JDK-Version mit 4./5. Jahrgang abstimmen — `versions.env` traegt `25.0.1-tem` als
  vorlaeufigen Wert mit TODO (7.3)
- `publish.sh` gegen den Schulwebspace laufen lassen (5.5)

**Braucht den anderen Change:**

- Governance-Vorlagen (Projektantrag, Projektauftrag, Meilensteinplan, Abnahme,
  zweisprachig) aus `define-syp3-curriculum` Gruppe 2 — erst danach 8.2
- Uebernahme von Fragen aus dem bestehenden Katalog mit Modulzuordnung (6.2)

**Naechster sinnvoller Schritt:** `/opsx:apply define-syp3-curriculum` — Gruppe 1
(Abdeckungstabelle Requirement -> topic-id) und Gruppe 2 (Governance-Vorlagen). Danach
die ersten Module inhaltlich schreiben, in der Reihenfolge der Eroeffnungssequenz
(U1-U10), und ihre Themen auf `status: ready` setzen.
