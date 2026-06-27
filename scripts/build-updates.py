#!/usr/bin/env python3
# build-updates.py — generate the "living book" update loop:
#   docs/changelog.html   the human-readable updates page
#   docs/feed.xml         an RSS 2.0 feed readers can subscribe to
# This turns the "it stays current" promise into a recurring touchpoint.
# Add a new entry at the TOP of ENTRIES on every release, then run:
#   python3 scripts/build-updates.py     (from the repo root)
import os
import html
from email.utils import formatdate
from datetime import datetime, timezone

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

BASE = "https://angelogeminiani.github.io/claude-la-guida-completa/"

# -----------------------------------------------------------------------------------------------------------------
#  data — newest entry first
# -----------------------------------------------------------------------------------------------------------------
ENTRIES = [
    {"version": "Rev. 2", "date": "2026-06-27",
     "title": "Dati volatili aggiornati e nuovo sito",
     "points": [
         "Modelli: Fable 5 e Mythos 5 risultano sospesi (direttiva di export "
         "control del governo USA del 12/06/2026). Il manuale lo segnala, invece "
         "di darli per disponibili.",
         "Context window: 500K token in chat per i modelli di punta, 200K per gli "
         "altri, fino a 1M in Claude Code.",
         "Cowork: aggiornato lo stato (macOS/Windows, piani a pagamento) e "
         "aggiunte le modalità di permessi.",
         "Sito: tema scuro, 33 capitoli leggibili online, pulsanti di "
         "condivisione e mini-tool «quale piano e modello fa per te»."]},
    {"version": "Rev. 1", "date": "2026-06-22",
     "title": "Prima edizione completa",
     "points": [
         "33 capitoli su sei livelli: dai fondamenti fino a Skills, MCP, "
         "automazioni e API.",
         "Sito di presentazione con PDF A5 scaricabile gratis."]},
]

# -----------------------------------------------------------------------------------------------------------------
#  shared markup
# -----------------------------------------------------------------------------------------------------------------
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

NAV = (
    '<header class="nav"><div class="row">'
    '<a class="brand" href="index.html"><svg class="mark"><use href="#ast"/></svg>'
    ' Claude · la guida completa</a><div class="nav-right">'
    '<a class="nav-cta" href="leggi.html">Leggi online</a>'
    '<a class="nav-cta" href="feed.xml">RSS</a>'
    '<button class="theme-toggle" id="theme-toggle" type="button" '
    'aria-label="Cambia tema chiaro/scuro" title="Cambia tema">'
    '<svg class="i-moon" aria-hidden="true"><use href="#moon"/></svg>'
    '<svg class="i-sun" aria-hidden="true"><use href="#sun"/></svg>'
    '</button></div></div></header>')

FOOTER = (
    '<footer><div class="wrap">© 2026 Gian Angelo Geminiani. Pubblicazione '
    '<strong>indipendente e non ufficiale</strong>: non affiliata, sponsorizzata '
    'né approvata da Anthropic.</div></footer>')


# -----------------------------------------------------------------------------------------------------------------
#  builders
# -----------------------------------------------------------------------------------------------------------------
def _css():
    return "<style>" + open("docs/assets/book.css").read() + "</style>"


def _pubdate(date_str):
    dt = datetime.strptime(date_str, "%Y-%m-%d").replace(
        hour=9, tzinfo=timezone.utc)
    return formatdate(dt.timestamp(), usegmt=True)


def _changelog_html():
    canonical = BASE + "changelog.html"
    blocks = []
    for e in ENTRIES:
        pts = "".join("<li>%s</li>" % html.escape(p) for p in e["points"])
        blocks.append(
            '<article style="margin:0 0 30px"><p class="qn" '
            'style="font-weight:700;letter-spacing:.1em;font-size:12px;'
            'color:var(--coral-d);text-transform:uppercase;margin:0 0 2px">'
            '%s · %s</p><h2 class="part-h" style="margin:2px 0 8px">%s</h2>'
            '<ul>%s</ul></article>' % (
                html.escape(e["version"]), html.escape(e["date"]),
                html.escape(e["title"]), pts))

    head = (
        '<!DOCTYPE html><html lang="it"><head><meta charset="utf-8">'
        '<meta name="viewport" content="width=device-width, initial-scale=1">'
        '<title>Aggiornamenti ed errata — Claude: la guida completa</title>'
        '<meta name="description" content="Cosa è cambiato nel manuale: dati di '
        'prodotto aggiornati, correzioni e novità. Iscriviti via RSS per restare '
        'aggiornato.">'
        '<link rel="canonical" href="%s">'
        '<link rel="alternate" type="application/rss+xml" '
        'title="Claude: la guida completa — aggiornamenti" href="feed.xml">'
        '<meta name="theme-color" content="#FAF9F5">'
        '<link rel="icon" href="%s">'
        '<link rel="preconnect" href="https://fonts.googleapis.com">'
        '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
        '<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;'
        '600;700&family=Lora:ital,wght@0,600;1,500&display=swap" rel="stylesheet">'
        '%s%s</head><body>%s' % (
            canonical, FAVICON, _css(), THEME_SCRIPT, SYMBOLS))

    intro = (
        '<h1 style="font-family:Lora,Georgia,serif;font-size:clamp(30px,5vw,42px);'
        'margin:18px 0 4px">Aggiornamenti</h1><div class="accent"></div>'
        '<p class="lead">I dati su Claude cambiano in fretta: qui trovi cosa è '
        'stato aggiornato nel manuale. Vuoi essere avvisato? '
        '<a href="feed.xml">Iscriviti via RSS</a> oppure '
        '<a href="https://github.com/angelogeminiani/claude-la-guida-completa">'
        'metti una Watch su GitHub</a>.</p>')

    body = (NAV + '<main class="wrap">' + intro + "".join(blocks) +
            '</main>' + FOOTER + TOGGLE_SCRIPT + "</body></html>")
    return head + body


def _feed_xml():
    items = []
    for e in ENTRIES:
        desc = " ".join(e["points"])
        link = BASE + "changelog.html"
        items.append(
            "<item><title>%s — %s</title><link>%s</link>"
            "<guid isPermaLink=\"false\">claude-guida-%s</guid>"
            "<pubDate>%s</pubDate><description>%s</description></item>" % (
                html.escape(e["version"]), html.escape(e["title"]), link,
                e["version"].replace(" ", "-").lower(), _pubdate(e["date"]),
                html.escape(desc)))
    return (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<rss version="2.0"><channel>'
        '<title>Claude: la guida completa — aggiornamenti</title>'
        '<link>%schangelog.html</link>'
        '<description>Aggiornamenti, errata e novità del manuale italiano '
        'sull\'ecosistema Claude.</description><language>it</language>'
        '%s</channel></rss>\n' % (BASE, "".join(items)))


def build():
    os.makedirs("docs", exist_ok=True)
    with open("docs/changelog.html", "w") as fh:
        fh.write(_changelog_html())
    with open("docs/feed.xml", "w") as fh:
        fh.write(_feed_xml())
    print("Creato docs/changelog.html e docs/feed.xml (%d voci)" % len(ENTRIES))


if __name__ == "__main__":
    build()
