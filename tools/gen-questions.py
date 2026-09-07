#!/usr/bin/env python3
"""Fragenkatalog aus den questions.adoc der Module (P3, P8).

Die Zuordnungsmerkmale — Block, unterrichtender Jahrgang, voraussetzender
Jahrgang, Thema — stammen aus dem Modell und stehen nicht im Fragentext.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from tools import adoc, generated  # noqa: E402
from tools.curriculum import DEFAULT_PATH, Curriculum, load  # noqa: E402

OUTPUT = "questions/index.adoc"
DATA_OUTPUT = "questions/questions.json"


def collect(model: Curriculum) -> list[dict]:
    rows: list[dict] = []
    for topic in model.topics:
        # Nur fertige Module: ein Skelett traegt Platzhalterfragen, die im
        # Katalog nichts verloren haben.
        if not topic.is_ready or not topic.questions_path.is_file():
            continue
        for question in adoc.read(topic.questions_path).questions():
            rows.append(
                {
                    "question": question.title,
                    "topic": topic.id,
                    "topic_title": topic.title,
                    "block": topic.block,
                    "kind": topic.kind,
                    "lesson": topic.lesson,
                    "taught_in": topic.taught_in,
                    "prerequisite_for": topic.prerequisite_for,
                    "covers": list(question.covers),
                    "source": str(topic.questions_path.relative_to(model.root)),
                    "line": question.line,
                }
            )
    return rows


FILTER_FIELDS = ("block", "taught_in", "prerequisite_for", "topic", "kind")


def select(rows: list[dict], **criteria: str) -> list[dict]:
    """Fragen nach den Merkmalen des Modells auswaehlen.

    Dieselbe Auswahl, die die erzeugte Seite im Browser anbietet — hier fuer
    Abfragen auf der Kommandozeile und fuer die Tests.
    """
    unknown = set(criteria) - set(FILTER_FIELDS)
    if unknown:
        raise ValueError(f"unbekanntes Merkmal: {', '.join(sorted(unknown))}")
    return [
        row
        for row in rows
        if all(str(row.get(field)) == str(value) for field, value in criteria.items())
    ]


def _filter_ui(rows: list[dict]) -> str:
    """Auswahlfelder und Tabelle als HTML — die Merkmale sind Datenattribute."""
    options = {
        field: sorted({str(row[field]) for row in rows}) for field in FILTER_FIELDS
    }
    selects = "\n".join(
        "<label>{label}: <select data-field=\"{field}\">"
        "<option value=\"\">alle</option>{opts}</select></label>".format(
            label=field.replace("_", " "),
            field=field,
            opts="".join(f'<option value="{value}">{value}</option>' for value in values),
        )
        for field, values in options.items()
    )
    body = "\n".join(
        "<tr {attrs}><td>{lesson}</td><td>{topic_title}</td><td>{question}</td>"
        "<td>{covers}</td></tr>".format(
            attrs=" ".join(f'data-{field}="{row[field]}"' for field in FILTER_FIELDS),
            lesson=f"U{row['lesson']}",
            topic_title=row["topic_title"],
            question=row["question"],
            covers=", ".join(row["covers"]) or "—",
        )
        for row in rows
    )
    return f"""++++
