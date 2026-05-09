#formula #subsets #permutations #math 
# Formula

## 1. Total Number of Subsets of N Items

**Formula:** $2^N$

**Derivation:**
For each of the N items, you make an independent binary choice — either **include** it in the subset or **exclude** it. Since these choices are independent, by the multiplication principle the total number of ways is:

$$\underbrace{2 \times 2 \times \cdots \times 2}_{N \text{ times}} = 2^N$$

This also counts the empty subset (all excluded) and the full set (all included).

---

## 2. Permutations of N Items (Arranging All N)

**Formula:** $N!$

**Derivation:**
You are filling N distinct positions one by one. For the 1st position you have N choices, for the 2nd you have $N-1$ remaining choices, and so on down to 1 choice for the last position. By the multiplication principle:

$$nPn = n!$$

$$N \times (N-1) \times (N-2) \times \cdots \times 1 = N!$$

---

## 3. Partial Permutations — Arranging R Items from N (P(N, R))

**Formula:** $P(N, R) = \dfrac{N!}{(N-R)!}$

Standard permutation formula $nPr$

---

## 4. Total Permutations Across All Group Sizes (1 to N)

**Formula:** $\approx e \cdot N!$ 

>[!note] This formula is valid only when N is large

**Derivation:**
You sum $P(N, r)$ for every group size $r$ from 1 to N:

$$^NP_1 + ^NP_2 + ^NP_3 + \cdots + ^NP_N$$

$$= \frac{N!}{(N-1)!} + \frac{N!}{(N-2)!} + \frac{N!}{(N-3)!} + \cdots + \frac{N!}{0!}$$

$$= N! \left(\frac{1}{(N-1)!} + \frac{1}{(N-2)!} + \cdots + \frac{1}{0!}\right)$$

$$= N! \sum_{k=0}^{N-1} \frac{1}{k!} \approx e \cdot N!$$

The last step uses the fact that the Taylor series for $e$ is $\displaystyle\sum_{k=0}^{\infty} \frac{1}{k!}$, so the partial sum converges to $e$ as N grows large.
