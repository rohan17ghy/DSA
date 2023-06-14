# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
 
class Solution:
    def buildTree(self, inorder, postorder):
        N = len(inorder)
        valMap = {}
        for i, val in enumerate(inorder):
            valMap[val] = i

        def constructTree(sIn, eIn, sPo, ePo):
            if sIn == eIn:
                return TreeNode(inorder[sIn])
            if sIn > eIn:
                return None
            if sIn < 0 or eIn >= N or sPo < 0 or ePo >= N:
                return None

            root = TreeNode(postorder[ePo])
            rootIndex = valMap[root.val]

            noElements = rootIndex - sIn
            root.left = constructTree(sIn, rootIndex-1, sPo, sPo + noElements - 1)
            root.right = constructTree(rootIndex+1, eIn, rootIndex, ePo-1)
            return root
        
        return constructTree(0, N-1, 0, N-1)      

inorder = [1,2,3,4,5]
postorder = [4,3,5,2,1]

sol = Solution()
ans = sol.buildTree(inorder, postorder)
print(ans)