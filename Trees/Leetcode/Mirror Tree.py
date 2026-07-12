class TreeNode:
    def __init__(self,val = 0,left = None , right = None):
        self.val = val
        self.right = right
        self.left = left

class Solution:
    def isMirror(self,left,right):
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False
        if left.val != right.val:
            return False
        left_same = self.isMirror(left.left , right.right)
        right_same = self.isMirror(left.right , right.left)

        return  left_same and right_same

root = TreeNode(10)
root.left = TreeNode(20)
root.right = TreeNode(20)
root.left.left = TreeNode(30)
root.left.right = TreeNode(40)
root.right.left = TreeNode(40)
root.right.right = TreeNode(30)

a = Solution()
print(a.isMirror(root.left,root.right))
