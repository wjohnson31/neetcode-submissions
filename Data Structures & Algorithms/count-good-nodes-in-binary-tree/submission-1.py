# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0
        self.res = []
        def dfs(node, pathMax):
            if not node:
                return None
            if node.val >= pathMax:
                self.count += 1
                self.res.append(node.val)
            left = dfs(node.left, max(pathMax, node.val))
            right = dfs(node.right, max(pathMax, node.val))
            
        dfs(root, root.val)
        return self.count

