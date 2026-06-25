#!/usr/bin/env python3
# build-elegant.py — build the manual as an elegant A5 PDF in the Claude.ai
# style (cream background, coral accents, Lora titles) via HTML/CSS -> WeasyPrint.
# Diagrams are rendered to on-brand SVG by mermaid2svg.py.
#
# Usage:  python3 scripts/build-elegant.py [output.pdf]
# Run from the repo root (git-repo/).
import os
import re
import sys
import subprocess
import importlib.util

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

# -----------------------------------------------------------------------------------------------------------------
#  chapter order (front matter -> levels 1-6 -> closing)
# -----------------------------------------------------------------------------------------------------------------
PARTS = [
    ("Front matter", [
        "F-1-prefazione", "F-2-ecosistema", "F-3-modelli-e-piani",
        "F-4-percorsi-di-lettura"]),
    ("Livello 1 — Fondamenti", [
        "L1-1-primo-contatto", "L1-2-conversare-bene",
        "L1-3-impostazioni-e-stili"]),
    ("Livello 2 — Installazione locale", [
        "L2-1-installare-desktop", "L2-2-installare-code",
        "L2-3-autenticazione", "L2-4-configurare-progetto"]),
    ("Livello 3 — Lavoro quotidiano", [
        "L3-1-cowork-primi-passi", "L3-2-projects", "L3-3-connettori",
        "L3-4-documenti", "L3-5-slide-ed-excel"]),
    ("Livello 4 — Design", [
        "L4-1-design-il-canvas", "L4-2-design-system-import",
        "L4-3-da-design-a-codice", "L4-4-design-dentro-cowork",
        "L4-5-export-e-canva"]),
    ("Livello 5 — Skills e identità", [
        "L5-1-anatomia-di-una-skill", "L5-2-la-tua-prima-skill",
        "L5-3-skills-operative-in-cowork", "L5-4-far-suonare-claude-come-te"]),
    ("Livello 6 — Avanzato", [
        "L6-1-claude-code-avanzato", "L6-2-mcp-custom",
        "L6-3-automazioni-controllo-remoto", "L6-4-gestire-i-limiti-uso",
        "L6-5-claude-al-lavoro-sicuro", "L6-6-integrare-via-api"]),
    ("Chiusura", ["C-1-progetto-end-to-end", "C-2-appendici"]),
]

# -----------------------------------------------------------------------------------------------------------------
#  helpers
# -----------------------------------------------------------------------------------------------------------------
_spec = importlib.util.spec_from_file_location(
    "mermaid2svg", os.path.join(ROOT, "scripts", "mermaid2svg.py"))
_m2s = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_m2s)


def _embed_diagrams(md):
    def repl(match):
        svg = _m2s.render(match.group(1))
        return '\n<div class="fig">' + svg + "</div>\n"
    return re.sub(r"```mermaid\n(.*?)```", repl, md, flags=re.S)


def _strip_heading_tags(md):
    # Remove the (VOLATILE)/(EVERGREEN) status tags from headings only, for a
    # cleaner reading experience. Source files keep them; inline body tags stay
    # (F.1 explains what they mean).
    return re.sub(
        r"^(#{1,6}\s+.*?)\s*\((?:VOLATILE|EVERGREEN)\)\s*$",
        r"\1", md, flags=re.M)


def _title_of(md):
    m = re.search(r"^#\s+(.*)$", md, re.M)
    return m.group(1).strip() if m else "?"


def _md_to_html(md):
    md = _strip_heading_tags(md)
    md = _embed_diagrams(md)
    p = subprocess.run(
        ["pandoc", "-f", "markdown", "-t", "html5"],
        input=md, capture_output=True, text=True)
    if p.returncode != 0:
        sys.stderr.write(p.stderr)
        raise SystemExit("pandoc error")
    return p.stdout


# -----------------------------------------------------------------------------------------------------------------
#  assemble
# -----------------------------------------------------------------------------------------------------------------
def build(out_pdf):
    css = open("scripts/style-claude.css").read()
    chapters_html = []
    toc_rows = []
    for part, stems in PARTS:
        toc_rows.append('<li class="part">' + part + "</li>")
        for stem in stems:
            path = os.path.join("capitoli", stem + ".md")
            md = open(path).read()
            title = _title_of(md)
            html = _md_to_html(md)
            chapters_html.append(
                '<section class="chapter" id="%s">\n%s\n</section>' %
                (stem, html))
            toc_rows.append(
                '<li><a href="#%s">%s</a></li>' % (stem, title))

    cover = ""
    if os.path.exists("risorse/copertina.png"):
        cover = ('<section class="cover">'
                 '<img src="risorse/copertina.png" alt="Copertina"></section>')

    toc = ('<section class="toc"><h1>Indice</h1><ul>' +
           "\n".join(toc_rows) + "</ul></section>")

    doc = (
        "<!DOCTYPE html><html lang=\"it\"><head><meta charset=\"utf-8\">"
        "<style>" + css + "</style></head><body>" +
        cover + toc +
        '<div class="book">' + "\n".join(chapters_html) + "</div>"
        "</body></html>")

    from weasyprint import HTML
    HTML(string=doc, base_url=ROOT).write_pdf(out_pdf)
    print("Creato", out_pdf)


if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else "manuale-elegante.pdf"
    build(out)
