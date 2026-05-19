"""
Question
https://leetcode.com/problems/maximum-population-year/
"""

# Approach
"""
-> Line sweep (1D difference array + prefix sum)
"""

# TC: O(n + Y)  Y = year range (101)
# SC: O(Y)

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
