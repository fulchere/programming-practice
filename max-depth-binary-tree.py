# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            l = 0
        elif root and root.left is not None:
            l = self.maxDepth(root.left)+1
        else:
            l = 1

        if root is None:
            r = 0
        elif root.right is not None:
            r = self.maxDepth(root.right)+1
        else:
            r = 1
        return l if l > r else r
