from leetcode.linkedlist import ListNode


class MyHashSet:

    def __init__(self):
        self.head = ListNode()

    def add(self, key: int) -> None:
        tmp = self.head
        while tmp.next:
            tmp = tmp.next
        tmp.next = ListNode(key)

    def remove(self, key: int) -> None:
        tmp = self.head
        while tmp and tmp.val != key:
            tmp = tmp.next
        if tmp:
            if tmp.next:
                tmp.val = tmp.next.val
                tmp.next = tmp.next.next
            else:
                tmp = None

    def contains(self, key: int) -> bool:
        tmp = self.head
        while tmp.next:
            if tmp.val == key:
                return True
            tmp = tmp.next
        return False


a = MyHashSet()

k = ["contains", "remove", "add", "add", "contains", "remove", "contains", "contains", "add", "add", "add",
     "add", "remove", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "contains", "add",
     "contains",
     "add", "add", "contains", "add", "add", "remove", "add", "add", "add", "add", "add", "contains", "add", "add",
     "add",
     "remove", "contains", "add", "contains", "add", "add", "add", "add", "add", "contains", "remove", "remove", "add",
     "remove", "contains", "add", "remove", "add", "add", "add", "add", "contains", "contains", "add", "remove",
     "remove",
     "remove", "remove", "add", "add", "contains", "add", "add", "remove", "add", "add", "add", "add", "add", "add",
     "add",
     "add", "remove", "add", "remove", "remove", "add", "remove", "add", "remove", "add", "add", "add", "remove",
     "remove",
     "remove", "add", "contains", "add"]
v = [[72], [91], [48], [41], [96], [87], [48], [49], [84], [82], [24], [7], [56], [87], [81], [55], [19], [40],
     [68], [23], [80], [53], [76], [93], [95], [95], [67], [31], [80], [62], [73], [97], [33], [28], [62], [81], [57],
     [40], [11], [89], [28], [97], [86], [20], [5], [77], [52], [57], [88], [20], [48], [42], [86], [49], [62], [53],
     [43], [98], [32], [15], [42], [50], [19], [32], [67], [84], [60], [8], [85], [43], [59], [65], [40], [81], [55],
     [56], [54], [59], [78], [53], [0], [24], [7], [53], [33], [69], [86], [7], [1], [16], [58], [61], [34], [53], [84],
     [21], [58], [25], [45], [3]]
index = 0
for i in k:
    if i == 'add':
        a.add(v[i])
        i += 1
    elif i == 'remove':
        a.remove(v[i])
        i += 1
zz