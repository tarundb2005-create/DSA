class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    
n1 = Node(5)
n2 = Node(10)
n3 = Node(15)

n1.next = n2
n2.next = n3
n3.next = None

head = n1
new_node = Node(20)
new_node.next = head
head = new_node

current = head

while current:
    print(current.data)
    current = current.next
