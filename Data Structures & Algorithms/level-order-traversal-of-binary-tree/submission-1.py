# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        from collections import deque
        d = deque()
        d.append(root)
        while d:
            level = []
            currLength = len(d)
            for i in range(currLength):
                node = d.popleft()
                if node:
                    level.append(node.val)
                    d.append(node.left)
                    d.append(node.right)
            if level:
                res.append(level)
        return res

