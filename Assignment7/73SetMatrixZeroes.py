class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rol = len(matrix)
        col = len(matrix[0])
        memo = []
        for m in range(0, rol):
            for n in range(0, col):
                if matrix[m][n] == 0:
                    memo.append((m,n))
        for (x,y) in memo:
            for i in range(0, col):
                matrix[x][i] = 0
            for i in range(0, rol):
                matrix[i][y] = 0
                    
        return matrix