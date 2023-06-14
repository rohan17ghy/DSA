"""
Question
https://practice.geeksforgeeks.org/problems/printing-longest-increasing-subsequence/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=printing-longest-increasing-subsequence

NOTE: The problem statement and the test cases do not match. The test cases are given for lexicographically 
smallest whereas the problem statement mentions lexicograhically largest. Below problem is done based on
lexicographically largest
"""

#Approach
"""
--> Continuation of 300_LIS_Medium.py
--> First we need to do bottom up approach to form the dp array
--> With dp array and prev dictionary we can reconstruct path


TC: O(N ^ 2), SC:O(N ^ 2)
"""

class Solution:
    def longestIncreasingSubsequence(self, N, nums):
        N = len(nums)
        dp = [0] * N
        prev = {}
        besti = -1
        
        #Bottom Up
        for i in range(N):
            if i == 0:
                dp[i] = 1
                continue
            
            ans = 1
            for j in range(i):
                prevLIS = dp[j]
                if nums[i] > nums[j] and prevLIS + 1 >= ans:
                    #If there is no previous index i.e. it is visited for first time [OR]
                    #If the current answer is higher than the previous answer [OR]
                    #If the current answer is same as the one before but this number is lexicographically larger
                    if i not in prev or prevLIS + 1 > ans or nums[j] > nums[prev[i]]:
                        prev[i] = j
                    ans = max(ans, prevLIS + 1)
            dp[i] = ans
            if besti < 0 or dp[besti] < ans:
                besti = i
                
        #Path reconstruction using prev dictionary
        i = besti
        ans = [nums[i]]
        while i in prev:
            ans.append(nums[prev[i]])
            i = prev[i]
        ans.reverse()
        return ans
        
