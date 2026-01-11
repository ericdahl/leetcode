class NeighborSum:

    def __init__(self, grid: List[List[int]]):
        rows = len(grid)
        cols = len(grid[0])

        # extend grid with 0 on each side to simplify logic
        self.extended_grid = [[0] * (cols + 2)]
        for row in grid:
            self.extended_grid.append([0] + row + [0])
        self.extended_grid.append([0] * (cols + 2))

        self.coordinates = {}

        for r in range(rows):
            for c in range(cols):
                self.coordinates[grid[r][c]] = (r + 1, c + 1)


    def adjacentSum(self, value: int) -> int:
        (r, c) = self.coordinates[value]
        s = 0
        s += self.extended_grid[r - 1][c]
        s += self.extended_grid[r + 1][c]
        s += self.extended_grid[r][c - 1]
        s += self.extended_grid[r][c + 1]
        return s


    def diagonalSum(self, value: int) -> int:
        (r, c) = self.coordinates[value]
        s = 0
        s += self.extended_grid[r - 1][c - 1]
        s += self.extended_grid[r - 1][c + 1]
        s += self.extended_grid[r + 1][c + 1]
        s += self.extended_grid[r + 1][c - 1]
        return s



# Your NeighborSum object will be instantiated and called as such:
# obj = NeighborSum(grid)
# param_1 = obj.adjacentSum(value)
# param_2 = obj.diagonalSum(value)