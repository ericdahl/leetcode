class Solution:
    def countPrimes(self, n: int) -> int:

        if n < 2: 
            return 0

        table = [True] * n
        table[0] = False
        table[1] = False

        for i in range(2, int(n ** 0.5) + 1):
            if not table[i]:
                continue

            for j in range(i + i, n, i):
                table[j] = False

        return table.count(True)

