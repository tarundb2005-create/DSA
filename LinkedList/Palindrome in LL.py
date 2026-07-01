class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def pali(head):
    if head is None:
        return None
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    temp = slow
    prev = None

    while temp:
        nxt = temp.next
        temp.next = prev
        prev = temp
        temp = nxt

    first = head
    second = prev

    while second:
        if first.data != second.data:
            return False
        first = first.next
        second = second.next
    return True

#creating a linked list

first = Node(10)
second = Node(20)
third = Node(30)
fourth = Node(20)
fifth = Node(10)

#link the list

first.next = second
second.next = third
third.next = fourth
fourth.next = fifth

head = first

print(pali(head))
