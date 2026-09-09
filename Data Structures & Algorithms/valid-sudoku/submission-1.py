class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        squares = [set() for _ in range(9)] 


        for i in range(9):
            for j in range(9):

                if board[i][j] == ".":
                    continue 

                if board[i][j] in rows[i]:
                    return False 
                rows[i].add(board[i][j]) 


                if board[i][j] in cols[j]:
                    return False 
                cols[j].add(board[i][j])

                index = (i // 3) * 3 + (j // 3)
                if board[i][j] in squares[index]:
                    return False 

                squares[index].add(board[i][j])

        return True

                
        