class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS = len(board)
        COLS = len(board[0]) 


        def capture(row, col):
            if row < 0 or row == ROWS or col < 0 or col == COLS or board[row][col] != 'O':
                return 

            print(f"capturing ({row}, {col})")

            board[row][col] = '#' 

            capture(row + 1, col)
            capture(row - 1, col)
            capture(row, col + 1)
            capture(row, col - 1)

        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == "O" and (row in [0, ROWS - 1] or col in [0, COLS - 1]):
                    capture(row, col) 

        print("board after capturing", board)
        
        for row in range(ROWS):
            for col in range(COLS): 
                if board[row][col] == "O":
                    board[row][col] = "X"

        for row in range(ROWS):
            for col in range(COLS): 
                if board[row][col] == "#":
                    board[row][col] = "O"

        

        