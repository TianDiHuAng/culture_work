# -*- coding: utf-8 -*-
"""SVG 配图生成器：依据作品 JSON 中的 svg 规格，生成人物关系图 / 主题结构图。
所有坐标由脚本计算并做边界检查，从构造上避免"出界"。
用法：from svggen import render; svg_text = render(spec)
"""
import math

FONT_STACK = "'Segoe UI','Microsoft YaHei','PingFang SC',sans-serif"

# ---------- 文本宽度估算（中文≈1em，英文/数字≈0.6em） ----------

def text_width(s, fs):
    w = 0.0
    for ch in s:
        w += fs if ord(ch) > 0x2E80 else fs * 0.6
    return w

# ---------- 边界检查 ----------

class Bounds:
    def __init__(self, w, h):
        self.w, self.h = w, h
        self.errors = []

    def check(self, x1, y1, x2, y2, what=""):
        if x1 < 0 - 1 or y1 < 0 - 1 or x2 > self.w + 1 or y2 > self.h + 1:
            self.errors.append(f"{what}: bbox=({x1:.1f},{y1:.1f})-({x2:.1f},{y2:.1f}) 超出 viewBox {self.w}x{self.h}")


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")

# ---------- 节点框 ----------

def node_box(n, fs=15, pad_x=12, pad_h=10):
    w = text_width(n["label"], fs) + pad_x * 2
    h = fs + pad_h * 2
    cx, cy = n["x"], n["y"]
    return (cx - w / 2, cy - h / 2, w, h)

COLORS = {"main": "#8c3b3b", "family": "#3b6b8c", "other": "#5e7d5a", "antagonist": "#a8642a",
          "group": "#7a5b96", "plain": "#55606b", "gold": "#9a7b2f"}

def node_svg(n, b, fs=15, fs_sub=11):
    x, y, w, h = node_box(n, fs=fs)
    color = COLORS.get(n.get("color", "plain"), COLORS["plain"])
    b.check(x, y, x + w, y + h, f"node {n.get('id')}")
    parts = [
        f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="7" fill="{color}" opacity="0.92"/>',
        f'<text x="{n["x"]:.1f}" y="{n["y"] + fs * 0.36:.1f}" font-size="{fs}" fill="#fff" text-anchor="middle">{esc(n["label"])}</text>',
    ]
    if n.get("sub"):
        sw = text_width(n["sub"], fs_sub)
        sx = n["x"] - sw / 2 - 4
        sy = y + h + 2 + fs_sub
        b.check(sx, y + h, sx + sw + 8, sy + 2, f"node {n.get('id')} sub")
        parts.append(f'<rect x="{sx:.1f}" y="{y + h + 2:.1f}" width="{sw + 8:.1f}" height="{fs_sub + 4:.1f}" rx="3" fill="#ffffff" opacity="0.75"/>')
        parts.append(f'<text x="{n["x"]:.1f}" y="{sy:.1f}" font-size="{fs_sub}" fill="#333" text-anchor="middle">{esc(n["sub"])}</text>')
    return "\n".join(parts)

def edge_svg(e, nodes, b):
    a, c = nodes[e["a"]], nodes[e["b"]]
    ax, ay, aw, ah = node_box(a)
    cx_, cy_, cw, ch = node_box(c)
    x1, y1 = a["x"], a["y"]
    x2, y2 = c["x"], c["y"]
    dash = ' stroke-dasharray="6,4"' if e.get("style") == "dashed" else ""
    color = e.get("color", "#9aa3ad")
    b.check(min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2), f"edge {e['a']}-{e['b']}")
    s = f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{color}" stroke-width="1.6"{dash}/>'
    if e.get("label"):
        fs = 12
        lw = text_width(e["label"], fs) + 8
        mx, my = (x1 + x2) / 2, (y1 + y2) / 2
        b.check(mx - lw / 2, my - 9, mx + lw / 2, my + 9, f"edge label {e['a']}-{e['b']}")
        s += f'<rect x="{mx - lw / 2:.1f}" y="{my - 9:.1f}" width="{lw:.1f}" height="18" rx="3" fill="#fdf9f1"/>'
        s += f'<text x="{mx:.1f}" y="{my + 4:.1f}" font-size="{fs}" fill="#555" text-anchor="middle">{esc(e["label"])}</text>'
    return s

# ---------- 各类型渲染 ----------

def render_graph(spec, b):
    nodes = {n["id"]: n for n in spec["nodes"]}
    parts = []
    for e in spec.get("edges", []):
        parts.append(edge_svg(e, nodes, b))
    for n in spec["nodes"]:
        parts.append(node_svg(n, b))
    return "\n".join(parts)

