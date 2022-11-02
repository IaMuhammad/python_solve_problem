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

root = TreeNode(9)
l = [5,3, 1,2,8, 10,12, 7,13,14,15,16,17,6]
for i in l:
    add(root, i)

print(find_root(root, 18))
# print(root.depth())
# print(depth(root))