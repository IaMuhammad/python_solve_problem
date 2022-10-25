from linkedlist import *


def deleteDuplicates(head: ListNode):
    l = head
    r = head.next

    while l and r.next:
        if l.val != r.val:
            l.next = r
            l = l.next
        r = r.next
    if r and l.val == r.val:
        l.next = None
    elif r:
        l.next = r
    return head

ll = list_to_ll([1,1,2,2,3,3])
print(deleteDuplicates(ll))