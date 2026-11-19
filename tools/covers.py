# -*- coding: utf-8 -*-
"""程序化书封生成器：根据作品元数据（书名/作者/国别/时代/年代/体裁）生成复古书卷风 SVG 封面。
纯函数 of work dict；不改动 works JSON（check.py 无需感知）。
"""
import math, pathlib, sys

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from svggen import Bounds, esc, text_width

# 国别 → 色板 {bg 深底, fg 纸色字, accent 点缀, sub 弱化字}
PALETTES = {
    "中国-古代": {"bg": "#6e1f1f", "fg": "#f2e6cf", "accent": "#d9b36a", "sub": "#e3c9a0"},
    "中国-近代": {"bg": "#4a3524", "fg": "#f2e6cf", "accent": "#d9b36a", "sub": "#dfc9a4"},
    "中国-现当代": {"bg": "#1f3a5f", "fg": "#f0e8d8", "accent": "#c8503c", "sub": "#c9b98f"},
    "日本": {"bg": "#3d3a63", "fg": "#f2e9e4", "accent": "#c98a8a", "sub": "#cfc3d6"},
    "俄国": {"bg": "#54232a", "fg": "#efe6d4", "accent": "#c9a45c", "sub": "#d8b9a4"},
    "英国": {"bg": "#1f4437", "fg": "#efe8d2", "accent": "#caa45a", "sub": "#c6c2a2"},
    "法国": {"bg": "#23355c", "fg": "#f0e9d8", "accent": "#d0a75a", "sub": "#c3c4d6"},
    "美国": {"bg": "#3e5c4f", "fg": "#f0ead6", "accent": "#d8b060", "sub": "#c4c9ad"},
    "德语区": {"bg": "#383d44", "fg": "#eee9da", "accent": "#c1a05a", "sub": "#bfc3c2"},
    "拉丁美洲": {"bg": "#7a3420", "fg": "#f4e9d0", "accent": "#e0b45c", "sub": "#e8c9a2"},
    "非洲与中东": {"bg": "#8a5c22", "fg": "#f6ecd4", "accent": "#f0d089", "sub": "#eccf9c"},
    "古典地中海": {"bg": "#39485e", "fg": "#ece5d0", "accent": "#c4a35c", "sub": "#bcc4cd"},
    "其他": {"bg": "#3e5871", "fg": "#efe9d8", "accent": "#cba45c", "sub": "#c2c6cd"},
}
REGION_MAP = {
    "日本": "日本", "俄国": "俄国", "英国": "英国", "法国": "法国", "美国": "美国",
    "德国": "德语区", "奥地利": "德语区", "爱尔兰": "德语区", "挪威": "德语区", "捷克": "德语区",
    "哥伦比亚": "拉丁美洲", "智利": "拉丁美洲", "墨西哥": "拉丁美洲", "秘鲁": "拉丁美洲", "阿根廷": "拉丁美洲",
    "尼日利亚": "非洲与中东", "南非": "非洲与中东", "埃及": "非洲与中东", "土耳其": "非洲与中东",
    "古希腊": "古典地中海", "古罗马": "古典地中海", "意大利": "古典地中海", "西班牙": "古典地中海",
}

def palette_for(w):
    if w["region"] == "中国":
        key = "中国-" + w.get("era", "古代")
        return PALETTES.get(key, PALETTES["中国-古代"])
    return PALETTES.get(REGION_MAP.get(w["region"], "其他"), PALETTES["其他"])

def clean(s):
    """去掉括注，用于封面书名/作者名。"""
    for sep in ("（", "("):
        if sep in s:
            s = s.split(sep)[0]
    return s.strip() or s

TITLE_FONT = "'KaiTi','STKaiti','SimSun','Songti SC','Noto Serif CJK SC',serif"
LABEL_FONT = "'SimSun','Songti SC','Noto Serif CJK SC',serif"
NUM_FONT = "'Georgia','Times New Roman',serif"

