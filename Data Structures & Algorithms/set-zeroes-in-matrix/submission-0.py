class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:

        rows = set() 
        cols = set() 

        m = len(matrix)
        n = len(matrix[0])

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)


        for row in rows:
            for col in range(n):
                matrix[row][col] = 0 

        for row in range(m):
            for col in cols:
                matrix[row][col] = 0

                



        


       
        
        