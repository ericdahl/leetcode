class Solution:
    def countTriples(self, n: int) -> int:
        squares = set(i * i for i in range(1, n + 1))
        count = 0
        for a in range(1, n + 1):
            for b in range(a, n + 1):
                if a**2 + b**2 in squares:
                    count += 2
        return count
