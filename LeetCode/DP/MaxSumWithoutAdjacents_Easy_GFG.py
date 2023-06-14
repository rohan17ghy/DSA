"""
Question
https://practice.geeksforgeeks.org/problems/max-sum-without-adjacents2430/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=max-sum-without-adjacents
"""

#Approach
"""
--> Simple observation that ans[i] will be max(ans[i-1], ans[i-2] + arr[i])

TC: O(N), SC: O(N)
"""

#Code
class Solution:	
	def findMaxSum(self,arr, n):
		#Code Here
		dp = [0] * n
		for i in range(n):
			if i == 0:
				dp[i] = arr[i]
				continue
			if i == 1:
				dp[i] = max(dp[i-1], arr[i])
				continue
			
			dp[i] = max(dp[i-1], dp[i-2] + arr[i])
		return dp[n-1]
