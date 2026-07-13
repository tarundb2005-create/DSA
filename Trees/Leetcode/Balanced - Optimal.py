class TreeNode:
    def __init__(self, val = 0 , left = None , right = None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self,root):
        if root is None:
            return 0
        left = self.maxDepth(root.left)
        if left == -1:
            return -1
        right = self.maxDepth(root.right)
        if right == -1:
            return -1
        if abs(left - right) > 1:
            return -1
        return 1 + max(left , right)
    def isBalanced(self,root):
        return self.maxDepth(root) != -1
            


root = TreeNode(10)
root.left = TreeNode(20)
root.right = TreeNode(20)
root.left.left = TreeNode(30)
root.left.right = TreeNode(30)

a = Solution()

print(a.isBalanced(root))
