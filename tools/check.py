# -*- coding: utf-8 -*-
"""全库校验器：必填字段、日期合法、事实带来源、无重复条目、内部链接、SVG 不出界。
用法：python tools/check.py  —— 错误时 exit 1。
"""
import json, pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
ERRS, WARNS = [], []

def err(msg):
    ERRS.append(msg)

def warn(msg):
    WARNS.append(msg)

def load_json(p):
    try:
        return json.loads(p.read_text(encoding="utf-8"))
    except Exception as e:
        err(f"{p}: JSON 解析失败 {e}")
        return None

# ---------- sources.json ----------

def check_sources():
    data = load_json(ROOT / "sources.json")
    if data is None:
        return {}
    ids = set()
    ver = 0
    for s in data:
        sid = s.get("id", "?")
        if sid in ids:
            err(f"sources: id 重复 {sid}")
        ids.add(sid)
        for k in ("id", "title", "author", "year", "url", "type", "verified"):
            if k not in s:
                err(f"sources[{sid}]: 缺字段 {k}")
        u = s.get("url", "")
        if not re.match(r"^https?://", u):
            err(f"sources[{sid}]: url 非法 {u}")
        if s.get("verified"):
            ver += 1
    if ver < 80:
        err(f"sources: verified={ver} < 80")
    print(f"  sources: {len(data)} 条, verified={ver}")
    return {s["id"]: s for s in data if s.get("id")}

# ---------- works ----------

W_REQUIRED = ["id", "title", "original_title", "region", "era", "era_detail", "genre", "genre_group",
              "language", "author_id", "author_name", "year_display", "year_sort", "background",
              "outline", "characters", "themes", "influence", "reading", "pending", "sources",
              "year_source", "author_source", "related_works", "svg"]
ERAS = {"古代", "近代", "现当代"}
GROUPS = {"小说", "诗歌", "戏剧", "散文", "故事集"}

def check_works(sources, authors):
    works = {}
    titles = {}
    wdir = ROOT / "data" / "works"
    for p in sorted(wdir.glob("*.json")):
        w = load_json(p)
        if not w:
            continue
        wid = w.get("id", p.stem)
        for k in W_REQUIRED:
            if k not in w:
                err(f"works[{wid}]: 缺必填字段 {k}")
        if wid in works:
            err(f"works: id 重复 {wid}")
        if w.get("title") in titles:
            err(f"works: 书名重复 {w.get('title')}（{titles.get(w.get('title'))} 与 {wid}）")
        titles[w.get("title")] = wid
        works[wid] = w
        if w.get("era") not in ERAS:
            err(f"works[{wid}]: era 非法 {w.get('era')}")
        if w.get("genre_group") not in GROUPS:
            err(f"works[{wid}]: genre_group 非法 {w.get('genre_group')}")
        if not isinstance(w.get("year_sort"), int):
            err(f"works[{wid}]: year_sort 必须为整数（负数表示公元前）")
        elif not (-3000 <= w["year_sort"] <= 2026):
            err(f"works[{wid}]: year_sort 超范围 {w['year_sort']}")
        # 来源要求
        for sid in w.get("sources", []):
            if sid not in sources:
                err(f"works[{wid}]: 来源不存在 {sid}")
            elif not sources[sid].get("verified"):
                err(f"works[{wid}]: 引用了未核实来源 {sid}")
        for k in ("year_source", "author_source"):
            sid = w.get(k)
            if sid is None:
                if k == "year_source" or not w.get("author_id"):
                    err(f"works[{wid}]: 缺 {k}")
            elif sid not in sources:
                err(f"works[{wid}]: {k} 指向不存在的来源 {sid}")
            elif not sources[sid].get("verified"):
                err(f"works[{wid}]: {k} 为未核实来源 {sid}")
        for inf in w.get("influence", []):
            if not inf.get("text") or not inf.get("source"):
                err(f"works[{wid}]: influence 条目缺 text/source")
            elif inf["source"] not in sources:
                err(f"works[{wid}]: influence 来源不存在 {inf['source']}")
            elif not sources[inf["source"]].get("verified"):
                err(f"works[{wid}]: influence 引用未核实来源 {inf['source']}")
        if len(w.get("background", [])) < 1 or len(w.get("outline", [])) < 1:
            err(f"works[{wid}]: background/outline 不得为空")
        if len(w.get("themes", [])) < 2:
            err(f"works[{wid}]: themes 少于 2 条")
        if len(w.get("influence", [])) < 2:
            err(f"works[{wid}]: influence 少于 2 条")
        r = w.get("reading", {})
        for k in ("difficulties", "editions", "order"):
            if not r.get(k):
                err(f"works[{wid}]: reading 缺 {k}")
        if "pending" not in w:
            err(f"works[{wid}]: 缺待核实字段 pending")
        # 作者引用：author_id 与 authors 的依赖在 main 第二轮校验
        for rid in w.get("related_works", []):
            if rid == wid:
                err(f"works[{wid}]: related_works 引用自身")
        # svg 规格
        svg = w.get("svg")
        if not isinstance(svg, dict) or "type" not in svg:
            err(f"works[{wid}]: svg 规格缺失或非对象")
        elif svg["type"] == "graph" and not svg.get("nodes"):
            err(f"works[{wid}]: graph 无节点")
    return works

