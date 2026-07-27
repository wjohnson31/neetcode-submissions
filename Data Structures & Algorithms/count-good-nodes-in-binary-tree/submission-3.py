# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(curr, maxVal):
            if not curr:
                return 0
            res = 1 if curr.val >= maxVal else 0
            maxVal = max(curr.val, maxVal)
            left = dfs(curr.left, maxVal)
            right = dfs(curr.right, maxVal)
            res += left
            res += right
            return res
        return dfs(root, root.val)

