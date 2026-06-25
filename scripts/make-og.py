#!/usr/bin/env python3
# make-og.py — render the social share image (og-image.png, 1200x630) in the
# Claude.ai style, embedding a thumbnail of the cover. Run from the repo root.
#   python3 scripts/make-og.py
import base64
import os
import cairosvg

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

CREAM = "#FAF9F5"
INK = "#1F1E1D"
CORAL = "#D97757"
CORAL2 = "#B65A3C"
MUTED = "#6B6760"
BORDER = "#E5DED2"

with open("risorse/copertina.png", "rb") as fh:
    cover_b64 = base64.b64encode(fh.read()).decode()


def _asterisk(cx, cy, r, stroke):
    # eight-armed coral mark, similar to the cover
    import math
    lines = []
    for i in range(8):
        a = math.radians(i * 45)
        x1 = cx + math.cos(a) * r * 0.32
        y1 = cy + math.sin(a) * r * 0.32
        x2 = cx + math.cos(a) * r
        y2 = cy + math.sin(a) * r
        lines.append(
            f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" '
            f'stroke="{stroke}" stroke-width="7" stroke-linecap="round"/>')
    return "".join(lines)


svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="630"
  viewBox="0 0 1200 630" font-family="Lora, Georgia, serif">
  <rect width="1200" height="630" fill="{CREAM}"/>
  <rect x="16" y="16" width="1168" height="598" rx="20" fill="none"
    stroke="{BORDER}" stroke-width="2"/>

  <!-- cover thumbnail, right -->
  <g transform="translate(792,86)">
    <rect x="6" y="10" width="322" height="458" rx="10" fill="#00000022"/>
    <image x="0" y="0" width="322" height="458" rx="10"
      href="data:image/png;base64,{cover_b64}"
      preserveAspectRatio="xMidYMid slice"/>
    <rect x="0" y="0" width="322" height="458" rx="10" fill="none"
      stroke="{BORDER}" stroke-width="2"/>
  </g>

  <!-- mark + kicker -->
  {_asterisk(110, 132, 26, CORAL)}
  <text x="150" y="124" font-family="Inter, Arial, sans-serif"
    font-size="22" letter-spacing="5" fill="{CORAL2}"
    font-weight="700">MANUALE OPERATIVO</text>

  <!-- title -->
  <text x="86" y="290" font-size="150" fill="{INK}"
    font-weight="600">Claude</text>
  <line x1="92" y1="330" x2="232" y2="330" stroke="{CORAL}"
    stroke-width="5"/>
  <text x="86" y="398" font-size="60" fill="{INK}"
    font-style="italic">la guida completa</text>

  <!-- subtitle -->
  <text x="88" y="470" font-family="Inter, Arial, sans-serif"
    font-size="27" fill="{MUTED}">Dal primo prompt all'automazione:</text>
  <text x="88" y="506" font-family="Inter, Arial, sans-serif"
    font-size="27" fill="{MUTED}">Claude Code, Cowork, Design, Skills e API.</text>

  <!-- badge -->
  <rect x="88" y="540" width="408" height="46" rx="23" fill="{CORAL}"/>
  <text x="292" y="570" font-family="Inter, Arial, sans-serif"
    font-size="20" fill="#FFFFFF" text-anchor="middle"
    font-weight="700">PDF gratuito · A5 · 152 pagine</text>
</svg>'''

os.makedirs("docs", exist_ok=True)
cairosvg.svg2png(bytestring=svg.encode(), write_to="docs/og-image.png",
                 output_width=1200, output_height=630)
print("Creato docs/og-image.png (1200x630)")
