# works but too slow
# class Solution:
#     def countGoodNumbers(self, n: int) -> int:

#         if n == 1:
#             return 5
#         p = (4 * 5) ** (n // 2)
#         if n % 2 == 1:
#             p *= 5

#         return p % (10 ** 9 + 7)

class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7

        def fast_power(base, exponent):
            result = 1
            while exponent > 0:
                if exponent % 2 == 1:
                    result = (result * base) % MOD
                base = (base * base) % MOD
                exponent //= 2
            return result

        if n == 1:
            return 5

        p = fast_power(4 * 5, n // 2)

        if n % 2 == 1:
            p = (p * 5) % MOD

        return p

