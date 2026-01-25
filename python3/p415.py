class Solution:

    @staticmethod
    def atoi(num: str) -> int:
        result = 0
        multiplier = 1
        for c in reversed(num):
            c_i = ord(c) - ord('0')
            result += c_i * multiplier
            multiplier *= 10
        return result

    @staticmethod
    def itoa(num: int) -> str:
        if num == 0:
            return '0'

        l = deque()
        while num > 0:
            l.appendleft(chr(ord('0') + num % 10))
            num //= 10

        return ''.join(l)


    def addStrings(self, num1: str, num2: str) -> str:
        result_int = Solution.atoi(num1) + Solution.atoi(num2)
        return Solution.itoa(result_int)