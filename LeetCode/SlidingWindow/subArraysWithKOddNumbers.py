"""
Q: Given an array of integers nums and an integer k. 
A continuous subarray is called nice if there are k odd numbers on it.

Return the number of nice sub-arrays.
"""

#Approach 1
#Better soln
#TC: O(N), SC: O(N)
"""
Replacing odd number by 1 and even numbers by 0.
Now find the number of subArray with sum = k
"""
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        #Replacing odd number with 1 and even with 0
        #Because doing that reduces the problem to number of subArray with sum = k
        for i in range(len(nums)):
            nums[i] = nums[i] % 2
            
        return self.subArrayWithSumK(nums, k)
            
        
    def subArrayWithSumK(self, nums, k):
        freq_map = {0: 1}
        prefixSum = 0
        ans = 0
        for i in range(len(nums)):
            prefixSum += nums[i]
            if(prefixSum - k in freq_map):
                ans += freq_map[prefixSum - k]
            freq_map[prefixSum] = freq_map.get(prefixSum, 0) + 1
        return ans

#Approach2
#Optimized soln
#TC: O(n) SC: O(1)
"""
If the problem was finding atmost k elements then we could have used sliding window as used in that 
problem.

The main idea here is to understand that
exactly(k) = atmost(k) - atmost(k-1)

For code of atmost(k) checkout .\subArraysWithAtMostKOddNumbers.py
"""
