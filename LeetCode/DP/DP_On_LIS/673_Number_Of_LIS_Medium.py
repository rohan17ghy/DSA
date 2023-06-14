"""
Question
https://practice.geeksforgeeks.org/problems/longest-bitonic-subsequence0824/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=longest-bitonic-subsequence0824
"""

#Approach
"""
Prerequisite: 300_LIS_Medium

--> In addition to storing the len of LIS(DP array) we need to store the number of LIS(DP array) at each step.
We are using "numberOfLIS" for that

TC: O(N ^ 2), SC:O(N)
"""

#Code
#Bottom Up Approach
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        N = len(nums)
        #maxLen array stores the maxLen of LIS ending with nums[i]
        #numberOfLIS stores the number of LIS ending with nums[i]
        maxLen = [1] * N
        numberOfLIS = [1] * N

        for i in range(N):
            for j in range(i):
                if nums[j] < nums[i] and 1 + maxLen[j] > maxLen[i]:
                    maxLen[i] = 1 + maxLen[j]
                    numberOfLIS[i] = numberOfLIS[j]
                elif nums[j] < nums[i] and 1 + maxLen[j] == maxLen[i]:
                    numberOfLIS[i] += numberOfLIS[j]
        
        #Find the total number of LIS 
        mx = max(maxLen)
        total = 0 
        for i in range(N):
            if maxLen[i] == mx:
                total += numberOfLIS[i]
        return total

        