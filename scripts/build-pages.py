#!/usr/bin/env python3
# build-pages.py — generate the online, SEO-friendly HTML version of the book:
#   docs/capitoli/<stem>.html   one full-text page per chapter
#   docs/leggi.html             the "read online" index (table of contents)
#   docs/sitemap.xml            sitemap for search engines
#   docs/robots.txt             robots file pointing at the sitemap
# Shares the Claude.ai look via docs/assets/book.css. Mermaid diagrams are
# rendered to on-brand inline SVG by mermaid2svg.py (no Chromium needed).
#
# Usage:  python3 scripts/build-pages.py     (run from the repo root)
import os
import re
import sys
import html
import subprocess
import importlib.util

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

BASE = "https://angelogeminiani.github.io/claude-la-guida-completa/"
TODAY = "2026-06-27"

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
    '<symbol id="sun" viewBox="0 0 24 24">'
    '<g fill="none" stroke="currentColor" stroke-width="1.8" '
    'stroke-linecap="round"><circle cx="12" cy="12" r="4.2"/>'
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
    "<script>(function(){var r=document.documentElement;"
    "function eff(){var f=r.getAttribute('data-theme');return f?f:"
    "(window.matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light');}"
    "function meta(t){var m=document.querySelector('meta[name=\"theme-color\"]');"
    "if(m)m.setAttribute('content',t==='dark'?'#1F1E1D':'#FAF9F5');}meta(eff());"
    "var b=document.getElementById('theme-toggle');if(b)b.addEventListener('click',"
    "function(){var n=eff()==='dark'?'light':'dark';r.setAttribute('data-theme',n);"
    "try{localStorage.setItem('theme',n);}catch(e){}meta(n);});})();</script>")


def _nav(home, leggi, pdf):
    return (
        '<header class="nav"><div class="row">'
        '<a class="brand" href="%s"><svg class="mark"><use href="#ast"/></svg> '
        'Claude · la guida completa</a>'
        '<div class="nav-right"><a class="nav-cta" href="%s">Indice</a>'
        '<a class="nav-cta" href="%s" download>Scarica il PDF →</a>'
        '<button class="theme-toggle" id="theme-toggle" type="button" '
        'aria-label="Cambia tema chiaro/scuro" title="Cambia tema">'
        '<svg class="i-moon" aria-hidden="true"><use href="#moon"/></svg>'
        '<svg class="i-sun" aria-hidden="true"><use href="#sun"/></svg>'
        '</button></div></div></header>') % (home, leggi, pdf)


FOOTER = (
    '<footer><div class="wrap">© 2026 Gian Angelo Geminiani. Pubblicazione '
    '<strong>indipendente e non ufficiale</strong>: non affiliata, sponsorizzata '
    'né approvata da Anthropic. «Claude» e «Anthropic» sono marchi dei rispettivi '
    'titolari, citati a solo scopo identificativo. Dati verificati alla data '
    'indicata e soggetti a modifica.</div></footer>')

# -----------------------------------------------------------------------------------------------------------------
#  helpers
# -----------------------------------------------------------------------------------------------------------------
_spec = importlib.util.spec_from_file_location(
    "mermaid2svg", os.path.join(ROOT, "scripts", "mermaid2svg.py"))
_m2s = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_m2s)

_css_cache = None


def _css():
    # Inline the shared stylesheet so every page is self-contained (renders
    # correctly in previews and when a single file is opened in isolation).
    global _css_cache
    if _css_cache is None:
        _css_cache = "<style>" + open("docs/assets/book.css").read() + "</style>"
    return _css_cache


def _embed_diagrams(md):
    def repl(match):
        return '\n<div class="fig">' + _m2s.render(match.group(1)) + "</div>\n"
    return re.sub(r"```mermaid\n(.*?)```", repl, md, flags=re.S)


def _strip_tags(md):
    # Remove the (VOLATILE)/(EVERGREEN) status markers used for maintenance.
    md = re.sub(r"^(#{1,6}\s+.*?)\s*\((?:VOLATILE|EVERGREEN)\)\s*$",
                r"\1", md, flags=re.M)
    return re.sub(r"\s*\((?:VOLATILE|EVERGREEN)\)", "", md)


