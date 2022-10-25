from leetcode.linkedlist import ListNode, list_to_ll, print_ll


def deleteDuplicates(head: ListNode):
    if not head:
        return head
    l, r = head, head.next
    b = False
    if l.val == r.val:
        try:
            while l.val == r.next.val:
                r = r.next
        except:
            return head
        l.next = r.next
        r = r.next
        b = True

    while r.next:
        if l.next.val == r.next.val:
            while r.next and l.next.val == r.next.val:
                r = r.next
            l.next = r.next
            r = r.next

            if not r:
                break
        else:
            l = l.next
            r = r.next

    if b:
        return head.next
    return head


ll = list_to_ll([1,1,1])
print(deleteDuplicates(ll))