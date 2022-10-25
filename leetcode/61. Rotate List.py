from linkedlist import *


def rotateRight(head: ListNode, k):
    tmp = head
    if not tmp:
        return head
    l = 1
    while tmp.next:
        l += 1
        tmp = tmp.next
    tmp.next = head
    k = k % l
    c = l - k - 1
    tmp = head
    while c:
        tmp = tmp.next
        c -= 1
    head = tmp.next
    tmp.next = None
    return head

ll = list_to_ll([1,2,3,4,5])

print(rotateRight(ll, 2))