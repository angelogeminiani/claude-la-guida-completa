#!/usr/bin/env python3
# build-en.py — generate the English landing page (docs/en/index.html).
# It reuses the Italian landing's inline <style> and icon symbols (so the look
# stays in sync and the page renders even in isolated previews), and swaps in
# English copy. The English edition is complete (full PDF + all chapters
# online), so the page mirrors the Italian landing: same sections, same
# funnel (download / read online / update loop via RSS and GitHub Watch).
#   python3 scripts/build-en.py     (run from the repo root)
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

BASE = "https://angelogeminiani.github.io/claude-la-guida-completa/"
REPO = "https://github.com/angelogeminiani/claude-la-guida-completa"

# The English cover is shipped as a cacheable file (docs/en/cover-en.png),
# referenced relatively instead of inlined as a data URI — smaller HTML,
# faster first paint, browser-cached across pages.


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
<meta name="description" content="Claude changes every week. This practical manual keeps up: from your first prompt to Claude Code, Cowork, Skills and the API. 33 chapters, free to read online and as an A5 PDF.">
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
<script type="application/ld+json">{{"@context":"https://schema.org","@type":"Book","name":"Claude: the complete guide","inLanguage":"en","numberOfPages":156,"bookEdition":"Rev. 3","datePublished":"2026-07-02","bookFormat":"https://schema.org/EBook","author":{{"@type":"Person","name":"Gian Angelo Geminiani"}},"about":["Claude","Claude Code","Cowork","Skills","Anthropic API"],"url":"{BASE}en/","image":"{BASE}og-image-en.png","isAccessibleForFree":true,"license":"https://opensource.org/licenses/MIT","translationOfWork":{{"@type":"Book","name":"Claude: la guida completa","inLanguage":"it","url":"{BASE}"}}}}</script>
</head>
<body>
{symbols}'''


def _body():
    # (label, title, description) — mirrors the Italian "Cosa c'è dentro".
    levels = [
        ("Front matter", "Get oriented",
         "Ecosystem, models, plans, reading paths."),
        ("Level 1", "Foundations",
         "First contact, prompting well, settings and styles."),
        ("Level 2", "Local install",
         "Desktop, Claude Code, authentication, project setup."),
        ("Level 3", "Daily work",
         "Cowork, Projects, connectors, documents, slides and Excel."),
        ("Level 4", "Design",
         "Canvas, design system, /design-sync, export and Canva."),
        ("Level 5", "Skills and identity",
         "Anatomy of a skill, your first skill, your voice."),
        ("Level 6", "Advanced",
         "Hooks, custom MCP, automation, usage limits, security, API."),
        ("Closing", "Putting it together",
         "An end-to-end project, glossary and troubleshooting."),
    ]
    lvl_html = "".join(
        '<div class="lvl"><div class="n">%s</div><div class="t">'
        '<b>%s</b><span>%s</span></div></div>' % (n, t, d)
        for n, t, d in levels)

    return f'''
<header class="nav">
  <div class="wrap">
    <a class="brand" href="../index.html">
      <svg class="mark"><use href="#ast"/></svg> Claude · the complete guide
    </a>
    <div class="nav-right">
      <a class="nav-cta" href="leggi.html">Read online</a>
      <a class="nav-cta" href="#download">Download</a>
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
        <p class="kicker">Operational handbook · 2026 edition · Rev. 3</p>
        <h1>Claude: the complete guide</h1>
        <div class="rule"></div>
        <p class="lead"><strong>Claude changes every week. This manual keeps
          up.</strong> Practical, from your first prompt to Claude Code, Cowork,
          Skills and the API — 33 chapters across six levels.</p>
        <div class="cta-row" id="download">
          <a class="btn btn-primary" href="claude-the-complete-guide.pdf" download>
            ↓ Download the free PDF</a>
          <a class="btn btn-ghost" href="leggi.html">Read online</a>
        </div>
        <p class="meta">PDF · A5 · 156 pages · 33 chapters · free, no signup ·
          <a href="changelog.html">updated July 2, 2026</a></p>
      </div>
      <div class="cover-shot">
        <img src="cover-en.png" width="300" height="426"
             alt="Cover of Claude: the complete guide"
             fetchpriority="high" decoding="async">
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

