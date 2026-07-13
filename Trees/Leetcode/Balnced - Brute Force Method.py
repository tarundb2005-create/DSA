class TreeNode:
    def __init__(self, val = 0 , left = None , right = None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    
    def maxDepth(self,root):
        if root is None:
            return 0
        left_height = self.maxDepth(root.left)
        right_height = self.maxDepth(root.right)
        
        return 1+max(left_height,right_height)




    def isBalanced(self,root):
        if root is None:
            return True

        left_height= self.maxDepth(root.left)
        right_height = self.maxDepth(root.right)

        if abs(right_height - left_height) > 1:
            return False
        left_a = self.isBalanced(root.left)
        right_a = self.isBalanced(root.right)

        return left_a and right_a


root = TreeNode(10)
root.left = TreeNode(20)
root.right = TreeNode(20)
root.left.left = TreeNode(30)
root.left.right = TreeNode(30)

a = Solution()

print(a.isBalanced(root))
