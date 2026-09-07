## Purpose

Legt den Jahresrahmen des Gegenstands fest — Umfang, Aufteilung zwischen Theorie und
Praxis, Reihenfolge der Themen, Umgang mit Terminausfaellen und die Verzahnung von
Unterricht und Projektarbeit.

## ADDED Requirements

### Requirement: Jahresrahmen und Umfang sind festgelegt
Der Jahresplan SHALL 30 Unterrichte zu je drei Unterrichtseinheiten umfassen, im
Regelfall aufgeteilt in eine Einheit Theorie und zwei Einheiten Praxis. Der Gesamtumfang
SHALL rund 25 Einheiten Theorie und rund 50 Einheiten Praxis betragen.

#### Scenario: Themenumfang wird geplant
- **WHEN** die Themen des Jahres auf Unterrichte verteilt werden
- **THEN** bleibt die Summe der Einheiten je Art innerhalb des festgelegten Budgets

### Requirement: Die Reserve liegt am Ende und traegt den verzichtbarsten Inhalt
Der Jahresplan SHALL eine Reservezone am Ende des Schuljahres vorsehen. Diese Zone SHALL
mit dem Inhalt belegt sein, dessen Entfall den geringsten Schaden anrichtet.

#### Scenario: Termine fallen aus
- **WHEN** Unterrichte durch schulische Veranstaltungen entfallen
- **THEN** trifft der Entfall den als entbehrlich geplanten Inhalt und keine Kerninhalte

### Requirement: Die Reihenfolge folgt der Werkzeugabhaengigkeit
Die Themenfolge SHALL sich daraus ergeben, welches Werkzeug fuer den naechsten
Arbeitsschritt verfuegbar sein muss, und MUST NOT der Kapitelreihenfolge eines Lehrbuchs
folgen.

#### Scenario: Projektstart
- **WHEN** die Schueler mit der eigenstaendigen Projektarbeit beginnen sollen
- **THEN** beherrschen sie die dafuer noetigen Werkzeuge bereits, weil deren Unterricht
  vorher liegt

### Requirement: Theorie und Praxis eines Unterrichts sind verzahnt
Der Theorieteil eines Unterrichts SHALL inhaltlich auf den Praxisteil desselben oder
eines nahen Unterrichts bezogen sein. Ein Governance-Artefakt SHALL unmittelbar nach der
zugehoerigen Theorieeinheit als Hausuebung entstehen.

#### Scenario: Governance-Artefakt wird beauftragt
- **WHEN** ein Projektantrag oder Projektauftrag als Hausuebung aufgegeben wird
- **THEN** lag die Theorieeinheit zu seiner Struktur unmittelbar davor, und ein Review
  folgt im naechsten Unterricht

### Requirement: Projektarbeit findet ausserhalb des Unterrichts statt
Die eigentliche Projektarbeit SHALL ausserhalb der Unterrichtszeit erfolgen. Der
Jahresplan SHALL Unterrichtszeit fuer Meilenstein-Reviews und Hilfestellung reservieren.

#### Scenario: Meilenstein steht an
- **WHEN** ein Meilenstein erreicht sein soll
- **THEN** steht im Unterricht Zeit fuer Review und Rueckmeldung zur Verfuegung, ohne
  dass Kerninhalte entfallen

### Requirement: Die Eroeffnungssequenz stellt Arbeitsfaehigkeit her
Der erste Unterricht SHALL Ueberblick ueber das Stoffgebiet, Organisation, Bewertung und
die Einrichtung der Lernumgebung umfassen. Die folgenden Unterrichte SHALL die
Werkzeugkette bereitstellen, bevor die Projektarbeit beginnt.

#### Scenario: Schueler beginnt das Schuljahr
- **WHEN** der erste Unterricht stattgefunden hat
- **THEN** kennt der Schueler den Stoffumfang des Jahres, die Bewertungsgrundlage und die
  Anforderungen an sein Geraet
