# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def helper(root):
            if not root:
                return [True, 0]
            leftHeight = helper(root.left)
            rightHeight = helper(root.right)
            diff = leftHeight[1] - rightHeight[1]
            balanced = (leftHeight[0] and rightHeight[0]) and abs(diff) <= 1
            return [balanced, 1 + max(leftHeight[1], rightHeight[1])]
        return helper(root)[0]
    