"""
Question
https://leetcode.com/problems/shortest-common-supersequence/description/
"""

#Approach
"""
--> The main idea is to use LCS and find the remaining characters from both the strings which are not part of LCS
--> The LCS characters we need it once in supersequence and the remaining characters in both strings
--> The order should also be maintained

TC: O(N * M), SC: O(N * M)
"""

#Code
#Bottom Up Approach
class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:

        #Find LCS
        def longestCommonSubsequence(text1: str, text2: str) -> int:
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

            ans = []
            #Path reconstruction to find the actual LCS
            while i < N1 and j < N2:
                if text1[i] == text2[j]:
                    ans.append(text1[i])
                    i += 1
                    j += 1
                else:
                    if dp[i+1][j] >= dp[i][j+1]:
                        i += 1
                    else:
                        j += 1

            return ''.join(ans)

        #Creating the supersequence with the help of LCS
        lcs = longestCommonSubsequence(str1, str2)
        N = len(lcs)
        i, j = 0, 0
        ans = []
        for k in range(N):
            while i < len(str1) and str1[i] != lcs[k]:
                ans.append(str1[i])
                i += 1
            
            while j < len(str2) and str2[j] != lcs[k]:
                ans.append(str2[j])
                j += 1

            ans.append(lcs[k])
            i += 1
            j += 1
        
        while i < len(str1):
            ans.append(str1[i])
            i += 1
            
        while j < len(str2):
            ans.append(str2[j])
            j += 1

        return ''.join(ans)



