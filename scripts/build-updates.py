#!/usr/bin/env python3
# build-updates.py — generate the "living book" update loop in both languages:
#   docs/changelog.html      Italian updates page
#   docs/en/changelog.html   English updates page
#   docs/feed.xml            RSS 2.0 feed readers can subscribe to
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
REPO = "https://github.com/angelogeminiani/claude-la-guida-completa"

# -----------------------------------------------------------------------------------------------------------------
#  data — newest entry first; each entry has Italian and English text
# -----------------------------------------------------------------------------------------------------------------
ENTRIES = [
    {"version": "Rev. 2", "date": "2026-06-27",
     "title_it": "Dati volatili aggiornati e nuovo sito",
     "title_en": "Volatile data updated and a new site",
     "points_it": [
         "Modelli: Fable 5 e Mythos 5 risultano sospesi (direttiva di export "
         "control del governo USA del 12/06/2026). Il manuale lo segnala.",
         "Context window: 500K token in chat per i modelli di punta, 200K per "
         "gli altri, fino a 1M in Claude Code.",
         "Cowork: aggiornato lo stato (macOS/Windows, piani a pagamento) e "
         "aggiunte le modalità di permessi.",
         "Sito: tema scuro, 33 capitoli online, condivisione, mini-tool e "
         "edizione inglese completa."],
     "points_en": [
         "Models: Fable 5 and Mythos 5 are suspended (a US government export "
         "control directive dated 2026-06-12). The manual flags this.",
         "Context window: 500K tokens in chat for the top models, 200K for the "
         "others, up to 1M in Claude Code.",
         "Cowork: status updated (macOS/Windows, paid plans) and the permission "
         "modes added.",
         "Site: dark theme, 33 chapters online, sharing, a mini-tool and a full "
         "English edition."]},
    {"version": "Rev. 1", "date": "2026-06-22",
     "title_it": "Prima edizione completa",
     "title_en": "First complete edition",
     "points_it": [
         "33 capitoli su sei livelli: dai fondamenti fino a Skills, MCP, "
         "automazioni e API.",
         "Sito di presentazione con PDF A5 scaricabile gratis."],
     "points_en": [
         "33 chapters across six levels: from the basics to Skills, MCP, "
         "automation and the API.",
         "Landing site with a free A5 PDF download."]},
]

# -----------------------------------------------------------------------------------------------------------------
#  per-language configuration
# -----------------------------------------------------------------------------------------------------------------
LANGS = {
    "it": {"lang": "it", "out": "docs/changelog.html", "root": "",
           "feed": "feed.xml",
           "brand": "Claude · la guida completa", "read": "Leggi online",
           "title": "Aggiornamenti ed errata — Claude: la guida completa",
           "desc": ("Cosa è cambiato nel manuale: dati di prodotto aggiornati, "
                    "correzioni e novità. Iscriviti via RSS."),
           "h1": "Aggiornamenti",
           "lead": ("I dati su Claude cambiano in fretta: qui trovi cosa è "
                    "stato aggiornato. Vuoi essere avvisato? "
                    "<a href=\"feed.xml\">Iscriviti via RSS</a> oppure "
                    "<a href=\"%s\">metti una Watch su GitHub</a>." % REPO),
           "tkey": "title_it", "pkey": "points_it",
           "footer": ("© 2026 Gian Angelo Geminiani. Pubblicazione "
                      "<strong>indipendente e non ufficiale</strong>: non "
                      "affiliata, sponsorizzata né approvata da Anthropic.")},
    "en": {"lang": "en", "out": "docs/en/changelog.html", "root": "",
           "feed": "../feed.xml",
           "brand": "Claude · the complete guide", "read": "Read online",
           "title": "Updates and errata — Claude: the complete guide",
           "desc": ("What changed in the manual: updated product data, fixes "
                    "and news. Subscribe via RSS."),
           "h1": "Updates",
           "lead": ("Claude's details change fast: here's what's been updated. "
                    "Want to be notified? "
                    "<a href=\"../feed.xml\">Subscribe via RSS</a> or "
                    "<a href=\"%s\">Watch on GitHub</a>." % REPO),
           "tkey": "title_en", "pkey": "points_en",
           "footer": ("© 2026 Gian Angelo Geminiani. An <strong>independent, "
                      "unofficial</strong> publication: not affiliated with, "
                      "sponsored or endorsed by Anthropic.")},
}

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
    "<script>(function(){var r=document.documentElement;var b="
    "document.getElementById('theme-toggle');if(b)b.addEventListener('click',"
    "function(){var f=r.getAttribute('data-theme');var e=f?f:(window.matchMedia("
    "'(prefers-color-scheme: dark)').matches?'dark':'light');var n=e==='dark'?"
    "'light':'dark';r.setAttribute('data-theme',n);try{localStorage.setItem("
    "'theme',n);}catch(x){}});})();</script>")

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


