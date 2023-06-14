"""
Question
https://leetcode.com/problems/shortest-path-in-binary-matrix/
"""

#Approach
"""
--> BFS
--> TLE:
For BFS, you need to mark a node the first time you 'see' it instead of when you 'visit' it.
That's the reason we set grid[row+dx][col+dy] = 1 inside for loop instead of wait and set grid[row][col] = 1 outside for loop when we pop it.
The reason is, if C is neighboring to A and B, when we visit A, we will put C to the queue.
If we didn't mark C here, next time when we visit B, we will put C again to the queue. There could be quite a lot redundant search and lead to the TLE.
DFS is another story as we will visit C before B.
"""

#Code
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        N = len(grid)
        direct = [[0, 1], [0, -1], [1, 0], [-1, 0], [-1, 1], [-1, -1], [1, -1], [1, 1]]
        def isSafe(row, col):
            if(row < 0 or row >= N):
                return False
            if(col < 0 or col >= N):
                return False
            if(grid[row][col] == 1):
                return False
            return True
        
        if(grid[0][0] or grid[N-1][N-1]):
            return -1
        
        q = collections.deque()
        q.append((0, 0, 1))
        while(len(q) > 0):
            row, col, dist = q.popleft()
            if(row == N-1 and col == N-1):
                return dist
            
            #Marking the row, col to visited here instead of inside for loop
            #can lead to TLE. Check the approach section for more details 
            #grid[row][col] = 1

            for dx, dy in direct:
                if(isSafe(row+dx, col+dy)):
                    q.append((row+dx, col+dy, dist+1))
                    grid[row+dx][col+dy] = 1
        
        return -1
            
        
        