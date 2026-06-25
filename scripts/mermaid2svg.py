#!/usr/bin/env python3
# mermaid2svg.py — minimal renderer for the "flowchart TB" subset used in
# this book. Produces an on-brand SVG (Claude.ai palette). Not a general
# Mermaid implementation: supports rectangular nodes [..], decision nodes {..},
# quoted labels ["..."], solid/dotted/labelled edges, and <br/> line breaks.
import re
import sys
import html

# -----------------------------------------------------------------------------------------------------------------
#  palette
# -----------------------------------------------------------------------------------------------------------------
CREAM = "#FAF9F5"
INK = "#1F1E1D"
CORAL = "#D97757"
BORDER = "#E5DED2"
BOXFILL = "#FFFFFF"
DECISIONFILL = "#FBEEE7"
MUTED = "#6B6760"

FONT = "Inter, 'Helvetica Neue', Arial, sans-serif"
FS = 13          # node font size
EFS = 11         # edge-label font size
LINEH = 16       # line height in a node
PADX, PADY = 14, 10
COLGAP, ROWGAP = 34, 40
CHARW = 7.0      # approx char width at FS


# -----------------------------------------------------------------------------------------------------------------
#  parsing
# -----------------------------------------------------------------------------------------------------------------
def _label_lines(raw):
    parts = re.split(r"<br\s*/?>", raw)
    return [html.escape(p.strip()) for p in parts]


def _parse(text):
    nodes = {}   # id -> (shape, [lines])
    edges = []   # (src, dst, label, dotted)

    def ensure(tok):
        # tok like  A[Label]  or  B{Label}  or  C["x"]  or just  A
        m = re.match(r'^(\w+)\s*(\[".*?"\]|\[.*?\]|\{.*?\})?\s*$', tok.strip(), re.S)
        if not m:
            nid = re.match(r"^(\w+)", tok.strip()).group(1)
            nodes.setdefault(nid, ("rect", [nid]))
            return nid
        nid, body = m.group(1), m.group(2)
        if body:
            if body.startswith("{"):
                shape, inner = "diamond", body[1:-1]
            elif body.startswith('["'):
                shape, inner = "rect", body[2:-2]
            else:
                shape, inner = "rect", body[1:-1]
            nodes[nid] = (shape, _label_lines(inner))
        else:
            nodes.setdefault(nid, ("rect", [nid]))
        return nid

    edge_re = re.compile(
        r'^(.*?)\s*(-\.->|-\.\s*.*?\s*\.->|-->|--\s*.*?\s*-->)\s*(.*)$')
    for line in text.splitlines():
        line = line.strip()
        if not line or line.startswith("flowchart") or line.startswith("graph"):
            continue
        m = edge_re.match(line)
        if not m:
            ensure(line)
            continue
        left, mid, right = m.group(1), m.group(2), m.group(3)
        dotted = mid.startswith("-.")
        lab = ""
        lm = re.match(r'^-\.\s*(.*?)\s*\.->$', mid) or \
            re.match(r'^--\s*(.*?)\s*-->$', mid)
        if lm:
            lab = lm.group(1).strip().strip('"').strip("'")
            lab = re.sub(r"<br\s*/?>", " ", lab)
        s = ensure(left)
        d = ensure(right)
        edges.append((s, d, lab, dotted))
    return nodes, edges


# -----------------------------------------------------------------------------------------------------------------
#  layout
# -----------------------------------------------------------------------------------------------------------------
def _levels(nodes, edges):
    succ = {n: [] for n in nodes}
    indeg = {n: 0 for n in nodes}
    fwd = []
    seen = set()
    for s, d, _, _ in edges:
        if (s, d) in seen:
            continue
        seen.add((s, d))
    # drop back-edges (target appears before source in declaration order)
    order = list(nodes.keys())
    pos = {n: i for i, n in enumerate(order)}
    for s, d, _, _ in edges:
        if pos[d] > pos[s]:
            succ[s].append(d)
            indeg[d] += 1
            fwd.append((s, d))
    level = {}
    roots = [n for n in order if indeg[n] == 0]
    for r in roots:
        level[r] = 0
    changed = True
    # longest path
    for n in order:
        level.setdefault(n, 0)
    for _ in range(len(order)):
        for s, d in fwd:
            if level[d] < level[s] + 1:
                level[d] = level[s] + 1
    return level


def _node_size(shape, lines):
    w = max(CHARW * len(t) for t in lines) + 2 * PADX
    h = LINEH * len(lines) + 2 * PADY
    if shape == "diamond":
        w += 46
        h += 26
    return max(w, 70), max(h, 38)


