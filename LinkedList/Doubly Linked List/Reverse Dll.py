def Reverse(head):
    if head is None or head.next is None:
        return head
    current = head
    temp = None
    while current:
        temp = current.prev
        current.prev = current.next
        current.next = temp

        current = current.prev
    head = temp.prev
    return head

first = Node(1)
second = Node(2)
third = Node(3)


first.next = second
second.prev = first

second.next = third
third.prev = second

head = first
current = head
print(" before reverse :",end = "")
while current:
    
    print(current.data,end = " ")
    current = current.next

head = Reverse(head)

current = head
print("\n after reverse :",end = "")
while current:
    
    print(current.data, end = " ")
    current = current.next
