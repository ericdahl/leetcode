class Solution:
    def numberOfChild(self, n: int, k: int) -> int:

        # if k is large enough simplify to starting point
        k %= (n - 1) * 2

        # passing right to left
        if k >= n:
            k %= (n - 1)
            return n - k - 1

        return k