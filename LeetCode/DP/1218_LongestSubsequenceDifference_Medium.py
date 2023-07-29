"""
Question
https://leetcode.com/problems/longest-increasing-subsequence/description/
"""

#Approach
"""
--> Bottom Up Approach for this problem is easier and comes more naturally
--> The main idea for this problem is to use a lookup


TC: O(N), SC:O(N)
"""

#Code
#Bottom Up Approach
class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = collections.Counter()

        #subproblem is lookup[x] is the longest subsequence ending with x
        for x in arr:
            if x-difference in dp:
                dp[x] = max(dp[x], 1 + dp[x-difference])
            else:
                dp[x] = 1
        return max(dp.values()) if len(dp) > 0 else 1       
