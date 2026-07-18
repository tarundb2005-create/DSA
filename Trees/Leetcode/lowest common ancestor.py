class TreeNode:
    def __init__(self,val = 0 , left = None , right = None):
        self.val = val
        self.right = right
        self.left = left
class Solution:
    def lowestCommonAncestor(self, root, p, q):
        if root is None:
            return None
        if root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left , p, q)
        right = self.lowestCommonAncestor(root.right , p, q)

        if left and right:
            return root
        return left if left else right


    
##                3
##              /   \
##             5     1
##            / \   / \
##           6   2 0   8
##              / \
##             7   4

root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(1)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)

p = root.left            # Node 5
q = root.left.right.right

a = Solution()
b = a.lowestCommonAncestor(root,p,q)
print(b.val)
