from typing import Optional

from leetcode.linkedlist import ListNode, list_to_ll


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        _ = 0
        answer = ListNode(0)
        _answer = answer
        while l1 and l2:
            _answer.next, _ = ListNode((l1.val + l2.val + _) % 10), (l1.val + l2.val + _) // 10
            _answer = _answer.next
            l1 = l1.next
            l2 = l2.next
        if l1:
            while l1:
                _answer.next, _ = ListNode((l1.val + _) % 10), (l1.val + _) // 10
                _answer = _answer.next
                l1 = l1.next
        elif l2:
            while l2:
                _answer.next, _ = ListNode((l2.val + _) % 10), (l2.val + _) // 10
                _answer = _answer.next
                l2 = l2.next
        if _:
            _answer.next = ListNode(_)

        return answer.next


ll1 = list_to_ll([9, 9, 9, 9, 9, 9, 9])
ll2 = list_to_ll([9, 9, 9, 9])
a = Solution()
print(a.addTwoNumbers(ll1, ll2))
