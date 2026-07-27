class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r, c = len(matrix), len(matrix[0])
        top, bot = 0, r - 1
        while top <= bot:
            curr = (top + bot) // 2
            if target > matrix[curr][-1]:
                top = curr + 1
            if target < matrix[curr][0]:
                bot = curr - 1
            else:
                break
        if not (top <= bot):
            return False
        row = (top + bot) // 2
        l, r = 0, c - 1
        while l <= r:
            m = (l + r) // 2
            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m - 1
            else:
                return True
        return False