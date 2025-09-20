class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:

        rows, cols = len(matrix), len(matrix[0])

        for c in range(1, cols):
            for r in range(1, rows):
                if matrix[r][c] != matrix[r - 1][c - 1]:
                    return False

        return True

