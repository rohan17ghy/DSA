"""
Question
https://practice.geeksforgeeks.org/problems/matrix-chain-multiplication0303/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=matrix-chain-multiplication
"""

#Approach
"""
PATTERN: PARTITION DP
--> This is a variance of partition DP. In this type of problems we partition the input recursively to find the ans
--> Lets say we are considering a window from i...j in arr. We can consider all the partitions between i and j
and find the minimum of them

--> TC: O(N^3) SC:O(N^2)

"""

#Code
#Top Down Approach
class Solution:
    def matrixMultiplication(self, N, arr):
        INF = 10 ** 20
        dp = [[-1] * N for _ in range(N)]
        
        def mcm(i, j):
            if j-i+1 < 3:
                return 0
            if j-i+1 == 3:
                return arr[i] * arr[i+1] * arr[j]
                
            if dp[i][j] != -1:
                return dp[i][j]
            
            minVal = INF
            for k in range(i + 1, j):
                minVal = min(minVal, mcm(i, k) + mcm(k, j) + arr[i] * arr[k] * arr[j])
            dp[i][j] = minVal
            return dp[i][j]
        
        return mcm(0, N-1)

#Bottom Up Approach
#Approach
"""
--> For converting the top down to bottom up we need to use fixed size sliding window concept
--> If we see the recurrence it is "min(minVal, mcm(i, k) + mcm(k, j) + arr[i] * arr[k] * arr[j])"
--> So from the recurrence we can observe that for bottom up we need to first calculate mcm(i, k) and mcm(k, j)
before calculating mcm(i, j)
--> From the above observation we can use a fixed size sliding window k
--> We can find the mcm for each k sized window
--> After that we can increase k and repeat

TC: O(N ^ 3)  SC: O(N ^ 2)
"""

#Code
class Solution:
    def matrixMultiplication(self, N, arr):
        INF = 10 ** 20
        dp = [[0] * N for _ in range(N)]
        
        #Fixed size sliding window
        #k = fixed size of window
        for k in range(1, N+1):
            #Window between i...j
            #Finding MCM between i...j
            #Note: We can calculate the MCM between i...j since the mcm of all the subarrays between i...j
            #are already calculated because of bottom up
            for j in range(k-1, N):
                i = j-k+1
                if j-i+1 < 3:
                    dp[i][j] = 0
                elif j-i+1 == 3:
                    dp[i][j] = arr[i] * arr[i+1] * arr[j]
                else:
                    minVal = INF
                    for mid in range(i + 1, j):
                        minVal = min(minVal, dp[i][mid] + dp[mid][j] + arr[i] * arr[mid] * arr[j])
                    dp[i][j] = minVal
        return dp[0][N-1]