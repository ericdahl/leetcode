class Solution:


    def maximalSquare(self, matrix: List[List[str]]) -> int:

        rows, cols = len(matrix), len(matrix[0])
        curr_max = 0

        m = [[0] * cols for r in range(rows)]

        for r_i in range(rows):
            for c_i in range(cols):
                m[r_i][c_i] = int(matrix[r_i][c_i])

        for r_i in range(rows):
            for c_i in range(cols):
                if matrix[r_i][c_i] != "1":
                    continue

                (left, up, up_left) = (0, 0, 0)
                if c_i > 0: left = m[r_i][c_i - 1]
                if r_i > 0: up = m[r_i - 1][c_i]
                if r_i > 0 and c_i > 0: up_left = m[r_i - 1][c_i - 1]

                m[r_i][c_i] += min(up, left, up_left)
                curr_max = max(curr_max, m[r_i][c_i])

        return curr_max ** 2
