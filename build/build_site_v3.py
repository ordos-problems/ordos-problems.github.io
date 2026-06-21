import html
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PAGES = ROOT / "problems"

data = json.load(open(ROOT / "problems_render.json"))
meta = data["metadata"]
embedded = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")


def esc(value):
    return html.escape(str(value or ""), quote=True)


def slugify(value):
    value = re.sub(r"[^a-z0-9]+", "-", str(value).lower()).strip("-")
    return value or "tag"


def page_name(problem):
    return f"{problem['id']}.html"


def problem_url(problem):
    return f"problems/{page_name(problem)}"


def full_problem_text(problem):
    open_problem = problem.get("open_problem") or open_problem_text(problem)
    refs = "\n".join(
        "- {authors}, {title} ({meta}){url}".format(
            authors=r.get("authors", ""),
            title=r.get("title", ""),
            meta=", ".join(str(x) for x in [r.get("year"), r.get("venue")] if x),
            url=(" " + r["url"]) if r.get("url") else "",
        )
        for r in problem.get("additional_refs", [])
    )
    return (
        f"ORdős Problems #{problem['number']} — {problem['title']}\n\n"
        f"SHORT STATEMENT\n{problem['short_statement']}\n\n"
        f"OPEN PROBLEM\n{open_problem}\n\n"
        f"PROBLEM (full statement with model)\n{problem['full_statement']}\n\n"
        + (f"KNOWN RESULTS\n{problem.get('known_results','')}\n\n" if problem.get("known_results") else "")
        + f"REMAINING OPEN PROBLEM\n{open_problem}\n\n"
        + "WHERE POSED: "
        + (problem.get("where_posed", {}) or {}).get("text", "")
        + (f" ({problem.get('where_posed', {}).get('url')})" if problem.get("where_posed", {}).get("url") else "")
        + "\n"
        + "SOURCE: "
        + problem.get("source", {}).get("authors", "")
        + ", "
        + problem.get("source", {}).get("title", "")
        + " ("
        + ", ".join(str(x) for x in [problem.get("source", {}).get("year"), problem.get("source", {}).get("venue")] if x)
        + ")"
        + (f" {problem.get('source', {}).get('url')}" if problem.get("source", {}).get("url") else "")
        + "\n"
        + (f"RELATED:\n{refs}\n" if refs else "")
        + "\nTask: Resolve this open problem (prove the conjecture, determine the exact value/ratio, or characterize the optimal policy). Math is in LaTeX."
    )


def script_json(value):
    return json.dumps(value, ensure_ascii=False).replace("</", "<\\/")


def strip_markup(value):
    value = re.sub(r"\\textbf\{([^{}]*)\}", r"\1", str(value or ""))
    value = re.sub(r"\s+", " ", value).strip()
    return value


def open_problem_text(problem):
    full = strip_markup(problem.get("full_statement", ""))
    markers = ["Open:", "Open Problem:", "Question:", "Conjecture:"]
    for marker in markers:
        idx = full.find(marker)
        if idx >= 0:
            tail = full[idx + len(marker):].strip()
            # Keep the extracted task concise for navigation/copy text.
            split = re.split(r"(?<=[.!?])\s+", tail, maxsplit=2)
            chosen = " ".join(split[:2]).strip()
            if chosen:
                return chosen
    short = strip_markup(problem.get("short_statement", ""))
    return f"Resolve the question in this model: {short}"