def render_grid(spec, b):
    cards = spec["cards"]
    cols = spec.get("cols", 3)
    gap, top, cw = 14, 40, 200
    rows = math.ceil(len(cards) / cols)
    W = cols * cw + (cols + 1) * gap
    H = top + rows * 120 + gap * rows + 10
    b.w, b.h = W, H
    parts = []
    for i, c in enumerate(cards):
        r, col = divmod(i, cols)
        x = gap + col * (cw + gap)
        y = top + r * (120 + gap)
        b.check(x, y, x + cw, y + 120, f"card {i}")
        parts.append(f'<rect x="{x}" y="{y}" width="{cw}" height="120" rx="8" fill="#fff" stroke="#d8cdbb"/>')
        parts.append(f'<rect x="{x}" y="{y}" width="{cw}" height="6" rx="3" fill="{COLORS.get(c.get("color","plain"),COLORS["plain"])}"/>')
        tfs = 15
        tw = text_width(c["title"], tfs)
        if tw > cw - 16:
            tfs = 13
            tw = text_width(c["title"], tfs)
        parts.append(f'<text x="{x + cw / 2:.1f}" y="{y + 26:.1f}" font-size="{tfs}" fill="#3a3a3a" text-anchor="middle">{esc(c["title"])}</text>')
        if c.get("sub"):
            parts.append(f'<text x="{x + cw / 2:.1f}" y="{y + 44:.1f}" font-size="11" fill="#8a8378" text-anchor="middle">{esc(c["sub"])}</text>')
        # 正文按 ~13 字/行换行
        lines = wrap_text(c.get("text", ""), 11.5, cw - 20)
        for j, ln in enumerate(lines[:5]):
            parts.append(f'<text x="{x + 10}" y="{y + 64 + j * 16:.1f}" font-size="12" fill="#555">{esc(ln)}</text>')
    return "\n".join(parts)

def wrap_text(s, fs, max_w):
    lines, cur, cw_now = [], "", 0.0
    for ch in s:
        w = fs if ord(ch) > 0x2E80 else fs * 0.6
        if cw_now + w > max_w:
            lines.append(cur); cur, cw_now = ch, w
        else:
            cur += ch; cw_now += w
    if cur:
        lines.append(cur)
    return lines

def render_tree(spec, b):
    root = spec["root"]
    kids = spec.get("children", [])
    gap = 12
    kfs = 13
    widths = []
    for k in kids:
        w = max(text_width(k["label"], kfs), text_width(k.get("sub", ""), 11)) + 20
        w = max(w, 96)
        widths.append(min(w, 150))
    total = sum(widths) + gap * (len(kids) - 1) if kids else 0
    W = max(total + 40, 420)
    H = 200
    b.w, b.h = W, H
    parts = []
    rx = W / 2
    rw = text_width(root["label"], 16) + 28
    b.check(rx - rw / 2, 16, rx + rw / 2, 52, "tree root")
    parts.append(f'<rect x="{rx - rw / 2:.1f}" y="16" width="{rw:.1f}" height="36" rx="8" fill="{COLORS["main"]}"/>')
    parts.append(f'<text x="{rx:.1f}" y="{16 + 24:.1f}" font-size="16" fill="#fff" text-anchor="middle">{esc(root["label"])}</text>')
    x0 = (W - total) / 2
    for k, kw in zip(kids, widths):
        kx = x0 + kw / 2
        ky = 118
        b.check(kx - kw / 2, ky - 24, kx + kw / 2, ky + 24, f"tree child {k.get('label')}")
        parts.append(f'<line x1="{rx:.1f}" y1="52" x2="{kx:.1f}" y2="{ky - 24}" stroke="#b9b0a3" stroke-width="1.5"/>')
        parts.append(f'<rect x="{kx - kw / 2:.1f}" y="{ky - 24}" width="{kw:.1f}" height="48" rx="7" fill="#fff" stroke="#c9bfae"/>')
        parts.append(f'<text x="{kx:.1f}" y="{ky - 6:.1f}" font-size="{kfs}" fill="#3a3a3a" text-anchor="middle">{esc(k["label"])}</text>')
        if k.get("sub"):
            parts.append(f'<text x="{kx:.1f}" y="{ky + 14:.1f}" font-size="11" fill="#8a8378" text-anchor="middle">{esc(k["sub"])}</text>')
        # 第三层：孙节点列表
        subs = k.get("children", [])
        for j, s_ in enumerate(subs[:4]):
            sy = ky + 44 + j * 18
            parts.append(f'<text x="{kx:.1f}" y="{sy:.1f}" font-size="12" fill="#666" text-anchor="middle">{esc(s_)}</text>')
        if subs:
            H = max(H, ky + 44 + min(len(subs), 4) * 18 + 8)
    b.h = H
    return "\n".join(parts)

