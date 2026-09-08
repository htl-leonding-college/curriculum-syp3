## Purpose

Legt den Jahresrahmen des Gegenstands fest — Umfang, Aufteilung zwischen Theorie und
Praxis, Reihenfolge der Themen, Umgang mit Terminausfällen und die Verzahnung von
Unterricht und Projektarbeit.

## ADDED Requirements

### Requirement: Jahresrahmen und Umfang sind festgelegt
Der Jahresplan SHALL 30 Unterrichte zu je drei Unterrichtseinheiten umfassen, im
Regelfall aufgeteilt in eine Einheit Theorie und zwei Einheiten Praxis. Der Gesamtumfang
SHALL rund 25 Einheiten Theorie und rund 50 Einheiten Praxis betragen.

#### Scenario: Themenumfang wird geplant
- **WHEN** die Themen des Jahres auf Unterrichte verteilt werden
- **THEN** bleibt die Summe der Einheiten je Art innerhalb des festgelegten Budgets

### Requirement: Die Reserve liegt am Ende und trägt den verzichtbarsten Inhalt
Der Jahresplan SHALL eine Reservezone am Ende des Schuljahres vorsehen. Diese Zone SHALL
mit dem Inhalt belegt sein, dessen Entfall den geringsten Schaden anrichtet.

#### Scenario: Termine fallen aus
- **WHEN** Unterrichte durch schulische Veranstaltungen entfallen
- **THEN** trifft der Entfall den als entbehrlich geplanten Inhalt und keine Kerninhalte

### Requirement: Die Reihenfolge folgt der Werkzeugabhängigkeit
Die Themenfolge SHALL sich daraus ergeben, welches Werkzeug für den nächsten
Arbeitsschritt verfügbar sein muss, und MUST NOT der Kapitelreihenfolge eines Lehrbuchs
folgen.

#### Scenario: Projektstart
- **WHEN** die Schüler mit der eigenständigen Projektarbeit beginnen sollen
- **THEN** beherrschen sie die dafür nötigen Werkzeuge bereits, weil deren Unterricht
  vorher liegt

### Requirement: Theorie und Praxis eines Unterrichts sind verzahnt
Der Theorieteil eines Unterrichts SHALL inhaltlich auf den Praxisteil desselben oder
eines nahen Unterrichts bezogen sein. Ein Governance-Artefakt SHALL unmittelbar nach der
zugehörigen Theorieeinheit als Hausübung entstehen.

#### Scenario: Governance-Artefakt wird beauftragt
- **WHEN** ein Projektantrag oder Projektauftrag als Hausübung aufgegeben wird
- **THEN** lag die Theorieeinheit zu seiner Struktur unmittelbar davor, und ein Review
  folgt im nächsten Unterricht

### Requirement: Projektarbeit findet außerhalb des Unterrichts statt
Die eigentliche Projektarbeit SHALL außerhalb der Unterrichtszeit erfolgen. Der
Jahresplan SHALL Unterrichtszeit für Meilenstein-Reviews und Hilfestellung reservieren.

#### Scenario: Meilenstein steht an
- **WHEN** ein Meilenstein erreicht sein soll
- **THEN** steht im Unterricht Zeit für Review und Rückmeldung zur Verfügung, ohne
  dass Kerninhalte entfallen

### Requirement: Die Eröffnungssequenz stellt Arbeitsfähigkeit her
Der erste Unterricht SHALL Überblick über das Stoffgebiet, Organisation, Bewertung und
die Einrichtung der Lernumgebung umfassen. Die folgenden Unterrichte SHALL die
Werkzeugkette bereitstellen, bevor die Projektarbeit beginnt.

#### Scenario: Schüler beginnt das Schuljahr
- **WHEN** der erste Unterricht stattgefunden hat
- **THEN** kennt der Schüler den Stoffumfang des Jahres, die Bewertungsgrundlage und die
  Anforderungen an sein Gerät

### Requirement: Der Gegenstand wird zu Beginn eingeordnet
Zu Beginn des Jahres SHALL vermittelt werden, womit sich der Gegenstand befasst und wie
das Jahr organisiert ist: Stoffüberblick, Werkzeugkette, Bewertung und der Begriff des
Software-Engineering.

#### Scenario: Schüler fragt nach dem Zweck des Gegenstands
- **WHEN** ein Schüler wissen will, warum Werkzeuge, Governance und Modellierung in
  einem Gegenstand zusammenliegen
- **THEN** ist das im ersten Unterricht behandelt worden und im Modul nachlesbar

### Requirement: Die Leistungsfeststellung ist vorab bekannt
Die Art der Leistungsfeststellung SHALL vor der ersten Prüfung behandelt werden. Zu
jedem Lernziel SHALL die zugehörige Prüfungsfrage vorab verfügbar sein.

#### Scenario: Schüler bereitet sich auf die mündliche Prüfung vor
- **WHEN** ein Schüler wissen will, woran er gemessen wird
- **THEN** findet er den Ablauf im Modul zur Leistungsfeststellung und die Fragen in den
  Modulen des jeweiligen Stoffs
