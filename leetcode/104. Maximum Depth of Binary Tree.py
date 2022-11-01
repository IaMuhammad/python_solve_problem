def maxDepth(self, root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    return max(maxDepth(root.right), maxDepth(root.left)) + 1