def render_flow(spec, b):
    steps = spec["steps"]
    n = len(steps)
    gap, top = 16, 60
    sw = (680 - gap * (n + 1)) / n
    H = top + 96 + 40
    b.w, b.h = 680, H
    parts = []
    for i, st in enumerate(steps):
        x = gap + i * (sw + gap)
        y = top
        b.check(x, y - 30, x + sw, y + 96, f"flow {i}")
        if i < n - 1:
            ax = x + sw + 3
            parts.append(f'<line x1="{ax}" y1="{y + 34}" x2="{ax + gap - 6}" y2="{y + 34}" stroke="#b9b0a3" stroke-width="1.8"/>')
            parts.append(f'<polygon points="{ax + gap - 6},{y + 30} {ax + gap},{y + 34} {ax + gap - 6},{y + 38}" fill="#b9b0a3"/>')
        color = COLORS.get(st.get("color", "plain"), COLORS["plain"])
        parts.append(f'<rect x="{x:.1f}" y="{y}" width="{sw:.1f}" height="68" rx="8" fill="#fff" stroke="{color}" stroke-width="1.6"/>')
        parts.append(f'<text x="{x + sw / 2:.1f}" y="{y + 24:.1f}" font-size="13" fill="{color}" text-anchor="middle">{esc(st["title"])}</text>')
        lines = wrap_text(st.get("text", ""), 12, sw - 14)[:3]
        for j, ln in enumerate(lines):
            parts.append(f'<text x="{x + sw / 2:.1f}" y="{y + 44 + j * 15:.1f}" font-size="12" fill="#555" text-anchor="middle">{esc(ln)}</text>')
    return "\n".join(parts)

def render_ring(spec, b):
    center = spec["center"]
    around = spec.get("nodes", [])
    cx, cy = 340, 220
    R = spec.get("radius", 150)
    fs = 14
    parts = []
    cwid = text_width(center["label"], 16) + 30
    b.check(cx - cwid / 2, cy - 20, cx + cwid / 2, cy + 20, "ring center")
    n = len(around)
    for i, a in enumerate(around):
        ang = -math.pi / 2 + i * (2 * math.pi / max(n, 1))
        ax, ay = cx + R * math.cos(ang), cy + R * math.sin(ang)
        w = text_width(a["label"], fs) + 20
        h = fs + 12
        b.check(ax - w / 2, ay - h / 2, ax + w / 2, ay + h / 2, f"ring {a.get('label')}")
        parts.append(f'<line x1="{cx}" y1="{cy}" x2="{ax:.1f}" y2="{ay:.1f}" stroke="#c4bcaa" stroke-width="1.4"/>')
        color = COLORS.get(a.get("color", "plain"), COLORS["plain"])
        parts.append(f'<rect x="{ax - w / 2:.1f}" y="{ay - h / 2:.1f}" width="{w:.1f}" height="{h:.1f}" rx="6" fill="{color}" opacity="0.9"/>')
        parts.append(f'<text x="{ax:.1f}" y="{ay + fs * 0.36:.1f}" font-size="{fs}" fill="#fff" text-anchor="middle">{esc(a["label"])}</text>')
    parts.append(f'<rect x="{cx - cwid / 2:.1f}" y="{cy - 20}" width="{cwid:.1f}" height="40" rx="9" fill="{COLORS["main"]}"/>')
    parts.append(f'<text x="{cx}" y="{cy + 5:.1f}" font-size="16" fill="#fff" text-anchor="middle">{esc(center["label"])}</text>')
    b.w, b.h = 680, 440
    return "\n".join(parts)

RENDERERS = {"graph": render_graph, "grid": render_grid, "tree": render_tree, "flow": render_flow, "ring": render_ring}

def render(spec):
    t = spec["type"]
    if t not in RENDERERS:
        raise ValueError(f"未知 svg 类型: {t}")
    W = spec.get("width", 680)
    H = spec.get("height", 460)
    b = Bounds(W, H)
    body = RENDERERS[t](spec, b)
    if b.errors:
        raise ValueError("SVG 出界: " + "; ".join(b.errors))
    caption = spec.get("caption", "")
    cap_y = H - 10
    cap = f'<text x="{W / 2}" y="{cap_y}" font-size="12" fill="#8a8378" text-anchor="middle">{esc(caption)}</text>' if caption else ""
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="100%" '
        f'role="img" font-family="{FONT_STACK}">\n'
        f'<rect x="0" y="0" width="{W}" height="{H}" fill="#fdf9f1" rx="10"/>\n'
        f'{body}\n{cap}\n</svg>\n'
    )

if __name__ == "__main__":
    import sys, json
    spec = json.loads(sys.stdin.read())
    print(render(spec))
