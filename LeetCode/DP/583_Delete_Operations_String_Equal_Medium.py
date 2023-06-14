"""
Question
https://leetcode.com/problems/delete-operation-for-two-strings/description/
"""

#Approach
"""
#Approach1: Longest Palindromic subsequence
--> Answer will be N1 + N2 - 2 * len(longest palindromic subsequence)

#Approach 2
--> The main thing is that we need to figure out wat should the recursive function return.
--> The subproblems we need to figure out for finding the answer

TC: O(N * N), SC: O(N * N)
"""

#Code
#Top Down Approach
class Solution:

    """
    The answer is basically the remaining string after removing Longest Common
    Subsequence
    """
    def minDistance(self, text1: str, text2: str) -> int:
        N1, N2 = len(text1), len(text2)
        
        dp = [[-1] * (N2 + 1) for _ in range(N1 + 1)]
        for i in range(N1, -1, -1):
            for j in range(N2, -1, -1):
                if i >= N1 or j >= N2:
                    dp[i][j] = 0                
                elif text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])
        
        return N1 + N2 - 2 * dp[0][0]

