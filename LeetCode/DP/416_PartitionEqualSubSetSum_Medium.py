"""
Question
https://leetcode.com/problems/minimum-falling-path-sum/description/
"""

#Approach
"""
--> One observation is that since we need to divide the total sum by 2 so it should be divisible by 2 
--> Initial approach can be that of backtracking.
is O(2^N)
--> This can be reduced to O(N) by caching the answer(DP)

TC: O(N), SC:O(N)
"""

#Code
#Recursion with Memoization soln
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        @lru_cache(maxsize=None)
        def dfs( n: int, subset_sum: int) -> bool:
            # Base cases
            if subset_sum == 0:
                return True
            if n == 0 or subset_sum < 0:
                return False
            result = (dfs(n - 1, subset_sum - nums[n - 1])
                    or dfs( n - 1, subset_sum))
            return result

        # find sum of array elements
        total_sum = sum(nums)

        # if total_sum is odd, it cannot be partitioned into equal sum subsets
        if total_sum % 2 != 0:
            return False

        subset_sum = total_sum // 2
        n = len(nums)
        return dfs( n - 1, subset_sum)
        

           




