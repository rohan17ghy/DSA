"""
Question
https://leetcode.com/problems/edit-distance/description/
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
    def minDistance(self, word1: str, word2: str) -> int:
        N, M = len(word1), len(word2)
        INF = 10 ** 20
        dp = [[-1] * M for _ in range(N)]

        #Number of oprations to convert word1[i1:] to word2[i2:]
        def operate(i1, i2):
            if i2 == M:
                return N-i1
            if i1 == N:
                return M-i2
            
            if dp[i1][i2] != -1:
                return dp[i1][i2]

            ans = 0
            if word1[i1] == word2[i2]:
                return operate(i1+1, i2+1)
            else:
                #Insert
                ans1 = 1 + operate(i1, i2 + 1)
                #Delete
                ans2 = 1 + operate(i1+1, i2)
                #Replace
                ans3 = 1 + operate(i1 + 1, i2 + 1)                
                ans = min(ans1, ans2, ans3)

                dp[i1][i2] = ans
                return dp[i1][i2]
        
        return operate(0, 0)
