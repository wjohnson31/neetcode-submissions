class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        def dfs(i, j):
            if i < 0 or i >= ROWS or j < 0 or j >= COLS or grid[i][j] == 0:
                return 0
            
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            grid[i][j] = 0
            area = 1
            for x, y in directions:
                area += dfs(i + x, j + y)
            return area

        maxValue = 0
        for i in range(ROWS):
            for j in range(COLS):
                maxValue = max(maxValue, dfs(i, j))
        return maxValue