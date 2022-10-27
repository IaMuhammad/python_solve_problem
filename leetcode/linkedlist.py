class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def length(self):
        tmp = self
        l = 0
        while tmp:
            l += 1
            tmp = tmp.next
        return l

    def __repr__(self):
        # return f'{self.val}'
        return f'{self.val}->{self.next}'

def print_ll(head):
    tmp = head
    while tmp:
        print(tmp.val, end=' ')
        tmp = tmp.next
    return

def list_to_ll(arr: list):
    head = ListNode(0)
    tmp = head

    for i in arr:
        tmp.next = ListNode(i)
        tmp = tmp.next

    return head.next

head = list_to_ll([1,2,3,4,5])
tmp = head
tmp.next = tmp.next.next
print()