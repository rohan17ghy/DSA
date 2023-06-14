"""
Question
https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/
"""

#Approach
"""
--> We can use backtracking for this problem. 
--> Finding out wat strings are already part of the current Ans and wat other strings
can be taken we can either use a set. But a better soln is to use a bitset

Reference for BitSet
https://www.youtube.com/watch?v=j3dZMmsw8zE

"""

#Code
class Solution:
    def maxLength(self, arr: List[str]) -> int:
        N = len(arr)
        bitSetArr = []
        count = []
        best = 0
        
        def getBitSet(s):
            b = 0
            for char in s:
                d = ord(char) - ord('a')
                if(b & (1<<d) > 0):
                    return -1
                b |= 1 << d
            return b
        
        for s in arr:
            bitSetArr.append(getBitSet(s))
            count.append(len(s))
            
            
        def backTrack(index, currBitSet, currL):
            if(index >= N):
                nonlocal best
                best = max(best, currL)
                return
            
            if(bitSetArr[index] != -1 and bitSetArr[index] & currBitSet == 0):
                backTrack(index+1, currBitSet | bitSetArr[index], currL + count[index])
            backTrack(index+1, currBitSet, currL)
        
        backTrack(0, 0, 0)
        return best