<div class="question-filter">
{selects}
<span class="count"></span>
</div>
<table class="questions" id="question-table">
<thead><tr>
<th data-sort="lesson">Unterricht</th>
<th data-sort="topic_title">Thema</th>
<th data-sort="question">Frage</th>
<th>Lernziele</th>
</tr></thead>
<tbody>
{body}
</tbody>
</table>
<script>
(function () {{
  var table = document.getElementById('question-table');
  if (!table) return;
  var rows = Array.prototype.slice.call(table.tBodies[0].rows);
  var selects = document.querySelectorAll('.question-filter select');
  var count = document.querySelector('.question-filter .count');

  function apply() {{
    var visible = 0;
    rows.forEach(function (row) {{
      var show = Array.prototype.every.call(selects, function (select) {{
        return !select.value ||
          row.getAttribute('data-' + select.dataset.field) === select.value;
      }});
      row.hidden = !show;
      if (show) visible++;
    }});
    count.textContent = visible + ' von ' + rows.length + ' Fragen';
  }}

  Array.prototype.forEach.call(selects, function (select) {{
    select.addEventListener('change', apply);
  }});

  Array.prototype.forEach.call(table.tHead.rows[0].cells, function (cell) {{
    if (!cell.dataset.sort) return;
    cell.style.cursor = 'pointer';
    cell.addEventListener('click', function () {{
      var index = cell.cellIndex;
      var descending = cell.dataset.direction === 'asc';
      rows.sort(function (a, b) {{
        var left = a.cells[index].textContent, right = b.cells[index].textContent;
        return (descending ? -1 : 1) * left.localeCompare(right, 'de', {{numeric: true}});
      }});
      cell.dataset.direction = descending ? 'desc' : 'asc';
      rows.forEach(function (row) {{ table.tBodies[0].appendChild(row); }});
    }});
  }});

  apply();
}})();
</script>
++++
"""


def render(model: Curriculum, rows: list[dict]) -> str:
    titles = {block.id: block.title for block in model.blocks}
    lines = [
        f"= Fragenkatalog {model.meta.get('gegenstand', 'SYP')} "
        f"{model.meta.get('jahrgang', '')}".rstrip(),
        ":toc: left",
        ":toc-title: Inhalt",
        ":toclevels: 3",
        ":icons: font",
        "",
        "ifdef::env-github[]",
        ":tip-caption: :bulb:",
        ":note-caption: :information_source:",
        ":important-caption: :heavy_exclamation_mark:",
        ":caution-caption: :fire:",
        ":warning-caption: :warning:",
        "endif::[]",
        "",
        f"{len(rows)} Fragen aus {len({r['topic'] for r in rows})} Modulen. "
        "Massgeblich fuer SYP 3. Jahrgang ab dem Schuljahr 2026/27; der bestehende "
        "https://htl-leonding-college.github.io/fragenkatalog[Fragenkatalog] bleibt "
        "als Archiv erhalten.",
        "",
    ]
    if not rows:
        lines += ["Noch keine Fragen — die Module tragen ihre Fragen selbst.", ""]
    else:
        lines += [
            "== Alle Fragen",
            "",
            "Sortieren durch Klick auf eine Spaltenueberschrift, filtern ueber die "
            "Auswahlfelder. Die Merkmale stammen aus `curriculum.yaml` und stehen "
            "nicht im Fragentext.",
            "",
            _filter_ui(rows),
            "",
        ]

    for block in model.blocks:
        block_rows = [r for r in rows if r["block"] == block.id]
        if not block_rows:
            continue
        lines += [f"== {titles.get(block.id, block.id)}", ""]
        for topic_id in sorted({r["topic"] for r in block_rows}):
            topic_rows = [r for r in block_rows if r["topic"] == topic_id]
            head = topic_rows[0]
            lines += [
                f"=== U{head['lesson']} {head['topic_title']}",
                "",
                f"[.tags]#block: {head['block']}# "
                f"[.tags]#taught_in: {head['taught_in']}# "
                f"[.tags]#prerequisite_for: {head['prerequisite_for']}# "
                f"[.tags]#topic: {topic_id}#",
                "",
            ]
            for row in topic_rows:
                covers = ", ".join(row["covers"]) or "—"
                lines += [
                    f". {row['question']} "
                    f"[.covers]#({covers})#",
                ]
            lines += [""]
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--curriculum", type=Path, default=DEFAULT_PATH)
    parser.add_argument("--build-dir", type=Path, default=None)
    args = parser.parse_args(argv)
    model = load(args.curriculum)
    rows = collect(model)
    target = generated.write(OUTPUT, render(model, rows), build_dir=args.build_dir)
    payload = {"generated": generated.MARKER, "questions": rows}
    data = generated.write(
        DATA_OUTPUT, json.dumps(payload, indent=2, ensure_ascii=False) + "\n",
        build_dir=args.build_dir,
    )
    print(target)
    print(data)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
