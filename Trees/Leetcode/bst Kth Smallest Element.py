class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root, k):
        count = 0
        ans =  None
        def helper(node):
            nonlocal count , ans
            if node is None:
                return
            helper(node.left)
            count += 1

            if count == k:
                ans = node.val
            helper(node.right)
        helper(root)
        return ans
