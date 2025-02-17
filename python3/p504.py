class Solution:
    def convertToBase7(self, num: int) -> str:

        if num == 0:
            return "0"

        negative = num < 0
        num = abs(num)

        r = []
        while num:
            r.append(str(num % 7))
            num //= 7

        r_str = "".join(r[::-1])
        return "-" + r_str if negative else r_str

