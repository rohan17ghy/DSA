"""
Question
https://leetcode.com/problems/minimum-cost-for-tickets/description/
"""

#Approach
"""
--> The main idea is to figure out the subproblem and the recurrence
--> Write down wat the recursive fn should return 

--> The tricky part is to write down wat the recursive function will return
--> Normally in DP problems that i have solved till now the recursive function is assumed to return answer between
i....N but in this problem it is opposite i.e. 0....i

TC: O(N), SC: O(N)
"""

#Code
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        N = len(days)
        travelling = set(days)
        dp = [-1] * 366 

        #Returns the minCost to travel starting from day 0 to day "day" in method params.
        def findMinCost(day):
            if day <= 0:
                return 0
            
            if dp[day] != -1:
                return dp[day]

            if day in travelling:
                ticket1 = findMinCost(day-1) + costs[0]
                ticket2 = findMinCost(day-7) + costs[1]
                ticket3 = findMinCost(day-30) + costs[2]            
                dp[day] = min(ticket1, ticket2, ticket3)
                return dp[day]
            
            dp[day] = findMinCost(day-1)
            return dp[day]
        
        return findMinCost(365)

