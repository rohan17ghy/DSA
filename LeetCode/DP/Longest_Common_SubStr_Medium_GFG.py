"""
Question
https://practice.geeksforgeeks.org/problems/print-all-lcs-sequences3413/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=print-all-lcs-sequences
"""

#Approach
"""
--> First we need to figure out wat should the recursive function return.
--> In approach 1 we use tuples because the function will return multiple values
--> In second approach we reduce this tuple usage instead we use a global variable "best"
--> Bottom Up approach of Approach1 gives TLE in GFG
--> Bottom Up approach of Approach2 is the AC answer

TC: O(N * M), SC: O(N * M)
"""

#Code
#Approach 1: With tuples
#Top Down Approach
class Solution:
    def longestCommonSubstr(self, S1, S2, n, m):
        # code here
        N1, N2 = n, m
        dp = {}
        
        try:
            #Gives two answers
            #1. Returns the longestCommonSubstr betweeen i1.....n and i2.....m starting
            #   at i1 and i2
            #2. Returns the longestCommonSubstr betweeen i1.....n and i2.....m not starting
            #   at i1 or i2
            def findSubStr(i1, i2):
                if i1 == N1 or i2 == N2:
                    return 0, 0
                
                if (i1, i2) in dp:
                    return dp[(i1, i2)]
                
                ans1, ans2 = 0, 0
                if S1[i1] == S2[i2]:
                    tempAns1, tempAns2 = findSubStr(i1+1, i2+1)
                    ans1, ans2 = 1 + tempAns1, tempAns2
                
                ans2 = max(ans2, findSubStr(i1, i2 + 1), findSubStr(i1 + 1, i2))
                dp[(i1, i2)] = ans1, ans2
                
                return dp[(i1, i2)]
        
            return max(findSubStr(0, 0))
        except Exception as ex:
            print(ex)

#Bottom Up approach
import collections
class Solution:
    def longestCommonSubstr(self, S1, S2, n, m):
        # code here
        N1, N2 = n, m
        dp = collections.defaultdict(lambda : (0, 0))
        
        for i in range(N1-1, -1, -1):
            for j in range(N2-1, -1, -1):
                tempAns1, tempAns2 = 0, 0
                if S1[i] == S2[j]:
                    tempAns1, tempAns2 = dp[(i+1, j+1)]
                    tempAns1, tempAns2 = 1 + tempAns1, tempAns2
                tempAns2 = max(tempAns2, max(dp[(i, j+1)]), max(dp[(i+1, j)]))
                dp[(i, j)] = tempAns1, tempAns2
        
        return max(dp[(0, 0)])


#Approach 2: Without tuples
# Top Down Approach
import collections
class Solution:
    def longestCommonSubstr(self, S1, S2, n, m):
        # code here
        N1, N2 = n, m
        dp = [[-1] * N2 for _ in range(N1)]
        best = 0
        try:
            #Returns the longestCommonSubstr starting at i1 and i2
            def findSubStr(i1, i2):
                if i1 == N1 or i2 == N2:
                    return 0
                
                if dp[i1][i2] != -1:
                    return dp[i1][i2]
                
                ans = 0
                maxVal = 0
                if S1[i1] == S2[i2]:
                    ans = 1 + findSubStr(i1 + 1, i2 + 1)
                    maxVal = max(maxVal, ans)
                maxVal = max(maxVal, findSubStr(i1, i2 + 1), findSubStr(i1 + 1, i2))
                
                nonlocal best
                best = max(best, maxVal)
                
                dp[i1][i2] = ans
                return ans
                
            findSubStr(0, 0)
            #print(dp)
            return best
            
        except Exception as ex:
            print(ex)

#Bottom Up Approach
#User function Template for python3
import collections
class Solution:
    def longestCommonSubstr(self, S1, S2, n, m):
        # code here
        N1, N2 = n, m
        dp = [[-1] * (N2+1) for _ in range(N1+1)]
        
        for i in range(N1+1):
            dp[i][N2] = 0
        for j in range(N2+1):
            dp[N1][j] = 0
        
        maxVal = 0
        for i in range(N1-1, -1, -1):
            for j in range(N2-1, -1, -1):
                ans = 0
                if S1[i] == S2[j]:
                    ans = 1 + dp[i + 1][j + 1]
                    maxVal = max(maxVal, ans)
                maxVal = max(maxVal, dp[i][j + 1], dp[i + 1][j])
                dp[i][j] = ans
        return maxVal 
