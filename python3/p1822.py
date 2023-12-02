class Solution:
    def arraySign(self, nums: List[int]) -> int:
        product = functools.reduce(operator.mul, nums)
        if product > 0:
            return 1
        elif product < 0:
            return -1
        return 0