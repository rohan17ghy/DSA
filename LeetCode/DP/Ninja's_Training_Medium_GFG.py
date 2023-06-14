"""
Question
https://practice.geeksforgeeks.org/problems/geeks-training/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=geeks-training
"""

#Approach
"""
--> Simulation problem
--> Main idea is to find the recurrence relation

TC: O(N), SC: O(N)
"""

#Code
class Solution:
    def maximumPoints(self, points, n):
        # Code here
        dp = [[0 for i in range(3)] for j in range(n)]
        for i in range(n):
            if i == 0:
                for j in range(3):
                    dp[i][j] = points[i][j]
                continue
            
            for  j in range(3):
                dp[i][j] = points[i][j] + max(dp[i-1][j-2], dp[i-1][j-1])
        
        return max(dp[n-1])
