from leetcode.linkedlist import ListNode, list_to_ll


def mergeNodes(head: ListNode) -> ListNode:
    res = ListNode(0)
    tmp_res = res
    tmp = head
    s = 0
    tmp = tmp.next
    while tmp:
        if tmp.val == 0:
            tmp_res.next = ListNode(s)
            tmp_res = tmp_res.next
            s = 0
        else:
            s += tmp.val
        tmp = tmp.next
    return res.next

ll = list_to_ll([0,3,1,0,4,5,2,0])
print(mergeNodes(ll))