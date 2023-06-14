"""
Question
https://practice.geeksforgeeks.org/problems/subset-sum-problem-1611555638/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=subset-sum-problem-1611555638
"""

#Approach
"""
--> Initial approach can be that of backtracking.
is O(2^(N*sum))
--> This can be reduced to O(N*sum) by caching the answer(DP)

TC: O(N*sum), SC:O(N*sum)

"""

#Code
class Solution:
    def isSubsetSum (self, N, arr, sum):
        # code here 
        has_cache = [[None] * (sum+1) for _ in range(N)]
        dp = [[False] * (sum+1) for _ in range(N)]
        
        def isSubset(i, remSum):
            if remSum < 0:
                return False
            if i >= N:
                return False
            if remSum - arr[i] == 0:
                return True
            if has_cache[i][remSum]:
                return dp[i][remSum]
            
            has_cache[i][remSum] = True
            dp[i][remSum] = isSubset(i+1, remSum-arr[i]) or isSubset(i+1, remSum)
            return dp[i][remSum]
            
        return isSubset(0, sum)