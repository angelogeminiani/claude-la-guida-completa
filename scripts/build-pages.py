#!/usr/bin/env python3
# build-pages.py — generate the online, SEO-friendly HTML edition of the book,
# in BOTH languages:
#   Italian  -> docs/capitoli/<stem>.html, docs/leggi.html
#   English  -> docs/en/capitoli/<stem>.html, docs/en/leggi.html
# plus docs/sitemap.xml and docs/robots.txt (both languages), with reciprocal
# hreflang and a per-page language switch. Shared look via the inlined book.css
# (so pages render even in isolated previews). Mermaid diagrams are rendered to
# on-brand inline SVG by mermaid2svg.py.
#
# Usage:  python3 scripts/build-pages.py     (run from the repo root)
import os
import re
import sys
import html
import importlib.util
import subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

BASE = "https://angelogeminiani.github.io/claude-la-guida-completa/"
TODAY = "2026-06-27"

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

ALL_STEMS = [s for _, _, stems in STRUCTURE for s in stems]

# -----------------------------------------------------------------------------------------------------------------
#  per-language configuration
# -----------------------------------------------------------------------------------------------------------------
LANGS = {
    "it": {
        "lang": "it", "src": "capitoli", "outdir": "docs", "part_idx": 0,
        "pdf": "claude-la-guida-completa.pdf",
        "brand": "Claude · la guida completa",
        "nav_read": "Leggi online", "nav_pdf": "Scarica il PDF →",
        "other_label": "EN",
        "crumb_home": "Home", "crumb_read": "Leggi online",
        "prev": "Precedente", "next": "Successivo",
        "cta_h": "Ti è utile? Prendi tutto il manuale",
        "cta_p": "33 capitoli in un unico PDF A5, gratis e senza registrazione.",
        "cta_btn": "↓ Scarica il PDF gratis",
        "leggi_title": "Leggi online — Claude: la guida completa",
        "leggi_desc": ("Leggi gratis online tutti i 33 capitoli del manuale "
                       "italiano sull'ecosistema Claude: chat, Claude Code, "
                       "Cowork, Design, Skills e API."),
        "leggi_h1": "Leggi online",
        "leggi_lead": ("Tutti i 33 capitoli, gratis. Preferisci la versione "
                       "completa? <a href=\"%s\" download>Scarica il PDF A5</a>."),
        "footer": ("© 2026 Gian Angelo Geminiani. Pubblicazione <strong>"
                   "indipendente e non ufficiale</strong>: non affiliata, "
                   "sponsorizzata né approvata da Anthropic. «Claude» e "
                   "«Anthropic» sono marchi dei rispettivi titolari, citati a "
                   "solo scopo identificativo. Dati verificati alla data "
                   "indicata e soggetti a modifica."),
    },
    "en": {
        "lang": "en", "src": "capitoli-en", "outdir": "docs/en", "part_idx": 1,
        "pdf": "claude-the-complete-guide.pdf",
        "brand": "Claude · the complete guide",
        "nav_read": "Read online", "nav_pdf": "Download the PDF →",
        "other_label": "IT",
        "crumb_home": "Home", "crumb_read": "Read online",
        "prev": "Previous", "next": "Next",
        "cta_h": "Found it useful? Get the whole manual",
        "cta_p": "33 chapters in a single A5 PDF, free and no signup.",
        "cta_btn": "↓ Download the free PDF",
        "leggi_title": "Read online — Claude: the complete guide",
        "leggi_desc": ("Read all 33 chapters of the practical guide to the "
                       "Claude ecosystem online, free: chat, Claude Code, "
                       "Cowork, Design, Skills and the API."),
        "leggi_h1": "Read online",
        "leggi_lead": ("All 33 chapters, free. Prefer the full version? "
                       "<a href=\"%s\" download>Download the A5 PDF</a>."),
        "footer": ("© 2026 Gian Angelo Geminiani. An <strong>independent, "
                   "unofficial</strong> publication: not affiliated with, "
                   "sponsored or endorsed by Anthropic. \"Claude\" and "
                   "\"Anthropic\" are trademarks of their respective owners, "
                   "used for identification only. Data verified on the date "
                   "shown and subject to change."),
    },
}

