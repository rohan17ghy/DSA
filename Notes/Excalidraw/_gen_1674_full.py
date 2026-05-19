import json
import uuid
from itertools import accumulate

OUT = r"c:\Code\DSA\Notes\Excalidraw\Line-Sweep-1674-Complementary.excalidraw"
NUMS = [1, 2, 4, 3, 5, 2, 6, 1]
LIMIT = 6
UNIT = 44
TX = 220
ROW_H = 72

def uid():
    return uuid.uuid4().hex[:10]

def text_el(x, y, content, fontSize=16, color="#1e1e1e", width=None):
    w = width or min(1100, max(80, len(max(content.split("\n"), key=len)) * fontSize * 0.55))
    return {
        "type": "text", "version": 1, "versionNonce": 1, "isDeleted": False,
        "id": uid(), "fillStyle": "solid", "strokeWidth": 2, "strokeStyle": "solid",
        "roughness": 1, "opacity": 100, "angle": 0, "x": x, "y": y,
        "strokeColor": color, "backgroundColor": "transparent",
        "groupIds": [], "frameId": None, "boundElements": [], "updated": 1,
        "link": None, "locked": False, "index": "a0", "hasTextLink": False, "seed": 1,
        "width": w, "height": fontSize * 1.45 * (content.count("\n") + 1),
        "fontSize": fontSize, "fontFamily": 5,
        "text": content, "originalText": content,
        "textAlign": "left", "verticalAlign": "top", "containerId": None, "lineHeight": 1.25,
        "baseline": int(fontSize * 0.75), "roundness": None, "autoResize": False, "rawText": ""
    }

def rect_el(x, y, w, h, stroke="#1e1e1e", fill="transparent", dashed=False, opacity=100):
    return {
        "type": "rectangle", "version": 1, "versionNonce": 1, "isDeleted": False,
        "id": uid(), "fillStyle": "solid", "strokeWidth": 2,
        "strokeStyle": "dashed" if dashed else "solid",
        "roughness": 1, "opacity": opacity, "angle": 0, "x": x, "y": y,
        "strokeColor": stroke, "backgroundColor": fill,
        "groupIds": [], "frameId": None, "boundElements": [], "updated": 1,
        "link": None, "locked": False, "index": "a0", "hasTextLink": False, "seed": 1,
        "width": w, "height": h, "roundness": {"type": 3}
    }

def line_el(x1, y1, x2, y2, color="#868e96", dotted=False, width=2):
    return {
        "type": "line", "version": 1, "versionNonce": 1, "isDeleted": False,
        "id": uid(), "fillStyle": "solid", "strokeWidth": width,
        "strokeStyle": "dotted" if dotted else "solid",
        "roughness": 1, "opacity": 100, "angle": 0, "x": x1, "y": y1,
        "strokeColor": color, "backgroundColor": "transparent",
        "groupIds": [], "frameId": None, "boundElements": [], "updated": 1,
        "link": None, "locked": False, "index": "a0", "hasTextLink": False, "seed": 1,
        "width": max(1, abs(x2 - x1)), "height": max(1, abs(y2 - y1)),
        "points": [[0, 0], [x2 - x1, y2 - y1]],
        "lastCommittedPoint": None, "startBinding": None, "endBinding": None,
        "startArrowhead": None, "endArrowhead": None
    }

def arrow_el(x1, y1, x2, y2, color="#1e1e1e"):
    return {
        "type": "arrow", "version": 1, "versionNonce": 1, "isDeleted": False,
        "id": uid(), "fillStyle": "solid", "strokeWidth": 2, "strokeStyle": "solid",
        "roughness": 1, "opacity": 100, "angle": 0, "x": x1, "y": y1,
        "strokeColor": color, "backgroundColor": "transparent",
        "groupIds": [], "frameId": None, "boundElements": [], "updated": 1,
        "link": None, "locked": False, "index": "a0", "hasTextLink": False, "seed": 1,
        "width": max(1, abs(x2 - x1)), "height": max(1, abs(y2 - y1)),
        "points": [[0, 0], [x2 - x1, y2 - y1]],
        "lastCommittedPoint": None, "startBinding": None, "endBinding": None,
        "startArrowhead": None, "endArrowhead": "arrow", "elbowed": False
    }

