class TreeNode:
    def __init__(self,val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
def inorder(root):
    if root is None:
        return
    
    inorder(root.left)
    inorder(root.right)
    print(root.val)

root = TreeNode(10)
root.left = TreeNode(5)
root.left.left = TreeNode(3)
root.left.right = TreeNode(7)
root.right = TreeNode(15)
root.right.right = TreeNode(20)
inorder(root)
