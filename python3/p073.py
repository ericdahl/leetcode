class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        zero_rows = set()
        zero_cols = set()

        for r in range(len(matrix)):
            for c in range(len(matrix[r])):
                if matrix[r][c] == 0:
                    zero_rows.add(r)
                    zero_cols.add(c)

        for zr in zero_rows:
            for c in range(len(matrix[0])):
                matrix[zr][c] = 0

        for zc in zero_cols:
            for r in range(len(matrix)):
                matrix[r][zc] = 0
