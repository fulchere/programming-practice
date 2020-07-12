class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


vals = []


def recur(nd):
    if nd is None:
        return
    recur(nd.left)
    vals.append(nd.val)
    recur(nd.right)


def kthSmallest(root: TreeNode, k: int) -> int:
    # preorder traversal
    recur(root)
    print(vals)
    return vals[k-1]


n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n4 = TreeNode(4)
n5 = TreeNode(5)

n4.left = n2
n4.right = n5
n2.left = n1
n2.right = n3

print(kthSmallest(n4, 5))
