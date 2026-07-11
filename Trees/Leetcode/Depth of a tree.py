class TreeNode:
    def __init__(self,val = 0 , left = None , right = None):
        self.val = val
        self.right = right
        self.left = left
class Solution:
    def maxDepth(self,root):
        if root is None:
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return 1 + max(left,right)

# Create the tree
#        3
#       / \
#      9   20
#         /  \
#        15   7
#        /\
#       12 18
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.left.left = TreeNode(12)
root.right.left.right = TreeNode(18)
root.right.right = TreeNode(7)


a = Solution()
print(a.maxDepth(root))
