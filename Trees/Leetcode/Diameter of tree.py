class TreeNode:
    def __init__(self, val = 0 , left = None , right = None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def dfs(self,root):
        if root is None:
            return 0
        left = self.dfs(root.left)
        right = self.dfs(root.right)

        self.diameter = max(self.diameter , left + right)

        return 1 + max(left , right)

    def DiameterofTree(self,root):
        self.diameter = 0
        self.dfs(root)
        return self.diameter
root = TreeNode(99)
root.left = TreeNode(69)
root.right = TreeNode(18)

a = Solution()
print(a.DiameterofTree(root))
