"""
Question
https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks/
"""

#Approach
"""
--> A fixed size sliding window can be used to find the max black blocks in k consecutive blocks
--> TEMPLATE: This can be used as a template for fixed size sliding window
"""

class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        N = len(blocks)
        black = 0
        maxBlack = 0
        
        for i in range(N):
            if(blocks[i] == 'B'):
                black += 1
            if(i-k >= 0 and blocks[i-k] == 'B'):
                black -= 1
            
            #Actual condition is i - k >= -1 which is same as i - k + 1 >= 0 
            if(i - k + 1 >= 0):
                maxBlack = max(maxBlack, black)
        
        return k-maxBlack