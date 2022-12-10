class Solution:

    def numSquares(self, n: int) -> int:

        squares = [n * n for n in range(int(n ** 0.5), 0, -1)]

        for length in count(1):
            for c in combinations_with_replacement(squares, length):
                if sum(c) == n:
                    return length
