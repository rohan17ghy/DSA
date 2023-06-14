"""
Question
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/
"""

#Approach
"""
#Approach 1: DP
--> Find a recurrence relation

TC: O(N), SC:O(1)

#Approach 2: Greedy
--> Since we can buy and sell on same day, so we keep on adding the profits that we get immediately in 
greedy fashion
--> Reference: Larry Video --> https://www.youtube.com/watch?v=UpR3XN4MDUo


TC: O(N), SC:O(1)
"""

#Code
#Approach 1: DP
#Bottom Up Approach
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        N = len(prices)
        dp = [[0] * 2 for _ in range(N+1)]

        prevJ, prev1MinusJ = 0, 0 
        ans = 0
        for i in range(N, -1, -1):
            for j in range(2):                
                profit = 0
                if j:
                    profit = prices[i] + prev1MinusJ
                else:
                    profit = -prices[i] + prev1MinusJ
                profit = max(profit, prevJ)
                ans = profit
        
        return dp[0][0]


#Code
#Approach 2: Greedy
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        N = len(prices)
        max_profit = 0
        for i in range(N-1):
            potential_profit = prices[i+1]-prices[i]
            max_profit += max(potential_profit, 0)
        return max_profit