"""
Question
https://leetcode.com/problems/tallest-billboard/
"""

#Approach
"""
--> Tricky part is to figure out the answer to return when total == 0
--> Also the tricky part is to add rods[i] to calc(i + 1, total + rods[i]) to return answer

TC: O(N * total), SC:O(N * total)
"""

#Code
class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        N = len(locations)
        MOD = 10 ** 9 + 7
        dp = [[-1] * (fuel+1) for _ in range(N)]
        def calc(i, currFuel):
            if currFuel < 0:
                return 0

            if dp[i][currFuel] != -1:
                return dp[i][currFuel]

            total = 0
            if i == finish:
                total = (total + 1) % MOD

            for j in range(N):
                if j != i:
                    total = (total + calc(j, currFuel - abs(locations[i] - locations[j]))) % MOD

            dp[i][currFuel] = total
            return dp[i][currFuel]
        
        return calc(start, fuel)


        

           




