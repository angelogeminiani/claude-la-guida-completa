#!/usr/bin/env python3
# build-elegant.py — build the manual as an elegant A5 PDF in the Claude.ai
# style (cream background, coral accents, Lora titles) via HTML/CSS -> WeasyPrint.
# Diagrams are rendered to on-brand SVG by mermaid2svg.py. Bilingual.
#
# Usage:
#   python3 scripts/build-elegant.py                      -> IT, manuale_produzione.pdf
#   python3 scripts/build-elegant.py out.pdf              -> IT, out.pdf (back-compat)
#   python3 scripts/build-elegant.py it [out.pdf]         -> Italian edition
#   python3 scripts/build-elegant.py en [out.pdf]         -> English edition
# Run from the repo root (git-repo/).
import os
import re
import sys
import subprocess
import importlib.util

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

# -----------------------------------------------------------------------------------------------------------------
#  structure — (italian part name, english part name, [stems])
# -----------------------------------------------------------------------------------------------------------------
STRUCTURE = [
    ("Front matter", "Front matter", [
        "F-1-prefazione", "F-2-ecosistema", "F-3-modelli-e-piani",
        "F-4-percorsi-di-lettura"]),
    ("Livello 1 — Fondamenti", "Level 1 — Foundations", [
        "L1-1-primo-contatto", "L1-2-conversare-bene",
        "L1-3-impostazioni-e-stili"]),
    ("Livello 2 — Installazione locale", "Level 2 — Local installation", [
        "L2-1-installare-desktop", "L2-2-installare-code",
        "L2-3-autenticazione", "L2-4-configurare-progetto"]),
    ("Livello 3 — Lavoro quotidiano", "Level 3 — Daily work", [
        "L3-1-cowork-primi-passi", "L3-2-projects", "L3-3-connettori",
        "L3-4-documenti", "L3-5-slide-ed-excel"]),
    ("Livello 4 — Design", "Level 4 — Design", [
        "L4-1-design-il-canvas", "L4-2-design-system-import",
        "L4-3-da-design-a-codice", "L4-4-design-dentro-cowork",
        "L4-5-export-e-canva"]),
    ("Livello 5 — Skills e identità", "Level 5 — Skills and identity", [
        "L5-1-anatomia-di-una-skill", "L5-2-la-tua-prima-skill",
        "L5-3-skills-operative-in-cowork", "L5-4-far-suonare-claude-come-te"]),
    ("Livello 6 — Avanzato", "Level 6 — Advanced", [
        "L6-1-claude-code-avanzato", "L6-2-mcp-custom",
        "L6-3-automazioni-controllo-remoto", "L6-4-gestire-i-limiti-uso",
        "L6-5-claude-al-lavoro-sicuro", "L6-6-integrare-via-api"]),
    ("Chiusura", "Closing", ["C-1-progetto-end-to-end", "C-2-appendici"]),
]

LANGS = {
    "it": {"src": "capitoli", "cover": "risorse/copertina.png",
           "colophon": "colophon.md", "toc": "Indice", "part_idx": 0,
           "keep_tags_stem": "F-1-prefazione", "default_out": "manuale_produzione.pdf"},
    "en": {"src": "capitoli-en", "cover": "risorse/copertina-en.png",
           "colophon": "colophon-en.md", "toc": "Contents", "part_idx": 1,
           "keep_tags_stem": "F-1-prefazione", "default_out": "docs/en/manuale_en.pdf"},
}

# -----------------------------------------------------------------------------------------------------------------
#  helpers
# -----------------------------------------------------------------------------------------------------------------
_spec = importlib.util.spec_from_file_location(
    "mermaid2svg", os.path.join(ROOT, "scripts", "mermaid2svg.py"))
_m2s = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_m2s)


def _embed_diagrams(md):
    def repl(match):
        return '\n<div class="fig">' + _m2s.render(match.group(1)) + "</div>\n"
    return re.sub(r"```mermaid\n(.*?)```", repl, md, flags=re.S)


def _strip_heading_tags(md):
    return re.sub(
        r"^(#{1,6}\s+.*?)\s*\((?:VOLATILE|EVERGREEN)\)\s*$", r"\1", md,
        flags=re.M)


def _strip_inline_tags(md):
    return re.sub(r"\s*\((?:VOLATILE|EVERGREEN)\)", "", md)


def _title_of(md):
    m = re.search(r"^#\s+(.*)$", md, re.M)
    return m.group(1).strip() if m else "?"


def _md_to_html(md, strip_inline=False):
    md = _strip_heading_tags(md)
    if strip_inline:
        md = _strip_inline_tags(md)
    md = _embed_diagrams(md)
    p = subprocess.run(["pandoc", "-f", "markdown", "-t", "html5"],
                       input=md, capture_output=True, text=True)
    if p.returncode != 0:
        sys.stderr.write(p.stderr)
        raise SystemExit("pandoc error")
    return p.stdout


# -----------------------------------------------------------------------------------------------------------------
#  assemble
# -----------------------------------------------------------------------------------------------------------------
def build(lang, out_pdf):
    cfg = LANGS[lang]
    css = open("scripts/style-claude.css").read()
    chapters_html = []
    toc_rows = []
    for part in STRUCTURE:
        part_name, stems = part[cfg["part_idx"]], part[2]
        toc_rows.append('<li class="part">' + part_name + "</li>")
        for stem in stems:
            path = os.path.join(cfg["src"], stem + ".md")
            md = open(path).read()
            title = _title_of(md)
            # F.1 explains the tags, so it keeps them; every other chapter has
            # them stripped from the body for a cleaner read.
            html = _md_to_html(md, strip_inline=(stem != cfg["keep_tags_stem"]))
            chapters_html.append(
                '<section class="chapter" id="%s">\n%s\n</section>' %
                (stem, html))
            toc_rows.append('<li><a href="#%s">%s</a></li>' % (stem, title))

    cover = ""
    if os.path.exists(cfg["cover"]):
        cover = ('<section class="cover"><img src="%s" alt="Cover"></section>'
                 % cfg["cover"])

    colophon = ""
    if os.path.exists(cfg["colophon"]):
        colophon = ('<section class="colophon">' +
                    _md_to_html(open(cfg["colophon"]).read()) + "</section>")

    toc = ('<section class="toc"><h1>%s</h1><ul>' % cfg["toc"] +
           "\n".join(toc_rows) + "</ul></section>")

    doc = (
        "<!DOCTYPE html><html lang=\"%s\"><head><meta charset=\"utf-8\">"
        "<style>" % lang + css + "</style></head><body>" +
        cover + colophon + toc +
        '<div class="book">' + "\n".join(chapters_html) + "</div>"
        "</body></html>")

    out_dir = os.path.dirname(out_pdf)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    from weasyprint import HTML
    HTML(string=doc, base_url=ROOT).write_pdf(out_pdf)
    print("Creato", out_pdf)


# -----------------------------------------------------------------------------------------------------------------
#  cli
# -----------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    args = sys.argv[1:]
    if not args:
        build("it", LANGS["it"]["default_out"])
    elif args[0].endswith(".pdf"):                       # back-compat: IT path
        build("it", args[0])
    elif args[0] in LANGS:
        out = args[1] if len(args) > 1 else LANGS[args[0]]["default_out"]
        build(args[0], out)
    else:
        raise SystemExit("usage: build-elegant.py [it|en|out.pdf] [out.pdf]")