COMMON_HEAD = r"""
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=EB+Garamond:wght@400;500;600;700&family=Figtree:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.css">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<style>
  :root{
    --bg:#ffffeb; --paper:#fffef6; --paper2:#fff9fd; --ink:#1a1a1a; --soft:#4b514d; --faint:#7b7d6f;
    --line:#e4e4d0; --line2:#eeeedd; --strong:#1a1a1a; --accent:#034f46; --accent2:#0f675d;
    --pink:#f0d7ff; --pink2:#f8edff; --orange:#ffa946; --link:#034f46; --tagink:#46514d;
    --maxw:1120px; --measure:860px; --radius:12px;
    --ui:"Figtree","Avenir Next","Avenir",-apple-system,system-ui,"Segoe UI",Arial,sans-serif;
    --display:"EB Garamond","Iowan Old Style","Palatino Linotype",Georgia,serif;
  }
  *{box-sizing:border-box}
  html{scroll-behavior:smooth}
  body{margin:0;background:var(--bg);color:var(--ink);font-family:var(--ui);font-size:17px;line-height:1.62;
    -webkit-font-smoothing:antialiased;text-rendering:optimizeLegibility;overflow-x:hidden;}
  a{color:var(--link);text-decoration-thickness:1px;text-underline-offset:3px;}
  .wrap{max-width:var(--maxw);margin:0 auto;padding:0 28px 96px;}

  header.site{padding:42px 0 22px;border-bottom:1px solid var(--line);}
  .headbar{display:grid;grid-template-columns:minmax(320px,max-content) minmax(280px,1fr);gap:22px;align-items:center;}
  .brand{display:flex;align-items:center;gap:14px;min-width:0;}
  .logo-link{display:block;width:42px;height:42px;flex:0 0 auto;border-radius:10px;line-height:0;}
  .logo-link:focus-visible{outline:3px solid var(--orange);outline-offset:3px;}
  .mono{width:42px;height:42px;flex:0 0 auto;}
  h1{font-family:var(--display);font-weight:600;font-size:3rem;letter-spacing:0;margin:0;line-height:1;color:var(--ink);}
  h1 .or{color:var(--accent);}
  .aboutbtn{font-size:.78rem;color:var(--ink);background:var(--pink);border:2px solid var(--strong);
    border-radius:10px;padding:7px 12px;cursor:pointer;font-family:var(--ui);font-weight:750;text-decoration:none;box-shadow:0 1px 0 var(--strong);white-space:nowrap;}
  .aboutbtn:hover{background:#f5e5ff;}
  .sub{color:var(--soft);font-size:1.03rem;margin:16px 0 0;max-width:78ch;font-weight:450;}
  .headsearch{display:flex;justify-content:flex-end;align-items:center;gap:10px;}
  .headsearch input{max-width:460px;}

  .tagfilters{margin-top:20px;}
  .statbar{display:flex;gap:8px;flex-wrap:wrap;align-items:center;}
  .statbtn{appearance:none;text-align:left;background:var(--paper);border:1px solid var(--line);border-radius:var(--radius);
    padding:6px 10px;min-height:34px;min-width:0;display:flex;align-items:center;gap:6px;cursor:pointer;
    color:var(--faint);font-family:var(--ui);transition:background .15s,border-color .15s,transform .15s;}
  .statbtn b{display:block;color:var(--ink);font-size:.78rem;line-height:1;font-weight:800;}
  .statbtn span{font-size:.78rem;line-height:1;color:var(--tagink);overflow-wrap:anywhere;}
  .statbtn:hover{background:var(--pink2);border-color:#dac6e6;transform:translateY(-1px);}
  .statbtn.active{background:var(--pink);border:2px solid var(--strong);padding:5px 9px;color:var(--ink);}
  .moretags{display:flex;align-items:center;gap:8px;margin-top:10px;}
  .moretags label{font-size:.76rem;font-weight:800;color:var(--faint);text-transform:uppercase;letter-spacing:.06em;}
  #tagselect{min-width:230px;max-width:100%;padding:8px 10px;font-size:.82rem;border:1px solid var(--line);
    border-radius:var(--radius);background:var(--paper);color:var(--ink);font-family:var(--ui);}
  #tagselect:focus{outline:3px solid #d8ece7;border-color:#74aaa1;}

  .modal{position:fixed;inset:0;z-index:100;display:none;align-items:center;justify-content:center;padding:24px;background:rgba(26,26,26,.32);}
  .modal.open{display:flex;}
  .modal-card{width:min(760px,100%);max-height:min(86vh,760px);overflow:auto;background:#fffdf2;border:2px solid var(--strong);
    border-radius:var(--radius);box-shadow:0 18px 60px rgba(0,0,0,.18);padding:28px 32px;}
  .modal-top{display:flex;align-items:flex-start;justify-content:space-between;gap:18px;margin-bottom:14px;}
  .modal-card h2{font-family:var(--display);font-weight:600;font-size:2.1rem;line-height:1.05;margin:0;color:var(--ink);}
  .modal-card h3{font-size:.78rem;letter-spacing:.08em;text-transform:uppercase;color:var(--accent);font-weight:800;margin:22px 0 7px;}
  .modal-card p{font-size:1rem;line-height:1.7;color:#303633;margin:.7em 0;}
  .closemodal{appearance:none;border:2px solid var(--strong);border-radius:10px;background:var(--pink);color:var(--ink);
    font-family:var(--ui);font-weight:800;cursor:pointer;padding:5px 10px;box-shadow:0 1px 0 var(--strong);}

  .controls{position:sticky;top:0;z-index:20;background:rgba(255,255,235,.96);backdrop-filter:saturate(1.05) blur(10px);
    border-bottom:1px solid var(--line);padding:11px 0;margin:18px 0 14px;}
  #q{width:100%;padding:12px 14px;font-size:.94rem;border:1px solid var(--line);border-radius:var(--radius);background:var(--paper);color:var(--ink);font-family:var(--ui);}
  #q:focus{outline:3px solid #d8ece7;border-color:#74aaa1;}
  .ctl-meta{display:flex;justify-content:space-between;align-items:center;gap:12px;}
  .filterstate{display:flex;align-items:center;gap:10px;flex-wrap:wrap;}
  .count{font-size:.8rem;color:var(--faint);}
  .selectedtags{display:flex;align-items:center;gap:6px;flex-wrap:wrap;}
  .selectedtag{appearance:none;border:1px solid var(--strong);background:var(--pink);border-radius:999px;padding:4px 8px;
    font-family:var(--ui);font-size:.74rem;font-weight:750;color:var(--ink);cursor:pointer;}
  .selectedtag:hover{background:#f5e5ff;}
  .clearfilter{font-size:.8rem;color:var(--link);background:none;border:none;cursor:pointer;font-family:var(--ui);padding:0;font-weight:700;}

  .grouphdr{font-weight:800;font-size:.78rem;letter-spacing:.07em;text-transform:uppercase;color:var(--accent);
    margin:34px 0 10px;padding-bottom:8px;border-bottom:1px solid var(--line);}
  .grouphdr .gn{color:var(--faint);font-weight:500;}

  article.p{background:#fffdf2;border:2px solid var(--strong);border-radius:var(--radius);
    padding:20px 22px 19px;margin:12px 0;scroll-margin-top:96px;}
  article.p:target{box-shadow:0 0 0 3px #d8ece7;}
  .p .top{display:flex;align-items:center;gap:12px;flex-wrap:wrap;margin-bottom:10px;}
  .num{font-weight:800;font-size:.76rem;color:#fff;background:var(--accent);padding:3px 9px;border-radius:7px;text-decoration:none;}
  .num:hover{background:#063f39;}
  .tagline{display:flex;gap:9px;flex-wrap:wrap;align-items:center;min-width:0;color:var(--tagink);font-size:.9rem;}
  .tag{color:var(--tagink);white-space:nowrap;}
  .tag.status-open{color:#7a5400;}
  .tag.status-partial{color:#155879;}
  .tag.med{color:#97402d;}
  .spacer{flex:1 1 auto;}
  .copy,.open-link,.back-link{font-size:.78rem;color:var(--ink);background:var(--pink);border:2px solid var(--strong);
    border-radius:10px;padding:7px 12px;cursor:pointer;font-family:var(--ui);font-weight:750;text-decoration:none;box-shadow:0 1px 0 var(--strong);}
  .copy:hover,.open-link:hover,.back-link:hover{background:#f5e5ff;}
  .copy.ok{background:#d8ead8;color:#064d20;}

  .problem-title{font-family:var(--display);font-size:1.42rem;line-height:1.18;font-weight:600;margin:0 0 8px;color:var(--ink);letter-spacing:0;}
  .problem-title a{text-decoration:none;color:inherit;}
  .problem-title a:hover{text-decoration:underline;text-decoration-thickness:1px;}
  .short{font-size:1rem;line-height:1.62;font-weight:500;margin:0 0 14px;color:#27302c;max-width:88ch;letter-spacing:0;}
  .card-actions{display:flex;gap:10px;align-items:center;flex-wrap:wrap;}
  .pagination{display:flex;align-items:center;justify-content:center;gap:5px;flex-wrap:nowrap;margin:24px 0 0;overflow-x:auto;padding-bottom:3px;}
  .pagebtn{font-size:.76rem;color:var(--ink);background:#fffdf2;border:2px solid var(--strong);border-radius:8px;
    padding:5px 8px;cursor:pointer;font-family:var(--ui);font-weight:800;min-width:30px;box-shadow:0 1px 0 var(--strong);white-space:nowrap;}
  .pagebtn:hover:not(:disabled),.pagebtn.active{background:var(--pink);}
  .pagebtn:disabled{opacity:.42;cursor:not-allowed;box-shadow:none;}
  .pagegap,.pageinfo{font-size:.76rem;color:var(--faint);font-weight:750;padding:0 3px;white-space:nowrap;}

  .detail-top{display:flex;align-items:center;justify-content:space-between;gap:16px;margin:24px 0 28px;}
  .detail-title{font-family:var(--display);font-size:3rem;line-height:1.04;font-weight:600;margin:0;color:var(--ink);max-width:900px;}
  .detail-meta{display:flex;gap:10px;flex-wrap:wrap;margin:16px 0 0;}
  .problem-nav{display:flex;gap:10px;align-items:stretch;justify-content:space-between;margin:22px 0 24px;max-width:var(--measure);}
  .problem-nav .navlink{flex:1 1 0;background:#fffdf2;border:2px solid var(--strong);border-radius:var(--radius);padding:12px 14px;
    text-decoration:none;color:var(--ink);font-weight:750;min-width:0;}
  .problem-nav .navlink:hover{background:var(--pink2);}
  .problem-nav .navlink.next{text-align:right;}
  .problem-nav .navlink.empty{visibility:hidden;}
  .problem-nav .navlabel{display:block;font-size:.72rem;letter-spacing:.07em;text-transform:uppercase;color:var(--faint);font-weight:800;margin-bottom:2px;}
  .detail-card{background:#fffdf2;border:2px solid var(--strong);border-radius:var(--radius);padding:28px 32px;margin:24px 0;max-width:var(--measure);}
  .detail-card h2{font-size:.8rem;letter-spacing:.08em;text-transform:uppercase;color:var(--accent);font-weight:800;margin:0 0 15px;}
  .prose{font-size:1.04rem;line-height:1.86;color:#252b28;}
  .prose p{margin:0 0 1.15em;}
  .prose .katex-display{margin:1.15em 0;}
  .known-prose{font-size:1rem;line-height:1.8;color:#303633;}
  .remaining-open{margin-top:18px;padding-top:14px;border-top:1px solid var(--line);}
  .remaining-open strong{color:var(--accent);}
  .source-list{font-size:.94rem;line-height:1.7;color:var(--soft);}
  .source-list p{margin:.65em 0;}
  .source-list .k{font-weight:800;color:var(--accent);}
  .refs{margin:8px 0 0;padding-left:21px;}
  .refs li{margin:.55em 0;color:var(--soft);}

  .katex{font-size:1.04em;}
  .katex-display{margin:.7em 0;overflow-x:auto;overflow-y:hidden;padding:2px 0;}

  footer{margin-top:48px;font-size:.8rem;color:var(--faint);border-top:1px solid var(--line);padding-top:18px;}
  footer a{color:var(--accent);font-weight:800;text-decoration:none;border-bottom:1px solid rgba(3,79,70,.28);}
  footer a:hover{border-bottom-color:var(--accent);}
  .toast{position:fixed;bottom:24px;left:50%;transform:translateX(-50%) translateY(20px);background:var(--ink);color:#fff;font-size:.85rem;padding:10px 18px;border-radius:10px;opacity:0;transition:.25s;pointer-events:none;z-index:50;}
  .toast.show{opacity:1;transform:translateX(-50%) translateY(0);}
  @media (max-width:900px){
    .headbar{grid-template-columns:1fr;}
    .headsearch{justify-content:flex-start;}
    .headsearch input{max-width:none;}
  }
  @media (max-width:760px){
    .wrap{padding:0 16px 72px;}
    header.site{padding-top:30px;}
    .brand{align-items:flex-start;}
    .brand h1{min-width:0;overflow-wrap:anywhere;}
    h1{font-size:2.15rem}
    .sub,.about,.problem-title,.short,.prose,.known-prose{overflow-wrap:anywhere;}
    .statbar{gap:6px;}
    .statbtn{padding:5px 8px;}
    .moretags{align-items:flex-start;flex-direction:column;}
    .ctl-meta{align-items:flex-start;gap:8px;flex-direction:column;}
    article.p{padding:17px 15px;}
    .copy,.open-link{width:100%;text-align:center;}
    .detail-title{font-size:2.2rem;}
    .detail-top{align-items:flex-start;flex-direction:column;}
    .problem-nav{flex-direction:column;}
    .problem-nav .navlink{width:100%;}
    .problem-nav .navlink.next{text-align:left;}
    .detail-card{padding:22px 18px;}
    .modal{padding:14px;}
    .modal-card{padding:22px 18px;}
    .modal-card h2{font-size:1.7rem;}
  }
</style>
"""