def motif_svg(group, cx, y, accent):
    """体裁纹样：诗歌=波浪，小说=双线夹菱，戏剧=三线，散文=点线，故事集=菱列。"""
    p = []
    if group == "诗歌":
        p.append(f'<path d="M {cx-110} {y} q 27 -12 55 0 t 55 0 t 55 0 t 55 0" fill="none" stroke="{accent}" stroke-width="1.6" opacity="0.85"/>')
        p.append(f'<path d="M {cx-110} {y+12} q 27 -12 55 0 t 55 0 t 55 0 t 55 0" fill="none" stroke="{accent}" stroke-width="1.1" opacity="0.5"/>')
    elif group == "小说":
        p.append(f'<line x1="{cx-110}" y1="{y}" x2="{cx-16}" y2="{y}" stroke="{accent}" stroke-width="1.4" opacity="0.85"/>')
        p.append(f'<line x1="{cx+16}" y1="{y}" x2="{cx+110}" y2="{y}" stroke="{accent}" stroke-width="1.4" opacity="0.85"/>')
        p.append(f'<rect x="{cx-6}" y="{y-6}" width="12" height="12" transform="rotate(45 {cx} {y})" fill="none" stroke="{accent}" stroke-width="1.4" opacity="0.9"/>')
    elif group == "戏剧":
        for dy, op in ((0, 0.9), (8, 0.55), (16, 0.3)):
            p.append(f'<line x1="{cx-90}" y1="{y+dy}" x2="{cx+90}" y2="{y+dy}" stroke="{accent}" stroke-width="1.4" opacity="{op}"/>')
    elif group == "散文":
        p.append(f'<line x1="{cx-90}" y1="{y}" x2="{cx+90}" y2="{y}" stroke="{accent}" stroke-width="1.2" opacity="0.6"/>')
        for dx in (-54, -18, 18, 54):
            p.append(f'<circle cx="{cx+dx}" cy="{y}" r="2.2" fill="{accent}" opacity="0.9"/>')
    else:  # 故事集等
        for dx in (-84, -42, 0, 42, 84):
            p.append(f'<rect x="{cx+dx-4}" y="{y-4}" width="8" height="8" transform="rotate(45 {cx+dx} {y})" fill="none" stroke="{accent}" stroke-width="1.3" opacity="0.8"/>')
    return "\n".join(p)

def column_chars(chars, x, y0, fs, step, b, bctx, color):
    out = []
    for i, ch in enumerate(chars):
        ty = y0 + i * step
        w = fs if ord(ch) > 0x2E80 else fs * 0.55
        b.check(x - w / 2, ty - fs * 0.88, x + w / 2, ty + fs * 0.26, f"{bctx}[{i}]")
        out.append(f'<text x="{x}" y="{ty:.1f}" font-size="{fs}" fill="{color}" text-anchor="middle">{esc(ch)}</text>')
    return out

def seal_svg(w, b):
    ys = w.get("year_sort")
    year = ""
    if isinstance(ys, int):
        year = f"前{-ys}" if ys < 0 else str(ys)
    elif ys:
        year = str(ys)
    if not year:
        return ""
    fs = 15 if len(year) <= 4 else 13
    sw = text_width(year, fs) + 16
    sh = fs + 16
    x, y = 306, 536 - sh - 14
    b.check(x, y, x + sw, y + sh, "seal")
    return (
        f'<rect x="{x}" y="{y}" width="{sw:.0f}" height="{sh}" rx="4" fill="#9e3223" opacity="0.94"/>'
        f'<rect x="{x+3}" y="{y+3}" width="{sw-6:.0f}" height="{sh-6}" rx="2" fill="none" stroke="#f2e6cf" stroke-width="0.8" opacity="0.7"/>'
        f'<text x="{x + sw / 2:.1f}" y="{y + sh / 2 + fs * 0.36:.1f}" font-size="{fs}" fill="#f2e6cf" text-anchor="middle" font-family="{NUM_FONT}">{esc(year)}</text>'
    )

