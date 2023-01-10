# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from leetcode.treenode import TreeNode


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        return is_same(p, q) or is_same(invert_bst(p), q)


def is_same(root1: TreeNode, root2: TreeNode):
    if not root1 and not root2:
        return True
    if not (root1 and root2) or root1.val != root2.val:
        return False

    return is_same(root1.left, root2.left) and is_same(root1.right, root2.right)


def invert_bst(root):
    if not root:
        return

    invert_bst(root.left)
    invert_bst(root.right)
    root.left, root.right = root.right, root.left
    return root
