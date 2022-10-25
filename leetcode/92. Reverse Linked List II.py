from linkedlist import ListNode, list_to_ll


def reverseBetween(head: ListNode, left: int, right: int):
    temp = head
    tmp1 = head
    i = 1

    while i < left-1:
        temp = temp.next
        tmp1 = tmp1.next
        i += 1
    temp = temp.next
    ext = ListNode(1000)

    ex = ext
    while i < right:
        ex.next = ListNode(temp.val)
        ex = ex.next
        temp = temp.next
        i += 1

    prev = None
    cur = ext
    while cur:
        tm = cur.next
        cur.next = prev
        prev = cur
        cur = tm
    while prev.val
    tmp1.next = prev
    while tmp1.next:
        tmp1 = tmp1.next
    tmp1.next = temp
    print()


ll = list_to_ll([1,2,3,4,5])
reverseBetween(ll, 2, 4)