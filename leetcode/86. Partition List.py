from leetcode.linkedlist import list_to_ll
from linkedlist import ListNode


def partition(head: ListNode, x: int) -> ListNode:
    if not head:
        return head
    head = ListNode(x-1, head)
    ans = ListNode()
    temp_ans = ans
    temp = ListNode()
    temp.next = head
    while temp.next:
        if temp.next.val >= x:
            temp_ans.next = ListNode(temp.next.val)
            temp_ans = temp_ans.next
            temp.next = temp.next.next
        else:
            temp = temp.next
    temp.next = ans.next
    return head.next

ll = list_to_ll([2,1])
print(partition(ll, 2))