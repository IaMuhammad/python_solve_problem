from linkedlist import ListNode, list_to_ll


def deleteMiddle(head: ListNode) -> ListNode:
    tmp = head
    l = 0
    while tmp:
        l += 1
        tmp = tmp.next
    tmp = head
    i = 0
    l = l // 2
    while i < l:
        tmp = tmp.next
        i += 1
    tmp.next = tmp.next.next
    print()

ll = list_to_ll([1,3,4,7,1,2,6])