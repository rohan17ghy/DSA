"""
Question
https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome/description/
"""

#Approach
"""
#Approach1: Longest Palindromic subsequence
--> Answer will be N - len(longest palindromic subsequence)

#Approach 2
--> The main thing is that we need to figure out wat should the recursive function return.
--> The subproblems we need to figure out for finding the answer

TC: O(N * N), SC: O(N * N)
"""

#Code
#Top Down Approach
class Solution:
    def minInsertions(self, s: str) -> int:
        N = len(s)
        dp = [[-1] * N for _ in range(N)]

        #Returns the min Insertions needed for s[l...r]
        def findMin(l, r):
            if l == r:
                return 0
            if l > r:
                return 0

            if dp[l][r] != -1:
                return dp[l][r]

            if s[l] == s[r]:
                dp[l][r] = findMin(l+1, r-1)
                return dp[l][r]
            else:
                dp[l][r] = min(1 + findMin(l, r-1), 1 + findMin(l+1, r))
                return dp[l][r]
        
        return findMin(0, N-1)

