"""
Question
https://leetcode.com/problems/unique-paths-ii/description/
"""

#Approach
"""
--> Initial approach can be that of backtracking. But that approach leads to TLE as time complexity
is O(2^N)
--> This can be reduced to O(N) by caching the answer(DP)

TC: O(N), SC:O(N)
"""

#Code
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        dp = {}
        R = len(obstacleGrid)
        C = len(obstacleGrid[0])

        def travel(row, col):
            if obstacleGrid[row][col] == 1:
                return 0
            if row == R-1 and col == C-1:
                return 1
            if (row, col) in dp:
                return dp[(row, col)]

            paths = 0
            if row + 1 < R:
                paths += travel(row + 1, col)
            if col + 1 < C:
                paths += travel(row, col + 1)

            dp[(row, col)] = paths
            return paths

        return travel(0, 0)            




