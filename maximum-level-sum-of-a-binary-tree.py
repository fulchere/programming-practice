# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        sums = []

        current_nodes = [root]
        while current_nodes:
            temp_sum = 0
            next_nodes = []

            for nd in current_nodes:
                temp_sum += nd.val
                if nd.left is not None:
                    next_nodes.append(nd.left)
                if nd.right is not None:
                    next_nodes.append(nd.right)

            current_nodes = next_nodes
            sums.append(temp_sum)

        return sums.index(max(sums)) + 1
