class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        hashRow = defaultdict(set)
        hashCol = defaultdict(set)
        squares = defaultdict(set)
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if board[r][c] in hashRow[r] or board[r][c] in hashCol[c] or board[r][c] in squares[(r // 3), (c // 3)]:
                    return False

                hashCol[c].add(board[r][c])
                hashRow[r].add(board[r][c])
                squares[(r // 3), (c // 3)].add(board[r][c])
        return True
