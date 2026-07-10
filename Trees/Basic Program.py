#      10
#     /  \
#    5    15    to print the val
class TreeNode:
    def __init__(self,val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
def preorder(root):
    if root is None:
        return
    print(root.val)
    preorder(root.left)
    preorder(root.right)

root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
preorder(root)