# -----------------------------------------------------------------------------------------------------------------
#  shared markup
# -----------------------------------------------------------------------------------------------------------------
SYMBOLS = (
    '<svg width="0" height="0" style="position:absolute" aria-hidden="true">'
    '<symbol id="ast" viewBox="0 0 32 32">'
    '<g stroke="#D97757" stroke-width="3.4" stroke-linecap="round">'
    '<line x1="16" y1="4" x2="16" y2="28"/><line x1="4" y1="16" x2="28" y2="16"/>'
    '<line x1="7.5" y1="7.5" x2="24.5" y2="24.5"/>'
    '<line x1="24.5" y1="7.5" x2="7.5" y2="24.5"/></g></symbol>'
    '<symbol id="moon" viewBox="0 0 24 24">'
    '<path d="M21 12.8A9 9 0 1 1 11.2 3a7 7 0 0 0 9.8 9.8z" fill="none" '
    'stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/></symbol>'
    '<symbol id="sun" viewBox="0 0 24 24"><g fill="none" stroke="currentColor" '
    'stroke-width="1.8" stroke-linecap="round"><circle cx="12" cy="12" r="4.2"/>'
    '<line x1="12" y1="2.5" x2="12" y2="5"/><line x1="12" y1="19" x2="12" y2="21.5"/>'
    '<line x1="2.5" y1="12" x2="5" y2="12"/><line x1="19" y1="12" x2="21.5" y2="12"/>'
    '<line x1="5.2" y1="5.2" x2="6.9" y2="6.9"/>'
    '<line x1="17.1" y1="17.1" x2="18.8" y2="18.8"/>'
    '<line x1="5.2" y1="18.8" x2="6.9" y2="17.1"/>'
    '<line x1="17.1" y1="6.9" x2="18.8" y2="5.2"/></g></symbol></svg>')

FAVICON = (
    "data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' "
    "viewBox='0 0 32 32'%3E%3Cg stroke='%23D97757' stroke-width='3' "
    "stroke-linecap='round'%3E%3Cline x1='16' y1='5' x2='16' y2='27'/%3E"
    "%3Cline x1='5' y1='16' x2='27' y2='16'/%3E%3Cline x1='8' y1='8' x2='24' "
    "y2='24'/%3E%3Cline x1='24' y1='8' x2='8' y2='24'/%3E%3C/g%3E%3C/svg%3E")

THEME_SCRIPT = (
    "<script>(function(){try{var s=localStorage.getItem('theme');"
    "if(s==='dark'||s==='light')document.documentElement.setAttribute("
    "'data-theme',s);}catch(e){}})();</script>")

TOGGLE_SCRIPT = (
    "<script>(function(){var r=document.documentElement;function eff(){var f="
    "r.getAttribute('data-theme');return f?f:(window.matchMedia("
    "'(prefers-color-scheme: dark)').matches?'dark':'light');}var b="
    "document.getElementById('theme-toggle');if(b)b.addEventListener('click',"
    "function(){var n=eff()==='dark'?'light':'dark';r.setAttribute('data-theme',"
    "n);try{localStorage.setItem('theme',n);}catch(e){}});})();</script>")

_css_cache = None


def _css():
    global _css_cache
    if _css_cache is None:
        _css_cache = "<style>" + open("docs/assets/book.css").read() + "</style>"
    return _css_cache


_spec = importlib.util.spec_from_file_location(
    "mermaid2svg", os.path.join(ROOT, "scripts", "mermaid2svg.py"))
_m2s = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_m2s)


