# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        
        return self.get_min_depth(root)
    
    def get_min_depth(self, root):
        if root is None:
            return float('inf')
        if root.left is None and root.right is None:
            return 1
        
        return min(self.get_min_depth(root.left), self.get_min_depth(root.right)) + 1
        