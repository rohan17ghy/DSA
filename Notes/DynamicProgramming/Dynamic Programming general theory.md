#DP #Pattern #Theory #DAG #Tree #DivideAndConquer 

# Dynamic Programming: When It Works, When It Fails

Dynamic Programming (DP) is not just recursion with a cache. A problem must satisfy a **dependency structure** (a DAG) and **two mathematical properties** (overlapping subproblems + optimal substructure). Even when those hold, three practical conditions can still make DP wrong or unusable.

Use this as a checklist before concluding if any DP can be used in some problem or not ?

---

## 1. The Core Structure: Directed Acyclic Graphs (DAGs)

If a problem is possible to solve with DP, its subproblems and their dependencies always form a **Directed Acyclic Graph (DAG)**.

| Element | Meaning |
|---|---|
| **Nodes** | Individual subproblems you must solve |
| **Directed edges (arrows)** | Dependencies — "To solve A, I first need the answer to B" |
| **Acyclic (no loops)** | Non-negotiable. If A depends on B and B depends on A, computation never terminates |

![[ExcalidrawEmbeds/DynamicProgramming/Ex-DP_DAG | 1000]]

> **Important:** A DAG is *necessary* for a well-defined DP order, but it is *not sufficient*. You still need the two pillars below — and you must watch for the failure cases in Section 3.

---

## 2. The Two Mandatory Pillars of DP

Even if you can map a problem as a DAG, DP is useless unless the problem has **both** of these properties.

### Pillar A: Overlapping Subproblems

**Definition:** It means that there should be subproblems that we need to solve repeatedly.

- **Why DP needs it:** DP's speed comes from **memoization** — compute each distinct subproblem once, store the result in a lookup table, and reuse it.
- **When it fails:** If every subproblem is unique and independent (e.g., splitting a list in half for Merge Sort), storing answers wastes memory with no lookup benefit. Use **Divide and Conquer** instead.

![[ExcalidrawEmbeds/DynamicProgramming/Ex-DP_Overlap_Tree | 1000]]

>[!info]
> If the subproblems are not overlapping than the DAG becomes a **tree** because each node(subproblem) will have only one incoming edge(dependency). Which means even if we memoize the subproblems, it is not going to help us because we will not encounter that subproblem again

### Quick comparison: DP vs Divide and Conquer

| | **Dynamic Programming** | **Divide and Conquer** |
|---|---|---|
| Subproblem overlap | Same subproblems recur | Subproblems are independent |
| Example | Fibonacci | Merge Sort |
| Cache benefit | High — lookups pay off | Low — nothing to reuse |

### Pillar B: Optimal Substructure

**Definition:** The *optimal* (best) solution to the overall problem is composed entirely of the *optimal* solutions to its subproblems.

- **The rule:** Local perfection = global perfection.
- **Why DP needs it:** DP finds the best local answer, stores it, and **discards all other options** to save time and memory. That only works if the globally best solution is built from locally best pieces.
- **When it fails:** If combining the "best" local pieces does **not** produce the best global whole, the problem lacks optimal substructure.

![[ExcalidrawEmbeds/DynamicProgramming/Ex-DP_OptimalSubstructure | 1000]]

> [!info]
> Lack of Optimal Substructure basically means that the answers of the subproblems can't be used to derive at the main problem's solution


---

## 3. When the Graph Is a DAG, but DP Still Fails

Sometimes a problem forms a valid DAG (no cycles), yet DP is **impossible** or **highly inefficient**. Three distinct conditions cause this.

### Condition A: The Goal Is Non-Additive

DP fails when the objective **cannot be combined in a straight line** — e.g., you optimize an **average**, **percentage**, or **ratio** rather than a sum, count, or min/max that aggregates cleanly.

- **Why it fails:** DP evaluates a node, keeps the path with the best local average (or ratio), and **throws away the rest**. But a path with a temporarily worse average might combine with a large final value to produce the best **overall** average. DP discards the winning piece because it looked sub-optimal locally.

![[ExcalidrawEmbeds/DynamicProgramming/Ex-DP_NonAdditive | 1000]]

> [!info]
> Non-additive means you can't combine subproblem results with a simple sum/min/max — e.g. optimizing average or ratio from a single local score can prune away the globally best path.