# -----------------------------------------------------------------------------------------------------------------
#  markdown helpers
# -----------------------------------------------------------------------------------------------------------------
def _embed_diagrams(md):
    def repl(match):
        return '\n<div class="fig">' + _m2s.render(match.group(1)) + "</div>\n"
    return re.sub(r"```mermaid\n(.*?)```", repl, md, flags=re.S)


def _strip_tags(md):
    md = re.sub(r"^(#{1,6}\s+.*?)\s*\((?:VOLATILE|EVERGREEN)\)\s*$",
                r"\1", md, flags=re.M)
    return re.sub(r"\s*\((?:VOLATILE|EVERGREEN)\)", "", md)


def _strip_hr(md):
    return re.sub(r"^\s*---\s*$", "", md, flags=re.M)


def _h1(md):
    m = re.search(r"^#\s+(.*)$", md, re.M)
    raw = m.group(1).strip() if m else "?"
    return re.sub(r"^(?:Capitolo|Chapter)\s+", "", raw)


def _chapter_id(title):
    return re.split(r"\s+—\s+", title, 1)[0].strip()


def _description(md):
    m = re.search(r"^##\s+(?:Obiettivo|Goal)\s*\n+(.+?)(?:\n\n|\n#)", md,
                  re.S | re.M)
    if not m:
        body = re.sub(r"^#.*$", "", md, flags=re.M)
        body = re.sub(r"^>.*$", "", body, flags=re.M)
        m = re.search(r"(\S.+?)(?:\n\n|\Z)", body, re.S)
    text = m.group(1) if m else ""
    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"[*`_>#\[\]]", "", text).strip()
    if len(text) > 155:
        text = text[:152].rsplit(" ", 1)[0] + "…"
    return text


def _md_to_html(md):
    md = _strip_hr(_strip_tags(md))
    md = _embed_diagrams(md)
    p = subprocess.run(["pandoc", "-f", "markdown", "-t", "html5"],
                       input=md, capture_output=True, text=True)
    if p.returncode != 0:
        sys.stderr.write(p.stderr)
        raise SystemExit("pandoc error")
    out = p.stdout
    out = out.replace("<table>", '<div class="tablewrap"><table>')
    out = out.replace("</table>", "</table></div>")
    return out


# -----------------------------------------------------------------------------------------------------------------
#  html building blocks
# -----------------------------------------------------------------------------------------------------------------
def _head(lang, title, desc, canonical, it_url, en_url, extra=""):
    esc_t, esc_d = html.escape(title), html.escape(desc)
    og_img = BASE + ("og-image.png" if lang == "it" else "og-image-en.png")
    return (
        '<!DOCTYPE html><html lang="%s"><head><meta charset="utf-8">'
        '<meta name="viewport" content="width=device-width, initial-scale=1">'
        '<title>%s</title><meta name="description" content="%s">'
        '<link rel="canonical" href="%s">'
        '<link rel="alternate" hreflang="it" href="%s">'
        '<link rel="alternate" hreflang="en" href="%s">'
        '<link rel="alternate" hreflang="x-default" href="%s">'
        '<meta name="theme-color" content="#FAF9F5">'
        '<meta name="author" content="Gian Angelo Geminiani">'
        '<meta property="og:type" content="article">'
        '<meta property="og:title" content="%s">'
        '<meta property="og:description" content="%s">'
        '<meta property="og:url" content="%s">'
        '<meta property="og:image" content="%s">'
        '<meta name="twitter:card" content="summary_large_image">'
        '<meta name="twitter:title" content="%s">'
        '<meta name="twitter:image" content="%s">'
        '<link rel="icon" href="%s">'
        '<link rel="preconnect" href="https://fonts.googleapis.com">'
        '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
        '<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;'
        '600;700&family=Lora:ital,wght@0,600;1,500&display=swap" rel="stylesheet">'
        '%s%s%s%s</head><body>%s') % (
            lang, esc_t, esc_d, canonical, it_url, en_url, it_url, esc_t, esc_d,
            canonical, og_img, esc_t, og_img, FAVICON, _css(), extra,
            THEME_SCRIPT, "", SYMBOLS)