<section>
  <div class="wrap">
    <div class="section-head">
      <h2>Who it's for</h2>
      <p>One path, three ways to read it.</p>
    </div>
    <div class="aud">
      <div class="card">
        <h3>Starting from scratch</h3>
        <p>You want to use Claude well without touching a terminal: chat,
          Cowork, Projects and documents.</p>
      </div>
      <div class="card">
        <h3>Developers</h3>
        <p>You install and configure locally: Claude Code, Design and the
          /design-sync bridge to your code.</p>
      </div>
      <div class="card">
        <h3>Automators</h3>
        <p>You integrate and work as a team: Skills, MCP, automation,
          governance and API access.</p>
      </div>
    </div>
  </div>
</section>

<section class="tool" id="tool">
  <div class="wrap">
    <div class="section-head">
      <h2>Which plan and model fit you?</h2>
      <p>Three questions, one tailored suggestion. A taste of ch. F.3.</p>
    </div>
    <div class="quiz" id="quiz" aria-live="polite"></div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="final">
      <h2>Download the manual, free</h2>
      <p>156 pages in A5 format. No email, no signup.</p>
      <div class="cta-row" style="justify-content:center">
        <a class="btn btn-primary" href="claude-the-complete-guide.pdf" download>
          ↓ Download the PDF</a>
        <a class="btn btn-ghost" href="{REPO}">Code and sources</a>
      </div>
    </div>
  </div>
</section>

<section class="levels" id="updates">
  <div class="wrap">
    <div class="section-head">
      <h2>Stay updated</h2>
      <p>Claude moves fast. Get told when the manual updates: no email
        required, you pick the channel.</p>
    </div>
    <div class="share-row" style="justify-content:center">
      <a class="sbtn" href="../feed.xml">
        <svg><use href="#i-rss"/></svg> Subscribe via RSS</a>
      <a class="sbtn" target="_blank" rel="noopener" href="{REPO}/subscription">
        <svg><use href="#i-gh"/></svg> Watch on GitHub
        <span class="cnt" id="gh-stars"></span></a>
      <a class="sbtn" href="changelog.html">
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
      <a class="sbtn" id="sh-x" href="#download" target="_blank" rel="noopener">
        <svg><use href="#i-x"/></svg> Post on X</a>
      <a class="sbtn" id="sh-li" href="#download" target="_blank" rel="noopener">
        <svg><use href="#i-li"/></svg> LinkedIn</a>
      <a class="sbtn" id="sh-wa" href="#download" target="_blank" rel="noopener">
        <svg><use href="#i-wa"/></svg> WhatsApp</a>
      <a class="sbtn" id="sh-tg" href="#download" target="_blank" rel="noopener">
        <svg><use href="#i-tg"/></svg> Telegram</a>
      <a class="sbtn" id="sh-rd" href="#download" target="_blank" rel="noopener">
        <svg><use href="#i-rd"/></svg> Reddit</a>
      <button class="sbtn" id="sh-copy" type="button">
        <svg><use href="#i-link"/></svg> Copy link</button>
      <a class="sbtn star" id="sh-gh" target="_blank" rel="noopener" href="{REPO}">
        <svg><use href="#i-gh"/></svg> Star on GitHub
        <span class="cnt" id="gh-stars-share"></span></a>
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
      <a href="leggi.html">Read online</a>
      <a href="claude-the-complete-guide.pdf" download>Download the PDF</a>
      <a href="changelog.html">Updates</a>
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
    set("sh-wa","https://wa.me/?text="+t+"%20"+u);
    set("sh-tg","https://t.me/share/url?url="+u+"&text="+t);
    set("sh-rd","https://www.reddit.com/submit?url="+u+"&title="+t);
    var copy=document.getElementById("sh-copy"), msg=document.getElementById("copied");
    if(copy)copy.addEventListener("click",function(){{
      var done=function(){{if(msg){{msg.textContent="Link copied!";setTimeout(function(){{msg.textContent="";}},2500);}}}};
      if(navigator.clipboard){{navigator.clipboard.writeText(url).then(done,done);}}else if(msg){{msg.textContent="Copy it from the address bar";setTimeout(function(){{msg.textContent="";}},3500);}}
    }});
    try{{
      fetch("https://api.github.com/repos/angelogeminiani/claude-la-guida-completa")
        .then(function(r){{return r.ok?r.json():null;}})
        .then(function(d){{
          // Hide the counter below a threshold: a tiny number is
          // negative social proof, the plain button works better.
          if(d&&typeof d.stargazers_count==="number"&&d.stargazers_count>=25){{
            ["gh-stars","gh-stars-share"].forEach(function(id){{
              var e=document.getElementById(id);
              if(e)e.textContent="· ★ "+d.stargazers_count;}});}}}});
    }}catch(e){{}}
  }})();
