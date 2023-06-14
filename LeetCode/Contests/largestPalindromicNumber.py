"""
Question
https://leetcode.com/contest/weekly-contest-307/problems/largest-palindromic-number/
"""

#Approach:
"""
--> Use a freq map
--> Use greedy to select the higher number first
--> Take care of edge cases
"""

import heapq
class Solution:
    def largestPalindromic(self, num: str) -> str:
        maxHeap = []
        hashMap = {}
        for digit in num: 
            hashMap[digit] = hashMap.get(digit, 0) + 1
            
        numInt = 9
        ansArray = []
        maxOddOccurNumber = -1
        while(numInt >= 0):
            num = str(numInt)
            if(hashMap.get(num, 0) > 0):
                freq = hashMap[num]
                if(freq % 2 != 0):
                    maxOddOccurNumber = num if maxOddOccurNumber == -1 else maxOddOccurNumber
                    freq = freq -1
                ansArray.extend([num] * (freq//2))
            
            numInt -= 1
        
        #Ignoring the leading zeros
        i=0
        while(i < len(ansArray) and ansArray[i] == '0'):
            i += 1
        
        ansString = ''.join(ansArray[i:])
        revString = ansString[::-1]
        
        #Handling a special case where ans will be '0'
        if(maxOddOccurNumber == -1 and ansString == ''):
            return '0'
        
        if(maxOddOccurNumber != -1):
            ansString += str(maxOddOccurNumber)
        
        res = ansString + revString
        return res
        
       
        
        
            
            