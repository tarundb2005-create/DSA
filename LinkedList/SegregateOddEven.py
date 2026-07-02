class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
def OddEven(head):
    if head is None:
        return None

    oddstart = oddend = None
    evenstart = evenend = None

    current = head

    while current:
        if current.data % 2 ==0:
            if evenstart is None:
                evenstart = evenend = current
            else:
                evenend.next = current
                evenend = current
        else:
            if oddstart is None:
                oddstart = oddend = current
            else:
                oddend.next = current
                oddend = current

        current = current.next

    if evenstart is None or oddstart is None:
        return head
    oddend.next = evenstart
    evenend.next = None
    return oddstart
##creating a list
head = Node(10)
head.next = Node(15)
head.next.next = Node(20)
head.next.next.next = Node(25)
head.next.next.next.next = Node(30)


head = OddEven(head)
current = head
while current:
    print(current.data , end = " ")
    current = current.next
