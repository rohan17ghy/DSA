"""
Question
https://practice.geeksforgeeks.org/problems/number-of-turns-in-binary-tree/1
"""

#Approach
"""
--> Find the LCA of both the nodes
--> Find the turns from first to LCA 
--> Find the turns from second to LCA
--> Calc the resultant turns 
"""
#TC: O(n) SC: O(Height of tree)

class Solution:
    def NumberOFTurns(self, root, first, second):
        #return the number of turns required to go from first node to second node
        lca = self.findLCA(root, first, second)
        
        # Below 'L' and 'R' are passed which signifies from which direction the parent has called that method
        # Instead of creating strings 'L' and 'R' at each recursion step, some space can be optimized by using
        # a boolean variable instead of strings   
        if(lca.data == first):
            lTurns = self.findTurns(lca.left, second, 'L', 0)
            rTurns = self.findTurns(lca.right, second, 'R', 0)
            ans = max(lTurns, rTurns)
            return ans if ans >= 0 else 0 
        if(lca.data == second):
            lTurns = self.findTurns(lca.left, first, 'L', 0)
            rTurns = self.findTurns(lca.right, first, 'R', 0)
            ans = max(lTurns, rTurns)
            return ans if ans >= 0 else 0
        
        
        lFirstTurns = self.findTurns(lca.left, first, 'L', 0)
        rFirstTurns = self.findTurns(lca.right, first, 'R', 0)
        
        lSecTurns = self.findTurns(lca.left, second, 'L', 0)
        rSecTurns = self.findTurns(lca.right, second, 'R', 0)
        
        
        ans = max(lFirstTurns, rFirstTurns) + max(lSecTurns, rSecTurns) + 1
        return ans if ans >= 0 else 0
        
    
    def findTurns(self, root, val, turn, count):
        if(root == None):
            return float('-inf')
        if(root.data == val):
            return count
        
        lCount = count if turn == 'L' else count + 1
        rCount = count if turn == 'R' else count + 1
        
        lTurns = self.findTurns(root.left, val, 'L', lCount)
        rTurns = self.findTurns(root.right, val, 'R', rCount)
        
        return max(lTurns, rTurns)

    def findLCA(self, root, first, second):
        if(root == None):
            return None
        
        if(root.data == first or root.data == second):
            return root
        
        left = self.findLCA(root.left, first, second)
        right = self.findLCA(root.right, first, second)
        
        if(left != None and right != None):
            return root
        elif(left):
            return left
        else:
            return right