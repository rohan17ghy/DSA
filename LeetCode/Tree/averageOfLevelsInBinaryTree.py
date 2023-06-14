"""
Question
https://leetcode.com/problems/average-of-levels-in-binary-tree/
"""

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        total = []
        count = []
        """
        This is not actually a level order traversal but does our work of finding the average
        on each level
        """ 
        def levelOrderTraversal(node, level):
            if(node == None):
                return
            
            if(level >= len(total)):
                total.append(0)
                count.append(0)
                
            total[level] += node.val
            count[level] += 1
            
            levelOrderTraversal(node.left, level + 1)
            levelOrderTraversal(node.right, level + 1)
        
        levelOrderTraversal(root, 0)
                
        return [t/c for t, c in zip(total, count)]