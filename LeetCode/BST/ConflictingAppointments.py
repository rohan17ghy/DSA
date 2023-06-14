from queue import Queue

class TreeNode:
    def __init__(self, min, max) -> None:
        self.left = None
        self.min = min
        self.max = max
        self.right = None

class Solution:
    
    def findConflictingAppointments(self, appointments):
        ans = []
        root = None
        for app in appointments:
            appNode = TreeNode(app[0], app[1])
            root = self.insertIfNonConflicting(root, appNode, ans)
        return ans    

    #If non-conflicting then insert into BST, if conflicting then increase the range of meeting
    # Eg: [2, 5] is the BST node and [3, 7] is another meeting conflicting. Modify [2, 5] to [2, 7]           
    def insertIfNonConflicting(self, root, node, ans):
        if(root == None):
            return TreeNode(node.min, node.max)

        if(self.isConflictingInterval(root, node)):
            ans.append([node.min, node.max])
            root.min = min(root.min, node.min)
            root.max = max(root.max, node.max)    
        else:
            if(node.min < root.min):
                root.left = self.insertIfNonConflicting(root.left, node, ans)
            else:
                root.right = self.insertIfNonConflicting(root.right, node, ans)            
        return root


    def isConflictingInterval(self, root1, root2):
        if(root1.max < root2.min or root2.max < root1.min):
            return False
        return True            



    

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



sol = Solution()
appointments = [[1, 5], [3, 7], [2, 6], [10, 15], [5, 6], [4, 100]]
conflictingAppointments = sol.findConflictingAppointments(appointments)
print(conflictingAppointments)