def sum_x(s, base=220, unit=44):
    return base + (s - 2) * unit

n = len(NUMS)
pairs = []
colors = [("#e8590c", "#fff3bf"), ("#1971c2", "#d0ebff"), ("#2f9e44", "#b2f2bb"), ("#7048e8", "#e5dbff")]
for i in range(n // 2):
    a, b = NUMS[i], NUMS[n - 1 - i]
    mn, mx = min(a, b), max(a, b)
    lo_t, hi_t = 1 + mn, LIMIT + mx
    pairs.append((f"P{i}", a, b, mn, mx, mn + mx, lo_t, hi_t, colors[i][0], colors[i][1]))

def build_diff():
    d = [0] * (2 * LIMIT + 2)
    for i in range(n // 2):
        x, y = NUMS[i], NUMS[n - 1 - i]
        if x > y:
            x, y = y, x
        d[2] += 2
        d[x + 1] -= 2
        d[x + 1] += 1
        d[x + y] -= 1
        d[x + y + 1] += 1
        d[y + LIMIT + 1] -= 1
        d[y + LIMIT + 1] += 2
    return d

diff = build_diff()
costs = list(accumulate(diff[2:]))
best_cost = min(costs)
best_T = costs.index(best_cost) + 2


def pair_diff_array(mn, mx, limit):
    """Code uses x=mn, y=mx: stamps at lo=1+mn, sum=mn+mx, hi+1=limit+mx+1."""
    d = [0] * (2 * limit + 2)
    d[2] += 2
    d[mn + 1] -= 2
    d[mn + 1] += 1
    d[mn + mx] -= 1
    d[mn + mx + 1] += 1
    d[mx + limit + 1] -= 1
    d[mx + limit + 1] += 2
    return d


def pair_moves(a, b, t, limit):
    mn, mx = min(a, b), max(a, b)
    s = mn + mx
    lo_t, hi_t = 1 + mn, limit + mx
    if t == s:
        return 0
    if t < lo_t or t > hi_t:
        return 2
    return 1


def total_moves_at(t):
    return sum(pair_moves(a, b, t, LIMIT) for _, a, b, *_ in pairs)


els = []

# Header
els.append(text_el(40, 0, "Line Sweep — 1674. Minimum Moves to Make Array Complementary", 28, width=920))
els.append(rect_el(40, 52, 1080, 72, "#1971c2", "#e7f5ff"))
els.append(text_el(58, 72, f"nums = {NUMS}   limit = {LIMIT}   →   answer = {best_cost}", 16, "#1971c2", 980))

# ── ① Mirror pairs ──
Y1 = 200
els.append(text_el(48, Y1, "① Mirror pairs", 24, "#2f9e44"))
els.append(text_el(64, Y1 + 44, "Index i is paired with n−1−i  →  4 pairs, one shared target T", 16, "#495057", 900))

ax, ay = 64, Y1 + 95
cell = 58
for i, v in enumerate(NUMS):
    x = ax + i * cell
    els.append(rect_el(x, ay, cell - 8, 36, "#868e96", "#f8f9fa"))
    els.append(text_el(x + 18, ay + 8, str(v), 16))
    els.append(text_el(x + 14, ay - 26, str(i), 12, "#868e96"))

for i in range(n // 2):
    x1 = ax + i * cell + 22
    x2 = ax + (n - 1 - i) * cell + 22
    sc = colors[i][0]
    els.append(line_el(x1, ay + 42, x2, ay + 42, sc, width=2))
    els.append(text_el((x1 + x2) / 2 - 12, ay + 48, f"P{i}", 12, sc))

py = ay + 105
for label, a, b, mn, mx, s, lo_t, hi_t, sc, fill in pairs:
    els.append(rect_el(64, py, 480, 44, sc, fill, opacity=35))
    els.append(text_el(80, py + 12, f"{label}:  ({a}) + ({b})  =  {s}", 15, sc))
    py += 58

Y1_END = py + 35

# ── ② Mental model ──
Y2 = Y1_END + 90
panel_top = Y2 + 48
rows_top = panel_top + 65
axis_y = rows_top + len(pairs) * ROW_H + 55
panel_bottom = axis_y + 85

els.append(rect_el(36, Y2, 1088, panel_bottom - Y2 + 25, "#e03131", "#fff5f5", dashed=True, opacity=65))
els.append(text_el(52, Y2 + 12, "② Pick target T — slide the vertical bar", 24, "#e03131"))
els.append(text_el(68, Y2 + 48, "Each row = current pair sum.  Move | left/right.  Minimize total moves.", 16, "#495057", 920))

axis_span = (2 * LIMIT - 2) * UNIT
for row, (label, a, b, mn, mx, s, lo_t, hi_t, sc, fill) in enumerate(pairs):
    ry = rows_top + row * ROW_H
    els.append(text_el(52, ry + 6, f"{label}  ({a}+{b})  sum={s}", 14, sc))
    bw = max((s - 2) * UNIT + 8, 16)
    els.append(rect_el(TX, ry + 28, axis_span + 24, 22, "#e9ecef", "#f8f9fa"))
    els.append(rect_el(TX, ry + 30, bw, 18, sc, fill))

els.append(line_el(TX, axis_y, TX + axis_span, axis_y, "#495057"))
for s in [2, 4, 6, 8, 10, 12]:
    els.append(text_el(sum_x(s, TX, UNIT) - 6, axis_y + 12, str(s), 12, "#495057"))

tx = sum_x(best_T, TX, UNIT)
els.append(line_el(tx, rows_top - 10, tx, axis_y + 30, "#7048e8", width=4))
els.append(text_el(tx - 20, rows_top - 38, f"T={best_T}", 16, "#7048e8"))

els.append(rect_el(52, panel_bottom - 50, 980, 48, "#ffc9c9", "#fff5f5"))
els.append(text_el(68, panel_bottom - 36, "✗ Wrong: pick T where most bars end (mode)", 15, "#e03131", 800))
els.append(text_el(68, panel_bottom - 14, "✓ Right: pick T with minimum total moves", 15, "#2f9e44", 600))

# ── ③ ONE pair — three concrete examples (no strip chart) ──
Y3 = panel_bottom + 120
CARD_W, CARD_H, CARD_GAP = 1000, 92, 28

els.append(text_el(48, Y3, "③ One pair only — how many moves for a chosen T?", 24, "#7048e8"))
els.append(text_el(64, Y3 + 44,
    "Forget the other pairs for a moment.  P1 = 2 and 6  →  sum is 8 today.", 17, "#495057", 920))

PAIR_Y = Y3 + 88
els.append(rect_el(64, PAIR_Y, CARD_W, 56, "#1971c2", "#e7f5ff", opacity=55))
els.append(text_el(88, PAIR_Y + 16, "P1 today:   2  +  6  =  8", 20, "#1971c2", 500))
els.append(text_el(520, PAIR_Y + 18, "If we force this pair to sum to T, how many edits?", 15, "#495057", 520))

def cost_card(y, t, explain, moves, stroke, fill):
    els.append(rect_el(64, y, CARD_W, CARD_H, stroke, fill, opacity=45))
    els.append(text_el(88, y + 14, f"If we pick  T = {t}", 18, stroke, 280))
    els.append(text_el(88, y + 42, explain, 15, "#343a40", 720))
    badge_x = 880
    els.append(rect_el(badge_x, y + 18, 150, 56, stroke, fill, opacity=80))
    label = "0 moves" if moves == 0 else ("1 move" if moves == 1 else "2 moves")
    els.append(text_el(badge_x + 28, y + 36, label, 20, stroke, 160))

card_y = PAIR_Y + 80
cost_card(card_y, 8, "Already 2 + 6 = 8  →  do nothing", 0, "#2f9e44", "#b2f2bb")
card_y += CARD_H + CARD_GAP
cost_card(card_y, 6, "Change one number, e.g. 6 → 4  so  2 + 4 = 6", 1, "#f08c00", "#fff3bf")
card_y += CARD_H + CARD_GAP
cost_card(card_y, 2, "Both numbers are far from 2  →  change both", 2, "#e03131", "#ffc9c9")

els.append(text_el(64, card_y + CARD_H + 24,
    "Same pair, different T → different cost.  Each pair only ever costs 0, 1, or 2.", 16, "#7048e8", 900))
els.append(text_el(64, card_y + CARD_H + 52,
    "§④ repeats this for all pairs and adds the numbers.", 15, "#868e96", 600))

Y3_END = card_y + CARD_H + 95

# ── ④ Global answer — 3 plain steps (no grid, no sweep chart) ──
Y4 = Y3_END + 100
W = 1000

els.append(text_el(48, Y4, "④ Put it together — the whole array", 24, "#f08c00"))
els.append(text_el(64, Y4 + 42,
    "§③ told you the cost for one pair.  Now every pair shares the same target T.", 17, "#495057", 920))


def step_box(y, num, title, body, h, stroke="#f08c00", fill="#fff9db"):
  els.append(rect_el(64, y, W, h, stroke, fill, opacity=40))
  els.append(rect_el(80, y + 14, 40, 40, stroke, "#ffffff", opacity=90))
  els.append(text_el(94, y + 24, str(num), 22, stroke))
  els.append(text_el(140, y + 18, title, 18, stroke, 800))
  els.append(text_el(140, y + 48, body, 15, "#343a40", 860))


# Step 1 — one T for all
S1_Y = Y4 + 88
step_box(S1_Y, "1", "Choose one target sum T for the entire array",
         "All 4 pairs must end with the same sum T  (not 4 different sums).", 88)

# Visual: four labels → one T
hub_y = S1_Y + 108
els.append(rect_el(64, hub_y, W, 72, "#7048e8", "#f3f0ff", opacity=35))
for i, (label, a, b, mn, mx, s, lo_t, hi_t, sc, fill) in enumerate(pairs):
    px = 100 + i * 220
    els.append(text_el(px, hub_y + 12, label, 14, sc))
    els.append(text_el(px, hub_y + 32, f"{a}+{b}", 14, "#495057"))
    els.append(line_el(px + 40, hub_y + 58, 520, hub_y + 58, sc, dotted=True))
els.append(rect_el(470, hub_y + 44, 120, 36, "#7048e8", "#e5dbff"))
els.append(text_el(498, hub_y + 54, "same T", 16, "#7048e8"))

# Step 2 — add at T=6 (receipt style)
S2_Y = hub_y + 100
step_box(S2_Y, "2", "Add each pair's moves (use §③ for each row)",
         "", 52)

ADD_Y = S2_Y + 68
els.append(rect_el(120, ADD_Y, 420, 220, "#2f9e44", "#ebfbee", opacity=50))
els.append(text_el(150, ADD_Y + 16, "Suppose we pick  T = 6", 20, "#2f9e44", 360))

ay = ADD_Y + 52
parts = []
for label, a, b, mn, mx, s, lo_t, hi_t, sc, fill in pairs:
    mv = pair_moves(a, b, 6, LIMIT)
    parts.append(mv)
    els.append(text_el(170, ay, f"{label}  needs", 16, sc, 120))
    els.append(text_el(310, ay, str(mv), 22, "#1e1e1e", 40))
    ay += 32

els.append(line_el(170, ay + 4, 380, ay + 4, "#495057", width=2))
els.append(text_el(170, ay + 18, "Total moves", 17, "#7048e8", 160))
els.append(text_el(310, ay + 14, str(sum(parts)), 26, "#7048e8", 60))

# Step 3 — compare two other T (link §②)
S3_Y = ADD_Y + 248
step_box(S3_Y, "3", "Try other T values — keep the smallest total",
         "§② mode suggested T = 8 (two pairs already sum to 8).  You still must ADD.", 72)

CMP_Y = S3_Y + 88
# T=8 panel
els.append(rect_el(100, CMP_Y, 400, 130, "#e03131", "#fff5f5", opacity=45))
els.append(text_el(130, CMP_Y + 14, "Try  T = 8  (mode from §②)", 17, "#e03131", 320))
t8_parts = [pair_moves(a, b, 8, LIMIT) for _, a, b, *_ in pairs]
els.append(text_el(130, CMP_Y + 48,
    f"{t8_parts[0]} + {t8_parts[1]} + {t8_parts[2]} + {t8_parts[3]}  =  {sum(t8_parts)} moves", 18, "#1e1e1e", 360))

# T=4 panel (worse)
els.append(rect_el(540, CMP_Y, 400, 130, "#868e96", "#f8f9fa", opacity=45))
els.append(text_el(570, CMP_Y + 14, "Try  T = 4  (worse example)", 17, "#495057", 320))
t4_parts = [pair_moves(a, b, 4, LIMIT) for _, a, b, *_ in pairs]
els.append(text_el(570, CMP_Y + 48,
    f"{t4_parts[0]} + {t4_parts[1]} + {t4_parts[2]} + {t4_parts[3]}  =  {sum(t4_parts)} moves", 18, "#1e1e1e", 360))

# End of ④ — naive works; point to ⑤
ANS_Y = CMP_Y + 155
els.append(rect_el(64, ANS_Y, W, 88, "#7048e8", "#e5dbff", opacity=55))
els.append(text_el(88, ANS_Y + 12,
    f"Naive: try every T, add all 4 pairs each time → best total = {best_cost} moves.  Correct!",
    16, "#7048e8", 920))
els.append(text_el(88, ANS_Y + 38,
    "Too slow if limit is large.  ↓↓↓  scroll to panel ⑤ below  ↓↓↓",
    17, "#e03131", 700))

Y4_END = ANS_Y + 110

# ── ⑤ Why line sweep? (intuition only) ──
Y5 = Y4_END + 100
P5_H = 300

els.append(rect_el(36, Y5, 920, P5_H, "#1971c2", "#f8f9ff", dashed=True, opacity=40))
els.append(text_el(56, Y5 + 16, "⑤ Why line sweep?", 22, "#1971c2"))

# From §④
els.append(rect_el(72, Y5 + 56, 400, 72, "#7048e8", "#e5dbff", opacity=50))
els.append(text_el(92, Y5 + 68, "From ④ — correct but slow", 15, "#7048e8", 280))
els.append(text_el(92, Y5 + 92,
    "For each T, add cost of all n/2 pairs  →  O(limit × n)",
    14, "#495057", 360))

els.append(arrow_el(490, Y5 + 92, 540, Y5 + 92, "#495057"))

# Insight
els.append(rect_el(552, Y5 + 56, 380, 72, "#2f9e44", "#ebfbee", opacity=50))
els.append(text_el(572, Y5 + 68, "Key insight", 15, "#2f9e44", 160))
els.append(text_el(572, Y5 + 92,
    "Each pair: cost(T) is flat on intervals of T",
    14, "#495057", 340))

# Pattern
els.append(rect_el(72, Y5 + 148, 860, 130, "#495057", "#f8f9fa", opacity=55))
els.append(text_el(96, Y5 + 162, "Pattern → line sweep / difference array", 16, "#1e1e1e", 400))
els.append(text_el(96, Y5 + 190,
    "• One shared parameter on a line (here: target sum T)",
    14, "#495057", 780))
els.append(text_el(96, Y5 + 214,
    "• Many items, each only changes the answer at a few boundaries",
    14, "#495057", 780))
els.append(text_el(96, Y5 + 238,
    "• Need min (or max) of the sum over all items  →  stamp + prefix walk",
    14, "#1971c2", 780))

els.append(text_el(96, Y5 + 268,
    "Same family as 1854, meeting rooms.  Code: [[Line Sweep general theory]]",
    13, "#868e96", 720))

Y5_END = Y5 + P5_H + 40

doc = {
    "type": "excalidraw", "version": 2,
    "source": "https://github.com/zsviczian/obsidian-excalidraw-plugin/releases/tag/2.22.3",
    "elements": els,
    "appState": {
        "theme": "light", "viewBackgroundColor": "#ffffff",
        "scrollX": 20, "scrollY": -920, "zoom": {"value": 0.32},
        "currentItemFontFamily": 5, "gridSize": 20, "gridModeEnabled": False
    },
    "files": {}
}
with open(OUT, "w", encoding="utf-8") as f:
    json.dump(doc, f, indent="\t")
print("heights: Y4_end", Y4_END, "Y5_end", Y5_END, "els", len(els))