def render(text, width=600):
    nodes, edges = _parse(text)
    level = _levels(nodes, edges)
    rows = {}
    for n, lv in level.items():
        rows.setdefault(lv, []).append(n)
    for lv in rows:
        rows[lv].sort(key=lambda n: list(nodes).index(n))

    size = {n: _node_size(*nodes[n]) for n in nodes}
    # y per row
    rowh = {lv: max(size[n][1] for n in rows[lv]) for lv in rows}
    y = {}
    cy = 16
    rowy = {}
    for lv in sorted(rows):
        rowy[lv] = cy
        cy += rowh[lv] + ROWGAP
    total_h = cy - ROWGAP + 16

    # x per node: center each row
    pos = {}
    for lv in sorted(rows):
        ns = rows[lv]
        tw = sum(size[n][0] for n in ns) + COLGAP * (len(ns) - 1)
        x = (width - tw) / 2
        for n in ns:
            w, h = size[n]
            yy = rowy[lv] + (rowh[lv] - h) / 2
            pos[n] = (x, yy, w, h)
            x += w + COLGAP

    out = []
    out.append(
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} '
        f'{int(total_h)}" width="100%" font-family="{FONT}">')
    out.append(
        '<defs><marker id="ah" markerWidth="9" markerHeight="9" refX="7" '
        'refY="3" orient="auto"><path d="M0,0 L7,3 L0,6 Z" '
        f'fill="{CORAL}"/></marker></defs>')

    def center(n):
        x, yy, w, h = pos[n]
        return (x + w / 2, yy + h / 2, w, h)

    # edges
    for s, d, lab, dotted in edges:
        sx, sy, sw, sh = center(s)
        dx, dy, dw, dh = center(d)
        back = level[d] <= level[s]
        dash = ' stroke-dasharray="4 3"' if dotted else ''
        if back:
            x1 = pos[s][0] + pos[s][2]
            y1 = sy
            x2 = pos[d][0] + pos[d][2]
            y2 = dy
            mx = max(x1, x2) + 38
            path = f'M{x1},{y1} C{mx},{y1} {mx},{y2} {x2},{y2}'
            out.append(
                f'<path d="{path}" fill="none" stroke="{CORAL}" '
                f'stroke-width="1.5"{dash} marker-end="url(#ah)"/>')
            if lab:
                out.append(
                    f'<text x="{mx+4}" y="{(y1+y2)/2}" font-size="{EFS}" '
                    f'fill="{MUTED}">{html.escape(lab)}</text>')
        else:
            y1 = pos[s][1] + pos[s][3]
            y2 = pos[d][1]
            out.append(
                f'<line x1="{sx}" y1="{y1}" x2="{dx}" y2="{y2-2}" '
                f'stroke="{CORAL}" stroke-width="1.5"{dash} '
                'marker-end="url(#ah)"/>')
            if lab:
                lx, ly = (sx + dx) / 2, (y1 + y2) / 2
                tw = CHARW * len(lab) + 6
                out.append(
                    f'<rect x="{lx-tw/2}" y="{ly-9}" width="{tw}" height="15" '
                    f'rx="3" fill="{CREAM}"/>')
                out.append(
                    f'<text x="{lx}" y="{ly+2}" font-size="{EFS}" '
                    f'fill="{MUTED}" text-anchor="middle">'
                    f'{html.escape(lab)}</text>')

    # nodes
    for n in nodes:
        x, yy, w, h = pos[n]
        shape, lines = nodes[n]
        if shape == "diamond":
            cx, cy2 = x + w / 2, yy + h / 2
            pts = f'{cx},{yy} {x+w},{cy2} {cx},{yy+h} {x},{cy2}'
            out.append(
                f'<polygon points="{pts}" fill="{DECISIONFILL}" '
                f'stroke="{CORAL}" stroke-width="1.5"/>')
        else:
            out.append(
                f'<rect x="{x}" y="{yy}" width="{w}" height="{h}" rx="7" '
                f'fill="{BOXFILL}" stroke="{BORDER}" stroke-width="1.2"/>')
        ty = yy + PADY + 12
        for ln in lines:
            out.append(
                f'<text x="{x+w/2}" y="{ty}" font-size="{FS}" fill="{INK}" '
                f'text-anchor="middle">{ln}</text>')
            ty += LINEH
    out.append('</svg>')
    return "\n".join(out)


if __name__ == "__main__":
    data = sys.stdin.read()
    sys.stdout.write(render(data))
