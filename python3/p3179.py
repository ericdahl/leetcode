class Solution:
    def valueAfterKSeconds(self, n: int, k: int) -> int:

        s = [1] * n
        for i in range(k):
            s = accumulate(s)

        s = list(s)
        return s[-1] % (10**9 + 7)