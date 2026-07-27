class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.res = False

        def backtrack(r, c, currStr):
            if self.res:
                return

            # 1) Use the current cell now
            ch = board[r][c]
            newStr = currStr + ch

            # 2) Prune if newStr isn't a prefix of word
            if not word.startswith(newStr):
                return

            # 3) If full match, done
            if newStr == word:
                self.res = True
                return

            # 4) Mark visited and explore neighbors
            board[r][c] = "#"
            for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < len(board) and 0 <= nc < len(board[0]) and board[nr][nc] != "#":
                    backtrack(nr, nc, newStr)
            board[r][c] = ch  # unmark

        for r in range(len(board)):
            for c in range(len(board[0])):
                backtrack(r, c, "")
                if self.res:
                    return True

        return self.res
