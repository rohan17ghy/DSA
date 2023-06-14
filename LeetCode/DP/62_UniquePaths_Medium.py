"""
Question
https://leetcode.com/problems/unique-paths/description/
"""

#Approach
"""
--> Initial approach can be that of backtracking. But that approach leads to TLE as time complexity
is O(2^N)
--> This can be reduced to O(N) by caching the answer(DP)

TC: O(N), SC:O(N)
"""

#Code
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = {}

        def travel(row, col):
            if (row, col) in dp:
                return dp[(row, col)] 
            if row == m-1 and col == n-1:
                return 1

            paths = 0            
            if row + 1 < m:
                paths += travel(row + 1, col)
            if col + 1 < n:
                paths += travel(row, col + 1)

            #Commenting below line leads to only backtracking without caching,
            #It leads to O(2 ^ N) time complexity as there are 2 paths to explore from each 
            #square. Caching the path as it can be used in future reduces the time complexity
            #to O(N)
            dp[(row, col)] = paths
            return paths  

        return travel(0, 0)           




