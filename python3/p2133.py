class Solution:

    @staticmethod
    def is_valid(cells: List[str]) -> bool:
        if len(set(cells)) != len(cells):
            return False
        return True

    # note - re-used answer from p019 (sudoku validator)
    def checkValid(self, matrix: List[List[int]]) -> bool:

        for col_index in range(len(matrix)):
            col = []
            for row_index in range(len(matrix)):

                row = matrix[row_index]
                col.append(row[col_index])

                if not self.is_valid(row):
                    return False

            if not self.is_valid(col):
                return False

        return True