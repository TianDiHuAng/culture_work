# -*- coding: utf-8 -*-
"""静态站点生成器：data/*.json + sources.json -> site/。
无外部依赖；输出 UTF-8 HTML，可 file:// 直接打开。
"""
import json, pathlib, html, sys, shutil

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from svggen import render

ROOT = pathlib.Path(__file__).resolve().parent.parent
DATA, SITE = ROOT / "data", ROOT / "site"

def esc(s):
    return html.escape(str(s), quote=True)

# ---------- CSS ----------

CSS = """\
:root{--ink:#33302a;--paper:#fdf9f1;--accent:#8c3b3b;--muted:#8a8378;--line:#e3d9c6;}
*{box-sizing:border-box}
body{margin:0;background:var(--paper);color:var(--ink);font:16px/1.85 "Segoe UI","Microsoft YaHei","PingFang SC",serif}
a{color:var(--accent);text-decoration:none}a:hover{text-decoration:underline}
header.site{background:#2f2a24;color:#f4ead6;padding:14px 24px;display:flex;flex-wrap:wrap;gap:8px 22px;align-items:baseline}
header.site .brand{font-size:20px;letter-spacing:2px}
header.site nav a{color:#e8d9b8;margin-left:4px;font-size:15px}
main{max-width:900px;margin:0 auto;padding:28px 20px 60px}
h1{font-size:26px;margin:.2em 0 .4em}h2{font-size:20px;border-left:4px solid var(--accent);padding-left:10px;margin-top:2.2em}
.meta{color:var(--muted);font-size:14px}
.meta b{color:var(--ink)}
table{border-collapse:collapse;width:100%;font-size:15px}
th,td{border:1px solid var(--line);padding:7px 10px;text-align:left;vertical-align:top}
th{background:#f3ecdd}
blockquote{margin:0;padding:2px 12px;border-left:3px solid var(--line);color:#5c564c}
.src{color:var(--muted);font-size:13px}
.fig{margin:26px 0;text-align:center}
.fig img{max-width:100%;border:1px solid var(--line);border-radius:10px}
.fig .cap{color:var(--muted);font-size:13px;margin-top:6px}
.card{background:#fff;border:1px solid var(--line);border-radius:10px;padding:14px 18px;margin:14px 0}
.filters{display:flex;flex-wrap:wrap;gap:10px;margin:14px 0 20px}
.filters select,.filters input{padding:6px 10px;border:1px solid var(--line);border-radius:6px;background:#fff;font-size:14px}
.worklist{display:grid;grid-template-columns:repeat(auto-fill,minmax(250px,1fr));gap:12px}
.worklist .card{margin:0}
.worklist h3{margin:0 0 6px;font-size:16px}
.worklist .meta{font-size:13px}
.tag{display:inline-block;background:#f3ecdd;border-radius:4px;padding:0 8px;font-size:12px;color:#6b6456;margin-right:6px}
footer.site{color:var(--muted);text-align:center;padding:24px;font-size:13px;border-top:1px solid var(--line);margin-top:40px}
.pending{color:#a8642a}
.crumb{color:var(--muted);font-size:13px;margin-bottom:14px}
.crumb a{color:var(--muted)}
.tl{position:relative;margin:20px 0 20px 8px;border-left:2px solid var(--line);padding-left:22px}
.tl .ev{position:relative;margin-bottom:18px}
.tl .ev:before{content:"";position:absolute;left:-29px;top:8px;width:10px;height:10px;border-radius:50%;background:var(--accent)}
.tl .ev .yr{font-weight:bold;color:var(--accent)}
@media print{header.site,footer.site{display:none}}
"""

NAV = '<header class="site"><span class="brand">中外文学名著导读库</span><nav><a href="index.html">首页</a><a href="works.html">作品总览</a><a href="authors.html">作家索引</a><a href="timeline.html">文学史时间线</a><a href="about.html">关于</a></nav></header>'

def nav(prefix=""):
    if not prefix:
        return NAV
    return NAV.replace('href="', f'href="{prefix}')

FOOT = '<footer class="site">中外文学名著导读库 · 静态站点 · 内容与来源以各页"待核实"节与 sources.json 为准</footer>'

def page(title, body, prefix=""):
    return f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)} · 中外文学名著导读库</title>
