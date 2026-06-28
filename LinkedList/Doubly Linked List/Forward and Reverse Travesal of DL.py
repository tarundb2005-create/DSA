class Node:
    def __init__(self,data):
        self.prev = None
        self.data = data
        self.next = None

first = Node(10)
second = Node(20)
third = Node(30)

second.prev = first
first.next = second

third.prev = second
second.next = third

head = first

current = head

print("forward Travesal:")
while current:
    print(current.data,end = " ")
    current = current.next

current = head



print("\nBackward Travesal:")
while current.next:
    current = current.next
while current:
    print(current.data, end = " ")
    current = current.prev
