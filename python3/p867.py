class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:

        m_rows = len(matrix)
        m_cols = len(matrix[0])

        transposed_rows = m_cols
        transposed_cols = m_rows

        transposed = [[None] * transposed_cols for i in range(transposed_rows)]
        for r in range(transposed_rows):
            for c in range(transposed_cols):
                transposed[r][c] = matrix[c][r]

        return transposed