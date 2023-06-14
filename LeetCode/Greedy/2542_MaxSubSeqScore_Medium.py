"""
Question
https://leetcode.com/problems/maximum-subsequence-score/description/
"""

#Approach: 
"""
--> Greedy solution with sorting
--> We need to maximize two things, so first of all we can put together both the arrays and sort according to nums2
--> So now whenever we move we will get the min element
--> Now the thing that is left is to maximize the nums1 part, we can use heap for that     

TC: O(NlogN); SC: O(k) 
"""

#Code
class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        nums = sorted(list(zip(nums1, nums2)), key = lambda x: -x[1])
        h = []
        best = 0
        total = 0
        for x, y in nums:
            while len(h) >= k:
                total -= heapq.heappop(h)

            heapq.heappush(h, x)
            total += x    

            if len(h) == k:
                best = max(best, total * y)      
        return best    
                

                    
                
        
        