# ---------- authors ----------

A_REQUIRED = ["id", "name", "country", "birth", "death", "era", "summary", "timeline",
              "major_works", "style", "status", "sources", "dates_source", "pending"]

def check_authors(sources, works):
    authors = {}
    names = {}
    adir = ROOT / "data" / "authors"
    for p in sorted(adir.glob("*.json")):
        a = load_json(p)
        if not a:
            continue
        aid = a.get("id", p.stem)
        for k in A_REQUIRED:
            if k not in a:
                err(f"authors[{aid}]: 缺必填字段 {k}")
        if aid in authors:
            err(f"authors: id 重复 {aid}")
        if a.get("name") in names:
            err(f"authors: 姓名重复 {a.get('name')}")
        names[a.get("name")] = aid
        authors[aid] = a
        by, dy = a.get("birth_year"), a.get("death_year")
        for label, v in (("birth_year", by), ("death_year", dy)):
            if v is None:
                continue
            if not isinstance(v, int) or not (-800 <= v <= 2026):
                err(f"authors[{aid}]: {label} 非法 {v}")
        if by is not None and dy is not None and dy < by:
            err(f"authors[{aid}]: death_year < birth_year")
        if not a.get("dates_source"):
            err(f"authors[{aid}]: 缺 dates_source")
        elif a["dates_source"] not in sources:
            err(f"authors[{aid}]: dates_source 不存在 {a['dates_source']}")
        elif not sources[a["dates_source"]].get("verified"):
            err(f"authors[{aid}]: dates_source 未核实")
        for sid in a.get("sources", []):
            if sid not in sources:
                err(f"authors[{aid}]: 来源不存在 {sid}")
            elif not sources[sid].get("verified"):
                err(f"authors[{aid}]: 引用未核实来源 {sid}")
        if len(a.get("timeline", [])) < 3:
            err(f"authors[{aid}]: timeline 少于 3 条")
        for ev in a.get("timeline", []):
            if not ev.get("year") or not ev.get("text"):
                err(f"authors[{aid}]: timeline 条目缺 year/text")
            if ev.get("src") and (ev["src"] not in sources or not sources[ev["src"]].get("verified")):
                err(f"authors[{aid}]: timeline 来源无效 {ev.get('src')}")
        if len(a.get("style", [])) < 2:
            err(f"authors[{aid}]: style 少于 2 条")
        for mw in a.get("major_works", []):
            wid = mw.get("work_id")
            if wid and wid not in works:
                err(f"authors[{aid}]: major_works 指向不存在作品 {wid}")
        if "pending" not in a:
            err(f"authors[{aid}]: 缺 pending 字段")
    return authors

# ---------- SVG ----------

NUM_ATTRS = ["x", "y", "cx", "cy", "x1", "y1", "x2", "y2", "rx", "ry", "r"]