# -----------------------------------------------------------------------------------------------------------------
#  builders
# -----------------------------------------------------------------------------------------------------------------
def _css():
    return "<style>" + open("docs/assets/book.css").read() + "</style>"


def _pubdate(date_str):
    dt = datetime.strptime(date_str, "%Y-%m-%d").replace(
        hour=9, tzinfo=timezone.utc)
    return formatdate(dt.timestamp(), usegmt=True)


def _nav(cfg):
    return (
        '<header class="nav"><div class="row">'
        '<a class="brand" href="%sindex.html"><svg class="mark">'
        '<use href="#ast"/></svg> %s</a><div class="nav-right">'
        '<a class="nav-cta" href="%sleggi.html">%s</a>'
        '<a class="nav-cta" href="%s">RSS</a>'
        '<button class="theme-toggle" id="theme-toggle" type="button" '
        'aria-label="theme" title="Theme">'
        '<svg class="i-moon" aria-hidden="true"><use href="#moon"/></svg>'
        '<svg class="i-sun" aria-hidden="true"><use href="#sun"/></svg>'
        '</button></div></div></header>') % (
            cfg["root"], cfg["brand"], cfg["root"], cfg["read"], cfg["feed"])


def _changelog_html(cfg):
    blocks = []
    for e in ENTRIES:
        pts = "".join("<li>%s</li>" % html.escape(p) for p in e[cfg["pkey"]])
        blocks.append(
            '<article style="margin:0 0 30px"><p style="font-weight:700;'
            'letter-spacing:.1em;font-size:12px;color:var(--coral-d);'
            'text-transform:uppercase;margin:0 0 2px">%s · %s</p>'
            '<h2 class="part-h" style="margin:2px 0 8px">%s</h2><ul>%s</ul>'
            '</article>' % (
                html.escape(e["version"]), html.escape(e["date"]),
                html.escape(e[cfg["tkey"]]), pts))

    head = (
        '<!DOCTYPE html><html lang="%s"><head><meta charset="utf-8">'
        '<meta name="viewport" content="width=device-width, initial-scale=1">'
        '<title>%s</title><meta name="description" content="%s">'
        '<link rel="alternate" type="application/rss+xml" '
        'title="updates" href="%s">'
        '<meta name="theme-color" content="#FAF9F5"><link rel="icon" href="%s">'
        '<link rel="preconnect" href="https://fonts.googleapis.com">'
        '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
        '<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;'
        '600;700&family=Lora:ital,wght@0,600;1,500&display=swap" rel="stylesheet">'
        '%s%s%s</head><body>%s' % (
            cfg["lang"], html.escape(cfg["title"]), html.escape(cfg["desc"]),
            cfg["feed"], FAVICON, _css(), THEME_SCRIPT, SYMBOLS, ""))

    intro = ('<h1 style="font-family:Lora,Georgia,serif;'
             'font-size:clamp(30px,5vw,42px);margin:18px 0 4px">%s</h1>'
             '<div class="accent"></div><p class="lead">%s</p>' % (
                 html.escape(cfg["h1"]), cfg["lead"]))

    return (head + _nav(cfg) + '<main class="wrap">' + intro +
            "".join(blocks) + '</main>'
            '<footer><div class="wrap">' + cfg["footer"] + '</div></footer>' +
            TOGGLE_SCRIPT + "</body></html>")


def _feed_xml():
    items = []
    for e in ENTRIES:
        desc = " ".join(e["points_it"])
        link = BASE + "changelog.html"
        items.append(
            "<item><title>%s — %s</title><link>%s</link>"
            "<guid isPermaLink=\"false\">claude-guida-%s</guid>"
            "<pubDate>%s</pubDate><description>%s</description></item>" % (
                html.escape(e["version"]), html.escape(e["title_it"]), link,
                e["version"].replace(" ", "-").lower(), _pubdate(e["date"]),
                html.escape(desc)))
    return ('<?xml version="1.0" encoding="UTF-8"?>\n<rss version="2.0">'
            '<channel><title>Claude: la guida completa — aggiornamenti</title>'
            '<link>%schangelog.html</link><description>Aggiornamenti, errata e '
            'novità del manuale sull\'ecosistema Claude.</description>'
            '<language>it</language>%s</channel></rss>\n' % (BASE, "".join(items)))


def build():
    os.makedirs("docs/en", exist_ok=True)
    for cfg in LANGS.values():
        with open(cfg["out"], "w") as fh:
            fh.write(_changelog_html(cfg))
    with open("docs/feed.xml", "w") as fh:
        fh.write(_feed_xml())
    print("Creato changelog IT+EN e feed.xml (%d voci)" % len(ENTRIES))


if __name__ == "__main__":
    build()
