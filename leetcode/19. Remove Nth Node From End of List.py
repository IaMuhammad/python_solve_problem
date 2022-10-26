from linkedlist import  *


def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
    if not head.next:
        return None
    l = head
    head = l
    r = head
    i = 1
    while i <= n:
        r = r.next
        i += 1
    try:
        while r.next:
            l = l.next
            r = r.next
    except:
        return head.next


    l.next = l.next.next

    return head

ll = list_to_ll([1,2,3,4,5])
print(removeNthFromEnd(ll, 5))