"""
Question
https://leetcode.com/problems/smallest-missing-non-negative-integer-after-operations/description/
"""

#Approach
"""
--> The main idea is to normalize all the values in between 0....value
--> After normalizing we can take any value and find out whether that can be achieved
--> This approach and intuition will make from practise :)

Reference: https://www.youtube.com/watch?v=NztQwlNn1XA&t=261s
"""

#Code
class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        d = collections.defaultdict(int)
        for i in range(len(nums)):
            d[nums[i] % value] += 1
 
        for i in range(len(nums)):
            if d[i % value] > 0:
                d[i % value] -= 1
            else:
                return i
        return len(nums)
