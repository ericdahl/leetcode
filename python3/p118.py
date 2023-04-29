class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        rows = [[1], [1,1]]
        for i in range(2, numRows):
            rows.append([1] * (i + 1))
            for j in range(1, i):
                rows[i][j] = rows[i - 1][j - 1] + rows[i - 1][j]


        return rows[:numRows]
