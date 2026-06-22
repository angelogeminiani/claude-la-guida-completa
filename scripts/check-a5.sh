#!/usr/bin/env bash
# check-a5.sh — flags CODE lines wider than the A5 limit.
# Skips mermaid blocks (rendered) and prose (reflows when typeset).
# Usage: bash scripts/check-a5.sh

set -euo pipefail

MAX=56
DIR="${1:-capitoli}"

found=$(awk -v max="$MAX" '
  /^```mermaid/ {inblock=1; mer=1; next}
  /^```/ {
    if (inblock) {inblock=0; mer=0}
    else {inblock=1; mer=0}
    next
  }
  inblock && !mer && length($0)>max {
    printf "%s:%d (%d) %s\n",FILENAME,NR,length($0),$0
  }
' "$DIR"/*.md 2>/dev/null || true)

if [ -n "$found" ]; then
  echo "Righe di codice oltre $MAX caratteri:"
  echo "$found"
  exit 1
else
  echo "OK: nessuna riga di codice oltre $MAX caratteri in $DIR/"
fi
