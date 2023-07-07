class Solution:

    @staticmethod
    def is_valid(grid, row, col, num):
        for i in range(9):
            if grid[row][i] == num:
                return False

            if grid[i][col] == num:
                return False

        for r in range(row // 3 * 3, (row // 3 + 1) * 3):
            for c in range(col // 3 * 3, (col // 3 + 1) * 3):
                if grid[r][c] == num:
                    return False
        return True

    @staticmethod
    def solve(grid, row, col):

        if col == 9:
            # went past end of board; loop around
            row += 1
            col = 0

        if row > 8:
            # at end of board, finished
            return True

        if grid[row][col] != ".":
            # number already set; go to next cell
            return Solution.solve(grid, row, col + 1)

        for num in "123456789":

            if Solution.is_valid(grid, row, col, num):

                grid[row][col] = num

                # recurse to solve next cell
                if Solution.solve(grid, row, col + 1):
                    # board is finished
                    return True

            grid[row][col] = "."
        return False

    def solveSudoku(self, board: List[List[str]]) -> None:
        Solution.solve(board, 0, 0)
