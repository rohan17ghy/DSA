"""
Question
https://leetcode.com/problems/shortest-common-supersequence/description/
"""

#Approach
"""
--> The main idea is to figure out the subproblem and the recurrence
--> Write down wat the recursive fn should return 

TC: O(N * M), SC: O(N * M)
"""

#Code
#Top Down Approach
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        N, M = len(s), len(t)
        dp = [[-1] * M for _ in range(N)]

        #Returns the distinct subsequences of s[i1:] which equal to t[i2:]
        def findDistSubseq(i1, i2):
            if i2 == M:
                return 1
            if i1 == N:
                return 0

            if dp[i1][i2] != -1:
                return dp[i1][i2]

            ans = 0
            if s[i1] == t[i2]:
                ans += findDistSubseq(i1 + 1, i2 + 1)
            
            ans += findDistSubseq(i1+1, i2)
            dp[i1][i2] = ans

            return dp[i1][i2]
            
        
        return findDistSubseq(0, 0)