class Node:
    def LenLL(self,data):
        count = 0
        current = head

        while current:
            count += 1
            current = current.next
        return count
