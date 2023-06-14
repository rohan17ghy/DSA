"""
Question
https://leetcode.com/problems/longest-string-chain/description/
"""

#Approach
"""
--> The main idea is to find the subproblem or the recurrence relation
--> Wat is the subproblem we should consider? Wat should the recursive function return
--> We can consider that the function "Returns the len of longest string chain with words[i] as last word for words[:i]".
--> There can be other ways to write it but this is the cleanest

TC: O(N ^ 2), SC:O(N ^ 2) --> predArr takes N ^ 2 space and dp array takes N space 
"""

#Code
#Bottom Up Approach
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        #Returns the len of longest string chain with words[i] as last word for words[:i]
        
        N = len(words)
        words.sort(key=lambda x: len(x))
        
        predArr = [[False] * N for _ in range(N)]
        for i in range(N):
            word = words[i]
            for j in range(i):
                predWord = words[j]
                #Using two pointer to find the predecessor
                wordLen, predWordLen = len(word), len(predWord)
                if predWordLen != wordLen - 1:
                    predArr[i][j] = False
                    continue
                
                i1, j1 = 0, 0
                skip = 0
                while i1 < wordLen and j1 < predWordLen:
                    if word[i1] != predWord[j1]:
                        skip += 1
                        i1 += 1
                    else:
                        i1 += 1
                        j1 += 1
                
                if skip <= 1:   
                    predArr[i][j] = True

        #Whether words[j] is predecessor of words[i]
        def isPredecessor(i, j):
            return predArr[i][j]


        dp = [1] * N
        for i in range(N):
            word = words[i]
            for j in range(i):
                predWord = words[j]
                if isPredecessor(i, j):
                    dp[i] = max(dp[i], 1 + dp[j])

        return max(dp)