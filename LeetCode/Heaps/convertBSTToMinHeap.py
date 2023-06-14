"""
Question
https://www.codingninjas.com/codestudio/problems/convert-bst-to-min-heap_920498?leftPanelTab=1
"""

#Approach
"""
--> Find the inorder of BST, it will be a sorted list
--> Populate the BST with the sorted list but in preorder fashion
--> This would ensure the heap order property of heap
--> It is already given that the BST is a complete binary tree so the structure
of the tree wouldn't change
"""

def convertBST(root):
    inorder = []
    inorderTraversal(root, inorder)
    #print(inorder)
    populatePreorder(root, inorder, [0])
    
    return root

def inorderTraversal(root, ans):
    if(root == None):
        return
    
    inorderTraversal(root.left, ans)
    ans.append(root.data)
    inorderTraversal(root.right, ans)
    
def populatePreorder(root, preorder, index):
    if(root == None or index[0] >= len(preorder)):
        return
    
    root.data = preorder[index[0]]
    index[0] += 1
    populatePreorder(root.left, preorder, index)
    populatePreorder(root.right, preorder, index)