#!/usr/bin/env bash
# Gemeinsame Einstellungen von local-convert.sh und publish.sh.
# Wird von beiden gesourct und ist die einzige Stelle fuer Versionen und Pfade.

# Containerisiertes asciidoctor — enthaelt asciidoctor-diagram, PlantUML,
# Graphviz und asciidoctor-revealjs. Nichts davon wird lokal installiert.
ASCIIDOCTOR_IMAGE="asciidoctor/docker-asciidoctor:1.83"

# Bauverzeichnis (ignoriert, wird bei jedem Lauf neu geschrieben)
BUILD_DIR="build"
SITE_DIR="${BUILD_DIR}/site"

# Ziel fuer publish.sh — Schulwebspace. Kein Zugangsdatum im Repository:
# der Zugang haengt am SSH-Schluessel des Ausfuehrenden.
WEBSPACE_HOST="${WEBSPACE_HOST:-edufs.edu.htl-leonding.ac.at}"
WEBSPACE_USER="${WEBSPACE_USER:-t.stuetz}"
WEBSPACE_PATH="${WEBSPACE_PATH:-~/public_html/curriculum-syp3}"

PYTHON="${PYTHON:-python3}"
