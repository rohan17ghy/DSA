"""
Question
https://leetcode.com/problems/longest-common-subsequence/description/
"""

#Approach
"""
--> Wat is the subproblem we should consider? --> LCS of "abc" and "adb" is 1 + LCS of "abc" and "adb"
                                                          ^         ^                    ^         ^
--> Wat is the input that will give the same output? We can take a function that returns
the LCS for the strings i1...N1 and i2....N2 and the params for that function is i1 and i2 

TC: O(N1 * N2), SC:O(N1 * N2)
"""

#Code
#Top Down Approach
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        N1, N2 = len(text1), len(text2)
        
        dp = [[-1] * N2 for _ in range(N1)]
        #Return the longestCommonSubsequence for the strings i1...N1 and i2....N2
        def findLongest(i1, i2):
            if i1 >= N1 or i2 >= N2:
                return 0
            
            if dp[i1][i2] != -1:
                return dp[i1][i2]
                        
            if text1[i1] == text2[i2]:
                return 1 + findLongest(i1 + 1, i2 + 1)

            dp[i1][i2] = max(findLongest(i1 + 1, i2), findLongest(i1, i2 + 1))
            return dp[i1][i2]
        
        return findLongest(0, 0)
        