def logo_svg():
    return """<svg class="mono" viewBox="0 0 100 100" aria-hidden="true">
        <rect x="3" y="3" width="94" height="94" rx="18" fill="#eef6f5" stroke="#034f46" stroke-width="5"/>
        <text x="50" y="63" text-anchor="middle" font-family="Figtree, Arial, sans-serif" font-size="36" font-weight="800" fill="#034f46">OP</text>
      </svg>"""


def logo_link(href):
    return f'<a class="logo-link" href="{esc(href)}" aria-label="ORdős Problems home">{logo_svg()}</a>'


def index_html():
    return r"""<!DOCTYPE html>
<html lang="en">
<head>
<title>ORdős Problems — Open Problems in CS, OR, OM & Applied Probability</title>
__COMMON_HEAD__
</head>
<body>
<div class="wrap">
  <header class="site">
    <div class="headbar">
      <div class="brand">
        __LOGO__
        <h1 title="a pun on Erdős"><span class="or">OR</span>dős Problems</h1>
      </div>
      <div class="headsearch">
        <button class="aboutbtn" id="aboutbtn" type="button">About</button>
        <input id="q" type="search" placeholder="Search statement, author, tag, area, number…" autocomplete="off">
      </div>
    </div>
    <p class="sub">A collection of Open Problems in Computer Science, Operations Research, Operations Management and Applied Probability.</p>
    <div class="tagfilters">
      <div class="statbar" id="statbar"></div>
      <div class="moretags">
        <label for="tagselect">More tags</label>
        <select id="tagselect">
          <option value="">Add a tag filter…</option>
        </select>
      </div>
    </div>
  </header>

  <div class="controls">
    <div class="ctl-meta">
      <div class="filterstate">
        <span class="count" id="count"></span>
        <span class="selectedtags" id="selectedtags"></span>
      </div>
      <button class="clearfilter" id="clearfilter">Show all problems</button>
    </div>
  </div>

  <main id="list"></main>
  <nav class="pagination" id="pager" aria-label="Problem list pages"></nav>
  <footer><p>Created by <a href="https://akshitkumar.github.io/">Akshit Kumar</a>. Problems curated with help of AI. Please verify for correctness.</p></footer>
</div>
<div class="toast" id="toast">Copied</div>
<div class="modal" id="aboutmodal" role="dialog" aria-modal="true" aria-labelledby="abouttitle">
  <div class="modal-card">
    <div class="modal-top">
      <h2 id="abouttitle">What This Repository Is For</h2>
      <button class="closemodal" id="closeabout" type="button" aria-label="Close about dialog">Close</button>
    </div>
    <p>ORdős Problems is intended to be a repository of hard, unsolved, research-level problems in Operations Research, Computer Science, Economics, and Applied Probability.</p>
    <h3>Ideal Problems</h3>
    <p>The ideal problem here has a relatively clean and parsimonious model, but something fundamental is still missing: the guarantees are not tight, a well-formed conjecture remains open, an algorithm is missing, or the right structural characterization is unknown.</p>
    <h3>What This Is Not</h3>
    <p>This is not primarily a collection of open-ended modelling questions. Modelling problems are important, but it is often unclear what the “right” model should be. The goal here is narrower: concrete hard questions whose resolution could plausibly appear in strong conferences or journals. More open-ended research problems may be added in the future.</p>
    <h3>Contributions</h3>
    <p>Contributions are welcome: new problems, corrections, better citations, more context, clearer exposition, improved known-results summaries, and suggestions about scope or organization. Contributions and corrections can be sent to <strong>ordos.problems@gmail.com</strong>.</p>
  </div>
</div>

<script type="application/json" id="ordos-data">__DATA__</script>
<script>
(function(){
  var DB=JSON.parse(document.getElementById('ordos-data').textContent);
  var P=DB.problems, M=DB.metadata;
  function el(t,c){var e=document.createElement(t);if(c)e.className=c;return e;}
  function txt(t,c,s){var e=el(t,c);e.textContent=s;return e;}
  function slug(s){return String(s||'').toLowerCase().replace(/[^a-z0-9]+/g,'-').replace(/^-|-$/g,'');}
  function discipline(p){
    var c=p.collection;
    if(c==='Operations Research'||c.indexOf('Online Resource')===0)return 'Operations Research';
    if(c==='Operations Management')return 'Operations Management';
    if(c==='Management Science')return 'Management Science';
    if(c==='Applied Probability')return 'Applied Probability';
    return 'Computer Science';
  }
  function page(p){return 'problems/'+p.id+'.html';}

  var sb=document.getElementById('statbar'), selectedTags=[];
  function tagsFor(p){
    var out=[p.status,discipline(p),p.area,p.collection].concat(p.tags||[]);
    var seen={};
    return out.map(slug).filter(function(t){if(!t||seen[t])return false;seen[t]=1;return true;});
  }
  var tagCounts={all:M.count};
  P.forEach(function(p){tagsFor(p).forEach(function(t){tagCounts[t]=(tagCounts[t]||0)+1;});});
  var priority=['all','open','operations-research','operations-management','management-science','applied-probability',
    'online-matching','prophet-inequality','scheduling','approximation-algorithms','fair-division','inventory'];
  var tiles=priority.filter(function(t){return tagCounts[t];})
    .map(function(t){return {tag:t,count:tagCounts[t]};});
  var extraTags=Object.keys(tagCounts).filter(function(t){return t!=='all'&&priority.indexOf(t)<0&&tagCounts[t]>=2;})
    .sort(function(a,b){return tagCounts[b]-tagCounts[a]||a.localeCompare(b);})
  var tagselect=document.getElementById('tagselect');
  extraTags.forEach(function(t){
    var o=document.createElement('option');o.value=t;o.textContent='#'+t+' ('+tagCounts[t]+')';tagselect.appendChild(o);
  });
  function hasSelected(tag){return selectedTags.indexOf(tag)>=0;}
  function addTag(tag){if(tag&&tag!=='all'&&!hasSelected(tag))selectedTags.push(tag);}
  function removeTag(tag){selectedTags=selectedTags.filter(function(t){return t!==tag;});}
  function toggleTag(tag){
    if(tag==='all'){selectedTags=[];apply();return;}
    if(hasSelected(tag))removeTag(tag);else addTag(tag);
    apply();
  }
  tiles.forEach(function(t){
    var b=el('button','statbtn');b.type='button';b.dataset.tag=t.tag;
    b.innerHTML='<b>'+t.count+'</b><span>#'+t.tag+'</span>';
    b.addEventListener('click',function(){toggleTag(t.tag);});
    sb.appendChild(b);
  });
  tagselect.addEventListener('change',function(){
    addTag(tagselect.value);
    tagselect.value='';
    apply();
  });

  var list=document.getElementById('list'), items=[], pageSize=5, currentPage=1;
  P.slice().sort(function(a,b){return a.number-b.number;}).forEach(function(p){list.appendChild(card(p));});

  function tag(text, cls){
    var s=txt('span','tag '+(cls||''),'#'+slug(text));
    return s;
  }
  function card(p){
    var a=el('article','p');a.id=String(p.number);
    var top=el('div','top');
    var num=el('a','num');num.href=page(p);num.textContent=p.number;num.title=p.ref;top.appendChild(num);
    var tags=el('div','tagline');
    tags.appendChild(tag(p.status,p.status==='partially resolved'?'status-partial':'status-open'));
    tags.appendChild(tag(p.area));
    (p.tags||[]).slice(0,3).forEach(function(t){tags.appendChild(tag(t));});
    if(p.confidence==='medium'||p.confidence==='low')tags.appendChild(tag('check source','med'));
    top.appendChild(tags);
    top.appendChild(el('span','spacer'));
    var cp=txt('button','copy','Copy for solver');cp.addEventListener('click',function(){copySolver(p,cp);});top.appendChild(cp);
    a.appendChild(top);

    var title=el('h2','problem-title');var link=el('a');link.href=page(p);link.textContent=p.title;title.appendChild(link);a.appendChild(title);
    var sh=el('p','short');sh.innerHTML=p.short_html;a.appendChild(sh);
    var actions=el('div','card-actions');
    var open=txt('a','open-link','Open full problem');open.href=page(p);actions.appendChild(open);
    a.appendChild(actions);

    var filterTags=tagsFor(p);
    var hay=[String(p.number),p.ref,p.short_statement,p.full_statement,p.known_results,(p.tags||[]).join(' '),p.area,p.collection,p.source.authors,p.source.title,discipline(p),filterTags.join(' ')].join(' ').toLowerCase();
    items.push({el:a,hay:hay,tags:filterTags});
    return a;
  }

  function copySolver(p,btn){
    var refs=(p.additional_refs||[]).map(function(r){return '- '+(r.authors||'')+', '+(r.title||'')+' ('+[r.year,r.venue].filter(Boolean).join(', ')+')'+(r.url?' '+r.url:'');}).join('\n');
    var t='ORdős Problems #'+p.number+' — '+p.title+'\n\nSHORT STATEMENT\n'+p.short_statement+'\n\nPROBLEM (full statement with model)\n'+p.full_statement+'\n\n'
      +(p.known_results?('KNOWN RESULTS\n'+p.known_results+'\n\n'):'')
      +'WHERE POSED: '+((p.where_posed&&p.where_posed.text)||'')+(p.where_posed&&p.where_posed.url?(' ('+p.where_posed.url+')'):'')+'\n'
      +'SOURCE: '+(p.source.authors||'')+', '+(p.source.title||'')+' ('+[p.source.year,p.source.venue].filter(Boolean).join(', ')+')'+(p.source.url?(' '+p.source.url):'')+'\n'
      +(refs?('RELATED:\n'+refs+'\n'):'')
      +'\nTask: Resolve this open problem (prove the conjecture, determine the exact value/ratio, or characterize the optimal policy). Math is in LaTeX.';
    navigator.clipboard.writeText(t).then(function(){btn.classList.add('ok');btn.textContent='Copied';toast('Full problem copied');setTimeout(function(){btn.classList.remove('ok');btn.textContent='Copy for solver';},1500);});
  }
  var te=document.getElementById('toast'),tt;
  function toast(m){te.textContent=m;te.classList.add('show');clearTimeout(tt);tt=setTimeout(function(){te.classList.remove('show');},1500);}

  var aboutBtn=document.getElementById('aboutbtn'),aboutModal=document.getElementById('aboutmodal'),closeAbout=document.getElementById('closeabout');
  function openAbout(){aboutModal.classList.add('open');closeAbout.focus();}
  function closeAboutModal(){aboutModal.classList.remove('open');aboutBtn.focus();}
  aboutBtn.addEventListener('click',openAbout);
  closeAbout.addEventListener('click',closeAboutModal);
  aboutModal.addEventListener('click',function(e){if(e.target===aboutModal)closeAboutModal();});
  document.addEventListener('keydown',function(e){if(e.key==='Escape'&&aboutModal.classList.contains('open'))closeAboutModal();});

  var q=document.getElementById('q'),cnt=document.getElementById('count'),selectedBox=document.getElementById('selectedtags'),clear=document.getElementById('clearfilter'),pager=document.getElementById('pager');
  function renderPager(totalPages,totalMatches){
    pager.innerHTML='';
    if(totalMatches===0)return;
    function button(label,page,cls,disabled){
      var b=txt('button','pagebtn '+(cls||''),label);
      b.type='button';
      b.disabled=!!disabled;
      b.addEventListener('click',function(){currentPage=page;apply(false,true);});
      pager.appendChild(b);
    }
    function gap(){pager.appendChild(txt('span','pagegap','...'));}
    function pageNumbers(){
      var pages=[], seen={};
      [1,currentPage-1,currentPage,currentPage+1,totalPages].forEach(function(p){
        if(p>=1&&p<=totalPages&&!seen[p]){seen[p]=1;pages.push(p);}
      });
      pages.sort(function(a,b){return a-b;});
      pages.forEach(function(p,i){
        if(i&&p-pages[i-1]>1)gap();
        button(String(p),p,p===currentPage?'active':'',false);
      });
    }
    button('Previous',Math.max(1,currentPage-1),'',currentPage===1);
    pageNumbers();
    button('Next',Math.min(totalPages,currentPage+1),'',currentPage===totalPages);
    pager.appendChild(txt('span','pageinfo','Page '+currentPage+' of '+totalPages));
  }
  function apply(resetPage,scrollList){
    if(resetPage!==false)currentPage=1;
    var t=q.value.trim().toLowerCase().replace(/#/g,'').split(/\s+/).filter(Boolean),matched=[];
    document.querySelectorAll('.statbtn').forEach(function(b){b.classList.toggle('active',(selectedTags.length===0&&b.dataset.tag==='all')||hasSelected(b.dataset.tag));});
    selectedBox.innerHTML='';
    selectedTags.forEach(function(tag){
      var pill=txt('button','selectedtag','#'+tag+' ×');
      pill.type='button';
      pill.title='Remove #'+tag;
      pill.addEventListener('click',function(){removeTag(tag);apply();});
      selectedBox.appendChild(pill);
    });
    items.forEach(function(it){
      var ok=true;
      if(selectedTags.length)ok=selectedTags.some(function(tag){return it.tags.indexOf(tag)>=0;});
      if(ok&&t.length)ok=t.every(function(w){return it.hay.indexOf(w)>=0;});
      it.el.style.display='none';
      if(ok)matched.push(it);
    });
    var totalPages=Math.max(1,Math.ceil(matched.length/pageSize));
    if(currentPage>totalPages)currentPage=totalPages;
    var start=(currentPage-1)*pageSize,end=Math.min(start+pageSize,matched.length);
    matched.slice(start,end).forEach(function(it){it.el.style.display='';});
    var range=matched.length?((start+1)+'-'+end):'0';
    cnt.textContent='Showing '+range+' of '+matched.length+' matching problems'+(matched.length!==items.length?' ('+items.length+' total)':'')+(selectedTags.length?' tagged '+selectedTags.map(function(t){return '#'+t;}).join(' or '):'');
    renderPager(totalPages,matched.length);
    if(scrollList)window.scrollTo({top:Math.max(0,list.getBoundingClientRect().top+window.pageYOffset-18),behavior:'smooth'});
  }
  q.addEventListener('input',function(){apply(true,false);});
  clear.addEventListener('click',function(){selectedTags=[];q.value='';tagselect.value='';apply(true,false);});
  apply();
})();
</script>
</body>
</html>
"""