def _nav(cfg, root, other_url):
    return (
        '<header class="nav"><div class="row">'
        '<a class="brand" href="%sindex.html"><svg class="mark">'
        '<use href="#ast"/></svg> %s</a><div class="nav-right">'
        '<a class="nav-cta" href="%sleggi.html">%s</a>'
        '<a class="nav-cta" href="%s%s" download>%s</a>'
        '<a class="nav-cta" href="%s">%s</a>'
        '<button class="theme-toggle" id="theme-toggle" type="button" '
        'aria-label="theme" title="Theme">'
        '<svg class="i-moon" aria-hidden="true"><use href="#moon"/></svg>'
        '<svg class="i-sun" aria-hidden="true"><use href="#sun"/></svg>'
        '</button></div></div></header>') % (
            root, cfg["brand"], root, cfg["nav_read"], root, cfg["pdf"],
            cfg["nav_pdf"], other_url, cfg["other_label"])


def _footer(cfg):
    return '<footer><div class="wrap">%s</div></footer>' % cfg["footer"]


# -----------------------------------------------------------------------------------------------------------------
#  page builders
# -----------------------------------------------------------------------------------------------------------------
def _chapter_page(cfg, meta, prev_m, next_m):
    stem = meta["stem"]
    it_url = BASE + "capitoli/%s.html" % stem
    en_url = BASE + "en/capitoli/%s.html" % stem
    canonical = it_url if cfg["lang"] == "it" else en_url
    other_url = ("../en/capitoli/%s.html" % stem if cfg["lang"] == "it"
                 else "../../capitoli/%s.html" % stem)

    jsonld = (
        '<script type="application/ld+json">{"@context":"https://schema.org",'
        '"@type":"TechArticle","headline":%s,"description":%s,"inLanguage":"%s",'
        '"author":{"@type":"Person","name":"Gian Angelo Geminiani"},'
        '"isPartOf":{"@type":"Book","name":"Claude: la guida completa"},'
        '"mainEntityOfPage":%s}</script>') % (
            _json(meta["title"]), _json(meta["desc"]), cfg["lang"],
            _json(canonical))

    head = _head(cfg["lang"], meta["title"] + " · Claude: la guida completa",
                 meta["desc"], canonical, it_url, en_url, extra=jsonld)

    pager = '<nav class="pager">'
    if prev_m:
        pager += ('<a href="./%s.html"><span class="lbl">← %s</span>%s</a>'
                  % (prev_m["stem"], cfg["prev"], html.escape(prev_m["title"])))
    if next_m:
        pager += ('<a class="nxt" href="./%s.html"><span class="lbl">%s →</span>'
                  '%s</a>' % (next_m["stem"], cfg["next"],
                             html.escape(next_m["title"])))
    pager += "</nav>"

    cta = ('<div class="readcta"><h2>%s</h2><p>%s</p>'
           '<a class="btn btn-primary" href="../%s" download>%s</a></div>' % (
               cfg["cta_h"], cfg["cta_p"], cfg["pdf"], cfg["cta_btn"]))

    crumbs = ('<div class="crumbs"><a href="../index.html">%s</a> · '
              '<a href="../leggi.html">%s</a> · %s</div>' % (
                  cfg["crumb_home"], cfg["crumb_read"],
                  html.escape(meta["part"])))

    body = (_nav(cfg, "../", other_url) + '<main class="wrap">' + crumbs +
            '<article>' + meta["html"] + '</article>' + pager + cta +
            '</main>' + _footer(cfg) + TOGGLE_SCRIPT + "</body></html>")
    return head + body


