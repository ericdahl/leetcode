class Solution:

    @staticmethod
    def calc_primes(limit):

        canidates = [True] * limit
        canidates[0] = False
        canidates[1] = False

        for i in range(2, int(math.sqrt(limit))):
            for j in range(i + i, limit, i):
                canidates[j] = False

        return [index for index, p in enumerate(canidates) if canidates[index]]


    def countPrimeSetBits(self, left: int, right: int) -> int:

        primes = Solution.calc_primes(50)

        count = 0

        # probably much faster to do this smarter with bit logic
        for i in range(left, right + 1):
            bstr = bin(i)[2:]
            set_bits = collections.Counter(bstr)['1']

            if set_bits in primes:
                count += 1

        return count