def render_cover(w):
    """封面 viewBox 400x560。书名竖排（右起），作者竖排（左下），体裁纹样横顶，年代朱印。"""
    W, H = 400, 560
    b = Bounds(W, H)
    pal = palette_for(w)
    title = clean(w["title"])
    author = clean(w.get("author_name", ""))
    group = w.get("genre_group", "")
    region_label = f'{w["region"]} · {w.get("era_detail", "")}'
    parts = [f'<rect x="0" y="0" width="{W}" height="{H}" fill="{pal["bg"]}"/>']
    # 双线书框
    parts.append(f'<rect x="14" y="14" width="{W-28}" height="{H-28}" fill="none" stroke="{pal["accent"]}" stroke-width="1.3" opacity="0.75"/>')
    parts.append(f'<rect x="21" y="21" width="{W-42}" height="{H-42}" fill="none" stroke="{pal["accent"]}" stroke-width="0.6" opacity="0.45"/>')
    # 顶部国别·时代
    rl_fs = 14
    while text_width(region_label, rl_fs) + rl_fs > 330 and rl_fs > 10:
        rl_fs -= 1
    rw = text_width(region_label, rl_fs)
    b.check(200 - rw / 2 - 4, 36, 200 + rw / 2 + 4, 52, "region label")
    parts.append(f'<text x="200" y="50" font-size="{rl_fs}" fill="{pal["sub"]}" text-anchor="middle" letter-spacing="3" font-family="{LABEL_FONT}">{esc(region_label)}</text>')
    parts.append(motif_svg(group, 200, 72, pal["accent"]))
    # 书名竖排：1 列 ≤6 字；2 列 ≤14 字；更多 3 列
    chars = list(title.replace(" ", ""))
    n = len(chars)
    cols = 1 if n <= 6 else (2 if n <= 14 else 3)
    col_xs = {1: [286], 2: [302, 232], 3: [312, 240, 168]}[cols]
    per_col = math.ceil(n / cols)
    area_top, area_h = 92, 408
    fs = 48
    while fs > 26 and per_col * fs * 1.24 > area_h:
        fs -= 2
    step = min(fs * 1.24, area_h / max(per_col, 1))
    total_h = step * (per_col - 1) + fs
    y0 = area_top + (area_h - total_h) / 2 + fs * 0.88
    k = math.ceil(n / cols)  # 每列字数（最后一列可能不满）
    emitted = 0
    for ci, cx in enumerate(col_xs):  # 右起竖排（传统书卷方向）
        if emitted >= n:
            break
        take = chars[emitted:emitted + k]
        emitted += len(take)
        parts += column_chars(take, cx, y0, fs, step, b, f"title col{ci}", pal["fg"])
    # 作者竖排（左下）
    if author:
        achs = list(author)
        afs, astep = 20, 25
        ah = astep * (len(achs) - 1) + afs
        ay0 = 176
        while ay0 + ah > 452 and afs > 13:
            afs -= 1; astep = afs * 1.25; ah = astep * (len(achs) - 1) + afs
        parts += column_chars(achs, 108, ay0, afs, astep, b, "author", pal["sub"])
        b.check(96, ay0 - afs * 0.88, 120, ay0 + ah, "author col")
        parts.append(f'<line x1="108" y1="{ay0 + ah + 12:.1f}" x2="108" y2="{min(ay0 + ah + 40, 470)}" stroke="{pal["accent"]}" stroke-width="1" opacity="0.6"/>')
    parts.append(seal_svg(w, b))
    body = "\n".join(parts)
    if b.errors:
        raise ValueError(f"封面出界 [{w['id']}] " + "; ".join(b.errors[:6]))
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="100%" '
        f'role="img" font-family="{TITLE_FONT}">\n{body}\n</svg>\n'
    )

if __name__ == "__main__":
    import json
    print(render_cover(json.loads(sys.stdin.read())))
