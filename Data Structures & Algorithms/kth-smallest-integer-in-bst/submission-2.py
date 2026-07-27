# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        inOrder = []

        def dfs(curr):
            if not curr:
                return None
            
            dfs(curr.left)
            inOrder.append(curr.val)
            dfs(curr.right)

            return curr
        dfs(root)
        for i in range(len(inOrder)):
            if k == i + 1:
                return inOrder[i]
