"""
Question
https://leetcode.com/problems/minimum-path-sum/description/
"""

#Approach
"""
--> Initial approach can be that of backtracking.
is O(2^N)
--> This can be reduced to O(N) by caching the answer(DP)

TC: O(NxM), SC:O(NxM)
"""

#Code

#Recursive soln with memoization
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        R = len(grid)
        C = len(grid[0])

        INF = 10 ** 20
        dp = {}
        def travel(row, col):
            if row == R-1 and col == C-1:
                return grid[row][col] 
            if (row, col) in dp:
                return dp[(row, col)]

            downPathSum, rightPathSum = INF, INF 
            if row + 1 < R:
                downPathSum = travel(row + 1, col)
            if col + 1 < C:
                rightPathSum = travel(row, col + 1)

            dp[(row, col)] = min(downPathSum, rightPathSum) + grid[row][col]
            return dp[(row, col)] 
        
        ans = travel(0, 0)                 
        return ans



#Tabulation soln
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        R = len(grid)
        C = len(grid[0])
        INF = 10 ** 20
        dp = [[INF for j in range (C)] for i in range(R)] 

        for i in range(R):
            for j in range(C):
                if i == 0 and j == 0:
                    dp[i][j] = grid[i][j]
                elif i == 0:
                    dp[i][j] = grid[i][j] + dp[i][j-1]
                elif j == 0:
                    dp[i][j] = grid[i][j] + dp[i-1][j]
                else:
                    dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])

        return dp[R-1][C-1]    

#Space Optimization soln
#Space optimization soln can be deduced from the above soln        
           




