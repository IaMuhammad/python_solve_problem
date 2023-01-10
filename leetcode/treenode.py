from queue import Queue


class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


    def depth(self):
        if not (self.left or self.right):
            return 1
        l = r = 0
        if self.left:
            l = self.left.depth() + 1
        if self.right:
            r = self.right.depth() + 1


        return max(l, r)

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

def depth(root):
    if not root:
        return 0
    return max(depth(root.left), depth(root.right)) + 1


def post_order(root):
    if not root:
        return
    post_order(root.left)
    post_order(root.right)
    print(root.val, end=' ')

# def is_balance(root: TreeNode):
#     if not root:
#         return
#     l = depth(root.left)
#     r = depth(root.right)
#     return abs(l-r) < 2

def find_root(root, n):
    if not root:
        return

    if root.val == n:
        return True
    elif root.val > n and root.left:
        return find_root(root.left, n)
    elif root.val < n and root.right:
        return find_root(root.right, n)
    else:
        return False

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

def is_same(root1: TreeNode, root2: TreeNode):
    if not root1 and not root2:
        return True
    if not (root1 and root2) or root1.val != root2.val:
        return False

    return is_same(root1.left, root2.left) and is_same(root1.right, root2.right)


def reverse_bst(root):
    if not root:
        return

    reverse_bst(root.left)
    reverse_bst(root.right)
    root.left, root.right = root.right, root.left

root = TreeNode(1)
for i in [2,3,4,5,6,7]:
    add(root,i)
print(reverse_bst(root))
print(reverse_bst(root))