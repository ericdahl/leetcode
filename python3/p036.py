class Solution:

    @staticmethod
    def is_valid(cells: List[str]) -> bool:
        cells_trimmed = [x for x in cells if x != "."]

        if len(set(cells_trimmed)) != len(cells_trimmed):
            return False
        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:

        box_cells = collections.defaultdict(list)

        for col_index in range(9):
            col = []
            for row_index in range(9):

                row = board[row_index]
                col.append(row[col_index])
                # organize the 3x3 grids in a dict, building a key
                # that's unique to the grid (key value itself doesn't matter)
                box_cells[col_index // 3 * 100 + row_index // 3].append(row[col_index])

                if not self.is_valid(row):
                    return False

            if not self.is_valid(col):
                return False

        for box in box_cells.values():
            if not self.is_valid(box):
                return False

        return True