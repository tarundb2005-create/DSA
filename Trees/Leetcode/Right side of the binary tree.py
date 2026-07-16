from collections import deque
class TreeNode:
    def __init__(self,val = 0, left = None,right = None):
        self.val = val
        self.left = left
        self.right = right
class Solutions:
    def balance(self,root):
        if root is None:
            return []
        result = []
        queue = deque([root])
        while queue:
            level_size= len(queue)
            level = []
            for _ in range(level_size):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                
            result.append(level[-1])
        return result
root = TreeNode(10)
root.left = TreeNode(20)
root.right = TreeNode(30)
root.left.left = TreeNode(40)
root.right.right = TreeNode(50)

a = Solutions()
print(a.balance(root))