<link rel="stylesheet" href="{prefix}style.css">
</head>
<body>
{nav(prefix)}
<main>
{body}
</main>
{FOOT}
</body>
</html>"""

# ---------- 加载数据 ----------

def load_all():
    works = {}
    for p in sorted((DATA / "works").glob("*.json")):
        w = json.loads(p.read_text(encoding="utf-8"))
        works[w["id"]] = w
    authors = {}
    for p in sorted((DATA / "authors").glob("*.json")):
        a = json.loads(p.read_text(encoding="utf-8"))
        authors[a["id"]] = a
    sources = {s["id"]: s for s in json.loads((ROOT / "sources.json").read_text(encoding="utf-8"))}
    return works, authors, sources

def src_ref(sid, sources):
    s = sources.get(sid)
    if not s:
        return f'<span class="src">[来源缺失 {esc(sid)}]</span>'
    label = f"{s['title']}（{s['type']}）"
    return f'<a class="src" href="{esc(s["url"])}" rel="noopener" target="_blank">{esc(label)}</a>'

def paras(lst):
    return "".join(f"<p>{esc(p)}</p>" for p in lst)

# ---------- 作品页 ----------

def work_page(w, authors, sources, works):
    aid = w.get("author_id")
    author_html = esc(w.get("author_name", "")) if not aid else f'<a href="../authors/{aid}.html">{esc(authors[aid]["name"])}</a>' if aid in authors else esc(w.get("author_name", ""))
    body = [f'<div class="crumb"><a href="../index.html">首页</a> › <a href="../works.html">作品总览</a> › {esc(w["title"])}</div>']
    body.append(f"<h1>{esc(w['title'])}</h1>")
    if w.get("original_title") and w["original_title"] != w["title"]:
        body.append(f'<p class="meta">又名：{esc(w["original_title"])}</p>')
    rows = [
        ("作者", author_html + (f'（{esc(w["co_authors"])}）' if w.get("co_authors") else "")),
        ("成书/出版", esc(w.get("year_display", "")) + f' <span class="src">{src_ref(w["year_source"], sources)}</span>'),
        ("国别/地区", esc(w["region"])),
        ("时代", f"{esc(w['era'])} · {esc(w['era_detail'])}"),
        ("体裁", esc(w["genre"])),
        ("语言", esc(w["language"])),
    ]
    body.append("<table>" + "".join(f"<tr><th>{k}</th><td>{v}</td></tr>" for k, v in rows) + "</table>")

    # SVG
    svg_path = SITE / "assets" / "svg" / f"{w['id']}.svg"
    svg_path.parent.mkdir(parents=True, exist_ok=True)
    svg_path.write_text(render(w["svg"]), encoding="utf-8")
    kind = "人物关系图" if w["svg"].get("type") in ("graph", "ring") else "主题·结构图"
    body.append(f'<div class="fig"><img src="../assets/svg/{w["id"]}.svg" alt="{esc(w["title"])}{kind}">'
                f'<div class="cap">{esc(w["svg"].get("caption", kind))}（{kind}）</div></div>')

    body.append("<h2>二、创作背景</h2>" + paras(w["background"]))
    body.append("<h2>三、内容脉络</h2>" + paras(w["outline"]))

    if w.get("characters"):
        body.append("<h2>四、主要人物表</h2><table><tr><th>人物</th><th>身份</th><th>说明</th></tr>")
        for c in w["characters"]:
            body.append(f"<tr><td>{esc(c['name'])}</td><td>{esc(c.get('identity',''))}</td><td>{esc(c.get('note',''))}</td></tr>")
        body.append("</table>")

    body.append("<h2>五、主题与艺术特点</h2>")
    body.append("<ul>" + "".join(f"<li>{esc(t)}</li>" for t in w["themes"]) + "</ul>")

    body.append("<h2>六、影响与评论</h2><ul>")
    for inf in w["influence"]:
        body.append(f"<li>{esc(inf['text'])}<br>{src_ref(inf['source'], sources)}</li>")
    body.append("</ul>")

    r = w["reading"]
    body.append("<h2>七、阅读建议</h2><div class='card'>")
    body.append("<b>难点</b><ul>" + "".join(f"<li>{esc(d)}</li>" for d in r["difficulties"]) + "</ul>")
    body.append("<b>推荐版本</b><ul>" + "".join(f"<li>{esc(d)}</li>" for d in r["editions"]) + "</ul>")
    if r.get("order"):
        body.append(f"<b>入门顺序</b><p>{esc(r['order'])}</p>")
    body.append("</div>")

    body.append("<h2>八、待核实</h2>")
    if w.get("pending"):
        body.append("<ul>" + "".join(f"<li class='pending'>{esc(p)}</li>" for p in w["pending"]) + "</ul>")
    else:
        body.append("<p class='pending'>暂无。</p>")

    body.append("<h2>本页主要来源</h2><ul>" + "".join(f"<li>{src_ref(s, sources)}</li>" for s in w["sources"]) + "</ul>")

    if w.get("related_works"):
        links = "".join(f'<a class="tag" href="../works/{rid}.html">{esc(works[rid]["title"])}</a>' for rid in w["related_works"] if rid in works)
        body.append(f"<p><b>相关作品：</b>{links}</p>")
    if aid and aid in authors:
        a = authors[aid]
        links = "".join(f'<a class="tag" href="../works/{wid}.html">{esc(works[wid]["title"])}</a>' for wid, _ in [(mw.get("work_id"), 0) for mw in a.get("major_works", [])] if wid in works)
        body.append(f"<p><b>{esc(a['name'])}的其他收录作品：</b>{links}</p>")
    return page(w["title"], "\n".join(body), prefix="../")

# ---------- 作家页 ----------

def author_page(a, works, sources):
    body = [f'<div class="crumb"><a href="../index.html">首页</a> › <a href="../authors.html">作家索引</a> › {esc(a["name"])}</div>']
    body.append(f"<h1>{esc(a['name'])}</h1>")
    fn = a.get("foreign_name")
    if fn:
        body.append(f'<p class="meta">{esc(fn)}</p>')
    birth = esc(a.get("birth", "?"))
    death = esc(a.get("death", "?"))
    body.append(f'<p class="meta"><b>{birth} — {death}</b> · {esc(a["country"])} · {esc(a["era"])}'
                f' <span class="src">{src_ref(a["dates_source"], sources)}</span></p>')
    body.append(paras([a["summary"]]) if isinstance(a["summary"], str) else paras(a["summary"]))

    body.append("<h2>生平年谱</h2><div class='tl'>")
    for ev in a["timeline"]:
        src = f' <span class="src">{src_ref(ev["src"], sources)}</span>' if ev.get("src") else ""
        body.append(f'<div class="ev"><span class="yr">{esc(ev["year"])}</span> — {esc(ev["text"])}{src}</div>')
    body.append("</div>")

    if a.get("major_works"):
        body.append("<h2>代表作品</h2><ul>")
        for mw in a["major_works"]:
            wid = mw.get("work_id")
            link = f'<a href="../works/{wid}.html">{esc(works[wid]["title"])}</a>' if wid in works else esc(mw.get("title", ""))
            note = f'：{esc(mw["note"])}</li>' if mw.get("note") else "</li>"
            body.append(f"<li>{link}{note}")
        body.append("</ul>")

    body.append("<h2>风格特点</h2><ul>" + "".join(f"<li>{esc(s)}</li>" for s in a["style"]) + "</ul>")
    body.append("<h2>文学史地位</h2>" + paras(a["status"]))
    body.append("<h2>待核实</h2>")
    body.append("<ul>" + "".join(f"<li class='pending'>{esc(p)}</li>" for p in a.get("pending", [])) + "</ul>" if a.get("pending") else "<p class='pending'>暂无。</p>")
    body.append("<h2>本页主要来源</h2><ul>" + "".join(f"<li>{src_ref(s, sources)}</li>" for s in a["sources"]) + "</ul>")
    return page(a["name"], "\n".join(body), prefix="../")

# ---------- 聚合页 ----------

def work_card(w, prefix="works/"):
    tags = f'<span class="tag">{esc(w["region"])}</span><span class="tag">{esc(w["era_detail"])}</span><span class="tag">{esc(w["genre_group"])}</span>'
    return (f'<div class="card work-item" data-region="{esc(w["region"])}" data-era="{esc(w["era"])}" '
            f'data-group="{esc(w["genre_group"])}"><h3><a href="{prefix}{w["id"]}.html">{esc(w["title"])}</a></h3>'
            f'<div class="meta">{esc(w.get("author_name",""))} · {esc(w.get("year_display",""))}</div><div style="margin-top:6px">{tags}</div></div>')

def overview_page(works, sources):
    items = "".join(work_card(w) for w in sorted(works.values(), key=lambda x: x.get("year_sort", 0)))
    regions = sorted({w["region"] for w in works.values()})
    groups = sorted({w["genre_group"] for w in works.values()})
    opts_r = "".join(f'<option value="{esc(r)}">{esc(r)}</option>' for r in regions)
    opts_g = "".join(f'<option value="{esc(g)}">{esc(g)}</option>' for g in groups)
    body = f"""<h1>作品总览</h1>
