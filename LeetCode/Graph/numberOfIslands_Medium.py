"""
Question
https://leetcode.com/problems/number-of-islands/
"""

#Approach
"""
--> Simple DFS
--> We can use the grid itself to keep track of visited nodes
--> TEMPLATE FOR DFS QUESTIONS. VERY CONCISE DFS WITHOUT VISITED ARRAY 

Reference: https://leetcode.com/problems/number-of-islands/discuss/56340/Python-Simple-DFS-Solution
"""

#Code
def numIslands(self, grid):
    if not grid:
        return 0
        
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                self.dfs(grid, i, j)
                count += 1
    return count

def dfs(self, grid, i, j):
    if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j] != '1':
        return
    grid[i][j] = '#'
    self.dfs(grid, i+1, j)
    self.dfs(grid, i-1, j)
    self.dfs(grid, i, j+1)
    self.dfs(grid, i, j-1)
