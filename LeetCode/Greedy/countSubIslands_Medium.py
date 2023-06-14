"""
Question
https://leetcode.com/problems/count-sub-islands/
"""

#Approach
"""
--> DFS on the second grid to find if it is a sub island

TEMPLATE CODE FOR DFS
TC: O(mn) SC:O(mn)
"""

#Code
"""
Template code for dfs
"""
class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        r, c = len(grid1), len(grid1[0])
            
        def dfs(i, j):
            if(i < 0 or i >= r or j < 0 or j >= c or grid2[i][j] == 0): 
                return 1
            
            grid2[i][j] = 0
            res = grid1[i][j]
            for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                res &= dfs(i + di, j + dj)
            return res
        
        ans = 0
        for i in range(r):
            for j in range(c):
                if(grid2[i][j]):
                    ans += dfs(i, j)
        return ans
                
                