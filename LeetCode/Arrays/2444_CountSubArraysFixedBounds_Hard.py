"""
Question
https://leetcode.com/problems/count-subarrays-with-fixed-bounds/
"""

#Approach
"""
--> Approach is little tricky and would be difficult to note it down. Please check the reference for
initial explanation

--> For the explanation given in the video O(N) space is used and we are exploring the right part only
to avoid duplicate counting of subarrays.

--> We can reduce this space complexity to O(1) if we explore only the left side and that can be done
while explorin the array from left to right

PATTERN: Number of subarrays that can be formed from the given range of subarray i.e. Degree of freedom

Reference: https://www.youtube.com/watch?v=utbe24g2khs
           https://www.youtube.com/watch?v=V-uRiEjsItc&t=803s

TC:O(N), SC:O(1)
"""

#Code
class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        N = len(nums)
        minIndex, maxIndex, outOfBoundIndex = -1, -1, 0
        total = 0
        for i in range(N):
            if nums[i] == minK:
                minIndex = i
            if nums[i] == maxK:
                maxIndex = i
            if nums[i] > maxK or nums[i] < minK:
                minIndex = -1
                maxIndex = -1
                outOfBoundIndex = i+1
            
            if minIndex >= 0 and maxIndex >= 0:
                total += min(minIndex, maxIndex) - outOfBoundIndex + 1
        return total
