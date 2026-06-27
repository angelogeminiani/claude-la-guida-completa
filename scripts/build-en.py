#!/usr/bin/env python3
# build-en.py — generate the English landing page (docs/en/index.html).
# It reuses the Italian landing's inline <style> and icon symbols (so the look
# stays in sync and the page renders even in isolated previews), and swaps in
# English copy. The page is honest: the book itself is in Italian and an English
# edition is in progress, so its main job is to capture the English-speaking
# audience into the update loop (RSS / GitHub Watch).
#   python3 scripts/build-en.py     (run from the repo root)
import os
import re
import base64

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

BASE = "https://angelogeminiani.github.io/claude-la-guida-completa/"
REPO = "https://github.com/angelogeminiani/claude-la-guida-completa"

# Embed the cover as a data URI so it renders everywhere — including isolated
# previews where a relative path like ../cover.png would not resolve.
with open("risorse/copertina.png", "rb") as _fh:
    COVER_DATA = "data:image/png;base64," + base64.b64encode(_fh.read()).decode()


# -----------------------------------------------------------------------------------------------------------------
#  helpers
# -----------------------------------------------------------------------------------------------------------------
def _extract(html_text, pattern):
    m = re.search(pattern, html_text, re.S)
    if not m:
        raise SystemExit("pattern not found: " + pattern)
    return m.group(0)


def _head(style, symbols):
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Claude: the complete guide — the manual that updates when Claude does</title>
<meta name="description" content="Claude changes every week. This practical manual keeps up: from your first prompt to Claude Code, Cowork, Skills and the API. Written in Italian, English edition in progress.">
<link rel="canonical" href="{BASE}en/">
<link rel="alternate" hreflang="it" href="{BASE}">
<link rel="alternate" hreflang="en" href="{BASE}en/">
<link rel="alternate" hreflang="x-default" href="{BASE}">
<link rel="alternate" type="application/rss+xml" title="Claude: la guida completa — updates" href="../feed.xml">
<meta name="theme-color" content="#FAF9F5">
<meta name="author" content="Gian Angelo Geminiani">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Claude: the complete guide">
<meta property="og:title" content="The Claude manual that updates when Claude does">
<meta property="og:description" content="Claude changes constantly, this manual changes with it. Practical, from your first prompt to Claude Code, Cowork, Skills and the API.">
<meta property="og:url" content="{BASE}en/">
<meta property="og:image" content="{BASE}og-image-en.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:locale" content="en_US">
<meta property="og:locale:alternate" content="it_IT">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="The Claude manual that updates when Claude does">
<meta name="twitter:description" content="Claude changes every week, this manual keeps up. 33 chapters, free to read.">
<meta name="twitter:image" content="{BASE}og-image-en.png">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Cg stroke='%23D97757' stroke-width='3' stroke-linecap='round'%3E%3Cline x1='16' y1='5' x2='16' y2='27'/%3E%3Cline x1='5' y1='16' x2='27' y2='16'/%3E%3Cline x1='8' y1='8' x2='24' y2='24'/%3E%3Cline x1='24' y1='8' x2='8' y2='24'/%3E%3C/g%3E%3C/svg%3E">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Lora:ital,wght@0,600;1,500&display=swap" rel="stylesheet">
{style}
<script>(function(){{try{{var s=localStorage.getItem('theme');if(s==='dark'||s==='light')document.documentElement.setAttribute('data-theme',s);}}catch(e){{}}}})();</script>
</head>
<body>
{symbols}'''


def _body():
    levels = [
        ("Foundations", "Get oriented: ecosystem, models, plans, reading paths."),
        ("Level 1", "First contact, prompting well, settings and styles."),
        ("Level 2", "Local install: Desktop, Claude Code, auth, project setup."),
        ("Level 3", "Daily work: Cowork, Projects, connectors, documents."),
        ("Level 4", "Design: canvas, design system, /design-sync, export."),
        ("Level 5", "Skills and identity: anatomy, your first skill, your voice."),
        ("Level 6", "Advanced: hooks, custom MCP, automation, limits, API."),
        ("Closing", "Putting it together: an end-to-end project, glossary."),
    ]
    lvl_html = "".join(
        '<div class="lvl"><div class="n">%s</div><div class="t">'
        '<span>%s</span></div></div>' % (n, d) for n, d in levels)

    return f'''
