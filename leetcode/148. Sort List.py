from linkedlist import ListNode, list_to_ll


def length(head: ListNode):
    temp = head
    l = 0
    while temp:
        l += 1
        temp = temp.next
    return l

def sortList(head: ListNode):

    pass

ll = list_to_ll([1,2,3,4])
sortList(ll)