<p class="meta">共 {len(works)} 部（中外各 30）。可按国别、时代、体裁筛选；不选即全部显示。禁用 JavaScript 时显示完整列表。</p>
<div class="filters">
<label>国别 <select id="f-region"><option value="">全部</option>{opts_r}</select></label>
<label>时代 <select id="f-era"><option value="">全部</option><option value="古代">古代</option><option value="近代">近代</option><option value="现当代">现当代</option></select></label>
<label>体裁 <select id="f-group"><option value="">全部</option>{opts_g}</select></label>
<label>搜索 <input id="f-q" type="search" placeholder="书名/作者"></label>
</div>
<div class="worklist">{items}</div>
<script>
(function(){{
 function apply(){{
  var r=document.getElementById('f-region').value, e=document.getElementById('f-era').value,
      g=document.getElementById('f-group').value, q=document.getElementById('f-q').value.trim().toLowerCase();
  document.querySelectorAll('.work-item').forEach(function(el){{
   var ok=(!r||el.dataset.region===r)&&(!e||el.dataset.era===e)&&(!g||el.dataset.group===g);
   if(ok&&q){{ok=el.textContent.toLowerCase().indexOf(q)>=0;}}
   el.style.display=ok?'':'none';
  }});
 }}
 ['f-region','f-era','f-group','f-q'].forEach(function(id){{
  var el=document.getElementById(id); el.addEventListener('change',apply); el.addEventListener('input',apply);
 }});
}})();
</script>"""
    return page("作品总览", body)

def authors_index_page(authors, works):
    by_region = {}
    for a in sorted(authors.values(), key=lambda x: (x.get("birth_year") or 0)):
        by_region.setdefault(a["country"], []).append(a)
    body = ["<h1>作家索引</h1>", f'<p class="meta">共 {len(authors)} 位（选集编者与无名氏作品不设作家页）。</p>']
    for region, lst in sorted(by_region.items()):
        body.append(f"<h2>{esc(region)}</h2><ul>")
        for a in lst:
            wids = [mw.get("work_id") for mw in a.get("major_works", []) if mw.get("work_id") in works]
            wl = "、".join(f'<a href="works/{wid}.html">{esc(works[wid]["title"])}</a>' for wid in wids)
            body.append(f"<li><a href='authors/{a['id']}.html'>{esc(a['name'])}</a>"
                        f"（{esc(a.get('birth','?'))}—{esc(a.get('death','?'))}）{('：' + wl) if wl else ''}</li>")
        body.append("</ul>")
    return page("作家索引", "\n".join(body))

def timeline_page(works):
    sorted_w = sorted(works.values(), key=lambda w: (w.get("year_sort", 0), w["region"]))
    body = ["<h1>文学史时间线</h1>",
            "<p class='meta'>按成书/出版年代排序（古代作品年代多有争议，取通行说法；红色为中国作品，蓝色为外国作品）。</p>",
            "<div class='tl'>"]
    for w in sorted_w:
        dot = "#8c3b3b" if w["region"] == "中国" else "#3b6b8c"
        body.append(f'<div class="ev" style="border-left-color:{dot}"><span class="yr">{esc(w.get("year_display",""))}</span> '
                    f'— <a href="works/{w["id"]}.html">{esc(w["title"])}</a>'
                    f'（{esc(w.get("author_name",""))}，{esc(w["region"])}）</div>')
    body.append("</div>")
    return page("文学史时间线", "\n".join(body))

def index_page(works, authors, sources):
    cn = [w for w in works.values() if w["region"] == "中国"]
    fr = [w for w in works.values() if w["region"] != "中国"]
    era_cn = {}
    for w in works.values():
        era_cn[w["era"]] = era_cn.get(w["era"], 0) + 1
    body = f"""<h1>中外文学名著导读库</h1>
