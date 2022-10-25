from linkedlist import ListNode, list_to_ll


def reverseList(head: ListNode):
    prev = None
    cur = head
    while cur:
        temp = cur.next
        cur.next = prev
        prev = cur
        cur = temp
    return prev

ll = list_to_ll([1,2,3,4,5])
print(reverseList(ll))