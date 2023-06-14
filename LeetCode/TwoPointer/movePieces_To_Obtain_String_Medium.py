"""
Question
https://leetcode.com/problems/move-pieces-to-obtain-a-string/
"""

#Approach
"""
--> We need to keep track of the sequence of the L's and R's 
--> Sequence should be same as L can't cross over R
--> Also we need to check if the L at index i  of start can reach the L at index j of target(same for R)   
"""

#Code
class Solution:
    def canChange(self, start: str, target: str) -> bool:
        if(start.count('L') != target.count('L')):
            return False
        if(start.count('R') != target.count('R')):
            return False
        
        N = len(start)
        i, j = 0, 0
        while(i < N and j < N):
            while(i < N and start[i] == '_'):
                i += 1
            while(j < N and target[j] == '_'):
                j += 1
            
            if(i >= N or j >= N):
                break
            
            if(start[i] == 'L' and target[j] == 'L'):
                if(i < j):
                    return False
                i += 1
                j += 1
            elif(start[i] == 'R' and target[j] == 'R'):
                if(i > j):
                    return False
                i += 1
                j += 1
            else:
                return False
        
        return True