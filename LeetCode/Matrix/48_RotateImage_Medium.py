"""
Question
https://leetcode.com/problems/rotate-image/description/
"""

#Approach
"""
--> Formula based 
--> Transpose + swap columns = rotate by 90degree  
--> Reference: https://leetcode.com/problems/rotate-image/solutions/1449737/rotation-90-code-180-270-360-explanation-inplace-o-1-space/

"""

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        N = len(matrix)
        #Transpose
        for i in range(N):
            for j in range(i):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
        
        #Swapping columns
        i, j = 0, N-1
        while i < j:
            for k in range(N):
                temp = matrix[k][i]
                matrix[k][i] = matrix[k][j]
                matrix[k][j] = temp
            i += 1
            j -= 1



