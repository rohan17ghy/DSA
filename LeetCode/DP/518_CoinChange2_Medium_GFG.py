"""
Question
https://leetcode.com/problems/coin-change-ii/description/
"""

#Approach
"""
--> Initially there could be few ways of coming up with the approach but those will give TLE
--> Another issue with other approaches is that there could be duplicates.
Eg: [1, 5], amount = 6
For another approach the answers could be
    -1, 5
    -5, 1
    -1, 1, 1, 1, 1, 1
But the 1, 5 and 5, 1 are repetative so we need to avoid it
--> At each index we either take that index and stay there or don't take anything and move forward

TC: O(index * amount), SC:O(index * amount)
"""

#Code
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        N = len(coins)
        dp = [[-1] * (amount + 1) for _ in range(N)]
        #Returns the number of combinations that make up "remAmount"
        def countCombinations(index, remAmount):
            if remAmount == 0:
                return 1
            
            if index >= N:
                return 0
            
            if dp[index][remAmount] != -1:
                return dp[index][remAmount]

            ans = 0
            if remAmount - coins[index] >= 0:
                ans += countCombinations(index, remAmount-coins[index])
            ans += countCombinations(index + 1, remAmount)

            dp[index][remAmount] = ans
            return dp[index][remAmount]
        return countCombinations(0, amount)
        
