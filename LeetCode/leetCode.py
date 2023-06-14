from queue import Queue

class TreeNode:
    def __init__(self, val) -> None:
        self.left = None
        self.val = val
        self.right = None

class Solution:
    def insertIntoBST(self, root, val):
        if(root == None):
            return TreeNode(val)

        if(val > root.val):
            root.right = self.insertIntoBST(root.right, val)
        else:
            root.left = self.insertIntoBST(root.left, val)
        return root
    
    def createBST(self, values):
        root = None
        for value in values:
            root = self.insertIntoBST(root, value)
        return root
    
    def levelOrderTraversal(self, root):
        queue = Queue()
        queue.put(root)
        queue.put('*')
        while(not queue.empty()):
            node = queue.get()
            if(node == '*'):
                queue.put('*') if not queue.empty() else None
                print()
                continue
            if(node == 'None'):
                print(node, end=" ")
                continue
            print(node.val, end=" ")
            queue.put(node.left) if node.left != None else queue.put('None')
            queue.put(node.right) if node.right != None else queue.put('None')
    
    def isBST(self, root):
        #code here
        return self.isBSTHelper(root, float('-inf'), float('+inf'))
        
    def isBSTHelper(self, root, lower, upper):
        if(root == None):
            return True
        
        if(root.val < lower or root.val > upper):
            return False
        
        left = self.isBSTHelper(root.left, lower, root.val)
        
        right = self.isBSTHelper(root.right, root.val, upper)
        
        return left and right



sol = Solution()
arr = [2, 1, 3]
root = sol.createBST(arr)
ans = sol.isBST(root)
sol.levelOrderTraversal(root)

