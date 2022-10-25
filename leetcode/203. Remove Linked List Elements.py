from linkedlist import ListNode, list_to_ll


def removeElements(head: ListNode, val: int) -> ListNode:
    tmp = head
    while tmp.next:
        if tmp.next.val == val:
            tmp.next = tmp.next.next
        else:
            tmp = tmp.next
    if head.val == val:
        return head.next
    return head
ll = list_to_ll([])
print(removeElements(ll, 6))