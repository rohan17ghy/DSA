"""
Question
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/
"""

#Approach
"""
#Approach: DP
--> Continuation of "Buy_Sell_Stock_4_Hard.py"
--> We need to extend that soln for a generic soln with k Transactions

TC: O(N * k), SC:O(N * k)
"""

#Code
#Approach:
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        N = len(prices)
        dp = [[[-1] * (2*k + 1) for _ in range(2)] for __ in range(N)]

        #Returns the maxProfit for prices[i:] when isBought=True/False with "transRem" transactions
        #remaining
        def findMaxProfit(i, isBought, transRem):
            if transRem <= 0:
                return 0
            
            if i >= N:
                return 0
            
            if dp[i][isBought][transRem] != -1:
                return dp[i][isBought][transRem]
            
            ans = 0
            if isBought:
                ans = max(ans, prices[i] + findMaxProfit(i+1, not isBought, transRem-1))
            else:
                ans = max(ans, -prices[i] + findMaxProfit(i+1, not isBought, transRem-1))
            ans = max(ans, findMaxProfit(i+1, isBought, transRem))

            dp[i][isBought][transRem] = ans
            return dp[i][isBought][transRem]
        
        return findMaxProfit(0, False, 2*k)

    