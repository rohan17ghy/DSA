"""
Question
https://leetcode.com/problems/maximum-distance-in-arrays/description/
"""

#Approach
"""
Naive approach

->  So the naive approach is to calculate the distance of all the pairs of arrays. 
    Let's considert 2 arrays [a1.....aN] and [b1.....bM]
    For each pair the max distance will be max(abs(aN-b1), abs(bM-a1))
TC: O(N^2); SC: O(1)

Greedy approach

->  In greedy approach we try to do in 1 iteration
->  We need to keep a running firstElement and lastElement and calc max for each array element
->  Now the greedy idea is to minimize the firstElement and maximize the last element, because that will only result in max distance 

TC: O(N) SC: O(1)
"""

#Code
class Solution:
    def maxDistance(self, nums: List[List[int]]) -> int:
        N = len(nums)
        first, last = nums[0][0], nums[0][-1]
        
        ans = 0
        for i in range(1, N):
            currentFirst, currentLast = nums[i][0], nums[i][-1]
            ans = max(ans, abs(currentLast - first), abs(last - currentFirst))
            first = min(currentFirst, first)
            last = max(currentLast, last)
        return ans