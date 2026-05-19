#lineSweep #template #pattern 

![[Ex-Line_Sweep_general_theory| 1000]]


# Complete Code

```python title:maximumPopulation.py
class Solution:

    def maximumPopulation(self, logs: List[List[int]]) -> int:

        years = [0] * 101
        INF = 10 ** 20

        for _, [birth, death] in enumerate(logs):
            years[birth - 1950] += 1
            years[death - 1950] -= 1

        current = 0
        best = -INF
        bestYear = -1
        for i in range(len(years)):
            current += years[i]
            if current > best:
                best = current
                bestYear = i
        return 1950 + bestYear
```

```python title:minMovesToMakeComplementary.py
class Solution:

    def minMoves(self, nums: List[int], limit: int) -> int:

        diff = [0] * (2 * limit + 2)
        n = len(nums)

        for i in range(n // 2):
            x, y = nums[i], nums[n - 1 - i]
            if x > y:
                x, y = y, x
            diff[2] += 2
            diff[x + 1] -= 2
            diff[x + 1] += 1
            diff[x + y] -= 1
            diff[x + y + 1] += 1
            diff[y + limit + 1] -= 1
            diff[y + limit + 1] += 2

        current = 0
        best = 10 ** 20
        for total in diff[2:]:
            current += total
            best = min(best, current)
        return best
```
