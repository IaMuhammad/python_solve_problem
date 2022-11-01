from leetcode.treenode import *

def inorderTraversal(root: TreeNode) -> list[int]:
    l = []
    if not root:
        return
    inorderTraversal(root.left)
    l.append(root.val)
    inorderTraversal(root.right)

    return l

root = TreeNode(1)
print(inorderTraversal(root))