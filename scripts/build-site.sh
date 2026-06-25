#!/usr/bin/env bash
# build-site.sh — refresh the landing site assets in docs/:
#   - the downloadable PDF (manuale_produzione.pdf)
#   - the social share image (og-image.png)
#   - the cover thumbnail (cover.png)
# Run from anywhere; paths are resolved from the repo root.
set -euo pipefail
cd "$(dirname "$0")/.."

python3 scripts/build-elegant.py docs/manuale_produzione.pdf
python3 scripts/make-og.py
cp risorse/copertina.png docs/cover.png

echo "Sito aggiornato in docs/ (PDF, og-image, copertina)."
