class Solution:
    def convert(self, s: str, numRows: int) -> str:

        if numRows == 1:
            return s

        grid = [ [ " " ] * 1000 for i in range(numRows) ]

        row = 0
        col = 0
        row_increment = 1
        col_increment = 0

        for c in s:
            # fell past end of rows
            if row >= numRows:
                row_increment = -1
                col_increment = 1

                row -= 2
                col += 1

            # fell up too high
            elif row < 0:
                row_increment = 1
                col_increment = 0

                row += 2
                col -= 1

            grid[row][col] = c
            row += row_increment
            col += col_increment


        s_list = []
        for row in grid:
            s_list += [c for c in row if c != " "]

        return "".join(s_list)