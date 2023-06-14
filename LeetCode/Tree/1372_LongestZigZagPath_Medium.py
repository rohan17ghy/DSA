"""
Question
https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/description/
"""

#Approach
"""
--> DFS and keep track of directions
--> I was able to write the code but "Programming with Larry" wrote a very clean soln. Check that out as well  
"""
#TC: O(n) SC: O(1)

#My Soln
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        #False --> left
        #True --> right 
        best = 0
        def longest(node, direction, currLen):
            if node is None:
                nonlocal best
                best = max(best, currLen)
                return

            if direction:
                longest(node.left, not direction, currLen+1)
                longest(node.right, direction, 1)
            else:
                longest(node.left, direction, 1)
                longest(node.right, not direction, currLen + 1)

        longest(root, True, 0)
        longest(root, False, 0)
        return best-1    

#Inspired from Programming Live with Larry
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        best = 0
        def goLeft(node, currLen):
            nonlocal best
            best = max(best, currLen-1)  
            
            if node is None:                
                return 

            goLeft(node.left, 1)
            goRight(node.right, currLen + 1)

        def goRight(node, currLen):
            nonlocal best
            best = max(best, currLen-1)

            if node is None:
                return

            goLeft(node.left, currLen + 1)
            goRight(node.right, 1)

        goLeft(root, 0)
        goRight(root, 0)
        return best          