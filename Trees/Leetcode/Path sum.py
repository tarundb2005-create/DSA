class TreeNode:
    def __init__(self, val = 0 , left = None , right = None):
        self.val = val
        self.left = left
        self.right = right



class Solution:
    def hasPathSum(self,root,remaining):
        if root is None:
            return False
        remaining -= root.val
        if root.left is None and root.right is None:
            return remaining == 0
            
        left = self.hasPathSum(root.left , remaining)
        right = self.hasPathSum(root.right , remaining)

        return left or right

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

a = Solution()
print(a.hasPathSum(root,7))