def _strip_hr(md):
    # Drop markdown thematic breaks: sections are separated by headings/spacing.
    return re.sub(r"^\s*---\s*$", "", md, flags=re.M)


def _h1(md):
    m = re.search(r"^#\s+(.*)$", md, re.M)
    raw = m.group(1).strip() if m else "?"
    return re.sub(r"^Capitolo\s+", "", raw)


def _chapter_id(title):
    # "F.3 — Modelli e piani" -> "F.3"; "L6.4 — ..." -> "L6.4".
    return re.split(r"\s+—\s+", title, 1)[0].strip()


def _description(md):
    # Use the first real paragraph (prefer the one under "## Obiettivo").
    m = re.search(r"^##\s+Obiettivo\s*\n+(.+?)(?:\n\n|\n#)", md, re.S | re.M)
    if not m:
        body = re.sub(r"^#.*$", "", md, flags=re.M)        # drop headings
        body = re.sub(r"^>.*$", "", body, flags=re.M)      # drop blockquotes
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
    # Make tables horizontally scrollable on narrow screens.
    out = out.replace("<table>", '<div class="tablewrap"><table>')
    out = out.replace("</table>", "</table></div>")
    return out


def _head(title, desc, canonical, og_url):
    esc_t = html.escape(title)
    esc_d = html.escape(desc)
    return (
        '<!DOCTYPE html><html lang="it"><head><meta charset="utf-8">'
        '<meta name="viewport" content="width=device-width, initial-scale=1">'
        '<title>%s</title>'
        '<meta name="description" content="%s">'
        '<link rel="canonical" href="%s">'
        '<meta name="theme-color" content="#FAF9F5">'
        '<meta name="author" content="Gian Angelo Geminiani">'
        '<meta property="og:type" content="article">'
        '<meta property="og:site_name" content="Claude: la guida completa">'
        '<meta property="og:title" content="%s">'
        '<meta property="og:description" content="%s">'
        '<meta property="og:url" content="%s">'
        '<meta property="og:image" content="%sog-image.png">'
        '<meta property="og:locale" content="it_IT">'
        '<meta name="twitter:card" content="summary_large_image">'
        '<meta name="twitter:title" content="%s">'
        '<meta name="twitter:description" content="%s">'
        '<meta name="twitter:image" content="%sog-image.png">'
        '<link rel="icon" href="%s">'
        '<link rel="preconnect" href="https://fonts.googleapis.com">'
        '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
        '<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;'
        '600;700&family=Lora:ital,wght@0,600;1,500&display=swap" rel="stylesheet">'
        '%s'
        '%s</head><body>%s') % (
            esc_t, esc_d, canonical, esc_t, esc_d, og_url, BASE, esc_t, esc_d,
            BASE, FAVICON, "__CSS__", THEME_SCRIPT, SYMBOLS)


# -----------------------------------------------------------------------------------------------------------------
#  page builders
# -----------------------------------------------------------------------------------------------------------------
def _chapter_page(meta, prev_m, next_m):
    title = meta["title"]
    canonical = BASE + "capitoli/" + meta["stem"] + ".html"
    jsonld = (
        '<script type="application/ld+json">{"@context":"https://schema.org",'
        '"@type":"TechArticle","headline":%s,"description":%s,'
        '"inLanguage":"it","author":{"@type":"Person","name":'
        '"Gian Angelo Geminiani"},"isPartOf":{"@type":"Book","name":'
        '"Claude: la guida completa"},"mainEntityOfPage":%s}</script>') % (
            _json(title), _json(meta["desc"]), _json(canonical))

    head = _head(title + " · Claude: la guida completa", meta["desc"],
                 canonical, canonical).replace(
        "__CSS__", _css() + jsonld)

    pager = '<nav class="pager">'
    if prev_m:
        pager += ('<a href="./%s.html"><span class="lbl">← Precedente</span>%s</a>'
                  % (prev_m["stem"], html.escape(prev_m["title"])))
    if next_m:
        pager += ('<a class="nxt" href="./%s.html"><span class="lbl">Successivo →'
                  '</span>%s</a>' % (next_m["stem"], html.escape(next_m["title"])))
    pager += "</nav>"

    cta = (
        '<div class="readcta"><h2>Ti è utile? Prendi tutto il manuale</h2>'
        '<p>33 capitoli in un unico PDF A5, gratis e senza registrazione.</p>'
        '<a class="btn btn-primary" href="../manuale_produzione.pdf" download>'
        '↓ Scarica il PDF gratis</a></div>')

    crumbs = ('<div class="crumbs"><a href="../index.html">Home</a> · '
              '<a href="../leggi.html">Leggi online</a> · %s</div>'
              % html.escape(meta["part"]))

    body = (
        _nav("../index.html", "../leggi.html", "../manuale_produzione.pdf") +
        '<main class="wrap">' + crumbs +
        '<article>' + meta["html"] + '</article>' +
        pager + cta + '</main>' + FOOTER + TOGGLE_SCRIPT +
        "</body></html>")
    return head + body


