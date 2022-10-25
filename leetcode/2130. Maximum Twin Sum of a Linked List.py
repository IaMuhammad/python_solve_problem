from leetcode.linkedlist import ListNode, list_to_ll


def pairSum(head: ListNode) -> int:
    l = 0
    arr = []
    while head:
        arr.append(head.val)
        l += 1
        head = head.next
    s = arr[0] + arr[-1]
    r = l-2
    for i in range(1, l//2):
        if arr[i] + arr[r] > s:
            s = arr[i] + arr[r]
        r -= 1
    return s
l = 6
# ll = list_to_ll([5,4,2,1])
# ll = list_to_ll([79,90,23,26,68,5])
ll = list_to_ll([47,22,81,46,94,95,90,22,55,91,6,83,49,65,10,32,41,26,83,99,14,85,42,99,89,69,30,92,32,74,9,81,5,9])
print(pairSum(ll))

