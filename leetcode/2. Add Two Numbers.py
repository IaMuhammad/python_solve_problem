from leetcode.linkedlist import ListNode, list_to_ll


def addTwoNumbers(l1: ListNode, l2: ListNode):
    a = b = ''
    while l1:
        a += str(l1.val)
        l1 = l1.next

    while l2:
        b += str(l2.val)
        l2 = l2.next

    a = str(int(a[::-1]) + int(b[::-1]))[::-1]
    i, l = 0, len(a)
    res = ListNode(0)
    tmp = res
    while i < l:
        tmp.next = ListNode(a[i])
        tmp = tmp.next
        i += 1

    return res.next
print(addTwoNumbers(list_to_ll([2,4,3,5]), list_to_ll([5,6,4])))