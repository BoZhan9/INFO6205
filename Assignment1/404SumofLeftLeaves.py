# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if root is None:
            return 0
        
        sum = 0
        if root.left is not None:
            left = root.left
            if left.left is None and left.right is None:
                sum += left.val
            else:
                sum += self.sumOfLeftLeaves(left)
        
        if root.right is not None:
            right = root.right
            sum += self.sumOfLeftLeaves(right)
        
        return sum