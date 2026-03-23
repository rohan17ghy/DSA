"""
Question
https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation/description
"""

#Approach
"""
Approach 1:
-> Formula based 
-> Transpose + swap columns = rotate by 90degree

Approach 2:
-> Now the problem starts if we don't know about this algo in interview.
-> In the case the algo, can be to use spiral traversal of matrix.
-> We can compare the original matrix spiral order with the target matrix spiral order, difference being the
spiral order of target matrix starts from all the four corners of the matrix. If anyone of the spiral 
order matches than it means that we can achieve the same matrix by rotation.

"""

from typing import List


class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        N = len(mat)
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        """
        This spiralOrder is not a normal spiral traversal that we do for a matrix. Because in that case
        the starting point is always (0, 0) which makes it easier. But here the spiralOrder can start from any one
        of the four corners of the matrix
        """
        def spiralOrder(matrix: List[List[int]], r, c, dirIndex) -> List[int]:
            M, N = len(matrix), len(matrix[0])
            
            res = []
            rowStart, rowEnd = 0, M-1
            colStart, colEnd = 0, N-1

            while rowStart <= rowEnd and colStart <= colEnd:
                dr, dc = directions[dirIndex]
                if(dc > 0):
                    for j in range(colStart, colEnd + 1):
                        r, c = r, j
                        res.append(matrix[r][c])                    
                    rowStart += 1
                elif(dr > 0):
                    for i in range(rowStart, rowEnd + 1):
                        r, c = i, c
                        res.append(matrix[r][c])
                    colEnd -= 1
                elif(dc < 0):
                    for j in range(colEnd, colStart - 1, -1):
                        r, c = r, j
                        res.append(matrix[r][j])
                    rowEnd -= 1
                else:
                    for i in range(rowEnd, rowStart - 1, -1):
                        r, c = i, c
                        res.append(matrix[i][c])
                    colStart += 1
                
                dirIndex = (dirIndex + 1) % 4
                dr, dc = directions[dirIndex]
                r, c = r + dr, c + dc
                
            return res
            
        #Spiral traversal of original matrix
        originalOrder = spiralOrder(mat, 0, 0, 0)

        #Call the spiralOrder function for all the four corners of the target matrix
        for i, j, index in [(0, 0, 0), (0, N-1, 1), (N-1, N-1, 2), (N-1, 0, 3)]:
            afterRotate = spiralOrder(target, i, j, index)
            isMatch = True
            for x in range(len(originalOrder)):
                if(originalOrder[x] != afterRotate[x]):
                    isMatch = False
                    break

            if(isMatch):
                return True
        
        return False






