"""
Question
https://leetcode.com/problems/number-of-enclaves/
"""

#Approach
"""
--> The approach for this kind of problems is that we do the reverse of wat the question is asking
--> Doing the reverse makes the problem easier
--> This is reverse of flood fill implementation
--> Do a DFS for the 1's in the boundary and convert the 1's encountered to 0.
--> After the DFS, remaining 1's will be the answer

"""

#Code
class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        R = len(grid)
        C = len(grid[0])
        dir = [[0, 1], [1, 0], [-1, 0], [0, -1]]

        def dfs(row, col):
            grid[row][col] = 0
            for dx, dy in dir:
                nx = dx + row
                ny = dy + col
                if 0 <= nx < R and 0 <= ny < C and grid[nx][ny] == 1:
                    dfs(nx, ny)
        
        for i in range(R):
            for j in [0, C-1]:
                if grid[i][j] == 1:
                    dfs(i, j)
        
        for i in [0, R-1]:
            for j in range(1, C-1):
                if grid[i][j] == 1:
                    dfs(i, j)
        
        ans = 0
        for i in range(R):
            for j in range(C):
                if grid[i][j] == 1:
                    ans += 1
        return ans