<p>本库收录 60 部中外文学名著（中国 30 部、外国 30 部），覆盖古代、近代与现当代。每部作品含八个固定栏目：基本信息、创作背景、内容脉络、主要人物表、主题与艺术特点、影响与评论（每条注明出处）、阅读建议与待核实事项；并配一张人物关系图或主题结构图。</p>
<p><b>收录统计</b>：作品 {len(works)} 部（中国 {len(cn)} · 外国 {len(fr)}）；作家页 {len(authors)} 篇；已核来源 {sum(1 for s in sources.values() if s.get('verified'))} 条。
时代分布：古代 {era_cn.get('古代',0)} · 近代 {era_cn.get('近代',0)} · 现当代 {era_cn.get('现当代',0)}。</p>
<h2>开始浏览</h2>
<ul>
<li><a href="works.html">作品总览</a> — 按国别、时代、体裁筛选全部 60 部作品</li>
<li><a href="authors.html">作家索引</a> — 按国别分组浏览 {len(authors)} 位作家</li>
<li><a href="timeline.html">文学史时间线</a> — 从《诗经》到《三体》的 60 个坐标</li>
<li><a href="about.html">关于本库</a> — 收录原则、来源与版权说明</li>
</ul>
<h2>作品速览</h2>
<div class="worklist">{''.join(work_card(w) for w in sorted(works.values(), key=lambda x: x.get('year_sort', 0))[:8])}</div>
<p class="meta"><a href="works.html">查看全部 →</a></p>"""
    return page("首页", body)

def about_page(works, sources):
    ver = sum(1 for s in sources.values() if s.get("verified"))
    body = f"""<h1>关于本库</h1>
