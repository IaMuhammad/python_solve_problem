from leetcode.linkedlist import ListNode, list_to_ll


def oddEvenList(head:ListNode):
    tmp = head
    odd = ListNode(0)
    odd_t = odd
    even = ListNode(0)
    even_t = even
    c = 1
    while tmp:
        if c & 1:
            odd_t.next = ListNode(tmp.val)
            odd_t = odd_t.next
        else:
            even_t.next = ListNode(tmp.val)
            even_t = even_t.next
        c += 1
        tmp = tmp.next
    odd_t.next = even.next
    return odd.next

ll = list_to_ll([1,4,5,7,3])
print(oddEvenList(ll))