"""
Question
https://leetcode.com/problems/largest-divisible-subset/description/
"""

#Approach
"""
--> The main idea is to find the subproblem or the recurrence relation
--> Wat is the subproblem we should consider? Wat should the recursive function return
--> We can consider that the function "Returns the largest DivisibleSubset for nums[:i] where
nums[i] is the largest number in set".
--> There can be other ways to write it but this is the cleanest
--> To consider this recurrence we would need to sort the array first

Follow Up: Try writing bottom up soln directly without writing the top down first

TC: O(N ^ 2), SC:O(N)
"""

#Code
#Bottom Up
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        #Recurrence/Recursive function returns:
        #Returns the largest DivisibleSubset for nums[:i] where nums[i] is the largest number in set

        N = len(nums)
        nums.sort()
        dp = [1] * N
        prev = [-1] * N

        #Creating the dp array which represent the largest subset length
        #Largest DivisibleSubset len for nums[:i] where nums[i] is the largest number in set
        for i in range(N):
            for j in range(i):
                if nums[i] % nums[j] == 0 and 1 + dp[j] > dp[i]:
                    dp[i] = 1 + dp[j]
                    prev[i] = j
        
        #Finding the max index
        besti = 0
        for i in range(N):
            if dp[i] > dp[besti]:
                besti = i
        
        #Path re-construction
        ans = [nums[besti]]
        while prev[besti] != -1:
            ans.append(nums[prev[besti]])
            besti = prev[besti]
        return ans
        
        