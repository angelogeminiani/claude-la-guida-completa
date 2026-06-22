#!/usr/bin/env bash
# build-a5.sh — build the manual as an A5 PDF with Pandoc + XeLaTeX.
# Requires: pandoc, a LaTeX engine (xelatex), and mermaid-filter for diagrams.
# Usage: bash scripts/build-a5.sh

set -euo pipefail

OUT="manuale.pdf"

# order chapters explicitly if needed; default = alphabetical in capitoli/
CHAPTERS=(capitoli/*.md)

# mermaid-filter renders ```mermaid blocks to images at build time.
# install once: npm install -g mermaid-filter
FILTER=()
if command -v mermaid-filter >/dev/null 2>&1; then
  FILTER=(-F mermaid-filter)
else
  echo "Nota: mermaid-filter non trovato: i diagrammi resteranno come codice."
  echo "Installa con: npm install -g mermaid-filter"
fi

pandoc "${CHAPTERS[@]}" \
  "${FILTER[@]}" \
  -o "$OUT" \
  --pdf-engine=xelatex \
  --toc \
  -V documentclass=scrbook \
  -V papersize=a5 \
  -V geometry:bindingoffset=8mm \
  -V geometry:margin=14mm \
  -V mainfont="Noto Serif" \
  -V monofont="Noto Sans Mono"

echo "Creato $OUT (formato A5)."
