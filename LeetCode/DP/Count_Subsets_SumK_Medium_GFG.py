"""
Question
https://practice.geeksforgeeks.org/problems/perfect-sum-problem5633/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=perfect-sum-problem
"""

#Approach
"""
--> Initial approach can be that of backtracking.
is O(2^N)
--> This can be reduced to O(N) by caching the answer(DP)

--> Time complexity of DP can be thought of number of subproblems/states * time to solve each state
--> There are (N * sum) states possible 

TC: O(N * sum), SC:O(N * sum)
"""

#Code
#Tabulation soln
class Solution:
    def perfectSum(self, arr, n, sum):
        # code here
        mod = 10 ** 9 + 7
        dp = [[0] * (sum+1) for _ in range(n)] 
        for i in range(n):
            for j in range(sum+1):
                if j == arr[i]:
                    dp[i][j] = dp[i][j] + 1
                if i > 0:
                    dp[i][j] = (dp[i][j] + dp[i-1][j]) % mod
                if i > 0 and j - arr[i] >= 0:
                    dp[i][j] = (dp[i][j] + dp[i-1][j-arr[i]]) % mod 
        
        return dp[n-1][sum]
        

           




