"""
Question
https://leetcode.com/problems/reorganize-string/
"""

#Approach:
"""
--> The idea is to exhaust all the alphabets with higher frequency, so that a valid 
string is formed
--> To exhaust the higher frequency alphabets we use a maxHeap
--> We find the frequency of alphabets using a dictionary 
"""

class Solution:
    def reorganizeString(self, s: str) -> str:
        dict = {}
        for char in s:
            dict[char] = dict.get(char, 0) + 1
        maxHeap = []
        for key, val in dict.items():
            heapq.heappush(maxHeap, (-1*val, key))
        
        ans = []
        prev = None
        while(len(maxHeap) > 0):
            maxVal, char = heapq.heappop(maxHeap)
            ans.append(char)
            maxVal += 1
            
            if(prev != None):
                heapq.heappush(maxHeap, prev)
            
            prev = None
            if(maxVal < 0):
                prev = (maxVal, char)
        
        if(len(ans) < len(s)):
            return ''
        
        return ''.join(ans)
        