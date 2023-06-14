"""
Question
https://leetcode.com/problems/surrounded-regions/description/
"""

#Approach
"""
--> The approach for this kind of problems is that we do the reverse of wat the question is asking
--> Doing the reverse makes the problem easier
--> This is reverse of flood fill implementation
--> The 'O's in the boundary of matrix will never be converted to X
--> The other cells surrounding 'O's in boundary will also not convert. So we need to travel the 'O's
starting from boundary
--> DFS of 'O's starting from boundary of the grid
"""

#Code
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        R = len(board)
        C = len(board[0])
        dir = [[-1, 0], [0, -1], [1, 0], [0, 1]]

        def dfs(row, col):
            if board[row][col] == 'X' or board[row][col] == '-':
                return
            
            board[row][col] = '-'
            for dx, dy in dir:
                next_row, next_col = row+dx, col+dy
                if 0 <= next_row < R and 0<= next_col < C and board[next_row][next_col] != '-':
                    dfs(next_row, next_col)
        
        for i in range(R):
            for j in [0, C-1]:
                if board[i][j] == 'O':
                    dfs(i, j)
        for i in [0, R-1]:
            for j in range(1, C-1):
                if board[i][j] == 'O':
                    dfs(i, j)

        print(board)
        for i in range(R):
            for j in range(C):
                if board[i][j] == '-':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'
