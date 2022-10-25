class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f'{self.val} {self.next}'

class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        # this method for print all value of linked list
        tmp = self.head
        while tmp:
            print(tmp.val)
            tmp = tmp.next

    def push(self, new_data):
        # this method is for adding value to the top of linked list
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def insert_after(self, prev_node, new_data):
        # this method is for adding value to after link of linked list
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def append(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
        else:
            last = self.head
            while last.next:
                last = last.next
            last.next = new_node

    def delete_node(self, key):
        tmp = self.head
        if tmp and tmp.val == key:
            self.head = tmp.next
            tmp = None
            return

        while tmp:
            if tmp.val == key:
                break
            prev = tmp
            tmp = tmp.next

        if tmp == None:
            return

        prev.next = tmp.next
        tmp = None
        pass

    def __repr__(self):
        return f'{self.head}'

llist = LinkedList()
dushanba = Node('Dushanba')
llist.head = dushanba

seshanba = Node('Sershanba')
dushanba.next = seshanba

chorshanba = Node('Chorshanba')
seshanba.next = chorshanba

payshanba = Node('Payshanba')
chorshanba.next = payshanba

llist.push('Yakshanba')

llist.insert_after(llist.head.next.next.next.next, 'Juma')
llist.append('Shanba')

llist.delete_node('Juma')
llist.print_list()