</script>

<script>
  // Plan + model finder. The logic mirrors chapter F.3 of the book
  // (kept in sync with the Italian landing's quiz).
  (function(){{
    var QUESTIONS=[
      {{qn:"Question 1 of 3",h:"What do you mostly want to do?",opts:[
        {{t:"Chat, write, create documents",v:"chat"}},
        {{t:"Code with Claude Code",v:"code"}},
        {{t:"Automate tasks on my files (Cowork)",v:"cowork"}},
        {{t:"Integrate Claude into my software (API)",v:"api"}}]}},
      {{qn:"Question 2 of 3",h:"How much will you use it?",opts:[
        {{t:"A little, just to try it",v:"prova"}},
        {{t:"Every day",v:"daily"}},
        {{t:"A lot, hours a day",v:"heavy"}},
        {{t:"As a team or company",v:"team"}}]}},
      {{qn:"Question 3 of 3",h:"Your most frequent task?",opts:[
        {{t:"Quick, simple answers",v:"haiku"}},
        {{t:"Varied everyday work",v:"sonnet"}},
        {{t:"Complex, difficult reasoning",v:"opus"}}]}}
    ];
    var MODELS={{
      haiku:{{n:"Haiku",w:"the fastest, perfect for short answers and simple tasks."}},
      sonnet:{{n:"Sonnet",w:"the ideal balance and the everyday choice: start here."}},
      opus:{{n:"Opus",w:"the most capable, for complex reasoning and long agentic work."}}
    }};
    var ans=[];
    var quiz=document.getElementById("quiz");
    if(!quiz)return;
    function planFor(use,freq){{
      if(freq==="team")return{{name:"Team or Enterprise",
        why:"For groups and companies: administration, SSO, security and centralized management."}};
      var needsPaid=(use!=="chat");
      if(freq==="heavy")return{{name:"Max",
        why:"Heavy use: Max raises the usage limits well beyond Pro, with the same products."}};
      if(freq==="prova"&&!needsPaid)return{{name:"Free",
        why:"To get started with chat, web search and file creation. Note: Code, Cowork and Design require at least Pro."}};
      return{{name:"Pro",why:needsPaid
        ?"It's the watershed: it unlocks Claude Code, Cowork and Design, which Free doesn't include."
        :"For everyday use: unlimited Projects, more models and all the products."}};
    }}
    function render(i){{
      if(i>=QUESTIONS.length){{result();return;}}
      var q=QUESTIONS[i],dots="";
      for(var d=0;d<QUESTIONS.length;d++)dots+='<i class="'+(d<=i?"on":"")+'"></i>';
      var opts=q.opts.map(function(o){{
        return '<button class="opt" data-v="'+o.v+'">'+o.t+'</button>';}}).join("");
      quiz.innerHTML='<div class="q-step"><p class="qn">'+q.qn+'</p><h3>'+q.h+
        '</h3><div class="opts">'+opts+'</div></div><div class="progress">'+dots+'</div>';
      Array.prototype.forEach.call(quiz.querySelectorAll(".opt"),function(b){{
        b.addEventListener("click",function(){{ans[i]=b.getAttribute("data-v");render(i+1);}});
      }});
    }}
    function result(){{
      var p=planFor(ans[0],ans[1]),m=MODELS[ans[2]]||MODELS.sonnet;
      var share="I found my Claude setup: "+p.name+" plan + "+m.n+
        " model. What's yours? "+location.href.split("#")[0];
      quiz.innerHTML=
        '<div class="result"><p class="pick">Our suggestion for you</p>'+
        '<p class="big">Plan <b>'+p.name+'</b> · model <b>'+m.n+'</b></p>'+
        '<p class="why">'+p.why+' About the model: '+m.w+'</p><div class="row">'+
        '<a class="btn btn-primary" href="capitoli/F-3-modelli-e-piani.html">'+
        'Read more in ch. F.3 →</a>'+
        '<a class="sbtn" target="_blank" rel="noopener" '+
        'href="https://twitter.com/intent/tweet?text='+encodeURIComponent(share)+'">'+
        '<svg><use href="#i-x"/></svg> Share the result</a></div>'+
        '<button class="restart" id="quiz-restart" type="button">Start over</button></div>';
      var r=document.getElementById("quiz-restart");
      if(r)r.addEventListener("click",function(){{ans=[];render(0);}});
    }}
    render(0);
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
