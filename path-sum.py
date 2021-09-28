# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rec(self, s, nd, targetSum):
        if nd is None:
            return 0
        else:
            s += nd.val
            if s == targetSum and nd.left is None and nd.right is None:
                return 1
            else:
                return 0 + self.rec(s, nd.left, targetSum) + self.rec(s, nd.right, targetSum)

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        return True if self.rec(0, root, targetSum) else False
