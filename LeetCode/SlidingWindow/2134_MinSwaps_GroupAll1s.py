"""
Question
https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together-ii
"""

#Approach
"""
-> Here the approach is that we need to bring together count(1) number of 1's 
-> We can use fixed size sliding window to find the current 1's in each subarray of size = count(1), from that we can find the min swaps required 
TC: O(n) SC:O(1)
"""

"""
Very clean code for sliding window
"""
class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        N, count = len(nums), nums.count(1)
        currCount, j = 0, 0
        ans = 10 ** 20
        for i in range(N + count):
            if i < count:
                if nums[i] == 1:
                    currCount += 1
                continue
            
            i = i % N
            if nums[i] == 1:
                currCount += 1

            if nums[j] == 1:
                currCount -= 1
            
            ans = min(ans, count - currCount)
            j += 1
        
        return ans