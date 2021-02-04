# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        m = {0:[]}

        def helper(node):        
            if node.left is None and node.right is None:
                m[0].append(node.val)
                return 0
            left, right = 0, 0
            if node.left is not None:
                left = helper(node.left)
            if node.right is not None:
                right = helper(node.right)

            maximun = max(left, right) + 1
            if maximun in m.keys():
                 m[maximun].append(node.val)
            else:
                temp = []
                temp.append(node.val)
                m[maximun] = temp               
            return maximun
        helper(root)
        arr = []
        for val in m.values():
            arr.append(val)
        return arr