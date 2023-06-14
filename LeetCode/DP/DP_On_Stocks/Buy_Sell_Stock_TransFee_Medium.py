"""
Question
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/
"""

#Approach
"""
#Approach: DP
--> Find a recurrence relation
--> Define wat the recursive function should return for us to get the answer

--> Ofcourse Space can be optimized further like any other DP problem with bottom up approach and space optimized 
approach

TC: O(N), SC:O(N)
"""

#Code
#Approach:
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        N = len(prices)
        dp = [[-1] * 2 for _ in range(N)]

        #Returns the max profit that can be achieved by prices[i:], with the state that the 
        #stock is either already bought or not "isBought"
        def findMaxProfit(i, isBought):
            if i >= N:
                return 0

            if dp[i][isBought] != -1:
                return dp[i][isBought] 

            ans = 0
            if isBought:
                ans = prices[i] - fee + findMaxProfit(i+1, not isBought)
            else:
                ans = -prices[i] + findMaxProfit(i+1, not isBought)
            ans = max(ans, findMaxProfit(i+1, isBought))
            dp[i][isBought] = ans
            return dp[i][isBought]
            

        return findMaxProfit(0, False)

