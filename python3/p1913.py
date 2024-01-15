class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:

        e_nums = sorted(enumerate(nums), key=lambda x: x[1])
        return e_nums[-1][1] * e_nums[-2][1] - e_nums[0][1] * e_nums[1][1]

