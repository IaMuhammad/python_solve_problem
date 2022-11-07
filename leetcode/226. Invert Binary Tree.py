from leetcode.treenode import TreeNode
from binarytree import build, Node


def invertTree(root: Node) -> Node:
    if not root:
        return
    invertTree(root.left)
    if root.left and root.right:
        root.left, root.right = root.right, root.left
    elif root.left:
        root.right = root.left
        root.left = None
    else:
        root.left = root.right
        root.right = None
    invertTree(root.left)
    return root

root = build([4,2,7,1,3,6,9])
print(invertTree(root))