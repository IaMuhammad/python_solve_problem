from leetcode.treenode import TreeNode, add


class Solution:
    def __init__(self):
        self.tre = TreeNode()
    def add(self, root, val):
        if not root:
            return TreeNode(val)
        if root.val > val:
            root.left = self.add(root.left, val)
        else:
            root.right = self.add(root.right, val)
        return root

    def increasingBST(self, root: TreeNode) -> TreeNode:
        if not root:
            return
        self.increasingBST(root.left)
        self.add(self.tre, root.val)
        self.increasingBST(root.right)

        return self.tre.right



root = TreeNode(5)
l = [3,6,2,4,8,1,7,9]
for i in l:
    add(root, i)
a = Solution()
print(a.increasingBST(root))