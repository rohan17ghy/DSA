"""Generate Dynamic Programming Excalidraw diagrams and Obsidian Ex-*.md exports."""
import json
import math
import uuid
from pathlib import Path

try:
    import lzstring
except ImportError:
    raise SystemExit("pip install lzstring")

ROOT = Path(r"c:\Code\DSA\Notes")
EMBED_DIR = ROOT / "ExcalidrawEmbeds" / "DynamicProgramming"
EX_DIR = ROOT / "Excalidraw"

WARNING = (
    "==⚠  Switch to EXCALIDRAW VIEW in the MORE OPTIONS menu of this document. ⚠== "
    "You can decompress Drawing data with the command palette: "
    "'Decompress current Excalidraw file'. For more info check in plugin settings under 'Saving'"
)

SOURCE = "https://github.com/zsviczian/obsidian-excalidraw-plugin/releases/tag/2.22.3"
APP_STATE = {
    "theme": "light",
    "viewBackgroundColor": "#ffffff",
    "currentItemStrokeColor": "#1e1e1e",
    "currentItemBackgroundColor": "transparent",
    "currentItemFillStyle": "solid",
    "currentItemStrokeWidth": 2,
    "currentItemStrokeStyle": "solid",
    "currentItemRoughness": 1,
    "currentItemOpacity": 100,
    "currentItemFontFamily": 5,
    "currentItemFontSize": 20,
    "currentItemTextAlign": "left",
    "currentItemStartArrowhead": None,
    "currentItemEndArrowhead": "arrow",
    "currentItemArrowType": "round",
    "scrollX": 0,
    "scrollY": 0,
    "zoom": {"value": 0.85},
    "gridSize": 20,
    "gridModeEnabled": False,
}

# Layout constants — generous spacing throughout
NODE_W = 112
NODE_H = 58
V_GAP = 125
H_GAP = 40
PANEL_PAD = 44
PANEL_TITLE_H = 58
CONTENT_PAD = 44
LINE_H = 1.45


