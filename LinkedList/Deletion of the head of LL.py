class Solution:
    def Deletion(self,node):
        node.val = node.next.val
        node.next = node.next.next
