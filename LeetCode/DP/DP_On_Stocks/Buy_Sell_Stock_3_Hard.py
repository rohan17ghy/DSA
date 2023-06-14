"""
Question
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/description/
"""

#Approach
"""
#Approach: DP
--> Find a recurrence relation
--> Define wat the recursive function should return for us to get the answer

--> More intuitive and scalable code is written by "Programming Live with Larry". Check that out
https://www.youtube.com/watch?v=KY_RBRXuXU4

--> Ofcourse Space be optimized further like any other DP problem with bottom up approach and space optimized 
approcah

TC: O(N), SC:O(N)
"""

#Code
#Approach:
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        N = len(prices)
        dp = [[[-1] * 5 for _ in range(2)] for __ in range(N)]

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
        
        return findMaxProfit(0, False, 4)

    