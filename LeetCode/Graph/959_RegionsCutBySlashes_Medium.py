"""
Question
https://leetcode.com/problems/regions-cut-by-slashes/description/
"""

#Approach
"""
NeetCode IO
https://www.youtube.com/watch?v=j8KrBYIxHK8

"""

#Code
class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        R = len(grid)
        C = len(grid[0])
        ngrid = [[False] * (C * 3) for _ in range(R * 3)]
        nR, nC = R * 3, C * 3 

        for i in range(R):
            for j in range(C):
                if grid[i][j] == '\\':
                    ngrid[i*3][j*3] = ngrid[i*3+1][j*3+1] = ngrid[i*3+2][j*3+2] = True
                elif grid[i][j] == '/':
                    ngrid[i*3+2][j*3] = ngrid[i*3+1][j*3+1] = ngrid[i*3][j*3+2] = True
        
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def dfs(x, y):
            ngrid[x][y] = True
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < nR and 0 <= ny < nR and not ngrid[nx][ny]:
                    dfs(nx, ny)
        
        ans = 0
        #print(ngrid)
        for i in range(nR):
            for j in range(nC):
                if not ngrid[i][j]:
                    ans += 1
                    dfs(i, j)
        return ans