def check_svg_files(works):
    sdir = ROOT / "site" / "assets" / "svg"
    for wid, w in works.items():
        f = sdir / f"{wid}.svg"
        if not f.exists():
            err(f"svg: 缺文件 {wid}.svg")
            continue
        txt = f.read_text(encoding="utf-8")
        m = re.search(r'viewBox="0 0 ([\d.]+) ([\d.]+)"', txt)
        if not m:
            err(f"svg[{wid}]: 无 viewBox")
            continue
        W, H = float(m.group(1)), float(m.group(2))
        if W <= 0 or H <= 0:
            err(f"svg[{wid}]: viewBox 尺寸非法")
            continue
        tol = 1.0
        # 数值定位属性
        for attr in NUM_ATTRS:
            for v in re.findall(rf'{attr}="(-?[\d.]+)"', txt):
                val = float(v)
                if attr in ("x1", "x2", "cx", "rx", "r", "x") and not (-tol <= val <= W + tol):
                    err(f"svg[{wid}]: {attr}={val} 超界(宽{W})")
                if attr in ("y1", "y2", "cy", "ry", "y") and not (-tol <= val <= H + tol):
                    err(f"svg[{wid}]: {attr}={val} 超界(高{H})")
        # polygon points
        for pts in re.findall(r'<polygon points="([^"]+)"', txt):
            for pair in pts.split():
                xy = pair.split(",")
                if len(xy) == 2:
                    x, y = float(xy[0]), float(xy[1])
                    if not (-tol <= x <= W + tol and -tol <= y <= H + tol):
                        err(f"svg[{wid}]: polygon 点({x},{y}) 超界")
        # text 估算宽度（中文≈1em，英文≈0.62em；按 text-anchor 区分起点）
        for m2 in re.finditer(r'<text x="(-?[\d.]+)" y="(-?[\d.]+)" font-size="([\d.]+)"([^>]*)>([^<]+)</text>', txt):
            x, y, fs, attrs, content = float(m2.group(1)), float(m2.group(2)), float(m2.group(3)), m2.group(4), m2.group(5)
            full = sum(fs if ord(c) > 0x2E80 else fs * 0.62 for c in content)
            anchor = re.search(r'text-anchor="(\w+)"', attrs)
            mode = anchor.group(1) if anchor else "start"
            if mode == "middle":
                x1t, x2t = x - full / 2, x + full / 2
            elif mode == "end":
                x1t, x2t = x - full, x
            else:
                x1t, x2t = x, x + full
            if not (-tol <= x1t and x2t <= W + tol):
                err(f"svg[{wid}]: 文本'{content[:12]}…'估算范围[{x1t:.0f},{x2t:.0f}]超界(宽{W})")
            if not (-tol <= y <= H + tol):
                err(f"svg[{wid}]: 文本 y={y} 超界")

# ---------- 内部链接 ----------

def check_links(works, authors):
    site = ROOT / "site"
    if not (site / "index.html").exists():
        err("site: 缺 index.html（先运行 tools/build.py）")
        return
    for f in list((site / "works").glob("*.html")) + list((site / "authors").glob("*.html")):
        txt = f.read_text(encoding="utf-8")
        base = f.parent
        for href in re.findall(r'href="([^"#?]+?)(?:#[^"]*)?"', txt):
            if href.startswith(("http://", "https://", "mailto:")):
                continue
            target = (base / href).resolve()
            if not target.exists():
                err(f"link: {f.relative_to(site)} -> {href} 目标不存在")
        for src in re.findall(r'src="([^"#?]+)"', txt):
            if src.startswith(("http://", "https://")):
                continue
            target = (base / src).resolve()
            if not target.exists():
                err(f"link: {f.relative_to(site)} -> {src} 资源不存在")
    # 每部作品被总览收录
    ov = (site / "works.html").read_text(encoding="utf-8")
    for wid in works:
        if f'works/{wid}.html' not in ov:
            err(f"overview: 未收录作品 {wid}")
    tl = (site / "timeline.html").read_text(encoding="utf-8")
    for wid in works:
        if f'works/{wid}.html' not in tl:
            err(f"timeline: 未收录作品 {wid}")

# ---------- main ----------

def main():
    print("== check 开始 ==")
    sources = check_sources()
    # 第一轮：works 先加载（authors 的 major_works 依赖 works）
    works = check_works(sources, {})
    authors = check_authors(sources, works)
    # 第二轮：works -> authors 依赖
    for wid, w in works.items():
        aid = w.get("author_id")
        if aid and aid not in authors:
            err(f"works[{wid}]: author_id 不存在 {aid}")
    check_svg_files(works)
    check_links(works, authors)
    print(f"  works: {len(works)}, authors: {len(authors)}")
    if WARNS:
        print("-- 警告 --")
        for x in WARNS:
            print("  W:", x)
    if ERRS:
        print("-- 错误 --")
        for x in ERRS:
            print("  E:", x)
        print(f"== check 失败：{len(ERRS)} 错误 ==")
        sys.exit(1)
    print(f"== check 全部通过 ==")

if __name__ == "__main__":
    main()
