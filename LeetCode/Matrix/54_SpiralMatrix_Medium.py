"""
Question
https://leetcode.com/problems/spiral-matrix/description/
"""

#Approach
"""
Approach:
-> Take boundary limits for row and columns in the form of rowStart, rowEnd, colStart, colEnd
-> After each row or col traversal we need to adjust these boundaries and redo.
-> Also need to handle the directions.

"""

#Comments
"""
The main difficulty I faced is not the intuition or approach, but rather the implementation.
This problem comes under the category of problems which is difficult to code.
"""





from ast import List
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        M, N = len(matrix), len(matrix[0])
        rowStart, colStart, rowEnd, colEnd = 0, 0, M-1, N-1
        
        ans = []

        while rowStart <= rowEnd and colStart <= colEnd:
            for j in range(colStart, colEnd+1):
                ans.append(matrix[rowStart][j])
            rowStart += 1

            for i in range(rowStart, rowEnd+1):
                ans.append(matrix[i][colEnd])
            colEnd -= 1

            if rowStart <= rowEnd and colStart <= colEnd:
                for j in range(colEnd, colStart-1, -1):
                    ans.append(matrix[rowEnd][j])
                rowEnd -= 1

            if rowStart <= rowEnd and colStart <= colEnd:
                for i in range(rowEnd, rowStart-1, -1):
                    ans.append(matrix[i][colStart])
                colStart += 1
            #print(rowStart, " ", rowEnd, " ", colStart, " ", colEnd)
            #print(ans)
        return ans