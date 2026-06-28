class Solution:
    def FindLL(self,head,key):
        current = head
        while current:
            
            if key == current.data:
                return True
            
            current = current.next
            
        return False
                
