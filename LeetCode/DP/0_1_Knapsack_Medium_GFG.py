"""
Question
https://practice.geeksforgeeks.org/problems/0-1-knapsack-problem0945/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=0-1-knapsack-problem0945
"""

#Approach
"""
--> Approach is easy but there can be silly mistakes while creating the recurrence 
--> First try to understand what the recursive function returns. In this case findMaxVal() returns the maxVal
from index......N when knapsack is having currWeight
--> One doubt that can occur is why only currWeight is enough to capture the state, why don't we need to capture
the elements that is used to create the current knapsack whose weight is currWeght ???
--> The ans to that is the recursive function returns the max from index.....N and it will consider all the max 
combinations possible from index....N so we don't need to worry about the elements from 0....index-1 only the weight
matters

TC: O(N * W), SC:O(N * W)
"""

#Code
class Solution:
    
    #Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self,W, wt, val, n):
        # code here
        dp = [[-1] * (W+1) for _ in range(n)]
        
        #Returns the maxVal from index......N when knapsack is having currWeight
        #No need to keep track of which elements are selected
        def findMaxVal(index, currWeight):
            if index == n:
                return 0
            
            if dp[index][currWeight] != -1:
                return dp[index][currWeight]
            
            take = 0
            if currWeight + wt[index] <= W:
                take = val[index] + findMaxVal(index + 1, currWeight + wt[index])
            notTake = findMaxVal(index + 1, currWeight)
            
            dp[index][currWeight] = max(take, notTake)
            return dp[index][currWeight]
        
        return findMaxVal(0, 0)
