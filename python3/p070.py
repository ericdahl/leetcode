class Solution:
    def climbStairs(self, n: int) -> int:
        stairs = [0] * 46
        stairs[1] = 1
        stairs[2] = 2
        stairs[3] = 3

        for i in range(4, 46):
            stairs[i] = stairs[i - 1] + stairs[i - 2]

        return stairs[n]