<header class="nav">
  <div class="wrap">
    <a class="brand" href="../index.html">
      <svg class="mark"><use href="#ast"/></svg> Claude · the complete guide
    </a>
    <div class="nav-right">
      <a class="nav-cta" href="../leggi.html">Read online</a>
      <a class="nav-cta" href="#updates">Get updates</a>
      <a class="nav-cta" href="../" hreflang="it" title="Versione italiana">IT</a>
      <button class="theme-toggle" id="theme-toggle" type="button"
              aria-label="Toggle light/dark theme" title="Toggle theme">
        <svg class="i-moon" aria-hidden="true"><use href="#moon"/></svg>
        <svg class="i-sun" aria-hidden="true"><use href="#sun"/></svg>
      </button>
    </div>
  </div>
</header>

<a id="top"></a>
<section class="hero">
  <div class="wrap">
    <div class="grid">
      <div>
        <p class="kicker">Operational handbook · 2026 edition</p>
        <h1>Claude: the complete guide</h1>
        <div class="rule"></div>
        <p class="lead"><strong>Claude changes every week. This manual keeps
          up.</strong> Practical, from your first prompt to Claude Code, Cowork,
          Skills and the API — 33 chapters across six levels.</p>
        <div class="cta-row">
          <a class="btn btn-primary" href="#updates">Get notified →</a>
          <a class="btn btn-ghost" href="../leggi.html">Read online</a>
        </div>
        <p class="meta"><strong>Written in Italian.</strong> An English edition is
          in progress — subscribe below and you'll be the first to know.</p>
      </div>
      <div class="cover-shot">
        <img src="{COVER_DATA}" alt="Cover of Claude: the complete guide"
             width="300">
      </div>
    </div>
  </div>
</section>

<section class="levels">
  <div class="wrap">
    <div class="section-head">
      <h2>What's inside</h2>
      <p>33 chapters across six levels, plus front matter and a closing project.</p>
    </div>
    <div class="lvl-list">{lvl_html}</div>
  </div>
</section>

<section class="tool">
  <div class="wrap">
    <div class="section-head">
      <h2>Why this guide</h2>
      <p>Honest about a product that changes fast.</p>
    </div>
    <div class="cards">
      <div class="card"><svg class="ic"><use href="#ast"/></svg>
        <h3>Beginner to expert</h3>
        <p>Six progressive levels, from the basics of chat to hooks, custom MCP
          and the API. Every chapter states its level.</p></div>
      <div class="card"><svg class="ic"><use href="#ast"/></svg>
        <h3>Practical, not theoretical</h3>
        <p>Commands verified against official sources, real examples, and the
          common mistakes to avoid.</p></div>
      <div class="card"><svg class="ic"><use href="#ast"/></svg>
        <h3>It doesn't age</h3>
        <p>Whatever changes is dated and tracked in the companion repo, so the
          text points to the current source.</p></div>
      <div class="card"><svg class="ic"><use href="#ast"/></svg>
        <h3>Carefully made</h3>
        <p>Vector diagrams, clean tables, A5 format. Built to read well, on paper
          and on screen.</p></div>
    </div>
  </div>
</section>

<section id="updates">
  <div class="wrap">
    <div class="section-head">
      <h2>Stay updated</h2>
      <p>Claude moves fast. Get told when the manual updates — and when the
        English edition lands. No email required.</p>
    </div>
    <div class="share-row" style="justify-content:center">
      <a class="sbtn" href="../feed.xml">
        <svg><use href="#i-rss"/></svg> Subscribe via RSS</a>
      <a class="sbtn" target="_blank" rel="noopener" href="{REPO}/subscription">
        <svg><use href="#i-gh"/></svg> Watch on GitHub
        <span class="cnt" id="gh-stars"></span></a>
      <a class="sbtn" href="../changelog.html">
        <svg><use href="#i-clock"/></svg> What changed</a>
    </div>
  </div>
