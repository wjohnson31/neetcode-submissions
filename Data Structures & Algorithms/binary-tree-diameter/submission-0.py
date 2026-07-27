# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        def dfs(root):
            if not root:
                return (0, 0)
            leftHeight, leftD = dfs(root.left)
            rightHeight, rightD = dfs(root.right)  
            currD = leftHeight + rightHeight
            bestD = max(leftD, rightD, currD)
            return (1 + max(leftHeight, rightHeight), bestD)
        _, d = dfs(root)
        return d