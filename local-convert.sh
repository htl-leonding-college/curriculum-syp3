#!/usr/bin/env bash
# Baut die Site lokal — derselbe Ablauf wie in der Pipeline.
#
#   ./local-convert.sh              prüfen, erzeugen, konvertieren
#   ./local-convert.sh --skip-check nur bauen (während des Schreibens)
#
set -euo pipefail
cd "$(dirname "$0")"
source ./config.sh

SKIP_CHECK=0
[[ "${1:-}" == "--skip-check" ]] && SKIP_CHECK=1

if [[ "${SKIP_CHECK}" -eq 0 ]]; then
  echo "==> Prüfung"
  "${PYTHON}" tools/check-curriculum.py
fi

echo "==> Generatoren"
for generator in gen-mindmap gen-nav gen-ue-overview gen-questions; do
  "${PYTHON}" "tools/${generator}.py" >/dev/null
done

echo "==> Quellen sammeln"
rm -rf "${SITE_DIR}"
mkdir -p "${SITE_DIR}"
cp site/index.adoc "${SITE_DIR}/index.adoc"
cp "${BUILD_DIR}"/nav.adoc "${BUILD_DIR}"/ue-overview.adoc "${BUILD_DIR}"/stoffstruktur.puml "${SITE_DIR}/"
mkdir -p "${SITE_DIR}/questions"
cp "${BUILD_DIR}"/questions/* "${SITE_DIR}/questions/"
# Nur fertige Module gehen auf die Site — ein Skelett mit TODO-Platzhaltern
# hat dort nichts verloren (status: ready in curriculum.yaml).
mkdir -p "${SITE_DIR}/modules"
while IFS= read -r topic; do
  [[ -d "modules/${topic}" ]] && cp -R "modules/${topic}" "${SITE_DIR}/modules/${topic}"
done < <("${PYTHON}" tools/curriculum.py ready)

echo "==> asciidoctor (${ASCIIDOCTOR_IMAGE})"
docker run --rm -u "$(id -u):$(id -g)" -e HOME=/tmp -v "${PWD}:/documents" -w /documents \
  "${ASCIIDOCTOR_IMAGE}" \
  asciidoctor -r asciidoctor-diagram --failure-level=WARN \
    -a toc=left -a icons=font -a source-highlighter=rouge \
    -a imagesdir@=images \
    "${SITE_DIR}/index.adoc" "${SITE_DIR}"/questions/index.adoc \
    $(find "${SITE_DIR}/modules" -name '*.adoc' 2>/dev/null | tr '\n' ' ')

echo "==> Präsentationen (revealjs)"
mkdir -p "${SITE_DIR}/slides"
while IFS= read -r module; do
  [[ -z "${module}" ]] && continue
  topic="$(basename "$(dirname "${module}")")"
  docker run --rm -u "$(id -u):$(id -g)" -e HOME=/tmp -v "${PWD}:/documents" -w /documents \
    "${ASCIIDOCTOR_IMAGE}" \
    asciidoctor-revealjs -r asciidoctor-diagram \
      -a revealjsdir=https://cdn.jsdelivr.net/npm/reveal.js@5.1.0 \
      -o "${SITE_DIR}/slides/${topic}.html" "${module}"
done < <(find "${SITE_DIR}/modules" -name 'index.adoc' 2>/dev/null)

echo "==> fertig: ${SITE_DIR}/index.html"
