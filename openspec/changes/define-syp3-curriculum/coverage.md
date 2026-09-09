# Abdeckung: Requirement -> Thema

Jede Zeile ordnet ein Requirement der acht Capabilities den Themen aus
`curriculum.yaml` zu, die es tragen. Beide Richtungen zählen: kein Requirement ohne
Thema, kein Thema ohne Requirement.

Stand 2026-09-07 · 54 Themen · Quellenvermerk je Thema in der letzten Spalte
(Aufgabe 4.3; `—` heißt ausdrücklich: keine fremde Quelle, Neuautorenschaft).

## curriculum/jahresplanung

Diese Capability beschreibt den Rahmen, nicht einzelne Unterrichte. Träger ist
deshalb `curriculum.yaml` selbst — `meta.budget`, `meta.zonen` und die Belegung der
Unterrichte —, geprüft durch die Prüfungen 2, 3 und 5.

| Requirement | Träger | Quelle |
|---|---|---|
| Jahresrahmen und Umfang sind festgelegt | `meta.unterrichte`, `meta.budget`, `meta.budget_je_block` | — |
| Die Reserve liegt am Ende und trägt den verzichtbarsten Inhalt | `meta.zonen.reserve` (U26–U30), `minikube-basics`, `minikube-deploy`, `minikube-services` | — |
| Die Reihenfolge folgt der Werkzeugabhängigkeit | `requires`-Graph aller Themen (Prüfung 3) | — |
| Theorie und Praxis eines Unterrichts sind verzahnt | Slot-Belegung je `lesson` (Prüfung 5) | — |
| Projektarbeit findet außerhalb des Unterrichts statt | `review-milestone-1`, `review-milestone-2`, `review-milestone-3` | — |
| Die Eröffnungssequenz stellt Arbeitsfähigkeit her | `course-overview`, `learning-environment-setup`, `git-basics` … `openspec-hands-on` (U1–U10) | — |
| *(neu)* Der Gegenstand wird zu Beginn eingeordnet | `course-overview`, `what-is-software-engineering` | Manz Kap. 1 (eigene Formulierung) |
| *(neu)* Die Leistungsfeststellung ist vorab bekannt | `assessment-written-and-oral`, `questions.adoc` jedes Moduls | — |

## curriculum/lernumgebung

| Requirement | Themen | Quelle |
|---|---|---|
| Einheitliche Lernumgebung | `learning-environment-setup` | — |
| Die Installation wird risikoarm vorbereitet | `learning-environment-setup` | eigene Installationsanleitung |
| Hardware-Voraussetzungen sind vorab geprüft | `course-overview` (Checkliste als HÜ vor U1) | — |
| Der Werkzeugstand ist klassenweit reproduzierbar | `learning-environment-setup` (Repository `klassen-setup`) | — |
| Die Lernumgebung ist Anknüpfungspunkt für späteren Stoff | `docker-basics`, `docker-images` | — |

## curriculum/praxis-toolchain

| Requirement | Themen | Quelle |
|---|---|---|
| Versionsverwaltung im Alleingang | `git-basics` | bestehender Fragenkatalog (Git) |
| Parallele Arbeit über Zweige | `git-branching` | bestehender Fragenkatalog (Git) |
| Änderungen werden vor der Übernahme begutachtet | `git-pull-requests` | bestehender Fragenkatalog (Git) |
| Konflikte werden aufgelöst | `git-conflicts-remotes` | bestehender Fragenkatalog (Git) |
| Dokumentation entsteht als Text neben dem Projekt | `asciidoctor-basics` | bestehender Fragenkatalog (Asciidoctor) |
| Veröffentlichung läuft automatisch | `gh-actions-pages` | Pipeline des Fragenkatalogs |
| Präsentationen entstehen aus derselben Quelle | `revealjs-presentations` | Pipeline des Fragenkatalogs |
| Eine neutrale Bauumgebung entscheidet Streitfälle | `gh-actions-pages`, `docker-multiarch` | — |

## curriculum/praxis-ai

| Requirement | Themen | Quelle |
|---|---|---|
| Grundlagen und Aufgabenformulierung | `ai-basics-prompting` | — |
| Kontext bewusst bereitstellen | `ai-context-continuation` | — |
| Arbeit über eine Sitzungsgrenze hinweg fortsetzen | `ai-context-continuation` | eigene Continuation-Prompts |
| Das Arbeitsumfeld des Agenten gestalten | `ai-harness-engineering` | — |
| Wiederholende Abläufe erkennen und begrenzen | `ai-agentic-loops` | — |
| Verantwortung für das Ergebnis bleibt beim Schüler | `ai-result-verification`, `ai-project-integration` | — |

