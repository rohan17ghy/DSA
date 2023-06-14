"""
Question
https://practice.geeksforgeeks.org/problems/geek-jump/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=geek-jump
"""

#Approach
"""
--> Recursive/Memoization approach would give stack overflow error
--> Need to convert to tabulation to reduce the space used by recursive stack space

TC: O(N), SC: O(N)
"""

#Code
class Solution:
    def minimumEnergy(self, height, n):
        # Code here
        dp = [-1] * n
        for k in range(n):
            print(k)
            if k == 0:
                dp[0] = 0
                continue
            if k == 1:
                dp[1] = abs(height[1] - height[0])
                continue
            
            dp[k] = min(dp[k-1] + abs(height[k-1]-height[k]), dp[k-2] + abs(height[k-2]-height[k]))
        
        return dp[n-1]
