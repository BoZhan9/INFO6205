# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.is_balanced = True
    def isBalanced(self, root: TreeNode) -> bool:
        self.helper(root)
        return self.is_balanced
    
    def helper(self, root):
        if root is None:
            return 0
        
        left = self.helper(root.left)
        right = self.helper(root.right)
        
        if (abs(left - right) > 1):
            self.is_balanced = False
        
        return max(left, right) + 1