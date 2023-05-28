class Solution:
    def addDigits(self, num: int) -> int:
        while num >= 10:
            num = sum([int(c) for c in str(num)])

        return num
