"""
Question
https://leetcode.com/problems/longest-increasing-subsequence/description/
"""

#Approach
"""
--> The main idea is to find the subproblem or the recurrence relation
--> Wat is the subproblem we should consider? Wat should the recursive function return
--> We can consider that the function "Returns the LIS length for nums[:i] which ends with nums[i]".
--> There can be other ways to write it but this is the cleanest


TC: O(N ^ 2), SC:O(N ^ 2)
"""

#Code
#Top Down Approach
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        N = len(nums)
        dp = [0] * N

        #Returns the LIS length for nums[:i] which ends with nums[i]
        def lenOfLIS(i):
            if i == 0:
                return 1
            
            if dp[i] != 0:
                return dp[i] 

            ans = 1
            for j in range(i):
                prevLIS = lenOfLIS(j)
                if nums[i] > nums[j]:
                    ans = max(ans, prevLIS + 1)
            dp[i] = ans  
            return dp[i]
        
        maxLen = 0
        for i in range(N):
            maxLen = max(maxLen, lenOfLIS(i))
            
        return maxLen

        