def _leggi_page(cfg, metas):
    it_url, en_url = BASE + "leggi.html", BASE + "en/leggi.html"
    canonical = it_url if cfg["lang"] == "it" else en_url
    other_url = "en/leggi.html" if cfg["lang"] == "it" else "../leggi.html"

    head = _head(cfg["lang"], cfg["leggi_title"], cfg["leggi_desc"],
                 canonical, it_url, en_url)

    parts_html = []
    for part_it, part_en, stems in STRUCTURE:
        part = part_it if cfg["lang"] == "it" else part_en
        rows = []
        for stem in stems:
            m = metas[stem]
            rows.append(
                '<li><a href="capitoli/%s.html"><span class="id">%s</span>'
                '<span>%s</span></a></li>' % (
                    stem, html.escape(m["id"]),
                    html.escape(m["title"].split("—", 1)[-1].strip())))
        parts_html.append('<h2 class="part-h">%s</h2><ul class="toc">%s</ul>'
                          % (html.escape(part), "".join(rows)))

    intro = (
        '<h1 style="font-family:Lora,Georgia,serif;font-size:clamp(30px,5vw,42px);'
        'margin:18px 0 4px">%s</h1><div class="accent"></div>'
        '<p class="lead">%s</p>' % (
            html.escape(cfg["leggi_h1"]), cfg["leggi_lead"] % cfg["pdf"]))

    body = (_nav(cfg, "", other_url) + '<main class="wrap">' + intro +
            "".join(parts_html) + '</main>' + _footer(cfg) + TOGGLE_SCRIPT +
            "</body></html>")
    return head + body


def _json(s):
    import json
    return json.dumps(s, ensure_ascii=False)


def _sitemap():
    urls = [BASE, BASE + "leggi.html", BASE + "changelog.html",
            BASE + "en/", BASE + "en/leggi.html", BASE + "en/changelog.html"]
    urls += [BASE + "capitoli/%s.html" % s for s in ALL_STEMS]
    urls += [BASE + "en/capitoli/%s.html" % s for s in ALL_STEMS]
    items = []
    for u in urls:
        pri = "1.0" if u in (BASE, BASE + "en/") else (
            "0.8" if u.endswith("leggi.html") else "0.6")
        items.append("<url><loc>%s</loc><lastmod>%s</lastmod>"
                     "<priority>%s</priority></url>" % (u, TODAY, pri))
    return ('<?xml version="1.0" encoding="UTF-8"?>\n'
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
            + "\n".join(items) + "\n</urlset>\n")


# -----------------------------------------------------------------------------------------------------------------
#  build
# -----------------------------------------------------------------------------------------------------------------
def _build_lang(cfg):
    metas = {}
    for part_it, part_en, stems in STRUCTURE:
        part = part_it if cfg["lang"] == "it" else part_en
        for stem in stems:
            md = open(os.path.join(cfg["src"], stem + ".md")).read()
            title = _h1(md)
            metas[stem] = {
                "stem": stem, "part": part, "title": title,
                "id": _chapter_id(title), "desc": _description(md),
                "html": _md_to_html(md)}

    chap_dir = os.path.join(cfg["outdir"], "capitoli")
    os.makedirs(chap_dir, exist_ok=True)
    for i, stem in enumerate(ALL_STEMS):
        prev_m = metas[ALL_STEMS[i - 1]] if i > 0 else None
        next_m = metas[ALL_STEMS[i + 1]] if i < len(ALL_STEMS) - 1 else None
        with open(os.path.join(chap_dir, stem + ".html"), "w") as fh:
            fh.write(_chapter_page(cfg, metas[stem], prev_m, next_m))

    with open(os.path.join(cfg["outdir"], "leggi.html"), "w") as fh:
        fh.write(_leggi_page(cfg, metas))


def build():
    for cfg in LANGS.values():
        _build_lang(cfg)
    with open("docs/sitemap.xml", "w") as fh:
        fh.write(_sitemap())
    with open("docs/robots.txt", "w") as fh:
        fh.write("User-agent: *\nAllow: /\nSitemap: %ssitemap.xml\n" % BASE)
    print("Generate IT+EN: %d capitoli per lingua, leggi.html, sitemap, robots"
          % len(ALL_STEMS))


if __name__ == "__main__":
    build()
