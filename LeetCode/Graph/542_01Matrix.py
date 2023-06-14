"""
Question
https://leetcode.com/problems/01-matrix/description/
"""

#Approach
"""
--> BFS starting with all zeros at the same time
"""

#Code
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        R = len(mat)
        C = len(mat[0])
        INF = 10 ** 20
        dir = [[0, 1], [1, 0], [-1, 0], [0, -1]]

        res = [[INF for j in range(C)] for i in range(R)]
        q = collections.deque([])
        for i in range(R):
            for j in range(C):
                if mat[i][j] == 0:
                    q.append((i, j))
                    res[i][j] = 0

        while q:
            row, col = q.popleft()
            for dx, dy in dir:
                new_row = row + dx
                new_col = col + dy

                if 0 <= new_row < R and 0 <= new_col < C and res[new_row][new_col] == INF:
                    #Grid cells which are 1 will reach here
                    res[new_row][new_col] = res[row][col] + 1
                    q.append((new_row, new_col))
        return res