#!/usr/bin/env bash
# build-site.sh — rebuild the whole site (Italian + English) in docs/:
#   - chapter pages, reading indexes, sitemap, robots (build-pages.py)
#   - changelog pages + RSS feed (build-updates.py)
#   - social share images (make-og.py)
#   - English landing (build-en.py)
#   - downloadable A5 PDFs, IT and EN (build-elegant.py)
#   - cover thumbnail for the landing
# Run from anywhere; paths are resolved from the repo root.
set -euo pipefail
cd "$(dirname "$0")/.."

# covers: (re)render the English cover PNG from its SVG so it stays in sync
python3 -c "import cairosvg; cairosvg.svg2png(url='risorse/copertina-en.svg', write_to='risorse/copertina-en.png', output_width=1748, output_height=2480)"

# PDFs
python3 scripts/build-elegant.py docs/claude-la-guida-completa.pdf   # Italian
python3 scripts/build-elegant.py en docs/en/claude-the-complete-guide.pdf     # English

# HTML site
python3 scripts/build-pages.py
python3 scripts/build-updates.py
python3 scripts/make-og.py
python3 scripts/build-en.py

# landing cover thumbnail
cp risorse/copertina.png docs/cover.png
cp risorse/copertina-en.png docs/en/cover-en.png

echo "Sito aggiornato in docs/ (IT+EN: PDF, capitoli, changelog, RSS, OG, cover)."
