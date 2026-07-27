class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def dfs(row, col):
            if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]) or grid[row][col] == "0":
                return 0

            grid[row][col] = "0"
            dfs(row - 1, col)
            dfs(row + 1, col)
            dfs(row, col - 1)
            dfs(row, col + 1)

        numIslands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                print(grid[i][j])
                if grid[i][j] != "0":
                    numIslands += 1
                    dfs(i, j)
    
            
        return numIslands
        