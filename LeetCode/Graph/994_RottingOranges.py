"""
Question
https://leetcode.com/problems/rotting-oranges/
"""

#Approach
"""
--> Do a BFS with all the rotten oranges at the same time
--> Keep track of each level of BFS, which tells about the minutes

"""

#Code
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        q = collections.deque([])
        fresh_cnt = 0

        #Appending rotten oranges to the queue
        #Finding the number of fresh oranges
        for r in range(m):
            for c in range(n):
                if(grid[r][c] == 2):
                    q.append((r, c))
                elif(grid[r][c] == 1):
                    fresh_cnt += 1
        
        dir = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        def isFresh(row, col):
            if(row < 0 or col < 0 or row >= m or col >= n):
                return False
            if(grid[row][col] == 1):
                return True
            return False

        count = len(q)
        minute = 0
        #BFS
        while q and fresh_cnt > 0:
            next_cnt = 0
            while count > 0:
                r, c = q.popleft()
                for dx, dy in dir:
                    if(isFresh(r+dx, c+dy)):
                        q.append((r+dx, c+dy))
                        grid[r+dx][c+dy] = 2
                        next_cnt += 1
                        fresh_cnt -= 1
                count -= 1
            minute += 1
            count = next_cnt
        
        if fresh_cnt > 0:
            return -1
        return minute