"""
Question
https://leetcode.com/problems/minimum-moves-to-make-array-complementary/
"""

# Approach
"""
-> Line sweep on target sum T (difference array + prefix min)

Reference: solution walkthrough after pair cost bands (0 / 1 / 2 moves)
"""

# TC: O(n + limit)
# SC: O(limit)

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
