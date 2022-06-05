class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        for i, value in enumerate(nums):

            j = i + 1
            while j < len(nums) and nums[j] == value:
                nums[j] = 999
                j += 1

        nums.sort()
        return len(nums) - nums.count(999)

