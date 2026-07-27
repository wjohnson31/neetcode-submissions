# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        from collections import deque
        res = []
        dq = deque()
        if root:
            dq.append(root)
        else:
            return []

        while dq:
            level = []
            length = len(dq)
            for i in range(length):
                node = dq.popleft()
                if node:
                    level.append(node.val)
                    if node.left:
                        dq.append(node.left)
                    if node.right:
                        dq.append(node.right)
            res.append(level)
        return res
