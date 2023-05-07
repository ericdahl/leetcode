class Solution:
    def mySqrt(self, x: int) -> int:

        if x == 0:
            return 0

        if x <= 3:
            return 1

        i = 2
        lower = 2

        while True:
            sq = i * i

            if sq == x or (i + 1) * (i + 1) > x:
                return i

            if sq < x:
                i += 1