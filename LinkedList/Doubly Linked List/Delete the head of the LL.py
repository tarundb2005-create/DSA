class Node:
    def __init__(self,data):
        self.prev = None
        self.data = data
        self.next = None

def Delete(head):
    if head is None:
        return None
    if head.next is None:
        return None
    head = head.next
    head.prev = None
    return head


first = Node(10)
second = Node(20)
third = Node(30)


second.prev = first
first.next = second

third.prev = second
second.next = third

head = first
head = Delete(head)

current = head

while current:
    print(current.data,end = " ")
    current = current.next
    
