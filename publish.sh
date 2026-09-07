#!/usr/bin/env bash
# Rollt die gebaute Site zusaetzlich auf den Schulwebspace aus.
#
# Bewusst lokal und manuell: Zugangsdaten fuer fremde Infrastruktur gehoeren
# nicht in die Automatisierung. Der Zugang haengt am SSH-Schluessel des
# Ausfuehrenden.
#
#   ./publish.sh            baut und rollt aus
#   ./publish.sh --dry-run  zeigt nur, was uebertragen wuerde
#
set -euo pipefail
cd "$(dirname "$0")"
source ./config.sh

DRY_RUN=()
[[ "${1:-}" == "--dry-run" ]] && DRY_RUN=(--dry-run)

[[ -f "${SITE_DIR}/index.html" ]] || ./local-convert.sh

echo "==> rsync nach ${WEBSPACE_USER}@${WEBSPACE_HOST}:${WEBSPACE_PATH}"
rsync -avz --delete "${DRY_RUN[@]}" \
  "${SITE_DIR}/" \
  "${WEBSPACE_USER}@${WEBSPACE_HOST}:${WEBSPACE_PATH}/"

echo "==> Die bestehende Hugo-Site liegt daneben und bleibt unberuehrt."
