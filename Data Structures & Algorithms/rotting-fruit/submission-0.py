class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        fresh = 0 
        queue = deque() 
        ROWS = len(grid)
        COLS = len(grid[0])

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    fresh += 1 

                elif grid[row][col] == 2:
                    queue.append((row, col))

        time = 0
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        while fresh > 0 and queue:
            for _ in range(len(queue)):
                row, col = queue.popleft()

                for dr, dc in directions:
                    newRow = row + dr 
                    newCol = col + dc 

                    # check if in bounds 
                    if newRow in range(ROWS) and newCol in range(COLS) and grid[newRow][newCol] == 1:
                        grid[newRow][newCol] = 2 
                        fresh -= 1 
                        queue.append((newRow, newCol))

            time += 1

        return time if fresh == 0 else -1
        