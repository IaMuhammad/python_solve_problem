from linkedlist import ListNode, list_to_ll


def isPalindrome(head: ListNode):
    tmp = head
    l = 0
    while tmp:
        l += 1
        tmp = tmp.next

    i = 1
    sec = []
    tmp = head
    while i <= l // 2:
        sec.append(tmp.val)
        tmp = tmp.next
        i += 1
    if l & 1:
        tmp = tmp.next
    for i in sec[::-1]:
        if i != tmp.val:
            return False
        tmp = tmp.next
    return True
    print()
ll = list_to_ll([1,2,1])
print(isPalindrome(ll))