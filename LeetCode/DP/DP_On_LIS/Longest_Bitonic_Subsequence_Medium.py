"""
Question
https://practice.geeksforgeeks.org/problems/longest-bitonic-subsequence0824/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=longest-bitonic-subsequence0824
"""

#Approach
"""
--> The main idea is to find the subproblem or the recurrence relation
--> Wat is the subproblem we should consider? Wat should the recursive function return
--> We need to combine 2 DP result, increasing from left and decreasing from right
--> 2 DP
	1st left to right: Recursive fn returns --> Returns the longest subsequence 
	    of nums[:i] with the largest number at nums[i]
	2nd right to left: Recursive fn returns --> Returns the longest subsequence
	    of nums[i:] with the largest number at nums[i]

--> There can be other ways to write it but this is the cleanest

TC: O(N ^ 2), SC:O(N)
"""

#Code
#Bottom Up Approach
class Solution:
    def LongestBitonicSequence(self, nums):
        #2 DP
        #1st left to right: Recursive fn returns --> Returns the longest subsequence 
        #of nums[:i] with the largest number at nums[i]
        #2nd right to left: Recursive fn returns --> Returns the longest subsequence
        #of nums[i:] with the largest number at nums[i]
        N = len(nums)
        bestL = [1] * N
        bestR = [1] * N

        for i in range(N):
            #Here wat is the length of longest increasing subsequence which ends here at i
            for j in range(i):
                if nums[j] < nums[i]:
                    bestL[i] = max(bestL[i], 1 + bestL[j])

        for i in range(N-1, -1, -1):
            #Here wat is the length of longest decreasing subsequence which starts here at i
            for j in range(i, N):
                if nums[j] < nums[i]:
                    bestR[i] = max(bestR[i], 1 + bestR[j])

        best = []
        for i in range(N):
            best.append(bestL[i] + bestR[i])
        return max(best) - 1

        