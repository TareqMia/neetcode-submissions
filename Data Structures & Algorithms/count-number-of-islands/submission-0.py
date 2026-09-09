class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        if not grid:
            return 0 

        islands = 0 

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1':
                    islands += 1 
                    self.dfs(row, col, grid)


        return islands 


    def dfs(self, row, col, grid):

        # check if out of bounds 
        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[row]) or grid[row][col] == '0':
            return

        grid[row][col] = '0'
        self.dfs(row + 1, col, grid)
        self.dfs(row - 1, col, grid)
        self.dfs(row, col + 1, grid)
        self.dfs(row, col - 1, grid)


        