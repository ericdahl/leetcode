class Solution:
    def divide(self, dividend: int, divisor: int) -> int:

        abs_dividend = abs(dividend)
        abs_divisor = abs(divisor)

        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1

        if abs_dividend == abs_divisor:
            if divisor < 0 and dividend > 0 or divisor > 0 and dividend < 0:
                return -1
            return 1

        if divisor == 1:
            return dividend

        if divisor == -1:
            return -1 * dividend

        result = 0
        while abs_dividend >= abs_divisor:
            n = abs_divisor
            multiple = 1
            while (n << 1) < abs_dividend:
                n <<= 1
                multiple <<= 1

            abs_dividend -= n
            result += multiple


        if divisor < 0 and dividend > 0 or divisor > 0 and dividend < 0:
            result *= -1

        return result
