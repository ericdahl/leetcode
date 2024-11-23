class Solution:
    def checkPerfectNumber(self, num: int) -> bool:

        s = 1
        sqrt_num = int(math.sqrt(num))

        for i in range(2, sqrt_num + 1):
            if num % i == 0:
                s += i + num // i

                if s > num:
                    return False

        # special case - for perfect squares, don't count it twice
        if sqrt_num * sqrt_num == num:
            s -= sqrt_num

        return s == num