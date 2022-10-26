from leetcode.linkedlist import ListNode, list_to_ll


def addTwoNumbers(l1: ListNode, l2: ListNode):
    a = b = ''
    while l1:
        a += str(l1.val)
        l1 = l1.next

    while l2:
        b += str(l2.val)
        l2 = l2.next
    a, b = int(a), int(b)
    a += b
    head = ListNode(0)
    tmp = head
    for i in str(a):
        tmp.next = ListNode(int(i))
        tmp = tmp.next

    return head.next


print(addTwoNumbers(list_to_ll([7, 2, 4, 3]), list_to_ll([5, 6, 4])))