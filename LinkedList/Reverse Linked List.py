class Node:
    def __init__(self,val=0,next = None):
        self.val = val
        self.next = next

    def Reverse(self,head):
        prev = none
        current = head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = new_node

        return prev