def _leggi_page(metas):
    canonical = BASE + "leggi.html"
    head = _head(
        "Leggi online — Claude: la guida completa",
        "Leggi gratis online tutti i 33 capitoli del manuale italiano "
        "sull'ecosistema Claude: chat, Claude Code, Cowork, Design, Skills e API.",
        canonical, canonical).replace("__CSS__", _css())

    parts_html = []
    for part, stems in PARTS:
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
        'margin:18px 0 4px">Leggi online</h1>'
        '<div class="accent"></div>'
        '<p class="lead">Tutti i 33 capitoli, gratis. Preferisci la versione '
        'completa? <a href="manuale_produzione.pdf" download>Scarica il PDF A5</a>.'
        '</p>')

    body = (
        _nav("index.html", "leggi.html", "manuale_produzione.pdf") +
        '<main class="wrap">' + intro + "".join(parts_html) + '</main>' +
        FOOTER + TOGGLE_SCRIPT + "</body></html>")
    return head + body


def _sitemap(metas):
    urls = [BASE, BASE + "leggi.html"]
    urls += [BASE + "capitoli/" + s + ".html"
             for _, stems in PARTS for s in stems]
    items = []
    for u in urls:
        pri = "1.0" if u == BASE else ("0.8" if u.endswith("leggi.html") else "0.6")
        items.append("<url><loc>%s</loc><lastmod>%s</lastmod>"
                     "<priority>%s</priority></url>" % (u, TODAY, pri))
    return ('<?xml version="1.0" encoding="UTF-8"?>\n'
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
            + "\n".join(items) + "\n</urlset>\n")


def _json(s):
    import json
    return json.dumps(s, ensure_ascii=False)


# -----------------------------------------------------------------------------------------------------------------
#  build
# -----------------------------------------------------------------------------------------------------------------
def build():
    metas = {}
    order = []
    for part, stems in PARTS:
        for stem in stems:
            md = open(os.path.join("capitoli", stem + ".md")).read()
            title = _h1(md)
            metas[stem] = {
                "stem": stem, "part": part, "title": title,
                "id": _chapter_id(title), "desc": _description(md),
                "html": _md_to_html(md)}
            order.append(stem)

    os.makedirs("docs/capitoli", exist_ok=True)
    for i, stem in enumerate(order):
        prev_m = metas[order[i - 1]] if i > 0 else None
        next_m = metas[order[i + 1]] if i < len(order) - 1 else None
        with open(os.path.join("docs/capitoli", stem + ".html"), "w") as fh:
            fh.write(_chapter_page(metas[stem], prev_m, next_m))

    with open("docs/leggi.html", "w") as fh:
        fh.write(_leggi_page(metas))
    with open("docs/sitemap.xml", "w") as fh:
        fh.write(_sitemap(metas))
    with open("docs/robots.txt", "w") as fh:
        fh.write("User-agent: *\nAllow: /\nSitemap: %ssitemap.xml\n" % BASE)

    print("Generate %d pagine capitolo + leggi.html + sitemap.xml + robots.txt"
          % len(order))


if __name__ == "__main__":
    build()
