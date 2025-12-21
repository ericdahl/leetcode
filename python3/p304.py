class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows = len(matrix)
        cols = len(matrix[0])

        # prefix[i][j] = sum of rectangle from (0,0) to (i-1,j-1)
        self.prefix = [[0] * (cols + 1) for _ in range(rows + 1)]

        for r in range(1, rows + 1):
            for c in range(1, cols + 1):
                self.prefix[r][c] = (
                        matrix[r-1][c-1] +           # current cell
                        self.prefix[r-1][c] +         # sum above
                        self.prefix[r][c-1] -         # sum to left
                        self.prefix[r-1][c-1]         # subtract overlap
                )


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        s = self.prefix[row2+1][col2+1]  # bottom right
        s -= self.prefix[row1][col2 + 1] # subtract above
        s -= self.prefix[row2+1][col1]   # subtract left
        s += self.prefix[row1][col1]     # add overlap

        return s

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)