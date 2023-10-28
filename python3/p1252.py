class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        matrix = [[0 for _ in range(n)] for _ in range (m)]

        for r, c in indices:
            for i in range(n):
                matrix[r][i] += 1

            for i in range(m):
                matrix[i][c] += 1

        total = 0
        for r in range(m):
            for c in range(n):
                total += matrix[r][c] % 2
        return total
