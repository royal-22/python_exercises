    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        length = len(matrix)
        for r in range(length):
            for c in range(r): 
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]

        for r in matrix: 
            r.reverse()
