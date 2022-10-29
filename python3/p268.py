class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        nums.sort()

        if nums[0] != 0:
            return 0

        for (i, j) in zip(nums, nums[1:]):
            if i + 1 != j:
                return i + 1

        return nums[-1] + 1