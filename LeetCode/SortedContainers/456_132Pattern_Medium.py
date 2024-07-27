"""
Question
https://leetcode.com/problems/132-pattern/description/?envType=daily-question&envId=2023-10-01
"""

#Approach
"""
--> We can break the problems as two parts if we assume we are at 3
--> The approach is if we reach the "3" that is the peak, we need to find the 1 and 2
--> 1 we can find by greedy, the smallest element on the left of 3
--> 2 can be found by using sorted list, 2 will be the greatest element which is smaller than 3 towards
the right of 3

--> For finding 1 we can use a prefix array/stack containing the min element from 0....i
--> For finding 2 we can use a sorted list

TC: O(N*log(N)) SC: O(N)
"""

#Code
from sortedcontainers import SortedList
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        N = len(nums)
        prefix = [nums[0]]
        for i in range(1, N):
          prefix.append(min(prefix[-1], nums[i]))
        
        sl = SortedList()
        for i in range(N-1, -1, -1):
          one = prefix.pop()
          twoIndex = sl.bisect_left(nums[i])
          if twoIndex > 0 and sl[twoIndex-1] > one:
            return True
          sl.add(nums[i])
        return False

