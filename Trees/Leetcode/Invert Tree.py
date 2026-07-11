class TreeNode:
    def __init__(self,val = 0,left = None,right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def Invert(self,root):
        if root is None:
            return None
        root.left , root.right = root.right , root.left
        self.Invert(root.left)
        self.Invert(root.right)
        return root
def preorder(root):
    if root is None:
        return

    print(root.val)
    preorder(root.left)
    preorder(root.right)

root = TreeNode(1)
root.right = TreeNode(2)
root.left = TreeNode(3)
root.right.left= TreeNode(4)
root.right.right = TreeNode(5)

a = Solution()

new_root = a.Invert(root)

preorder(new_root)
