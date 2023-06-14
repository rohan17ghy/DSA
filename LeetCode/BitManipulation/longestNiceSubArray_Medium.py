"""
Question
https://leetcode.com/problems/longest-nice-subarray/
"""

#Approach
"""
--> We expand the window and keep finding the ans
--> We can keep track of the current bit mask of the entire window by doing OR operation
--> We shrink the array if the new element entering the window is violating the AND condn
--> We keep shrinking the window by doing XOR operation on bitmask. 
--> XOR'ing a number from a bitmask would turn off (make them 0) the bits the number is
making 1 
"""

#Code
class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        N = len(nums)
        left, currBitMask, ans = 0, 0, 0
        #for loop expands the window when the condition is still true
        for right in range(N):
            #while loop reduces the window when the condition is violated
            while (currBitMask & nums[right] != 0):
                currBitMask ^= nums[left]
                left += 1
            currBitMask = currBitMask | nums[right]
            ans = max(ans, right-left+1)
            
        return ans  