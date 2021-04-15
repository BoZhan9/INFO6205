class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # Goaal: (i, j) to (j, n-1-i) 
        length = len(matrix)
        
        # Step 1: (i, j) to (j, i)
        for i in range(length):
            for j in range(i + 1, length):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        # Step 2: (j, i) to (j, n-1-i), reverse the column        
        for i in range(length):
            for j in range(length // 2):
                matrix[i][j], matrix[i][length - 1 - j] = matrix[i][length - 1 - j], matrix[i][j]