from linkedlist import ListNode, list_to_ll

def swapNodes(head: ListNode, k: int):
    l = head
    r = head
    temp_r = head
    i = 1
    while i < k:
        l = l.next
        temp_r = temp_r.next
        i += 1

    while temp_r:
        temp_r = temp_r.next
        r = r.next

    l.val, r.val = r.val, l.val
    return head

ll = list_to_ll([1,2,3,4,5])
print(swapNodes(ll, 2))