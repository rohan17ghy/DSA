"""
Question
https://practice.geeksforgeeks.org/problems/rod-cutting0840/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=rod-cutting0840
"""

#Approach
"""
--> Similar to 322_CoinChange_Medium.py problem

TC: O(N * N), SC:O(N)
"""

#Code
#Top Down Approach
class Solution:
    def cutRod(self, price, n):
        #code here
        dp = [-1] * (n+1)
        try:
            def findMaxVal(rodLen):
                if rodLen == 0:
                    return 0
                
                if dp[rodLen] != -1:
                    return dp[rodLen]
                
                best = 0
                for i in range(n):
                    if rodLen - (i+1) >= 0:
                        best = max(best, price[i] + findMaxVal(rodLen-(i+1)))
                dp[rodLen] = best
                return dp[rodLen]
            
            return findMaxVal(n)
        except Exception as ex:
            print(ex)
        
