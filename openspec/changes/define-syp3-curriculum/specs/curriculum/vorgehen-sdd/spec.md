## Purpose

Vermittelt Vorgehensmodelle als Instanzen eines gemeinsamen Musters mit
unterschiedlichem Takt und führt spezifikationsgetriebene Entwicklung als das Modell
ein, nach dem im Projekt tatsächlich gearbeitet wird.

## ADDED Requirements

### Requirement: Vorgehensmodelle als drei Taktfrequenzen desselben Musters
Der Schüler SHALL Wasserfall, Scrum und spezifikationsgetriebene Entwicklung als
Ausprägungen desselben Musters beschreiben können — Ziel klären, Umfang abgrenzen,
Anforderung präzise formulieren, bauen, verifizieren, Änderung kontrolliert einbringen
— und ihren Unterschied als Taktlänge benennen.

#### Scenario: Vergleich zweier Modelle
- **WHEN** der Schüler Wasserfall und Scrum vergleichen soll
- **THEN** benennt er den gemeinsamen Musterkern und den Unterschied im Takt, statt zwei
  unverbundene Schulen aufzuzählen

### Requirement: Vokabular der klassischen Modelle
Der Schüler SHALL die gängigen Begriffe der klassischen Modelle verstehen und
einordnen können, auch wenn im Projekt nicht danach gearbeitet wird.

#### Scenario: Begriff aus der Berufspraxis
- **WHEN** dem Schüler ein Begriff wie Sprint, Backlog oder Phase begegnet
- **THEN** kann er ihn einordnen und dem zugehörigen Modell zuweisen

### Requirement: Spezifikationsgetriebene Entwicklung anwenden
Der Schüler SHALL eine Änderung nach dem spezifikationsgetriebenen Ablauf durchführen
können: Anliegen und Umfang beschreiben, gewünschtes Verhalten als prüfbare
Anforderung formulieren, umsetzen, und die abgeschlossene Änderung in den Sollstand
überführen.

#### Scenario: Neue Funktion im Projekt
- **WHEN** ein Team eine Funktion ergänzt
- **THEN** existiert dazu eine beschriebene Änderung mit prüfbaren Anforderungen,
  bevor gebaut wird

### Requirement: Das Pflichtenheft wird einmal geschrieben, danach lebt der Sollzustand
Der Schüler SHALL im Projekt einmal ein Pflichtenheft nach der Gliederung des
Manz-Buchs verfassen und erklären können, warum danach ein fortgeschriebener
Sollzustand seine Anforderungen übernimmt und wodurch die Beurteilbarkeit trotzdem
erhalten bleibt.

#### Scenario: Pflichtenheft im Projekt
- **WHEN** der Projektauftrag freigegeben ist
- **THEN** schreibt das Team das Pflichtenheft einmal, stimmt es mit dem Auftraggeber
  ab und überträgt die nummerierten Anforderungen danach in `openspec/specs/`

#### Scenario: Frage nach dem Pflichtenheft
- **WHEN** der Schüler gefragt wird, wo im Projekt das Pflichtenheft steckt
- **THEN** nennt er das einmal abgestimmte Dokument, den Sollzustand als lebendes
  Gegenstück und den eingefrorenen Projektauftrag als Beurteilungsanker

### Requirement: Brücke zwischen Governance und Durchführung
Der Schüler SHALL jedes Feld des Projektantrags einem Artefakt der
spezifikationsgetriebenen Arbeitsweise zuordnen können und umgekehrt aus dem Stand des
Projekts den Fortschritt gegenüber dem Antrag ableiten.

#### Scenario: Nachweis eines Meilensteins
- **WHEN** ein Meilenstein nachgewiesen werden soll
- **THEN** zeigt der Schüler die zugehörige abgeschlossene Änderung und ihren Bezug
  zum Antragsfeld

### Requirement: Das Prinzip ist der Lerngegenstand, nicht das Werkzeug
Der Schüler SHALL das zugrunde liegende Prinzip vom eingesetzten Werkzeug unterscheiden
können.

#### Scenario: Werkzeug ändert sich
- **WHEN** das verwendete Werkzeug durch ein anderes ersetzt wird
- **THEN** bleibt das Gelernte anwendbar, weil der Schüler das Prinzip und nicht die
  Befehlsfolge gelernt hat