def source_link(source, text="source"):
    url = source.get("url") if source else ""
    return f'<a href="{esc(url)}" target="_blank" rel="noopener">{esc(text)}</a>' if url else esc(text)


def nav_item(problem, label, cls):
    if not problem:
        return '<span class="navlink empty" aria-hidden="true"></span>'
    return (
        f'<a class="navlink {cls}" href="{esc(page_name(problem))}">'
        f'<span class="navlabel">{esc(label)}</span>'
        f'#{problem["number"]} · {esc(problem["title"])}</a>'
    )


def detail_html(problem, prev_problem=None, next_problem=None):
    tags = [problem["area"], problem["status"], problem["collection"]] + list(problem.get("tags", []))
    if problem.get("confidence") in ("medium", "low"):
        tags.append("check source")
    deduped_tags = []
    seen_tags = set()
    for tag in tags:
        key = slugify(tag)
        if key and key not in seen_tags:
            seen_tags.add(key)
            deduped_tags.append(tag)
    tag_html = "\n".join(f'<span class="tag">#{esc(slugify(t))}</span>' for t in deduped_tags if t)
    where = problem.get("where_posed", {}) or {}
    source = problem.get("source", {}) or {}
    refs = problem.get("additional_refs", []) or []
    refs_html = ""
    if refs:
        refs_html = "<ol class=\"refs\">" + "".join(
            "<li>{authors}, <em>{title}</em> ({meta}) {url}</li>".format(
                authors=esc(r.get("authors", "")),
                title=esc(r.get("title", "")),
                meta=esc(", ".join(str(x) for x in [r.get("year"), r.get("venue")] if x)),
                url=source_link(r, "link") if r.get("url") else "",
            )
            for r in refs
        ) + "</ol>"
    known_html = problem.get("known_html") or esc(problem.get("known_results", ""))
    open_summary_html = problem.get("open_problem_html") or esc(problem.get("open_problem", "")) or problem.get("short_html") or esc(problem.get("short_statement", ""))
    remaining_open_html = f'<p class="remaining-open"><strong>Remaining open problem.</strong> {open_summary_html}</p>'
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<title>{esc(problem['title'])} | ORdős Problems</title>
{COMMON_HEAD}
</head>
<body>
<div class="wrap">
  <header class="site">
    <div class="brand">
      {logo_link("../index.html")}
      <h1><a href="../index.html" style="color:inherit;text-decoration:none"><span class="or">OR</span>dős Problems</a></h1>
    </div>
    <p class="sub">A collection of Open Problems in Computer Science, Operations Research, Operations Management and Applied Probability.</p>
  </header>

  <div class="detail-top">
    <div>
      <div class="tagline">{tag_html}</div>
      <h1 class="detail-title">{esc(problem['title'])}</h1>
      <div class="detail-meta"><span class="num">{problem['number']}</span><span class="tag">Problem {problem['number']} of {meta['count']}</span><span class="tag">#{esc(problem['ref'].lower())}</span></div>
    </div>
    <a class="back-link" href="../index.html">Back to all problems</a>
  </div>

  <nav class="problem-nav" aria-label="Problem navigation">
    {nav_item(prev_problem, 'Previous problem', 'prev')}
    {nav_item(next_problem, 'Next problem', 'next')}
  </nav>

  <section class="detail-card statement">
    <h2>Short Statement</h2>
    <div class="prose"><p>{problem.get('short_html') or esc(problem.get('short_statement',''))}</p></div>
  </section>

  <section class="detail-card statement">
    <h2>Open Problem</h2>
    <div class="prose"><p>{open_summary_html}</p></div>
  </section>

  <section class="detail-card statement">
    <h2>Statement &amp; Model</h2>
    <div class="prose">{problem.get('full_html') or esc(problem.get('full_statement',''))}</div>
  </section>

  <section class="detail-card">
    <h2>What Is Known</h2>
    <div class="known-prose">{known_html or '<p>No known-results summary has been added yet.</p>'}{remaining_open_html}</div>
  </section>

  <section class="detail-card">
    <h2>Sources</h2>
    <div class="source-list">
      <p><span class="k">Where posed:</span> {(where.get('text_html') or esc(where.get('text','')))} {source_link(where, 'link') if where.get('url') else ''}</p>
      <p><span class="k">Source:</span> {esc(source.get('authors',''))}, <em>{esc(source.get('title',''))}</em> ({esc(', '.join(str(x) for x in [source.get('year'), source.get('venue')] if x))}) {source_link(source, 'link') if source.get('url') else ''}</p>
      {('<p><span class="k">Related references:</span></p>' + refs_html) if refs_html else ''}
    </div>
  </section>

  <section class="detail-card">
    <h2>Copy for Solver</h2>
    <p class="known-prose">Copy the full statement, known results, and source information as plain text.</p>
    <button class="copy" id="copybtn">Copy full problem</button>
  </section>

  <footer><p>Created by <a href="https://akshitkumar.github.io/">Akshit Kumar</a>. Problems curated with help of AI. Please verify for correctness.</p></footer>
