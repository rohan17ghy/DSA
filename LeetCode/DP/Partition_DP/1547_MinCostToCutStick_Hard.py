"""
Question
https://leetcode.com/problems/minimum-cost-to-cut-a-stick/description/
"""

#Approach
"""
PATTERN: PARTITION DP
--> This is a variance of partition DP.
--> The main idea is to perform all the cuts and find the min cost
--> One thing that was observed during coding that since n <= 10 ^ 6 so using n during the dp results in TLE
--> So instead of using n and doing cut between them we can use the cuts array only

--> TC: O(k^3) SC:O(k^2),  k --> len(cuts)

"""

#Code
#Top Down Approach
class Solution:
    def minCost(self, N: int, cuts: List[int]) -> int:
        cuts.append(0)
        cuts.append(N)
        cuts.sort()
        N = len(cuts)
        INF = 10 ** 20
        dp = [[-1] * N for _ in range(N)]
        
        #Cuts in range i...j
        #Need to do one cut excluding i and j and recursively move forward
        #Returns the min cost to perform the cuts between i...j (excluding i and j as they are already cut)
        def findMinCosts(i, j):
            if i + 1 >= j:
                return 0

            if dp[i][j] != -1:
                return dp[i][j]

            cost = INF
            for k in range(i+1, j):
                cost = min(cost, cuts[j]-cuts[i]+findMinCosts(i, k)+findMinCosts(k,j))
            dp[i][j] = cost
            return dp[i][j]
        
        return findMinCosts(0, N-1)