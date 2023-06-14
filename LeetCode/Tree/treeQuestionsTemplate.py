#User function Template for python3

#new node
class newNode:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None
 
# Function to insert nodes in level order
def insertLevelOrder(arr, i, n):
    root = None
    # Base case for recursion
    if i < n:
        root = newNode(arr[i])
 
        # insert left child
        root.left = insertLevelOrder(arr, 2 * i + 1, n) if 2 * i + 1 < n and arr[2 * i + 1] != None else None
 
        # insert right child
        root.right = insertLevelOrder(arr, 2 * i + 2, n) if 2 * i + 2 < n and arr[2 * i + 2] != None else None
         
    return root  

#User function Template for python3

class Solution:
    #Function to return the lowest common ancestor in a Binary Tree.
    def printAllDups(self,root):
        #code here
        ans = []
        hashSet = {}
        self.printAllDupsHelper(root, hashSet, ans)
        return ans
        
    def printAllDupsHelper(self, root, hashSet, ans):
        if(root == None):
            return ''
         
        left = self.printAllDupsHelper(root.left, hashSet, ans)
        right = self.printAllDupsHelper(root.right, hashSet, ans)
        
        serialized = str(root.data) + "*" + left + "*" + right
        if(serialized in hashSet and hashSet[serialized] == False):
            hashSet[serialized] = True
            ans.append(root)
        else:
            hashSet[serialized] = False
        
        return serialized 
        
    
        
    

#For missing child provide None 
arr = [1, 2, 3, 4, None, 2, 4, None, None, 4]
root = insertLevelOrder(arr, 0, len(arr))
sol = Solution()
dll = sol.printAllDups(root)
print(dll)