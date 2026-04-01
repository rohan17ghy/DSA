#### 1. Identification of a DP Problem

To apply DP, a problem must satisfy two main criteria:

- ==Overlapping Subproblems==: The same subproblems are computed multiple times.
- ==Optimal Substructure==: The optimal solution to a larger problem can be constructed from the ==optimal solutions of its smaller subproblems==.

**Common DP Problem Types:**

- ==Counting== problems (e.g., number of ways to reach a goal).
- ==Optimization== problems (Maximization or Minimization).

---

#### 2. DP vs. Divide and Conquer (D&C)

While both involve recursion, they differ in how they handle subproblems:

- **D&C (e.g., Merge Sort):** Divides problems into **independent** parts. There are ==no repeating subproblems==, so DP is unnecessary.
- **DP (e.g., Fibonacci):** Handles **dependent** subproblems that recur frequently.

---

#### 3. Approaches: Top-Down vs. Bottom-Up

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