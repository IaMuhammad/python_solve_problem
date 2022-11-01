from treenode import *


def rangeSumBST(root: TreeNode, low: int, high: int) -> int:
    ans = 0
    if not root:
        return 0

    if low <= root.value and root.value <= high:
        ans += root.value

    ans += rangeSumBST(root.left, low, high)
    ans += rangeSumBST(root.right, low, high)

    return ans

root = TreeNode(10)
l = [5,15,3,7,18]
for i in l:
    add(root, i)

print(rangeSumBST(root, 7, 15))
