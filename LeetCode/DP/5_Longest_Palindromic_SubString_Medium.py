"""
Question
https://leetcode.com/problems/longest-palindromic-substring/description/
"""

#Approach
"""
--> The main thing is that we need to figure out wat should the recursive function return.
--> And also that the recursive function has a good time and space complexity

TC: O(N * N), SC: O(N * N)
"""

#Code
#Top Down Approach
class Solution:
    def longestPalindrome(self, s: str) -> str:
        N = len(s)
        best = ""
        has_cache = [[False] * N for _ in range(N)]
        cache = [[""] * N for _ in range(N)]

        bestL, bestR = -1, -1
        bestLen = 0                


        #Returns whether s[l...r] is a palindrome
        #Ex: Input: "sas", l = 0, r = 2;  Ouput: "sas"
        #Ex: Input: "asas", l = 0, r = 3; Ouput: "" 
        def isLPSubStr(l, r):
            nonlocal bestLen, bestL, bestR
            if l == r:
                if bestLen == 0:
                    bestL, bestR = l, r
                    bestLen = 1
                return True
            
            if l > r:
                return True

            if has_cache[l][r]:
                return cache[l][r]            
            
            if s[l] == s[r] and isLPSubStr(l+1, r-1):
                if r-l+1 > bestLen:
                    bestL, bestR = l, r
                    bestLen = r-l+1
                has_cache[l][r] = True
                cache[l][r] = True
                return True
            
            isLPSubStr(l, r - 1)
            isLPSubStr(l + 1, r)

            has_cache[l][r] = True
            cache[l][r] = False
            return False
        
        isLPSubStr(0, N-1)
        return s[bestL: bestR + 1]
