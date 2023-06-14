"""
Question
https://leetcode.com/problems/longest-palindromic-substring/description/
"""

#Approach
"""
#Approach1
--> One approach is that we reverse the string and then find the Longest Common Subsequence of both the strings
--> Refer striver video

#Approach 2 without LCS
--> The main thing is that we need to figure out wat should the recursive function return.
--> The subproblems we need to figure out for finding the answer

TC: O(N * N), SC: O(N * N)
"""

#Code
#Top Down Approach
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        N = len(s)
        dp = [[-1] * N for _ in range(N)]

        #Returns the length of the longest palindromic subsequence between s[l...r]
        def findLPS(l, r):
            if l > r:
                return 0
            if l == r:
                return 1

            if dp[l][r] != -1:
                return dp[l][r]

            if s[l] == s[r]:
                dp[l][r] = 2 + findLPS(l + 1, r - 1)
                return dp[l][r]
            
            dp[l][r] = max(findLPS(l, r-1), findLPS(l+1, r))
            return dp[l][r]
        
        return findLPS(0, N-1)

