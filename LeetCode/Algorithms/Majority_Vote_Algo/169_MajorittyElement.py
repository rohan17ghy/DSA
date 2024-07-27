"""
Question
https://leetcode.com/problems/majority-element/description/
"""

#Approach
"""
--> Boyer Moore majority voting algorithm

--> TC: O(N), SC:O(N)
"""

#Code
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        N = len(nums)

        candidate = None
        count = 0
        for num in nums:
            if count == 0:
                candidate = num
                count += 1
            elif num == candidate:
                count += 1
            else:
                count -= 1
        return candidate       
