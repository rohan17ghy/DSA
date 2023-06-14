"""
Question
https://practice.geeksforgeeks.org/problems/knapsack-with-duplicate-items4201/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=knapsack-with-duplicate-items
"""

#Approach
"""
--> Similar to 0-1 knapsack problem

TC: O(amount * N), SC:O(amount)
"""

#Code
#Top Down Approach
class Solution:
    def knapSack(self, N, W, val, wt):
        # code here
        dp = [-1] * (W+1)
        try:
            def findMaxProfit(weight):
                if weight == 0:
                    return 0
                
                
                if dp[weight] != -1:
                    return dp[weight]
                
                best = 0
                for i in range(N):
                    if weight - wt[i] >= 0:
                        best = max(best, val[i] + findMaxProfit(weight-wt[i]))
                        
                dp[weight] = best
                return dp[weight]
        
            return findMaxProfit(W)
        except Exception as e:
            print(e)


# Bottom Up Approach 
class Solution:
    def knapSack(self, N, W, val, wt):
        # code here
        dp = [-1] * (W+1)
        dp[0] = 0
        for i in range(W+1):
            best = 0
            for j in range(N):
                if i - wt[j] >= 0:
                    best = max(best, val[j] + dp[i-wt[j]])
            
            dp[i] = best
        
        return dp[W]
        
