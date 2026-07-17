class TreeNode:
    def __init__(self , val = 0 , left = None , right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root):
        def helper(node , low , high):
            if node is None:
                return True
            if not (low < node.val < high):
                return False
            left = helper(node.left , low , node.val)
            right = helper(node.right , node.val , high)
            return left and right
        return helper(root , float("-inf") , float("inf"))
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)

a = Solution()
print(a.isValidBST(root))
