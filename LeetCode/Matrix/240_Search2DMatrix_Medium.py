"""
Question
https://leetcode.com/problems/search-a-2d-matrix-ii/description/
"""

#Approach
"""
#Approach 1: Binary Search
--> Refer https://leetcode.com/problems/search-a-2d-matrix-ii/submissions/935738946/

TC: O(RLogC), SC: O(1)

#Approach 2: Search from i = 0, j = C-1
--> The main idea is to search from i, j = 0, C-1 OR i, j = R-1, 0 Because this would make the conditions easier

TC: O(max(R, C))
"""

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        R, C = len(matrix), len(matrix[0])        

        #Main idea is to start from either i, j = 0, C-1 OR i, j = R-1, 0
        #Because this would make the conditions easier
        #Easier because if matrix[i][j] > target we go one direcction and if matrix[i][j] < target
        #we go another direction 
        i, j = 0, C-1
        while i < R and j >= 0:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                i += 1
            else:
                j -= 1
        return False



