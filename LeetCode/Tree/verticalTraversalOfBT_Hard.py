"""
Question
https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/
"""

#Approach:
"""
--> Use a SortedDictionary with key = tuple (col, row) and value = list of nodes at (row, col)
--> After creating this dictionary combine the same col keys in order  

"""

#Code
from sortedcontainers import SortedDict, SortedList
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        lookup = SortedDict()
        def traverse(node, x, y):
            if(node == None):
                return
            if((y, x) in lookup):
                lookup[(y, x)].add(node.val)
            else:
                lookup.update({(y, x): SortedList([node.val])})
            
            traverse(node.left, x+1, y-1)
            traverse(node.right, x+1, y+1)
        traverse(root, 0, 0)
        
        print(lookup)
        
        #Bringing all the nodes of the same col in a single list
        ans = []
        lastCol = -1
        currList = []
        for y, x in lookup:
            if(lastCol == y):
                currList.extend(lookup[(y, x)])
            else:
                ans.append(currList) if currList else None
                currList = list(lookup[(y, x)])            
            lastCol = y
        if(len(currList) > 0):
            ans.append(currList)
        return ans