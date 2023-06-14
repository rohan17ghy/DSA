"""
Question
https://leetcode.com/problems/partition-array-into-two-arrays-to-minimize-sum-difference/description/
"""

#Approach
"""
--> Normal DP with memoization won't work as there time complexity will be 2 ^ 30 as there are that
many states.
--> So we need to apply "Meet in Middle" algorithm
--> It is pretty difficult i was not able to solve even after going through soln, try after few
days when my level would have increased :)
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
        

           




