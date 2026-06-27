#!/usr/bin/env python3
# make-og.py — render the social share images (1200x630) in the Claude.ai
# style. Benefit-led: the promise leads, the cover is a small brand cue.
# Produces docs/og-image.png (Italian) and docs/og-image-en.png (English).
# Run from the repo root:  python3 scripts/make-og.py
import base64
import math
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
    COVER_B64 = base64.b64encode(fh.read()).decode()


# -----------------------------------------------------------------------------------------------------------------
#  helpers
# -----------------------------------------------------------------------------------------------------------------
def _asterisk(cx, cy, r, stroke):
    # eight-armed coral mark, like the cover
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


def _claim(lines, size):
    # stacked claim lines (the hook), left aligned
    y = 250
    out = []
    for ln in lines:
        out.append(f'<text x="86" y="{y}" font-size="{size}" fill="{INK}" '
                   f'font-weight="600">{ln}</text>')
        y += int(size * 1.06)
    return "".join(out), y


def _svg(kicker, claim_lines, claim_size, subline, badge):
    claim, y_end = _claim(claim_lines, claim_size)
    rule_y = y_end - claim_size + 22
    badge_w = 24 + len(badge) * 12
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="630"
  viewBox="0 0 1200 630" font-family="Lora, Georgia, serif">
  <rect width="1200" height="630" fill="{CREAM}"/>
  <rect x="16" y="16" width="1168" height="598" rx="20" fill="none"
    stroke="{BORDER}" stroke-width="2"/>

  <!-- cover thumbnail, right -->
  <g transform="translate(872,116)">
    <rect x="6" y="10" width="252" height="358" rx="9" fill="#00000022"/>
    <image x="0" y="0" width="252" height="358"
      href="data:image/png;base64,{COVER_B64}"
      preserveAspectRatio="xMidYMid slice"/>
    <rect x="0" y="0" width="252" height="358" rx="9" fill="none"
      stroke="{BORDER}" stroke-width="2"/>
  </g>

  <!-- mark + kicker -->
  {_asterisk(104, 116, 24, CORAL)}
  <text x="142" y="124" font-family="Inter, Arial, sans-serif"
    font-size="21" letter-spacing="5" fill="{CORAL2}"
    font-weight="700">{kicker}</text>

  <!-- claim (the hook) -->
  {claim}
  <line x1="90" y1="{rule_y}" x2="250" y2="{rule_y}" stroke="{CORAL}"
    stroke-width="5"/>

  <!-- subline -->
  <text x="90" y="{rule_y + 52}" font-family="Inter, Arial, sans-serif"
    font-size="25" fill="{MUTED}">{subline}</text>

  <!-- badge -->
  <rect x="90" y="540" width="{badge_w}" height="46" rx="23" fill="{CORAL}"/>
  <text x="{90 + badge_w / 2:.0f}" y="570" font-family="Inter, Arial, sans-serif"
    font-size="20" fill="#FFFFFF" text-anchor="middle"
    font-weight="700">{badge}</text>
</svg>'''


# -----------------------------------------------------------------------------------------------------------------
#  build
# -----------------------------------------------------------------------------------------------------------------
def build():
    os.makedirs("docs", exist_ok=True)

    it = _svg(
        kicker="MANUALE OPERATIVO",
        claim_lines=["Il manuale su Claude", "che si aggiorna", "con Claude."],
        claim_size=72,
        subline="Pratico, in italiano · Code, Cowork, Skills, API",
        badge="PDF gratis · 33 capitoli · A5")
    cairosvg.svg2png(bytestring=it.encode(), write_to="docs/og-image.png",
                     output_width=1200, output_height=630)

    en = _svg(
        kicker="OPERATIONAL HANDBOOK",
        claim_lines=["The Claude manual", "that updates when", "Claude does."],
        claim_size=66,
        subline="Practical · Code, Cowork, Skills, API",
        badge="Read free online · 33 chapters")
    cairosvg.svg2png(bytestring=en.encode(), write_to="docs/og-image-en.png",
                     output_width=1200, output_height=630)

    print("Creato docs/og-image.png e docs/og-image-en.png (1200x630)")


if __name__ == "__main__":
    build()
