"""
Question
https://leetcode.com/problems/target-sum/description/
"""

#Approach
"""
--> At each index we can either add or substract that number

TC: O(i * target), SC:O(i * target)
"""

#Code
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        N = len(nums)
        totalPosSum = sum(nums)
        dp = [[-1] * (2 * totalPosSum + 2000) for _ in range(N)]
        #Returns the total expressions which total to remTarget from index i
        def numberOfExpression(i, remTarget):
            if i == N:
                if remTarget == 0:
                    return 1
                return 0
            
            if dp[i][remTarget + totalPosSum] != -1:
                return dp[i][remTarget + totalPosSum]

            add = numberOfExpression(i+1, remTarget - nums[i])
            substract = numberOfExpression(i+1, remTarget + nums[i])

            dp[i][remTarget + totalPosSum] = add + substract
            return dp[i][remTarget + totalPosSum]
        
        return numberOfExpression(0, target)