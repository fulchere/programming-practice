# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        begin_node = node
        vals = []
        while True:
            vals.append(node.val)
            if node.next is not None:
                node = node.next
            else:
                break

        vals.pop(0)
        node = begin_node
        for val in vals:
            if node is not None and node.next is not None and node.next.next is None:
                node.next = None
                break
            node.val = val
            if node.next is not None:
                node = node.next
            else:
                break
