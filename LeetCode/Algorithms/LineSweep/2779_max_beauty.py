"""
Question
https://leetcode.com/problems/maximum-beauty-of-an-array-after-applying-operation
"""

#Approach
"""
-> Line sweep algorithm

Reference: https://www.youtube.com/watch?v=oyJUeIawGdQ&t=582s
"""

#TC: O(N * logN)
#SC: O(N)

class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        events = []
        for x in nums:
            events.append((x - k, 1))
            events.append((x + k + 1, -1))
        
        events.sort()

        best = 0
        curr = 0
        for _, d in events:
            curr += d
            best = max(best, curr)
        return best