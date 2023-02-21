class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        cols = set()
        rows = set()
        
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    cols.add(j)
                    rows.add(i)
                    
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if i in rows or j in cols:
                    matrix[i][j] = 0
        