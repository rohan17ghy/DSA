"""
Question
https://leetcode.com/problems/minimum-limit-of-balls-in-a-bag/description/
"""

#Approach
"""
-> Pattern: Binary search on answer

Time complexity: O(N * log(max(nums)))
Space complexity: O(1)
"""

#Code
class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        left = 1
        right = 10 ** 9

        def good(target):
            operations = 0

            for x in nums:
                operations += math.ceil(x / target) - 1
            
            return operations <= maxOperations

        while (left < right):
            mid = (left + right) // 2
            if good(mid):
                right = mid
            else:
                left = mid + 1

        return left