# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        maxdepth = 0
        nodes = [(root, 0, False), (root, 0, True)]
        while nodes:
            node, depth, right = nodes.pop()
            if node:
                maxdepth = max(depth, maxdepth)
                nodes.append(
                    (node.right if right else node.left, depth + 1, not right))
                nodes.append((node.left if right else node.right, 1, right))
        return maxdepth
