"""
Question
https://leetcode.com/problems/profitable-schemes/
"""

#Approach
"""
--> Approach is similar to take/notTake pattern.
--> This is a good problem because of the optimization used to reduce Time Complexity.
    --> Normally and inutitively we would have the current profit in the parameters but that parameter can range
    from 0 ~ 100,000 which would make the algo slow. We can optimize this by not considering the current profit
    but instead consider the minProfitNeeded because that ranges from 0 ~ 100 which improves the Time complexity

L --> Length of group/profit 
TC: O(L * N * minProfit), SC: O(L * N * minProfit)
"""

#Code
class Solution:
    def profitableSchemes(self, N: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        mod = 10 ** 9 + 7
        L = len(group)
        dp = [[[-1] * (minProfit+1) for _ in range(N+1)] for __ in range(L+1)]
        #Returns the all schemes for group[i:] and profit[i:] with "members" members remaining
        #and with "minProfitNeeded" minimum profit
        #
        #TRICK TO OPTIMIZE TIME COMPLEXITY: We can't use current profit in the parameters because
        #it would be 100 * 100 = 100,000 which would be quite slow exceeding the total TC by 10 ^ 8. 
        #So instead we use minProfitNeeded since that would reduce 100,000 to 100
        def findAllSchemes(i, members, minProfitNeeded):
            if members < 0:
                return 0
            if i == L:
                if minProfitNeeded <= 0:
                    return 1
                return 0
            
            if minProfitNeeded < 0:
                minProfitNeeded = 0

            if dp[i][members][minProfitNeeded] != -1:
                return dp[i][members][minProfitNeeded]

            best = 0
            take = findAllSchemes(i + 1, members-group[i], minProfitNeeded-profit[i])
            notTake = findAllSchemes(i + 1, members, minProfitNeeded)
            best = (take + notTake) % mod

            dp[i][members][minProfitNeeded] = best
            return dp[i][members][minProfitNeeded]
            
        
        return findAllSchemes(0, N, minProfit)




