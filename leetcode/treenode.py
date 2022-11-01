class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

    def __str__(self) -> str:
        return f'{self.val}'


def add(root, n):
    if not root:
        return TreeNode(n)
    if root.val > n:
        root.left = add(root.left, n)
    else:
        root.right = add(root.right, n)
    return root


def pre_order(root):
    if not root:
        return
    print(root.val, end=' ')
    pre_order(root.left)
    pre_order(root.right)


def in_order(root):
    if not root:
        return
    in_order(root.left)
    print(root.val, end=' ')
    in_order(root.right)


def post_order(root):
    if not root:
        return
    post_order(root.left)
    post_order(root.right)
    print(root.val, end=' ')

def is_balance(root: TreeNode):
    if not root:
        return
    l = depth(root.left)
    r = depth(root.right)
    return abs(l-r) < 2

def depth(root):
    if not root:
        return 0
    return max(depth(root.right), depth(root.left)) + 1

def bfs_print(root):
    que = Queue()
    que.put(root)

    while not que.empty():
        node = que.get()
        print(node.val, end=' ')
        if node.left:
            que.put(node.left)
        if node.right:
            que.put(node.right)

root = TreeNode(19)
l = [14,12,15,13,10,21,19,24,28,25,26,23,33,30,35,34]
for i in l:
    add(root, i)
print('inorder: ', in_order(root))