</section>

<section class="share">
  <div class="wrap">
    <div class="section-head">
      <h2>Spread the word</h2>
      <p>It's free and built to be shared. One link helps more than you think.</p>
    </div>
    <p class="quote">«The Claude manual that updates when Claude does.»</p>
    <div class="share-row" id="share-row">
      <a class="sbtn" id="sh-x" target="_blank" rel="noopener">
        <svg><use href="#i-x"/></svg> Post on X</a>
      <a class="sbtn" id="sh-li" target="_blank" rel="noopener">
        <svg><use href="#i-li"/></svg> LinkedIn</a>
      <button class="sbtn" id="sh-copy" type="button">
        <svg><use href="#i-link"/></svg> Copy link</button>
    </div>
    <p class="copied" id="copied"></p>
  </div>
</section>

<footer>
  <div class="wrap">
    <div class="legal">
      © 2026 Gian Angelo Geminiani. An <strong>independent, unofficial</strong>
      publication: not affiliated with, sponsored or endorsed by Anthropic.
      "Claude" and "Anthropic" are trademarks of their respective owners, used
      for identification only.
    </div>
    <div class="links">
      <a href="../leggi.html">Read online</a>
      <a href="../changelog.html">Updates</a>
      <a href="../feed.xml">RSS</a>
      <a href="../">Italiano</a>
      <a href="{REPO}">GitHub</a>
    </div>
  </div>
</footer>

<script>
  (function(){{
    var r=document.documentElement;
    function eff(){{var f=r.getAttribute('data-theme');return f?f:(window.matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light');}}
    function meta(t){{var m=document.querySelector('meta[name="theme-color"]');if(m)m.setAttribute('content',t==='dark'?'#1F1E1D':'#FAF9F5');}}
    meta(eff());
    var b=document.getElementById('theme-toggle');
    if(b)b.addEventListener('click',function(){{var n=eff()==='dark'?'light':'dark';r.setAttribute('data-theme',n);try{{localStorage.setItem('theme',n);}}catch(e){{}}meta(n);}});
    var url=location.href.split('#')[0];
    var title="Claude: the complete guide — the manual that updates when Claude does";
    var u=encodeURIComponent(url), t=encodeURIComponent(title);
    function set(id,href){{var e=document.getElementById(id);if(e)e.href=href;}}
    set("sh-x","https://twitter.com/intent/tweet?text="+t+"&url="+u);
    set("sh-li","https://www.linkedin.com/sharing/share-offsite/?url="+u);
    var copy=document.getElementById("sh-copy"), msg=document.getElementById("copied");
    if(copy)copy.addEventListener("click",function(){{
      var done=function(){{if(msg){{msg.textContent="Link copied!";setTimeout(function(){{msg.textContent="";}},2500);}}}};
      if(navigator.clipboard){{navigator.clipboard.writeText(url).then(done,done);}}else{{done();}}
    }});
    try{{
      fetch("https://api.github.com/repos/angelogeminiani/claude-la-guida-completa")
        .then(function(r){{return r.ok?r.json():null;}})
        .then(function(d){{if(d&&typeof d.stargazers_count==="number"){{var e=document.getElementById("gh-stars");if(e)e.textContent="· ★ "+d.stargazers_count;}}}});
    }}catch(e){{}}
  }})();
</script>
</body>
</html>'''


def build():
    html_text = open("docs/index.html").read()
    style = _extract(html_text, r"<style>.*?</style>")
    symbols = _extract(html_text, r'<svg width="0" height="0".*?</svg>')
    os.makedirs("docs/en", exist_ok=True)
    with open("docs/en/index.html", "w") as fh:
        fh.write(_head(style, symbols) + _body())
    print("Creato docs/en/index.html")


if __name__ == "__main__":
    build()
