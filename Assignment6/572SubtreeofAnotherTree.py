# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if s is None:
            return t is None
        
        if t is None:
            return False
        
        if s.val == t.val and self.helper(s, t):
            return True
        
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

    def helper(self, s, t):
        if s is None:
            return t is None
        
        if t is None:
            return False
        
        if s.val != t.val:
            return False
        
        return self.helper(s.left, t.left) and self.helper(s.right, t.right)