<div class="card">
<p><b>定位</b>：面向普通读者的文学名著导读。情节概括只写到"读者需要的程度"，不逐章复述；引文不超过一两句并注明版本；现代译本受版权保护，不作大段搬用。</p>
<p><b>事实与来源</b>：页面关键事实（作者生卒、成书年代、体裁、评论）均标注来源。全库共 {len(sources)} 条来源记录，其中 {ver} 条经实际打开核对（ Britannica、英文维基百科、央视网、求是、人民网、中国作家网、中国新闻网、书格古籍库等）。评价类内容写明是谁的观点；有争议的话题（如《哈克贝利·费恩历险记》的种族语言争议、《白鹿原》的获奖修订）列出各方说法。</p>
<p><b>查不到的怎么办</b>：记入各页"待核实"一栏，不编造。</p>
<p><b>配图</b>：每部作品一幅 SVG 图——长篇小说与戏剧为人物关系图，诗集、短篇集等选集为主题·结构图。图为原创绘制（示意性质，非学术考据图）。</p>
<p><b>技术</b>：纯静态站点（HTML+CSS+少量原生 JS 筛选），无外部依赖，可离线浏览。</p>
</div>
<h2>主要来源类型</h2><ul>
<li>百科全书：Encyclopaedia Britannica、维基百科（英文）</li>
<li>官方媒体与机构：央视网、求是、人民网（含党史频道）、中国作家网（中国作协）、中国新闻网、新华网</li>
<li>古籍数字资源：书格（香港中文大学图书馆藏本影印）</li>
</ul>"""
    return page("关于", body)

# ---------- 主流程 ----------

def main():
    works, authors, sources = load_all()
    (SITE / "works").mkdir(parents=True, exist_ok=True)
    (SITE / "authors").mkdir(parents=True, exist_ok=True)
    (SITE / "assets" / "svg").mkdir(parents=True, exist_ok=True)
    (SITE / "style.css").write_text(CSS, encoding="utf-8")

    for w in works.values():
        (SITE / "works" / f"{w['id']}.html").write_text(work_page(w, authors, sources, works), encoding="utf-8")
    for a in authors.values():
        (SITE / "authors" / f"{a['id']}.html").write_text(author_page(a, works, sources), encoding="utf-8")

    (SITE / "index.html").write_text(index_page(works, authors, sources), encoding="utf-8")
    (SITE / "works.html").write_text(overview_page(works, sources), encoding="utf-8")
    (SITE / "authors.html").write_text(authors_index_page(authors, works), encoding="utf-8")
    (SITE / "timeline.html").write_text(timeline_page(works), encoding="utf-8")
    (SITE / "about.html").write_text(about_page(works, sources), encoding="utf-8")
    print(f"build ok: {len(works)} works, {len(authors)} authors -> site/")

if __name__ == "__main__":
    main()
