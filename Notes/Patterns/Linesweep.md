#lineSweep #pattern

How to spot **line sweep** (difference array / event sweep) before coding.  
Templates and full code: [[Line Sweep general theory]].

---

## Core idea

Many objects each affect a **1D axis** (time, year, target value, coordinate) only on an **interval** `[L, R)`:

- Inside the interval, some quantity is **constant** (or changes only at endpoints).
- The global answer is **min / max / first crossing** of the **sum** (or balance) of all contributions along that axis.

Instead of checking every coordinate, **stamp +1 / −1 at boundaries** and walk once — **O(stamps + axis length)** or **O(n log n)** if you sort events.

---

## Use line sweep when…

Picture a **number line** (years, target sum `T`, time, …). You slide a point along it and care about a **total** at each position.

**Yes — line sweep is a good fit if all of these are true:**

1. **One number must work for everyone**  
   - 1854: which **year** has the most people alive?  
   - 1674: which **target sum `T`** should every mirror pair hit?

2. **Each person/pair only “does something” between two points on that line**  
   - 1854: alive from **birth** until **death** → +1 at birth, −1 after death.  
   - 1674: for one pair, **cost stays 0, then 1, then 2** in chunks as `T` moves — only changes at a few `T` values.

3. **You need the best total after adding everyone up**  
   - Not “what is the most common value today?”  
   - But “if I pick this spot on the line, what is **births − deaths** or **sum of all pair costs**?”

4. **Each item only touches the line at a few spots** (usually 2–4 stamps)  
   - So you can mark those spots and walk the line once instead of recalculating from scratch every time.

>[!info] **Quick test:** Can you write: *“For each item, from position A to B the contribution is X; outside that it’s something else”*? If yes, think line sweep.

---

## Do **not** use line sweep when…

**1. You only care about what the data looks like *right now*, not “cost to move to every choice”**  
- 1674 trap: two pairs already sum to **8** → mode says pick `T = 8`.  
- But another `T` might need **fewer moves** to get there.  
- **Instead:** count or pick a mode only if the problem truly asks for frequency — not minimum effort.

**2. The hard part is pairing, order, or choices — not adding numbers on one line**  
- Example vibe: assign people to tasks, reorder array for minimum swaps, pick which intervals to keep.  
- **Instead:** greedy with proof, DP, two pointers — whatever matches the constraint.

**3. The line is huge and almost empty** (e.g. values up to `10^9`, only `n` intervals)  
- You still *can* sweep by **sorting start/end events** — you do **not** need an array of size `10^9`.  
- If you’re tempted to loop `for T in range(1, 10^9)` → that’s wrong; sort events and walk those instead.

**4. The problem is really 2D** (grid, rectangle overlap area as the main object)  
- Line sweep might appear **with extra tricks** (e.g. + heap).  
- **Don’t** assume “intervals → always simple diff array” on the first read.

>[!info] **Rule of thumb:** Line sweep = *slide along one axis and add up many interval contributions.* If the story doesn’t sound like that, look at another pattern first.

---

## On a new problem — walk through this

Use the same order every time. If you get stuck, compare to [[1854. Maximum Population Year]] or [[1674. Minimum Moves to Make Array Complementary]].

### Step 1 — What is the “slider”?

Ask: *What one number are we choosing for the whole input?*

| Problem | The slider |
|---------|------------|
| 1854 | A **year** on a timeline |
| 1674 | A **target sum `T`** every pair must hit |

If there is no single shared number (everyone picks their own target), line sweep is usually **not** the first idea.

---

### Step 2 — Pick one item; draw its effect on that line

Take **one** log, pair, booking, etc. As the slider moves, does the item’s contribution stay **flat for a while**, then **jump**?

- **1854, one person:** alive every year from birth to death → flat +1 in the middle, 0 before/after.  
- **1674, one pair `(2,6)`:** cost is **2** for low `T`, **1** in the middle, **0** at `T=8`, **1** again, **2** at high `T` — flat **chunks**, not a new formula at every `T`.

If you can sketch **2–4 ranges** per item (“from here to here it’s always 0 moves / always +1 person”), you’re on the right track.

---

### Step 3 — What is the question about the slider?

After you fix a position on the line, **add up** every item’s contribution at that spot. The problem wants one of:

| Wording in the problem | What you track while walking |
|------------------------|------------------------------|
| “Maximum population / overlap / concurrent …” | **Largest** running total |
| “Minimum total cost / moves …” | **Smallest** running total |
| “First time capacity is exceeded …” | First position where total **crosses** a limit |

This is the link to the sections above: not “most common value in the array,” but **best total if we place the slider here**.

---

### Step 4 — Naive vs sweep (why we bother)

**Naive (always works as a check):** try every slider position; for each, loop all items and add contributions.  
That is what [[1674. Minimum Moves to Make Array Complementary]] §④ does for every `T`.

**Sweep:** each item only changes the total at **start/end of its flat ranges** → mark those spots, walk the line once.  
That is §⑤ — same answer, faster when there are many positions.

If Step 2 gave only a few jumps per item, Step 4 is the payoff.

---

### Step 5 — Sanity-check on paper (2 minutes)

Pick **two** slider values (e.g. `T = 4` and `T = 6` in 1674, or two years in 1854).

1. By hand: add all items at that position.  
2. Your stamps + walk should give the **same** totals.

If they match, implement using [[Line Sweep general theory]]. If not, re-draw Step 2 for one item.

---

## Problem map (in this vault)

| Problem | What it teaches |
|---------|-----------------|
| [[1854. Maximum Population Year]] | Slide over **years**; each person adds +1 while alive; find the year with the **most** people |
| [[1674. Minimum Moves to Make Array Complementary]] | Slide over **target sum `T`**; add each pair’s move cost; find **`T` with fewest total moves** |
| `2779` Maximum Beauty (code only) | Slide over **values**; each number covers a range; find **most overlap** |

Add more rows as you solve similar problems (meeting rooms, flight bookings, …).

---

## One-line pattern summary

>[!info] Many intervals on one line + min/max/sum over the whole line → difference array or sorted events + one pass.

Related: [[Line Sweep general theory]] · [[1674. Minimum Moves to Make Array Complementary]] (full thought process) · [[1854. Maximum Population Year]]
