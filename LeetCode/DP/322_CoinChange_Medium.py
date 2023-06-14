"""
Question
https://leetcode.com/problems/coin-change/
"""

#Approach
"""
--> One approach we can think of(similar to take/NotTake approach) is to take 1 or many coins at each index 
and then find the min coins recursively. But the time complexity will be subproblems * time/subproblem i.e
Length of coins * Amount * Amount(time/subproblem) = 12 * 10^4 * 10^4 ~ > 10 ^ 8 so will get TLE

--> So we need to figure out another subproblem to create a recursion. We can select any one coin amongst
the given choices and then recursively find out the minimum amongst them


TC: O(coins * amount), SC:O(amount)
"""

#Code
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        INF = 10 ** 20
        N = len(coins)
        has_cache = [False] * (amount + 1)
        cache = [None] * (amount + 1)  

        #Returns the min coins needed to get to amount.
        #Coins is not needed in params as infinite coins can be used
        def getMinCoins(amount):
            if amount == 0:
                return 0
            
            if has_cache[amount]:
                return cache[amount]

            best = INF
            for i in range(N):
                if amount - coins[i] >= 0:
                    best = min(best, 1 + getMinCoins(amount-coins[i]))
            
            has_cache[amount] = True
            cache[amount] = best
            return cache[amount]

        ans = getMinCoins(amount)
        if ans >= INF:
            return -1
        return ans
