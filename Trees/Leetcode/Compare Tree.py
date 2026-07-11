class TreeNode:
    def __init__(self,val = 0,left = None,right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def comparee(self,p,q):
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        if p.val != q.val:
            return False
        left = self.comparee(p.left , q.left)
        right = self.comparee(p.right , q.right)
        return left and right
#   p               q

#   5               5
#  /               /
#10              10

        
p = TreeNode(5)
q = TreeNode(5)
q.left = TreeNode(10)
p.left = TreeNode(10)


a = Solution()
print(a.comparee(p,q))
