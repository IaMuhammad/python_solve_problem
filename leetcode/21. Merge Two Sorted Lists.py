from linkedlist import *


def mergeTwoLists(list1: ListNode, list2: ListNode):
    head = ListNode(0)
    res = head
    while list1 and list2:
        if list1.val <= list2.val:
            res.next = ListNode(list1.val)
            res = res.next
            list1 = list1.next
        else:
            res.next = ListNode(list2.val)
            res = res.next
            list2 = list2.next

    if list1:
        res.next = list1
    elif list2:
        res.next = list2
    return head.next

ll1 = list_to_ll([1,2,4])
ll2 = list_to_ll([1,3,5])
print(mergeTwoLists(ll1, ll2))