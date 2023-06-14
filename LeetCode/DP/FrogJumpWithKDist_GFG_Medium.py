"""
Question
https://practice.geeksforgeeks.org/problems/minimal-cost/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=minimal-cost
"""

#Approach
"""
--> Continuation from FrogJump_Easy_GFG.py
--> Instead of jumping from only i-1 and i-2, need to generalize to i-1, i-2,.......i-k 
--> Recursive/Memoization approach would give stack overflow error
--> Need to convert to tabulation to reduce the space used by recursive stack space

TC: O(Nk), SC: O(N)
"""

#Code
class Solution:
    def minimizeCost(self, height, n, k):
        dp = [-1] * n
        INF = 10 ** 20
        for i in range(n):
            if i == 0:
                dp[0] = 0
                continue
            
            best = INF
            for j in range(i-1, i-k-1, -1):
                if j < 0:
                    break
                best = min(best, dp[j] + abs(height[j] - height[i]))
            dp[i] = best
        return dp[n-1]
