from leetcode.linkedlist import ListNode, list_to_ll


def swapPairs(head: ListNode):
    temp = head
    head = ListNode(0)
    head.next = temp
    temp = head
    while temp.next and temp.next.next:
        t = temp.next.next.next
        temp.next.val, temp.next.next.val = temp.next.next.val, temp.next.val
        temp = temp.next.next
    return head.next

def swapPairsChange(head: ListNode):
    if not head:
        return None

    temp = head
    l = temp
    r = temp.next
    while temp.next:
        dummy = temp.next.next
        r.next = l

    return head


ll = list_to_ll([1,2,3,4,5])
print(swapPairsChange(ll))
# print(swapPairs(ll))