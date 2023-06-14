class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

node1, node2 = TreeNode(3), TreeNode(3)


tuple1, tuple2 = (3, node1), (3, node2)
print(tuple1 < tuple2)

print(node1 == node2)