class Builder:
    def __init__(self):
        self.elements = []
        self._idx = 0

    def _next_index(self):
        self._idx += 1
        return f"a{self._idx}"

    def _base(self, el_type, x, y, **kwargs):
        eid = kwargs.pop("id", None) or uuid.uuid4().hex[:10]
        el = {
            "type": el_type,
            "version": 1,
            "versionNonce": uuid.uuid4().int % (2**31),
            "isDeleted": False,
            "id": eid,
            "fillStyle": kwargs.pop("fillStyle", "solid"),
            "strokeWidth": kwargs.pop("strokeWidth", 2),
            "strokeStyle": kwargs.pop("strokeStyle", "solid"),
            "roughness": 1,
            "opacity": 100,
            "angle": 0,
            "x": x,
            "y": y,
            "strokeColor": kwargs.pop("strokeColor", "#1e1e1e"),
            "backgroundColor": kwargs.pop("backgroundColor", "transparent"),
            "groupIds": kwargs.pop("groupIds", []),
            "frameId": None,
            "boundElements": [],
            "updated": 1,
            "link": None,
            "locked": False,
            "index": self._next_index(),
            "hasTextLink": False,
            "seed": 1,
        }
        el.update(kwargs)
        self.elements.append(el)
        return eid

    def text(self, x, y, content, fontSize=20, color="#1e1e1e", width=520, align="left", auto_resize=True):
        lines = content.split("\n")
        height = fontSize * LINE_H * max(len(lines), 1)
        return self._base(
            "text",
            x,
            y,
            width=width,
            height=height,
            fontSize=fontSize,
            fontFamily=5,
            text=content,
            originalText=content,
            textAlign=align,
            verticalAlign="top",
            containerId=None,
            lineHeight=LINE_H,
            autoResize=auto_resize,
            strokeColor=color,
            rawText="",
        )

    def rect(self, x, y, w, h, fill="#e7f5ff", stroke="#1971c2", stroke_width=2):
        return self._base(
            "rectangle",
            x,
            y,
            width=w,
            height=h,
            backgroundColor=fill,
            strokeColor=stroke,
            strokeWidth=stroke_width,
            roundness={"type": 3},
        )

    def arrow(self, x1, y1, x2, y2, color="#495057", dashed=False, width=2, via=None):
        if via:
            pts = [[0, 0]]
            for vx, vy in via:
                pts.append([vx - x1, vy - y1])
            pts.append([x2 - x1, y2 - y1])
            xs = [p[0] for p in pts]
            ys = [p[1] for p in pts]
            self._base(
                "arrow",
                x1,
                y1,
                width=max(xs) - min(xs) or 1,
                height=max(ys) - min(ys) or 1,
                points=pts,
                strokeColor=color,
                strokeWidth=width,
                strokeStyle="dashed" if dashed else "solid",
                roundness={"type": 2},
                startBinding=None,
                endBinding=None,
                lastCommittedPoint=None,
                startArrowhead=None,
                endArrowhead="arrow",
            )
        else:
            dx, dy = x2 - x1, y2 - y1
            self._base(
                "arrow",
                x1,
                y1,
                width=abs(dx) or 1,
                height=abs(dy) or 1,
                points=[[0, 0], [dx, dy]],
                strokeColor=color,
                strokeWidth=width,
                strokeStyle="dashed" if dashed else "solid",
                roundness={"type": 2},
                startBinding=None,
                endBinding=None,
                lastCommittedPoint=None,
                startArrowhead=None,
                endArrowhead="arrow",
            )

    def node(self, cx, cy, label, w=NODE_W, h=NODE_H, fill="#d0ebff", stroke="#1971c2", font_size=19):
        x, y = cx - w / 2, cy - h / 2
        rid = self._base(
            "rectangle",
            x,
            y,
            width=w,
            height=h,
            backgroundColor=fill,
            strokeColor=stroke,
            strokeWidth=2,
            roundness={"type": 3},
        )
        self._base(
            "text",
            x + 8,
            y + 8,
            width=w - 16,
            height=h - 16,
            fontSize=font_size,
            fontFamily=5,
            text=label,
            originalText=label,
            textAlign="center",
            verticalAlign="middle",
            containerId=rid,
            lineHeight=LINE_H,
            autoResize=True,
            strokeColor=stroke,
            rawText="",
        )
        return cx, cy

    def edge_down(self, cx1, cy1, cx2, cy2, color="#495057", dashed=False, h=NODE_H):
        self.arrow(cx1, cy1 + h / 2 + 4, cx2, cy2 - h / 2 - 4, color=color, dashed=dashed)

    def panel(self, x, y, w, h, title):
        self.rect(x, y, w, h, fill="#f8f9fa", stroke="#dee2e6", stroke_width=1)
        self.text(x + PANEL_PAD, y + 18, title, fontSize=24, color="#343a40", width=w - PANEL_PAD * 2)
        return x, y, w, h

    def gap_label(self, x, y, text, fontSize=16, color="#868e96", width=130):
        """Place a short label centred in a vertical gap between rows."""
        self.text(x, y, text, fontSize=fontSize, color=color, width=width, align="left")

    def title_block(self, title, subtitle, width=1100):
        self.text(48, 28, title, fontSize=34, color="#1e1e1e", width=width)
        self.text(48, 82, subtitle, fontSize=19, color="#495057", width=width)

    def caption(self, x, y, text, color="#495057", width=480):
        self.text(x, y, text, fontSize=17, color=color, width=width)

    def build(self):
        return {
            "type": "excalidraw",
            "version": 2,
            "source": SOURCE,
            "elements": self.elements,
            "appState": APP_STATE,
            "files": {},
        }


def export_md(json_path: Path, md_path: Path):
    raw = json_path.read_text(encoding="utf-8")
    data = json.loads(raw)
    text_lines = []
    for el in data.get("elements", []):
        if el.get("isDeleted") or el.get("type") != "text":
            continue
        txt = (el.get("text") or el.get("originalText") or "").strip()
        if not txt:
            continue
        eid = el.get("id", "")
        first = txt.split("\n")[0].strip()
        text_lines.append(f"{first} ^{eid}")

    compressed = lzstring.LZString.compressToBase64(raw)
    wrapped = "\n".join(compressed[i : i + 76] for i in range(0, len(compressed), 76))
    body = f"""---
excalidraw-plugin: parsed
tags: [excalidraw]

---
{WARNING}


# Excalidraw Data

## Text Elements
{chr(10).join(text_lines)}

%%
## Drawing
```compressed-json
{wrapped}
```
%%
"""
    md_path.write_text(body, encoding="utf-8")
    print(f"wrote {md_path.name} ({len(text_lines)} labels)")


