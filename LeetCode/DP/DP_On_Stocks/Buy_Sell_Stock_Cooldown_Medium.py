"""
Question
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/
"""

#Approach
"""
#Approach: DP
--> Find a recurrence relation
--> Define wat the recursive function should return for us to get the answer

TC: O(N), SC:O(N)
"""

#Code
#Approach:
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        N = len(prices)
        dp = [[-1] * 2 for _ in range(N)]

        #Returns the maxProfit that can be achieved by prices[i:] if the stock can be either
        #bought or sold depending on "isBoought"
        def findMaxProfit(i, isBought):
            if i >= N:
                return 0

            if dp[i][isBought] != -1:
                return dp[i][isBought]

            ans = 0
            if isBought:
                ans = max(ans, prices[i] + findMaxProfit(i+2, not isBought))
            else:
                ans = max(ans, -prices[i] + findMaxProfit(i+1, not isBought))
            ans = max(ans, findMaxProfit(i+1, isBought))
            dp[i][isBought] = ans
            return dp[i][isBought]
        return findMaxProfit(0, False)

    