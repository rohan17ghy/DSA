"""
Question
https://leetcode.com/problems/find-k-th-smallest-pair-distance/description
"""

#Approach
"""
-> This is a combination of binary search on result and two pointer.
-> The answer is within the range of 0 <= ans < max(nums).
-> We can do binary search on the answer space.
-> Now the problem statement gets reduced to `finding the number of pairs <= distance(given distance from mid of binary search) in a sorted array`

TC: O(NLogN)
SC: O(1)
"""

#Code
class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        N = len(nums)
        start, end = 0, nums[-1]

        #region two pointer
        def isGood(target):
            right, count = 0, 0
            for left in range(N):
                while right < N and nums[right] - nums[left] <= target:
                    right += 1
                count += right - 1 - left
            return count >= k
        #endregion two pointer

        while start < end:
            mid = (start + end) // 2

            if isGood(mid):
                end = mid
            else:
                start = mid + 1
        return start