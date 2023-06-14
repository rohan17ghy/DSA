"""
Question
https://practice.geeksforgeeks.org/problems/longest-sub-array-with-sum-k0809/1
"""

#Approach: Optimal
"""
--> Initially it feels like a sliding window problem but sliding window won't work here
--> Please refer notes(backtracking part) to find why sliding window won't work here
--> Using PrefixSum
"""
#TC: O(n) SC: O(n)

class Solution:
    def lenOfLongSubarr (self, arr, n, k) : 
        #Complete the function
        
        prefixSum = [0] * n
        maxLen = 0
        dict = {}
        runSum = 0
        
        #dict[0] = -1 is added because initially the prefixSum will be zero and if we 
        #encounter prefixSum[i] = 0 again, that means 0...i can be an answer
        dict[0] = -1
        for i in range(n):
            prefixSum[i] = runSum + arr[i]
            runSum = prefixSum[i]
            if(prefixSum[i] - k in dict):
                maxLen = max(maxLen, i - dict[prefixSum[i] - k])
            
            if(prefixSum[i] not in dict):
                dict[prefixSum[i]] = i
        
        return maxLen