</div>
<div class="toast" id="toast">Copied</div>
<script type="application/json" id="copy-data">{script_json(full_problem_text(problem))}</script>
<script>
(function(){{
  var btn=document.getElementById('copybtn'), toast=document.getElementById('toast'), timer;
  function show(m){{toast.textContent=m;toast.classList.add('show');clearTimeout(timer);timer=setTimeout(function(){{toast.classList.remove('show');}},1500);}}
  btn.addEventListener('click',function(){{
    navigator.clipboard.writeText(JSON.parse(document.getElementById('copy-data').textContent)).then(function(){{
      btn.textContent='Copied';btn.classList.add('ok');show('Full problem copied');
      setTimeout(function(){{btn.textContent='Copy full problem';btn.classList.remove('ok');}},1500);
    }});
  }});
}})();
</script>
</body>
</html>
"""


HTML = (
    index_html()
    .replace("__COMMON_HEAD__", COMMON_HEAD)
    .replace("__LOGO__", logo_link("index.html"))
    .replace("__DATA__", embedded)
    .replace("__GEN__", meta["generated"])
    .replace("__N__", str(meta["count"]))
)

(ROOT / "index.html").write_text(HTML)

PAGES.mkdir(exist_ok=True)
for stale in PAGES.glob("*.html"):
    stale.unlink()
ordered_problems = sorted(data["problems"], key=lambda item: item["number"])
for index, problem in enumerate(ordered_problems):
    prev_problem = ordered_problems[index - 1] if index else None
    next_problem = ordered_problems[index + 1] if index + 1 < len(ordered_problems) else None
    (PAGES / page_name(problem)).write_text(detail_html(problem, prev_problem, next_problem))

print("wrote index.html", len(HTML), "bytes")
print("wrote problem pages", len(data["problems"]))
