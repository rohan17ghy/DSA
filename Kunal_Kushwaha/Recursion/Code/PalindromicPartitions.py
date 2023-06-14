from typing import List
import math

"""
Below soln is recursive. Solution of below
https://www.geeksforgeeks.org/given-a-string-print-all-possible-palindromic-partition/
"""
class Solution:
    def printAllPalindrome(self, s, currentPart, res):

        if(not s):
            res.append(currentPart.copy())
            return
        
        for i in range(0, len(s)):
            if(self.isPalindrome(s[:i+1])):
                currentPart.append(s[:i+1])
                self.printAllPalindrome(s[i+1:], currentPart, res)
                currentPart.pop()

    
    def isPalindrome(self, s):
        i=0
        j=len(s)-1
        while(i<j):
            if(s[i] != s[j]):
                return False
            i+=1
            j-=1
        return True
     
sol = Solution()
res = []
sol.printAllPalindrome("geeks", [], res)
print(res)
