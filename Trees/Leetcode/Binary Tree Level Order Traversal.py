from collections import deque
class TreeNode:
    def __init__(self, val = 0 , left = None , right = None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def bfs(self,root):
        if root is None:
            return []
        queue = deque([root])
        result = []
        while queue:
            level_size = len(queue)
            level = []
            for _ in range(level_size):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level)
        return result        
root = TreeNode(99)
root.left = TreeNode(69)
root.right = TreeNode(18)
root.left.left =TreeNode(19)

a = Solution()
print(a.bfs(root))
