class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
def FL(head):
    if head is None:
        return None
    
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            count = 1
            temp = slow.next
            while slow != temp:
                count += 1
                temp = temp.next
            return count
    return 0
            

#creating the linked list

first = Node(10)
second = Node(20)
third = Node(30)
fourth = Node(40)


#linking the list

first.next = second
second.next = third
third.next = fourth
fourth.next = second

head = first

print(FL(head))
