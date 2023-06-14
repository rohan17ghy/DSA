"""
Question
https://leetcode.com/problems/minimum-time-to-complete-trips/description/
"""

#Approach
"""
--> Following the binary search template we start with the answer space.
--> For a particular time we need to either go left(reduce time) or right(increase time)
--> For a particular time we need to find the trips that can be made and based on that we can move
left or right

TC: O(nLogR) R --> Range of the answer, SC:O(1)
"""

#Code
class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        N = len(time)
        left = 1
        right = min(time) * totalTrips

        def good(currTime):
            count = 0            
            for i in range(N):
                count += currTime // time[i]
                i += 1
            return count >= totalTrips

        while left < right:
            mid = (left + right) // 2
            if good(mid):
                right = mid
            else:
                left = mid + 1

        return left

