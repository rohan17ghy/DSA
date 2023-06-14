"""
Question
https://leetcode.com/problems/number-of-closed-islands/
"""

#Approach:
"""
--> Use DFS to traverse through each island
--> DFS should return true or false depending on whether the island is closed
--> Don't need visited array, can change the grid to keep track of visited elements

TC: O(rows * cols) SC: O(rows * cols) --> space will be taken by recursive stack memory
"""

#Code
class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        r, c = len(grid), len(grid[0])
        def dfs(row, col):
            if(row < 0 or row >= r or col < 0 or col >= c):
                return False
            if(grid[row][col] == 1 or grid[row][col] == '#'):
                return True
            
            grid[row][col] = '#'
            """ IMPORTANT Note: 
        WHY I CANNOT USE `return dfs(g, i+1, j) && dfs(g, i, j+1) && dfs(g, i-1, j) && dfs(g, i, j-1);`???
        BECAUSE IF ANY OF THE FIRST DFS() RETURNS FALSE, FOLLOWING ONES WILL NOT EXECUTE!!! THEN WE DON'T
        HAVE THE CHANCE TO MARK THOSE 0s TO 1s!!!
        """
            down = dfs(row+1, col)
            up = dfs(row-1, col)
            right = dfs(row, col+1) 
            left = dfs(row, col-1)
            
            return left and right and up and down
        
        ans = 0
        for i in range(r):
            for j in range(c):
                if(grid[i][j] == 0 and dfs(i, j)):
                    ans += 1
                    print((i, j))
        return ans
        