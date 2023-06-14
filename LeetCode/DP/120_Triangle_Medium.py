"""
Question
https://leetcode.com/problems/minimum-path-sum/description/
"""

#Approach
"""
--> Initial approach can be that of backtracking.
is O(2^N)
--> This can be reduced to O(N) by caching the answer(DP)

TC: O(N), SC:O(N)
"""

#Code

#Recursive soln with memoization
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        R = len(triangle)
        dp = {}

        def travel(i, j):
            if i == R-1:
                return triangle[i][j]
            
            if (i, j) in dp:
                return dp[(i, j)]

            dp[(i, j)] = triangle[i][j] + min(travel(i+1, j), travel(i+1, j+1))

            return dp[(i, j)]

        return travel(0, 0)  



#Tabulation soln
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        R = len(triangle)
        dp = {}
        
        for i in range(R-1, -1, -1):
            C = len(triangle[i])
            for j in range(C):
                if i == R-1:
                    dp[(i, j)] = triangle[i][j]
                else:
                    dp[(i, j)] = triangle[i][j] + min(dp[(i+1, j)], dp[(i+1, j+1)]) 
        return dp[(0, 0)] 

#Space Optimization soln
#Space optimization soln can be deduced from the above soln
           




