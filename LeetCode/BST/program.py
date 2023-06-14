#User function Template for python3

#new node
class newNode:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

class Info:
    def __init__(self, maxVal, minVal, size, isBST):
        self.maxVal = maxVal
        self.minVal = minVal
        self.size = size
        self.isBST = isBST
    
 
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

    def largestBst(self, root):
        maxSize = [0]
        self.solve(root, Info(float('-inf'), float('inf'), 0, False), maxSize)
        return maxSize[0]
        
    def solve(self, root, info, maxSize):
        if(root == None):
            return Info(float('-inf'), float('inf'), 0, True)
        
        leftInfo = self.solve(root.left, info, maxSize)
        leftInfoMax = leftInfo.maxVal
        leftInfoMin = leftInfo.minVal
        leftInfoSize = leftInfo.size
        leftInfoIsBST = leftInfo.isBST
        rightInfo = self.solve(root.right, info, maxSize)
        rightInfoMax = rightInfo.maxVal
        rightInfoMin = rightInfo.minVal
        rightInfoSize = rightInfo.size
        rightInfoIsBST = rightInfo.isBST

        info.maxVal = max(root.data, rightInfoMax)
        info.minVal = min(root.data, leftInfoMin)
        info.isBST = leftInfoIsBST and rightInfoIsBST and root.data > leftInfoMax and root.data < rightInfoMin
        info.size = leftInfoSize + rightInfoSize + 1
        
        if(info.isBST):
            maxSize[0] = max(maxSize[0], leftInfoSize + rightInfoSize + 1)
        
        return info
        
    
        
    

#For missing child provide None 
arr = [7, 4, 6, None, 9]
root = insertLevelOrder(arr, 0, len(arr))
sol = Solution()
dll = sol.largestBst(root)
print(dll)