## curriculum/praxis-container

| Requirement | Themen | Quelle |
|---|---|---|
| Container-Grundlagen | `docker-basics`, `docker-images` | bestehender Fragenkatalog (Docker) |
| Daten und Konfiguration überleben den Container | `docker-volumes-config` | bestehender Fragenkatalog (Docker) |
| Abbilder laufen auf unterschiedlichen Prozessorarchitekturen | `docker-multiarch` | — |
| Anwendungen aus mehreren Diensten | `compose-basics`, `compose-multi-service`, `compose-networks-dependencies` | bestehender Fragenkatalog (Compose) |
| Orchestrierung im lokalen Überblick | `minikube-basics`, `minikube-deploy`, `minikube-services` | bestehender Fragenkatalog (Kubernetes) |

## curriculum/projekt-governance

| Requirement | Themen | Quelle |
|---|---|---|
| Projektbegriff und Ausgangslage | `governance-project-basics` | Manz Kap. 1–2 (eigene Formulierung) |
| Ideenfindung mit sechs Techniken, eine davon durchgeführt | `governance-idea-generation` | PUMA8_12 Kreativitätstechniken (Brainstorming, 6-3-5, Morphologischer Kasten, Mindmapping, Bionik, Delphi) |
| Projektauswahl ist kriterienbasiert und nachvollziehbar | `governance-weighted-scoring` | PUMA8_05 Nutzwertanalyse |
| Stakeholder und Zielsetzung | `governance-stakeholders-goals` | Manz Kap. 3 (eigene Formulierung) |
| Projektantrag und Projektauftrag erstellen | `governance-project-charter` | DA-Antragsformular der Schule |
| Der Projektauftrag ist eingefroren und bleibt Beurteilungsanker | `governance-project-charter`, `sdd-specs-replace-requirements` | — |
| Schätz-Hygiene statt Schätzverfahren | `governance-estimation-hygiene` | Manz (Verfahren nur benannt) |
| Meilensteinplanung und Abnahme | `governance-milestones`, `governance-acceptance`, `review-milestone-1`, `review-milestone-2`, `review-milestone-3` | Manz Kap. 5 (eigene Formulierung) |
| Governance ist unabhängig vom Vorgehensmodell | `bridge-charter-to-specs`, `bridge-progress-and-milestones` | — |

## curriculum/vorgehen-sdd

| Requirement | Themen | Quelle |
|---|---|---|
| Vorgehensmodelle als drei Taktfrequenzen desselben Musters | `process-models-overview` | `01.Vorgehensmodelle.key` |
| Vokabular der klassischen Modelle | `process-waterfall`, `process-scrum` | `01.Vorgehensmodelle.key`, Manz Kap. 4 |
| Spezifikationsgetriebene Entwicklung anwenden | `sdd-openspec-artifacts`, `sdd-change-lifecycle`, `openspec-hands-on` | openspec-Dokumentation |
| Der Sollzustand ersetzt das Pflichtenheft | `sdd-why-specs`, `sdd-specs-replace-requirements` | — |
| Brücke zwischen Governance und Durchführung | `bridge-charter-to-specs`, `bridge-progress-and-milestones` | — |
| Das Prinzip ist der Lerngegenstand, nicht das Werkzeug | `sdd-principle-not-tool` | — |

## curriculum/uml-basics

| Requirement | Themen | Quelle |
|---|---|---|
| Anwendungsfalldiagramm erstellen und lesen | `uml-use-case` | UML-Skripten Uni Heidelberg |
| Klassen- und Objektdiagramm erstellen und lesen | `uml-class-object` | UML-Skripten Uni Heidelberg |
| Aktivitätsdiagramm erstellen und lesen | `uml-activity` | UML-Skripten Uni Heidelberg |
| Zustandsdiagramm im Überblick | `uml-state-overview` | UML-Skripten Uni Heidelberg |
| Diagramme werden als Quelltext geführt | `uml-overview` und alle UML-Themen | PlantUML-Dokumentation |

## Gegenprobe

Alle 54 Themen kommen oben vor. Zwei Themen hatten anfangs kein Requirement —
`what-is-software-engineering` und `assessment-written-and-oral`; dafür sind die beiden mit
*(neu)* markierten Requirements in `specs/curriculum/jahresplanung/spec.md` ergänzt
worden (Aufgabe 1.2). Kein Requirement blieb ohne Thema.
