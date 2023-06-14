"""
Question
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
"""

#Approach
"""
--> We need to keep track of the best price that has occured in past
--> We need to find the maxProfit possible while traversing the array when we have the past best price

TC: O(N), SC:O(1)
"""

#Code
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        INF = 10 ** 20
        pastPrice = INF
        best = 0
        for price in prices:
            if price - pastPrice > best:
                best = price - pastPrice
            pastPrice = min(pastPrice, price)
        return best