def _merged_fib_positions(panel_x, panel_w, top_y):
    """Merged subproblem DAG — one node per distinct state."""
    cx = panel_x + panel_w / 2
    y0 = top_y
    y1 = y0 + NODE_H + V_GAP
    y2 = y1 + NODE_H + V_GAP
    spread = 155
    return {
        "fib(5)": (cx, y0),
        "fib(4)": (cx - spread, y1),
        "fib(3)": (cx + spread, y1),
        "fib(2)": (cx - spread // 2, y2),
        "fib(1)": (cx + spread, y2),
    }, y2


def _draw_merged_fib_dag(b, pos, highlight=("fib(3)",), base_key="fib(1)", highlight_style="overlap"):
    """Draw fib(5) dependency DAG with shared subproblems as single nodes."""
    if highlight_style == "compose":
        hi_fill, hi_stroke = "#d3f9d8", "#2f9e44"
    else:
        hi_fill, hi_stroke = "#ffe8cc", "#e8590c"
    base_fill, base_stroke = "#d3f9d8", "#2f9e44"
    default_fill, default_stroke = "#d0ebff", "#1971c2"

    nodes = {}
    for key, (ncx, ncy) in pos.items():
        if key == base_key:
            fill, stroke = base_fill, base_stroke
        elif key in highlight:
            fill, stroke = hi_fill, hi_stroke
        else:
            fill, stroke = default_fill, default_stroke
        nodes[key] = b.node(ncx, ncy, key, fill=fill, stroke=stroke)

    f5, f4, f3, f2, f1 = nodes["fib(5)"], nodes["fib(4)"], nodes["fib(3)"], nodes["fib(2)"], nodes["fib(1)"]

    b.edge_down(f5[0], f5[1], f4[0], f4[1])
    b.edge_down(f5[0], f5[1], f3[0], f3[1])
    b.arrow(f4[0] + NODE_W / 2 + 4, f4[1], f3[0] - NODE_W / 2 - 4, f3[1], color="#495057")
    b.edge_down(f4[0], f4[1], f2[0], f2[1])
    b.edge_down(f3[0], f3[1], f2[0], f2[1])
    b.edge_down(f3[0], f3[1], f1[0], f1[1])


def _draw_course_cycle(b, panel_x, panel_w, top_y):
    """Real-life cyclic dependency: circular course prerequisites."""
    cx = panel_x + panel_w / 2
    y0 = top_y + 58

    y1 = y0 + NODE_H + V_GAP
    y2 = y1 + NODE_H + V_GAP
    red_fill, red_stroke = "#ffe3e3", "#c92a2a"

    b.text(
        panel_x + PANEL_PAD,
        top_y,
        "Example: course registration",
        fontSize=16,
        color="#868e96",
        width=panel_w - PANEL_PAD * 2,
    )

    ml = b.node(cx, y0, "ML course", w=132, h=NODE_H, fill=red_fill, stroke=red_stroke, font_size=18)
    stats = b.node(cx, y1, "Stats course", w=144, h=NODE_H, fill=red_fill, stroke=red_stroke, font_size=18)
    calc = b.node(cx, y2, "Calc course", w=140, h=NODE_H, fill=red_fill, stroke=red_stroke, font_size=18)

    b.edge_down(ml[0], ml[1], stats[0], stats[1], color="#c92a2a")
    b.edge_down(stats[0], stats[1], calc[0], calc[1], color="#c92a2a")

    margin_x = panel_x + 44
    b.arrow(
        calc[0] - 70,
        calc[1],
        ml[0] - 70,
        ml[1],
        color="#c92a2a",
        dashed=True,
        width=2,
        via=[(margin_x, calc[1]), (margin_x, ml[1])],
    )

    req_x = cx + 92
    b.text(req_x, y0 + 6, "requires", fontSize=14, color="#c92a2a", width=72)
    b.text(req_x, y1 + 6, "requires", fontSize=14, color="#c92a2a", width=72)
    b.text(margin_x - 6, (y1 + y2) / 2 - 10, "requires", fontSize=14, color="#c92a2a", width=72, align="center")

    cap_y = y2 + NODE_H / 2 + 56
    b.caption(
        panel_x + PANEL_PAD,
        cap_y,
        "ML → Stats → Calc → ML  (no course can be taken first)",
        "#c92a2a",
        panel_w - PANEL_PAD * 2,
    )
    return y2


def build_dag_diagram():
    b = Builder()
    b.title_block(
        "① DAG — Subproblem Dependencies",
        'Nodes = subproblems   ·   Arrows = "need answer first"   ·   Acyclic = no loops',
    )

    top = 130
    pw, ph = 620, 680
    gap = 88
    px1 = 48
    px2 = px1 + pw + gap

    graph_y = top + PANEL_TITLE_H + CONTENT_PAD
    b.panel(px1, top, pw, ph, "Valid DAG")
    pos, bottom_y = _merged_fib_positions(px1, pw, graph_y)
    _draw_merged_fib_dag(b, pos, highlight=("fib(3)",), base_key="fib(1)")

    cap_y = bottom_y + NODE_H / 2 + 56
    b.caption(px1 + PANEL_PAD, cap_y, "Orange fib(3) = one node, two incoming edges (overlap)", "#e8590c", pw - PANEL_PAD * 2)
    b.caption(px1 + PANEL_PAD, cap_y + 36, "Green fib(1) = base case", "#2f9e44", pw - PANEL_PAD * 2)

    b.panel(px2, top, pw, ph, "Invalid — Cycle ✗")
    _draw_course_cycle(b, px2, pw, top + PANEL_TITLE_H + CONTENT_PAD - 8)

    return b.build()


def build_overlap_tree_diagram():
    b = Builder()
    b.title_block(
        "② Overlap vs Tree — When Memo Helps",
        "Same subproblem state twice? Memo pays off.   All unique states? Skip the table.",
    )

    top = 130
    pw, ph = 620, 700
    gap = 88
    px1, px2 = 48, 48 + pw + gap

    graph_y = top + PANEL_TITLE_H + CONTENT_PAD
    b.panel(px1, top, pw, ph, "Overlapping — Fibonacci")
    pos, bottom_y = _merged_fib_positions(px1, pw, graph_y)
    _draw_merged_fib_dag(b, pos, highlight=("fib(3)",))
    b.caption(px1 + PANEL_PAD, bottom_y + NODE_H / 2 + 56, "fib(3) shared → memoize & reuse ✓", "#e8590c", pw - PANEL_PAD * 2)

    b.panel(px2, top, pw, ph, "Tree — Zero Overlap (Merge Sort)")
    cx = px2 + pw / 2
    y0 = graph_y
    y1 = y0 + NODE_H + V_GAP
    y2 = y1 + NODE_H + V_GAP
    spread1 = 135
    spread2 = 148

    root = b.node(cx, y0, "[0, 7]", w=120, h=NODE_H, font_size=17)
    l1a = b.node(cx - spread1, y1, "[0, 3]", w=120, h=NODE_H, font_size=17)
    l1b = b.node(cx + spread1, y1, "[4, 7]", w=120, h=NODE_H, font_size=17)
    l2a = b.node(cx - spread1 - spread2 / 2, y2, "[0, 1]", w=120, h=NODE_H, font_size=17)
    l2b = b.node(cx - spread1 + spread2 / 2, y2, "[2, 3]", w=120, h=NODE_H, font_size=17)
    l2c = b.node(cx + spread1 - spread2 / 2, y2, "[4, 5]", w=120, h=NODE_H, font_size=17)
    l2d = b.node(cx + spread1 + spread2 / 2, y2, "[6, 7]", w=120, h=NODE_H, font_size=17)

    for parent, child in [(root, l1a), (root, l1b), (l1a, l2a), (l1a, l2b), (l1b, l2c), (l1b, l2d)]:
        b.edge_down(parent[0], parent[1], child[0], child[1])

    b.caption(px2 + PANEL_PAD, y2 + NODE_H / 2 + 56, "Every interval unique → memo never reused ✗", "#495057", pw - PANEL_PAD * 2)

    return b.build()


def _edge_h(b, left_cx, cy, right_cx, label, color="#495057", node_w=72, node_h=NODE_H, font_size=15):
    """Horizontal edge between two node centres with a weight label above."""
    y = cy
    x1 = left_cx + node_w / 2 + 4
    x2 = right_cx - node_w / 2 - 4
    b.arrow(x1, y, x2, y, color=color, width=2)
    if label:
        mid = (x1 + x2) / 2
        b.text(mid - 18, y - 28, label, fontSize=font_size, color=color, width=36, align="center")


def _edge_diag(b, cx1, cy1, cx2, cy2, label, color="#495057", node_w=72, node_h=NODE_H, font_size=15, label_dx=0, label_dy=-24):
    """Diagonal edge between node centres."""
    dx, dy = cx2 - cx1, cy2 - cy1
    dist = math.hypot(dx, dy) or 1
    ux, uy = dx / dist, dy / dist
    x1 = cx1 + ux * (node_w / 2 + 4)
    y1 = cy1 + uy * (node_h / 2 + 4)
    x2 = cx2 - ux * (node_w / 2 + 4)
    y2 = cy2 - uy * (node_h / 2 + 4)
    b.arrow(x1, y1, x2, y2, color=color, width=2)
    if label:
        mid_x = (x1 + x2) / 2 + label_dx
        mid_y = (y1 + y2) / 2 + label_dy
        b.text(mid_x - 18, mid_y, label, fontSize=font_size, color=color, width=36, align="center")


def _coin_change_dp(amount, coins):
    inf = 10**9
    dp = [inf] * (amount + 1)
    dp[0] = 0
    parent = {}
    for i in range(1, amount + 1):
        for c in sorted(coins):
            if c <= i and dp[i - c] + 1 < dp[i]:
                dp[i] = dp[i - c] + 1
                parent[i] = (i - c, c)
    return dp, parent


def _draw_coin_change_substructure(b, panel_x, panel_y, panel_w, amount, coins):
    """Compact coin-change graph — optimal path + a few alternative first choices."""
    dp, _parent = _coin_change_dp(amount, coins)

    node_fill = "#ffffff"
    node_stroke = "#ced4da"
    edge_color = "#ced4da"
    green_fill, green_stroke = "#d3f9d8", "#2f9e44"

    nh, nw = 58, 96
    cx = panel_x + panel_w / 2
    y0 = panel_y + 175
    y1 = y0 + nh + 100
    y2 = y1 + nh + 100
    spread = 220

    def draw_node(x, y, label, on_path):
        fill = green_fill if on_path else node_fill
        stroke = green_stroke if on_path else node_stroke
        return b.node(x, y, label, w=nw, h=nh, fill=fill, stroke=stroke, font_size=16)

    def connect(x1, y1, x2, y2, color, width, coin_label, label_side=0):
        b.arrow(x1, y1 + nh / 2 + 4, x2, y2 - nh / 2 - 4, color=color, width=width)
        mx, my = (x1 + x2) / 2 + label_side, (y1 + y2) / 2
        b.text(mx - 22, my - 10, coin_label, fontSize=14, color=color, width=44, align="center")

    draw_node(cx, y0, f"${amount}  ·  {dp[amount]}", on_path=True)
    draw_node(cx - spread, y1, f"$5  ·  {dp[5]}", on_path=False)
    draw_node(cx, y1, f"$3  ·  {dp[3]}", on_path=True)
    draw_node(cx + spread, y1, f"$2  ·  {dp[2]}", on_path=False)
    draw_node(cx, y2, "$0", on_path=True)

    connect(cx, y0, cx - spread, y1, edge_color, 2, "−$1", label_side=-28)
    connect(cx, y0, cx, y1, green_stroke, 3, "−$3")
    connect(cx, y0, cx + spread, y1, edge_color, 2, "−$4", label_side=28)
    connect(cx, y1, cx, y2, green_stroke, 3, "−$3")

    b.text(
        cx + spread + 56,
        y1 + 8,
        "→ 3 coins",
        fontSize=14,
        color="#868e96",
        width=88,
    )

    leg_y = y2 + nh / 2 + 48
    b.text(
        panel_x + CONTENT_PAD,
        leg_y,
        "Green = optimal path ($3 + $3 = 2 coins)     Gray = other choices DP also evaluates",
        fontSize=15,
        color="#495057",
        width=panel_w - CONTENT_PAD * 2,
    )
    b.text(
        cx - 210,
        y0 - nh / 2 - 32,
        "each node = remaining amount  ·  number = min coins needed",
        fontSize=14,
        color="#868e96",
        width=420,
        align="center",
    )
    return leg_y, dp[amount]


def build_optimal_substructure_diagram():
    b = Builder()
    b.text(48, 20, "Pillar B — Optimal Substructure", fontSize=28, color="#1e1e1e", width=860)
    b.text(
        48,
        58,
        "Global optimum = combine optimal sub-answers — the best whole is built from the best pieces.",
        fontSize=19,
        color="#495057",
        width=1000,
    )

    amount = 6
    coins = [1, 3, 4]

    px, py, pw, ph = 48, 92, 1000, 760
    b.rect(px, py, pw, ph, fill="#f8f9fa", stroke="#dee2e6", stroke_width=1)

    b.text(
        px + CONTENT_PAD,
        py + 22,
        "Coin change — given coin values, make a target amount using the fewest coins possible.",
        fontSize=18,
        color="#495057",
        width=pw - CONTENT_PAD * 2,
    )
    b.text(
        px + CONTENT_PAD,
        py + 52,
        f"Example: make ${amount} with coins $1, $3, $4  —  arrows show coin picked at each step.",
        fontSize=16,
        color="#868e96",
        width=pw - CONTENT_PAD * 2,
    )

    green_stroke = "#2f9e44"
    graph_bottom, opt_count = _draw_coin_change_substructure(b, px, py, pw, amount, coins)

    cap_y = graph_bottom + 56
    b.text(
        px + CONTENT_PAD,
        cap_y,
        f"opt(${amount}) = 1 + opt($3) = 1 + 1 = {opt_count} coins  ($3 + $3)  ✓",
        fontSize=19,
        color=green_stroke,
        width=pw - CONTENT_PAD * 2,
        align="center",
    )
    b.caption(
        px + CONTENT_PAD,
        cap_y + 44,
        "Follow green: every step uses an optimal sub-answer → global optimum",
        green_stroke,
        pw - CONTENT_PAD * 2,
    )
    b.caption(
        px + CONTENT_PAD,
        cap_y + 84,
        "Gray branches = suboptimal first choices  ·  green = optimal sub-answers composed",
        "#495057",
        pw - CONTENT_PAD * 2,
    )

    return b.build()


def build_non_additive_diagram():
    b = Builder()
    b.text(48, 20, "③ Non-Additive Goal — maximize trip average", fontSize=28, color="#1e1e1e", width=860)

    px, py, pw, ph = 48, 72, 1000, 920
    b.rect(px, py, pw, ph, fill="#f8f9fa", stroke="#dee2e6", stroke_width=1)

    b.text(
        px + CONTENT_PAD,
        py + 22,
        "2-day hike — rate each day 0–10.  Goal: best average across both days.",
        fontSize=18,
        color="#495057",
        width=pw - CONTENT_PAD * 2,
    )

    label_x = px + CONTENT_PAD
    cx = px + 500
    spread = 270
    nh = 68
    v_gap = 150

    y_hdr = py + 80
    y_start = y_hdr + 52
    y1 = y_start + nh + v_gap
    y2 = y1 + nh + v_gap
    y3 = y2 + nh + v_gap

    red_fill, red_stroke = "#ffe3e3", "#c92a2a"
    green_fill, green_stroke = "#d3f9d8", "#2f9e44"
    blue_fill, blue_stroke = "#e7f5ff", "#1971c2"

    b.text(cx - spread, y_hdr, "Path A  (naive keeps)", fontSize=17, color="#c92a2a", width=220, align="center")
    b.text(cx + spread, y_hdr, "Path B  (gets pruned)", fontSize=17, color="#2f9e44", width=220, align="center")

    start = b.node(cx, y_start, "Start", w=100, h=nh, fill=blue_fill, stroke=blue_stroke, font_size=20)

    d1a = b.node(cx - spread, y1, "8", w=80, h=nh, fill=red_fill, stroke=red_stroke, font_size=24)
    d1b = b.node(cx + spread, y1, "2", w=80, h=nh, fill=green_fill, stroke=green_stroke, font_size=24)
    d2a = b.node(cx - spread, y2, "0", w=80, h=nh, fill=red_fill, stroke=red_stroke, font_size=24)
    d2b = b.node(cx + spread, y2, "8", w=80, h=nh, fill=green_fill, stroke=green_stroke, font_size=24)
    avg_a = b.node(cx - spread, y3, "4  ✗", w=96, h=nh, fill=red_fill, stroke=red_stroke, font_size=22)
    avg_b = b.node(cx + spread, y3, "5  ✓", w=96, h=nh, fill=green_fill, stroke=green_stroke, font_size=22)

    for p, c in [(start, d1a), (start, d1b), (d1a, d2a), (d1b, d2b), (d2a, avg_a), (d2b, avg_b)]:
        b.edge_down(p[0], p[1], c[0], c[1], h=nh)

    # Row labels sit in the vertical gaps (never on top of nodes)
    def mid(y_a, y_b):
        return (y_a + nh / 2 + y_b - nh / 2) / 2

    b.gap_label(label_x, mid(y_start, y1) - 8, "Day 1")
    b.gap_label(label_x, mid(y1, y2) - 8, "Day 2")
    b.gap_label(label_x, mid(y2, y3) - 8, "Trip avg")

    fork_y = mid(y_start, y1) - 24
    b.text(cx - 108, fork_y, "8 > 2  →  keep Path A", fontSize=16, color="#c92a2a", width=216, align="center")

    rail_x = cx + spread + 58
    b.arrow(rail_x, y1 + nh / 2 + 8, rail_x, y3 - nh / 2 - 8, color="#c92a2a", dashed=True, width=2)
    b.text(rail_x + 12, mid(y1, y3) - 10, "pruned", fontSize=15, color="#c92a2a", width=72)

    b.text(
        px + CONTENT_PAD,
        y3 + nh / 2 + 52,
        "Path B wins globally (avg 5) — but naive DP discards it after Day 1",
        fontSize=17,
        color="#495057",
        width=pw - CONTENT_PAD * 2,
    )

    return b.build()


def build_state_space_diagram():
    b = Builder()
    b.title_block(
        "④ State Space Explosion — Curse of Dimensionality",
        "Each unique (i, w, …) tuple = one memo slot. More dimensions → combinatorial blow-up.",
    )

    top = 130
    pw, ph = 520, 560
    gap = 96
    px1, px2 = 48, 48 + pw + gap

    graph_y = top + PANEL_TITLE_H + CONTENT_PAD + 16
    b.panel(px1, top, pw, ph, "2D state — dp[i][w]")
    cell, gap_c = 54, 18
    ox = px1 + PANEL_PAD + 48
    oy = graph_y
    for r in range(4):
        for c in range(4):
            fill = "#d0ebff" if (r, c) == (2, 3) else "#ffffff"
            stroke = "#1971c2" if (r, c) == (2, 3) else "#ced4da"
            b.rect(ox + c * (cell + gap_c), oy + r * (cell + gap_c), cell, cell, fill=fill, stroke=stroke, stroke_width=1)
    b.text(ox - 28, oy + 2 * (cell + gap_c) + 14, "i", fontSize=17, color="#868e96", width=24)
    b.text(ox + 4 * (cell + gap_c) + 16, oy - 28, "w", fontSize=17, color="#868e96", width=24)
    grid_bottom = oy + 4 * (cell + gap_c)
    b.caption(px1 + PANEL_PAD, grid_bottom + 44, "4 × 4 = 16 slots  (manageable)", "#495057", pw - PANEL_PAD * 2)

    b.panel(px2, top, pw, ph, "4D state — dp[x][y][bat][spd]")
    tx = px2 + PANEL_PAD
    ty = graph_y
    b.text(tx, ty, "x × y × battery × speed", fontSize=22, color="#343a40", width=420)
    b.text(tx, ty + 56, "Each dimension multiplies\nmemo table size", fontSize=18, color="#495057", width=420)
    b.text(tx, ty + 124, "Continuous precision → ∞ keys", fontSize=18, color="#495057", width=420)

    box_y = ty + 204
    rid = b.rect(tx, box_y, 380, 84, fill="#ffe3e3", stroke="#c92a2a", stroke_width=2)
    b._base(
        "text",
        tx + 16,
        box_y + 18,
        width=348,
        height=48,
        fontSize=20,
        fontFamily=5,
        text="RAM exhausted",
        originalText="RAM exhausted",
        textAlign="center",
        verticalAlign="middle",
        containerId=rid,
        lineHeight=LINE_H,
        autoResize=True,
        strokeColor="#c92a2a",
        rawText="",
    )

    arrow_y = oy + 2 * (cell + gap_c) + cell / 2
    b.arrow(px1 + pw - 12, arrow_y, px2 + 4, arrow_y, color="#868e96", width=2)
    b.text(px1 + pw + 10, arrow_y - 32, "add dims", fontSize=15, color="#868e96", width=80, align="center")

    return b.build()


def _audit_diagram(name, data):
    """Print overlap / clip report (ignores bound text, panels, grid cells)."""
    items, panels = [], []
    for el in data["elements"]:
        if el.get("isDeleted") or el.get("containerId"):
            continue
        t = el["type"]
        if t not in ("rectangle", "text", "ellipse"):
            continue
        x, y = el["x"], el["y"]
        w, h = el.get("width", 20), el.get("height", 14)
        if t == "text":
            h = max(h, el.get("fontSize", 14) * LINE_H * max(1, (el.get("text") or "").count("\n") + 1))
        label = (el.get("text") or el.get("originalText") or t)[:30]
        box = (label, x, y, x + w, y + h)
        is_panel = t == "rectangle" and el.get("strokeColor") == "#dee2e6" and w > 400
        is_grid = t == "rectangle" and w <= 58 and h <= 58
        if is_panel:
            panels.append(box)
        elif not is_grid:
            items.append(box)

    ov = []
    for i, a in enumerate(items):
        for j, b in enumerate(items):
            if i >= j:
                continue
            if a[1] < b[3] - 3 and a[3] > b[1] + 3 and a[2] < b[4] - 3 and a[4] > b[2] + 3:
                ov.append((a[0], b[0]))

    clips = []
    for panel in panels or [("canvas", 40, 20, 1400, 900)]:
        _, bx1, by1, bx2, by2 = panel
        for label, x1, y1, x2, y2 in items:
            if x2 <= bx1 or x1 >= bx2 or y2 <= by1 or y1 >= by2:
                continue
            if x1 < bx1 + 8:
                clips.append(f"{label!r} left {x1 - bx1:+.0f}px")
            if y1 < by1 + 8:
                clips.append(f"{label!r} top {y1 - by1:+.0f}px")
            if x2 > bx2 - 8:
                clips.append(f"{label!r} right {x2 - bx2:+.0f}px")
            if y2 > by2 - 8:
                clips.append(f"{label!r} bottom {y2 - by2:+.0f}px")

    status = "OK" if not ov and not clips else "ISSUES"
    print(f"  audit {name}: {status}  overlaps={len(ov)}  clips={len(clips)}")
    for o in ov[:4]:
        print(f"    overlap: {o[0]} / {o[1]}")
    for c in clips[:4]:
        print(f"    clip: {c}")


def main():
    diagrams = [
        ("Dynamic-Programming-DAG.excalidraw", "Ex-DP_DAG.md", build_dag_diagram),
        ("Dynamic-Programming-Overlap-Tree.excalidraw", "Ex-DP_Overlap_Tree.md", build_overlap_tree_diagram),
        ("Dynamic-Programming-OptimalSubstructure.excalidraw", "Ex-DP_OptimalSubstructure.md", build_optimal_substructure_diagram),
        ("Dynamic-Programming-NonAdditive.excalidraw", "Ex-DP_NonAdditive.md", build_non_additive_diagram),
        ("Dynamic-Programming-StateSpace.excalidraw", "Ex-DP_StateSpace.md", build_state_space_diagram),
    ]
    EX_DIR.mkdir(parents=True, exist_ok=True)
    EMBED_DIR.mkdir(parents=True, exist_ok=True)

    for json_name, md_name, builder_fn in diagrams:
        data = builder_fn()
        json_path = EX_DIR / json_name
        json_path.write_text(json.dumps(data, indent="\t"), encoding="utf-8")
        export_md(json_path, EMBED_DIR / md_name)
        _audit_diagram(json_name, data)
        print(f"wrote {json_path.name}")


if __name__ == "__main__":
    main()
