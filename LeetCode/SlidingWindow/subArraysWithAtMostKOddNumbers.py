"""
Q: Given an array of integers nums and an integer k. 
A continuous subarray is called nice if there are atmost k odd numbers on it.
Return the number of nice sub-arrays.
"""

#Approach 1:
#Brute Force approach
#TC: O(n^2) SC: O(1)
"""
Create all subarrays and calc the number of elements which are odd while creating the subarrays
Keep a count of the number of subarrays having k odd elements
"""

#Approach2
#Better sol
#TC: O(N), SC: O(N)
"""
Use a prefix Sum type array where prefix[i] gives the number of odd numbers from 0 to i
"""

#Approach3
#Better soln
#TC: O(n), SC: O(n)
"""
Replace all odd numbers by 1 and even numbers by 0
Now the problem becomes calc the number of subarrays where sum is atmost k
"""

#Approach 4
#Optimized soln
#TC: O(N), SC: O(1)
class Solution:
    def atMostK(self, nums, k):
        start = end = count = ans = 0
        n = len(nums)
        
        while(end < n):
            #Below statement is equivalent of following logic
            #if(nums[end] % 2 != 0):
            #   count += 1
            count += nums[end] % 2
            
            while(count > k):
                count -= nums[start] % 2
                start += 1
            
            #Total no. of subarrays ending with the end of the window(end-1) = 
            #Length of the subarray
            #Eg: Subarray -> [1, 2, 3]
            #Subarrays end at 3 are : [1, 2, 3], [2, 3], [3] = Length of subarray
            ans += end-start
            end += 1
        
        return ans