"""
Question
https://leetcode.com/problems/minimum-number-of-operations-to-make-array-continuous/description/?envType=daily-question&envId=2023-10-10
"""

#Approach
"""
--> Sort the array
--> One crucial observation from the rules is that the array will be having all whole numbers within a range
--> Assume the range [left, right] 
--> Iterate the array to find the range considering the nums[i] = left 
--> Now with binary search we can find the number of elements which are in the range [left, right] and hence find the operations to make contiguous

--> TC: O(NlogN), SC:O(NlogN) --> space from sorting
"""

#Code
import bisect
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        N = len(nums)

        #Done for handling duplicates
        nums = sorted(set(nums))
        M = len(nums)

        best = N-1
        #Range is between [left, right]
        #While iterating assume nums[i] is left and then try to build continuos array and find the min operations 
        for i in range(M):
            left = nums[i]
            right = nums[i] + N - 1
            index = bisect.bisect_left(nums, right+1)
            best = min(best, i + (N-index))
            #print(left, " ", right, " ", index, " ", best)
        return best    
