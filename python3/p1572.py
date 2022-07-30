class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:

        n = len(mat)

        diag_sum = 0

        secondary_i = n - 1
        for i in range(n):
            diag_sum += mat[i][i]

            if i != secondary_i:
                diag_sum += mat[i][secondary_i]

            secondary_i -= 1


        return diag_sum
