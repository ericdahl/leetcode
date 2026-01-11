class NeighborSum:

    def __init__(self, grid: List[List[int]]):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.coordinates = {}

        for r in range(self.rows):
            for c in range(self.cols):
                self.coordinates[grid[r][c]] = (r,c)


    def adjacentSum(self, value: int) -> int:
        (r, c) = self.coordinates[value]
        s = 0
        if r > 0:
            s += self.grid[r - 1][c]
        if r < self.rows - 1:
            s += self.grid[r + 1][c]
        if c > 0:
            s += self.grid[r][c - 1]
        if c < self.cols - 1:
            s += self.grid[r][c + 1]
        return s



    def diagonalSum(self, value: int) -> int:
        (r, c) = self.coordinates[value]
        s = 0
        if r > 0 and c > 0:
            s += self.grid[r - 1][c - 1]
        if r > 0 and c < self.cols - 1:
            s += self.grid[r - 1][c + 1]
        if r < self.rows - 1 and c < self.cols - 1:
            s += self.grid[r + 1][c + 1]
        if r < self.rows - 1 and c > 0:
            s += self.grid[r + 1][c - 1]
        return s



# Your NeighborSum object will be instantiated and called as such:
# obj = NeighborSum(grid)
# param_1 = obj.adjacentSum(value)
# param_2 = obj.diagonalSum(value)