### Condition B: The DAG Is a Tree (Zero Overlap)

A tree is technically a DAG (edges point one way, no cycles). But tree branches **diverge and never merge back**.

- **Why it fails (efficiency, not correctness):** You *can* use DP on a problem with tree structure, but it is **horribly inefficient**. You allocate memory for every subproblem, yet because branches never merge, you **never look up stored answers again**. You pay the memory cost for **zero speed benefit**.
- **Takeaway:** On trees with no shared subproblems, plain recursion (or DFS) is usually enough — no memo table needed.

*(See **Tree — Zero Overlap** panel in diagram above.)*

>[!info]
> If the subproblems are not overlapping than the DAG becomes a **tree** because each node(subproblem) will have only one incoming edge(dependency). Which means even if we memoize the subproblems, it is not going to help us because we will not encounter that subproblem again

### Condition C: State Space Explosion (The Memory Bottleneck)

A problem may satisfy every mathematical rule (DAG + optimal substructure + overlap) and still be **physically un-runnable** due to the **curse of dimensionality**.

- **Why it fails:** DP needs a memoization slot for **every unique subproblem**. If state tracks many variables (X, Y, battery level, speed, …), the table must cover **every combination** of those variables.
- **The result:** Adding dimensions or using highly precise continuous values (e.g., weight limit `50.19483` lbs instead of `50`) makes the number of combinations grow exponentially. DP doesn't fail on time alone — the machine **runs out of RAM** building the lookup table.

![[ExcalidrawEmbeds/DynamicProgramming/Ex-DP_StateSpace | 1000]]

>[!info]
>It means that the subproblems are too many and it is not time nor space efficient to use DP

---

## 4. Decision Checklist

Before using DP, verify all of the following:

1. **DAG:** Subproblem dependencies have no cycles.
2. **Overlapping subproblems:** Same subproblem appears more than once.
3. **Optimal substructure:** Best global solution = best local pieces combined.
4. **Additive (or decomposable) objective:** Local decisions can be merged without hidden global context (or your state encodes that context).
5. **Feasible state space:** Distinct subproblem count fits in memory.

| Check | Pass → | Fail → |
|---|---|---|
| DAG | Well-defined computation order | Infinite loop / undefined order |
| Overlapping subproblems | Memoization helps | Use Divide and Conquer |
| Optimal substructure | DP can prune safely | Greedy-like local choices mislead |
| Additive objective | Standard DP states work | Redesign state or change approach |
| Bounded state space | Tabulation / memo is practical | Memory blow-up; approximate or restructure |

---

## 5. Approaches: Top-Down vs. Bottom-Up

|Feature|Top-Down (==Memoization==)|Bottom-Up (==Tabulation==)|
|:--|:--|:--|
|**Logic**|Starts from the original problem and breaks it down.|Starts from base cases and builds up to the target.|
|**Implementation**|==Recursive== with a "memo" (storage).|==Iterative== using loops and a table/array.|
|**Space**|$O(N)$ for array + $O(N)$ recursion stack.|$O(N)$ for array only.|
|**Complexity**|Often ==easier to write== for complex states (e.g., Bitmask DP).|Generally more ==memory efficient== at a granular level.|

**Approach Diagram:**

```
graph TD
    subgraph Top_Down_Memoization
    N(Big Problem) --> S1(Subproblem)
    S1 --> S2(Smaller Subproblem)
    S2 --> B(Base Case)
    end

    subgraph Bottom_Up_Tabulation
    B2(Base Case) --> S3(Small Subproblem)
    S3 --> S4(Bigger Subproblem)
    S4 --> N2(Original Problem)
    end
```

---

#### 4. Iterative (Bottom-Up) Logic for Fibonacci

To solve DP iteratively, you must ==manually control the order== of computation:

1. Initialize a ==DP array== where `dp[i]` represents the $i^{th}$ value.
2. Define **Base Cases**: `dp = 0`, `dp = 1`.
3. **Loop** from the smallest subproblem to $N$: `for (int i = 2; i <= n; i++) { dp[i] = dp[i-1] + dp[i-2]; }`
4. The loop ensures that by the time you need `dp[i]`, the required ==smaller subproblems== are already solved.
