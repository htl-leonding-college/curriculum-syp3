#!/usr/bin/env bash
# Rollt die gebaute Site zusätzlich auf den Schulwebspace aus.
#
# Bewusst lokal und manuell: Zugangsdaten für fremde Infrastruktur gehören
# nicht in die Automatisierung. Der Zugang hängt am SSH-Schlüssel des
# Ausführenden.
#
#   ./publish.sh            baut und rollt aus
#   ./publish.sh --dry-run  zeigt nur, was übertragen würde
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

echo "==> Die bestehende Hugo-Site liegt daneben und bleibt unberührt."
