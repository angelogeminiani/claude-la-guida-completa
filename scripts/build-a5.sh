#!/usr/bin/env bash
# build-a5.sh — build the manual as an A5 PDF with Pandoc + XeLaTeX.
# Requires: pandoc, a LaTeX engine (xelatex), and mermaid-filter for diagrams.
# Usage: bash scripts/build-a5.sh

set -euo pipefail

OUT="manuale.pdf"

# Explicit reading order: front matter -> levels 1-6 -> closing.
# Alphabetical globbing would wrongly place C-* (Chiusura) before F-*.
CHAPTERS=(
  capitoli/F-1-prefazione.md
  capitoli/F-2-ecosistema.md
  capitoli/F-3-modelli-e-piani.md
  capitoli/F-4-percorsi-di-lettura.md
  capitoli/L1-1-primo-contatto.md
  capitoli/L1-2-conversare-bene.md
  capitoli/L1-3-impostazioni-e-stili.md
  capitoli/L2-1-installare-desktop.md
  capitoli/L2-2-installare-code.md
  capitoli/L2-3-autenticazione.md
  capitoli/L2-4-configurare-progetto.md
  capitoli/L3-1-cowork-primi-passi.md
  capitoli/L3-2-projects.md
  capitoli/L3-3-connettori.md
  capitoli/L3-4-documenti.md
  capitoli/L3-5-slide-ed-excel.md
  capitoli/L4-1-design-il-canvas.md
  capitoli/L4-2-design-system-import.md
  capitoli/L4-3-da-design-a-codice.md
  capitoli/L4-4-design-dentro-cowork.md
  capitoli/L4-5-export-e-canva.md
  capitoli/L5-1-anatomia-di-una-skill.md
  capitoli/L5-2-la-tua-prima-skill.md
  capitoli/L5-3-skills-operative-in-cowork.md
  capitoli/L5-4-far-suonare-claude-come-te.md
  capitoli/L6-1-claude-code-avanzato.md
  capitoli/L6-2-mcp-custom.md
  capitoli/L6-3-automazioni-controllo-remoto.md
  capitoli/L6-4-gestire-i-limiti-uso.md
  capitoli/L6-5-claude-al-lavoro-sicuro.md
  capitoli/L6-6-integrare-via-api.md
  capitoli/C-1-progetto-end-to-end.md
  capitoli/C-2-appendici.md
)

# Safety check: warn if a chapter file exists but is not in the list above.
listed=${#CHAPTERS[@]}
found=$(ls capitoli/*.md 2>/dev/null | wc -l | tr -d ' ')
if [ "$listed" != "$found" ]; then
  echo "Attenzione: $found file in capitoli/ ma $listed in lista."
  echo "Aggiorna l'array CHAPTERS in scripts/build-a5.sh."
fi

# mermaid-filter renders ```mermaid blocks to images at build time.
# install once: npm install -g mermaid-filter
FILTER=()
if command -v mermaid-filter >/dev/null 2>&1; then
  FILTER=(-F mermaid-filter)
else
  echo "Nota: mermaid-filter non trovato: i diagrammi resteranno come codice."
  echo "Installa con: npm install -g mermaid-filter"
fi

# Cover: if risorse/copertina.png exists, put it full-bleed as page 1
# (replacing the default title page). Otherwise fall back to a text title page.
COVER=()
TITLE=(-M title="Claude: la guida completa"
       -M author="Gian Angelo Geminiani")
if [ -f risorse/copertina.png ]; then
  COVER=(--include-before-body=scripts/a5-cover.tex)
  TITLE=()  # the cover carries the title
else
  echo "Nota: risorse/copertina.png non trovata: uso la pagina-titolo testuale."
fi

# Colophon (legal page) right after the cover, not in the TOC.
COLO=()
if [ -f colophon.md ]; then
  COLTEX="$(mktemp).tex"
  {
    echo '\clearpage\begingroup\thispagestyle{empty}\footnotesize'
    echo '\textbf{\large Note legali}\par\medskip'
    tail -n +2 colophon.md | pandoc -f markdown -t latex
    echo '\endgroup\clearpage'
  } > "$COLTEX"
  COLO=(--include-before-body="$COLTEX")
fi

pandoc "${CHAPTERS[@]}" \
  "${FILTER[@]}" \
  -o "$OUT" \
  --pdf-engine=xelatex \
  --resource-path=.:risorse \
  --toc \
  -H scripts/a5-header.tex \
  "${COVER[@]}" \
  "${COLO[@]}" \
  "${TITLE[@]}" \
  -M lang=it \
  -V documentclass=scrbook \
  -V papersize=a5 \
  -V geometry:bindingoffset=8mm \
  -V geometry:margin=14mm \
  -V mainfont="Lora" \
  -V monofont="Noto Sans Mono"

# Note: mainfont "Lora" matches the elegant Claude.ai style and is a Google
# Font; install it if missing (or change to a serif you have). The header
# scripts/a5-header.tex maps arrows/symbols missing from many serif fonts.

echo "Creato $OUT (formato A5)."
