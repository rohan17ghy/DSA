"""
Question
https://practice.geeksforgeeks.org/problems/is-binary-tree-heap/1
"""

#Approach
"""
--> Need to check 2 things 
    1. If the Binary tree is complete
    2. If the Binary tree follows heap order
"""

#Code I have written
class Solution:
    #Your Function Should return True/False
    def isHeap(self, root):
        #Code Here
        maxHeight, isCBT = self.isCBT(root)
        if(not isCBT):
            return False
            
        return self.isCBTHeap(root, float('inf'))
    
    def isCBT(self, root):
        if(root == None):
            return 0, True
        
        leftH, leftCBT = self.isCBT(root.left)
        rightH, rightCBT = self.isCBT(root.right)
        
        isHeightBalanced = False
        if(leftH == rightH or leftH == rightH+1):
            isHeightBalanced = True
        
        isCBT = leftCBT and rightCBT and isHeightBalanced
        
        #print("Root.data: ", root.data, " ", max(leftH, rightH) + 1, " ", isCBT)
        
        return max(leftH, rightH) + 1, isCBT
    
    def isCBTHeap(self, root, upperRange):
        if(root == None):
            return True
        
        if(root.data > upperRange):
            return False
        left = self.isCBTHeap(root.left, root.data)
        right = self.isCBTHeap(root.right, root.data)
        
        return left and right

#isCBT() method can be more cleaner
#Check the below code for cleaner isCBT() function.
#Check out Love Babbar Lecture 75: 19:00 timestamp

class Solution:
    #Your Function Should return True/False
    def isHeap(self, root):
        #Code Here
        n = self.countNodes(root)
        return self.isCBT(root, 0, n) and self.isCBTHeap(root, float('inf'))
        
    def countNodes(self, root):
        if(root == None):
            return 0
        
        left = self.countNodes(root.left)
        right = self.countNodes(root.right)
        
        return left + right + 1
    
    def isCBT(self, root, i, n):
        if(root == None):
            return True
        
        if(i >= n):
            return False
            
        left = self.isCBT(root.left, 2*i + 1, n)
        right = self.isCBT(root.right, 2*i + 2, n)
        
        return left and right
        
    
    def isCBTHeap(self, root, upperRange):
        if(root == None):
            return True
        
        if(root.data > upperRange):
            return False
        left = self.isCBTHeap(root.left, root.data)
        right = self.isCBTHeap(root.right, root.data)
        
        return left and right

