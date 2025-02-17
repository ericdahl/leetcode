class Solution:
    def convertToBase7(self, num: int) -> str:

        if num == 0:
            return "0"

        negative = num < 0
        num = abs(num)

        # [0,0,0,0,0,0,0,2,0,2]
        r = [num // (7 ** i) % 7 for i in range(9, -1, -1)]

        r = "".join((str(d) for d in r))
        r = r.lstrip("0")
        if negative:
            r = "-" + r
        return r
