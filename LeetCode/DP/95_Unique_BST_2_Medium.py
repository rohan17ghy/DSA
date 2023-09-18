"""
Question
https://leetcode.com/problems/unique-binary-search-trees-ii/description/
"""

#Approach
"""
--> PATTERN: Catalan's sequence

"""

#Code
#Top Down Approach
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, N: int) -> List[Optional[TreeNode]]:        
        #Catalan's sequence
        #Return the list of BST between start and end
        def genBST(start, end):
            if start > end:
                return [None]
            if start == end:
                return [TreeNode(start)]
            
            ans = []
            for i in range(start, end+1):
                left = genBST(start, i-1)
                right = genBST(i+1, end)

                for l in left:
                    for r in right:
                        root = TreeNode(i)
                        root.left = l
                        root.right = r
                        print(root)
                        ans.append(root)
            return ans
        
        return genBST(1, N)
