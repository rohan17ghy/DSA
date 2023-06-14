#Approach1: Better soln
"""
 1. Find the inorder of both BST's
 2. Merge both the arrays
 3. Convert the inorder to BST
"""
#TC: O(N + M) SC: O(N + M)



#Approach2: Optimized soln
"""
 1. Convert both BST into sorted LL's
 2. Merge 2 sorted LL
 3. Convert the sorted LL's to BST
 """
#TC: O(N + M) SC:O(h1 + h2) --> height of the bst's
class TreeNode:
    def __init__(self, data) :
        self.data = data
        self.left = None
        self.right = None

    def __del__(self):
        if self.left:
            del self.left
        if self.right:
            del self.right

def mergeBST(root1, root2):
	# Write your code here.
    head1 = [None]
    head2 = [None]
    convertBSTToDLL(root1, head1)
    convertBSTToDLL(root2, head2)
    
    head = mergeTwoDLL(head1[0], head2[0])
    n = countNodes(head)
    return convertDLLToBalancedBST([head], n)
    
def mergeTwoDLL(root1, root2):    
    ptr1 = root1
    ptr2 = root2
    if(ptr2.data < ptr1.data):
        ptr1 = root2
        ptr2 = root1
    ans = ptr1
    while(ptr1.right != None and ptr2 != None):
        if(ptr1.right.data > ptr2.data):
            next1 = ptr1.right
            next2 = ptr2.right
            ptr1.right = ptr2
            ptr2.left = ptr1
            ptr2.right = next1
            next1.left = ptr2
            
            ptr1 = ptr1.right
            ptr2 = next2
        else:
            ptr1 = ptr1.right
    
    if(ptr1.right == None):
        ptr1.right = ptr2
        if(ptr2):
            ptr2.left = ptr1
    return ans

def countNodes(head):
    count = 0
    while(head != None):
        count += 1
        head = head.right
    return count

def convertDLLToBalancedBST(head, n):
    if(head == None or n == 0):
        return None
    
    left = convertDLLToBalancedBST(head, n//2)
    root = head[0]
    root.left = left
    head[0] = head[0].right
    root.right = convertDLLToBalancedBST(head, n-n//2-1)
    
    return root
    
        
def convertBSTToDLL(root, head):
    if(root == None):
        return

    convertBSTToDLL(root.right, head)
    root.right = head[0]
    if(head[0] != None):
        head[0].left = root
    head[0] = root
    convertBSTToDLL(root.left, head)


def createBST(values):
    root = None
    for value in values:
        root = insertIntoBST(root, value)
    return root  

def insertIntoBST(root, val):
    if(root == None):
        return TreeNode(val)

    if(val > root.data):
        root.right = insertIntoBST(root.right, val)
    else:
        root.left = insertIntoBST(root.left, val)
    return root   

def levelOrderTraversal(root):
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
        print(node.data, end=" ")
        queue.put(node.left) if node.left != None else queue.put('None')
        queue.put(node.right) if node.right != None else queue.put('None')     

arr1 = [4, 2, 7, 3]
arr2 = [5, 1, 7]
root1 = createBST(arr1) 
root2 = createBST(arr2)

root = mergeBST(root1, root2)

levelOrderTraversal(root)



    
    
    