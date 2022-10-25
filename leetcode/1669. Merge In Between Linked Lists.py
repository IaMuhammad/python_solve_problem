from linkedlist import ListNode, list_to_ll


def mergeInBetween(list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
    tmp1_l1 = list1
    tmp2_l1 = list1
    tmp1_l2 = list2

    i = 0
    while i <= b:
        tmp1_l1 = tmp1_l1.next
        i += 1

    while tmp1_l2.next:
        tmp1_l2 = tmp1_l2.next
    tmp1_l2.next = tmp1_l1

    i = 0
    while i < a-1:
        tmp2_l1 = tmp2_l1.next
        i += 1

    tmp2_l1.next = list2
    return list1


ll1 = list_to_ll([0,1,2,3,4,5])
a, b = 3, 4
ll2 = list_to_ll([1000000,1000001,1000002])
print(mergeInBetween(ll1, a, b, ll2))