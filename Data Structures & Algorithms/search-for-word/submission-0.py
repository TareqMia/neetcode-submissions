class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])

        if len(word) > rows * cols:
            return False 


        def backtrack(i, j, index):
            if i < 0 or j < 0 or i >= rows or j >= cols or board[i][j] != word[index]:
                return False 

            if index == len(word) - 1:
                return True 

            letter = board[i][j]
            board[i][j] = " " 

            found =  (backtrack(i + 1, j, index + 1) or backtrack(i - 1, j, index + 1) \
            or backtrack(i, j + 1, index + 1) or backtrack(i, j - 1, index + 1))

            board[i][j] = letter

            return found


        for row in range(rows):
            for col in range(cols):
                if backtrack(row, col, 0):
                    return True 

        return False 



        

        