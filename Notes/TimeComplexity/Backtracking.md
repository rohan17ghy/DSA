# 🌟 Golden Rule for Backtracking Time Complexity

## 🧠 Core Idea
**Time Complexity = (number of choices per step) ^ (number of steps)**

---

## 🔍 How to Analyze Any Backtracking Problem

Ask these 2 questions:

### 1️⃣ How many choices do I have at each step?
- 2 choices → (e.g., include / exclude, right / down)
- k choices → (e.g., pick from k options)

### 2️⃣ What is the maximum depth of recursion?
- Number of steps taken
- Number of elements
- Length of decision sequence

---

## 🧮 Formula

```
Time Complexity = (choices) ^ (depth)
```

---

## ✅ Backtracking Problem Examples

### 🔹 Grid Path Problem
- **Problem:** Find all paths from top-left to bottom-right in an m×n grid, moving only right or down.  
- **Why Backtracking:** At each cell, we have a choice to move right or down → we explore all possible paths recursively.  
- **Time Complexity:**  
  - Choices per step = 2 (right or down)  
  - Depth = total number of moves = m + n − 2  
```
Time = 2^(m + n - 2) ≈ O(2^(m + n))
```

---

### 🔹 Subsets Problem
- **Problem:** Generate all subsets of a set of n elements.  
- **Why Backtracking:** For each element, we can choose to include it or not → recursively explore all combinations.  
- **Time Complexity:**  
  - Choices per step = 2 (include or exclude)  
  - Depth = n elements  
```
Time = O(2^n)
```

---

### 🔹 Permutations Problem
- **Problem:** Generate all permutations of n elements.  
- **Why Backtracking:** Each position in the permutation can be filled by any remaining element → recursively explore all orderings.  
- **Time Complexity:**  
  - First position → n choices, next → n-1, … → total n! combinations  
```
Time = O(n!)
```

---

### 🔹 k-ary Decision Problem
- **Problem:** Make a sequence of n decisions, each with k options. Example: coloring n positions with k colors.  
- **Why Backtracking:** At each decision point, we explore all k options → recursively explore all sequences.  
- **Time Complexity:**  
  - Choices per step = k  
  - Depth = n  
```
Time = O(k^n)
```

---

## ⚠️ Important Notes

- Time complexity here is the **worst-case upper bound**.  
- Backtracking explores all branches in the recursion tree.  
- Pruning or constraints may reduce actual runtime, but the upper bound stays.

---

## 🎯 Quick Interview Trick

Think:

- Backtracking = Recursion Tree 🌳  
- Time = **Branching Factor ^ Depth**  

---

## 🧾 Summary Table

| Problem Type | What the Problem Is | Choices | Depth | Complexity |
| ------------ | ----------------- | ------- | ----- | ---------- |
| Grid Paths   | All paths in m×n grid moving right/down | 2 | m+n | O(2^(m+n)) |
| Subsets      | All subsets of n elements | 2 | n | O(2^n) |
| Permutations | All orderings of n elements | n | n | O(n!) |
| k choices    | Sequence of n decisions, each with k options | k | n | O(k^n) |