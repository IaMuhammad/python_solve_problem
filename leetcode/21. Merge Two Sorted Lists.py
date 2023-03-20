from linkedlist import *


#
#
# def mergeTwoLists(list1: ListNode, list2: ListNode):
#     head = ListNode(0)
#     res = head
#     while list1 and list2:
#         if list1.val <= list2.val:
#             res.next = ListNode(list1.val)
#             res = res.next
#             list1 = list1.next
#         else:
#             res.next = ListNode(list2.val)
#             res = res.next
#             list2 = list2.next
#
#     if list1:
#         res.next = list1
#     elif list2:
#         res.next = list2
#     return head.next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 or not l2:
            return l1 or l2
        answer = l1
        t1, t2 = l1.next, l2.next
        while l1.next and l2.next:
            if l1.val >= l2.val:
                t1 = l1.next
                l1.next = l2
                l1 = l1.next
                l2 = t1
            else:
                l1 = l1.next

        return answer


ll1 = list_to_ll([1, 2, 4])
ll2 = list_to_ll([1, 3, 5])
a = Solution()
print(a.mergeTwoLists(ll1, ll2))
