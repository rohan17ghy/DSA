"""
Question
https://leetcode.com/problems/making-a-large-island/description/
"""

#Approach
"""
falls under a pattern of coloring graph

Check out the votrubac solution for explanation
https://leetcode.com/problems/making-a-large-island/solutions/127015/paint-the-picture/

"""

#Code
class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        color = 2
        colorCounter = collections.Counter()
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        def bfs(r, c):
            dq = collections.deque([])
            dq.append((r, c))
            nonlocal color
            count = 0

            while len(dq) > 0:
                x, y = dq.popleft()
                if grid[x][y] != 1:
                    continue
                grid[x][y] = color
                count += 1
                #print(x, y, count, color)
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < R and 0 <= ny < C and grid[nx][ny] == 1:
                        dq.append((nx, ny))
            
            colorCounter[color] = count
            color += 1
        
        def calcAfterOperation(x, y):
            colorSet = set()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < R and 0 <= ny < C:
                    colorSet.add(grid[nx][ny])
            
            ans = 1
            for color in colorSet:
                ans += colorCounter[color]

            return ans


        for i in range(R):
            for j in range(C):
                if grid[i][j] == 1:
                    bfs(i, j)
        
        #print(grid)
        #print(colorCounter)
        ans = 0
        for i in range(R):
            for j in range(C):
                if grid[i][j] == 0:
                    ans = max(ans, calcAfterOperation(i, j))

        return ans if ans > 0 else R * C



                    
        