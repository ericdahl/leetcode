class Spreadsheet:

    def __init__(self, rows: int):
        self.grid = defaultdict(int)

    def setCell(self, cell: str, value: int) -> None:
        self.grid[cell] = value
        
    def resetCell(self, cell: str) -> None:
        self.setCell(cell, 0)
        
    def _getCell(self, cell: str) -> int:
        return self.grid[cell]

    def _eval(self, expression: str) -> int:
        if expression[0].isalpha():
            return self._getCell(expression)
        return int(expression)

    def getValue(self, formula: str) -> int:
        left, right = formula[1:].split("+")
        return self._eval(left) + self._eval(right)


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)
