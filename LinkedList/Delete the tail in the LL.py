class Node:
    def __init__(self,data):
        self.prev = None
        self.data = data
        self.next = None

def DeleteTail(head):
    if head is None:
        return None
    if head.next is None:
        return None
    current = head
    while current.next:
        current = current.next

    current.prev.next = None
    return head

first = Node(10)
second = Node(20)
third = Node(30)

first.next = second
second.prev = first

second.next = third
third.prev = second

head = first

head = DeleteTail(head)



current = head

while current:
    print(current.data,end = " ")
    current = current.next
