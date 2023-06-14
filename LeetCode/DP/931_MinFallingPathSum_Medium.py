"""
Question
https://leetcode.com/problems/minimum-falling-path-sum/description/
"""

#Approach
"""
--> Initial approach can be that of backtracking.
is O(3^N)
--> This can be reduced to O(N) by caching the answer(DP)

TC: O(N), SC:O(N)
"""

#Code
#Tabulation soln
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        N = len(matrix)
        dp = [[100*N] * N for _ in range(N)]
        directions = [[1, 0], [1, -1], [1, 1]]

        for i in range(N-1, -1, -1):
            for j in range(N):
                if i == N-1:
                    dp[i][j] = matrix[i][j]
                    continue

                for dx, dy in directions:
                    if  0 <= i + dx < N and 0 <= j + dy < N:
                        dp[i][j] = min(dp[i][j], dp[i+dx][j+dy] + matrix[i][j])

        return min(dp[0])
        

           




