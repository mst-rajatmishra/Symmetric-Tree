# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # Helper function to check if two trees are mirror images of each other
        def isMirror(tree1: Optional[TreeNode], tree2: Optional[TreeNode]) -> bool:
            if not tree1 and not tree2:
                return True
            if not tree1 or not tree2:
                return False
            return (tree1.val == tree2.val and 
                    isMirror(tree1.left, tree2.right) and 
                    isMirror(tree1.right, tree2.left))
        
        # Initial call to the helper function
        return isMirror(root, root)

# Example usage
solution = Solution()
root1 = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(2, TreeNode(4), TreeNode(3)))
print(solution.isSymmetric(root1))  # Output: True

root2 = TreeNode(1, TreeNode(2, None, TreeNode(3)), TreeNode(2, None, TreeNode(3)))
print(solution.isSymmetric(root2))  # Output: False
