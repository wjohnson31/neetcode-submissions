# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxD = 0
        def dfs(root):
            if not root:
                return 0
            height1 = dfs(root.left)
            height2 = dfs(root.right)

            self.maxD = max(self.maxD, height1 + height2)
            return 1 + max(height1, height2)
        dfs(root)
        return self.maxD
