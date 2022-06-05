class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        count = 0
        for index, value in enumerate(nums):
            if value == val:
                nums[index] = 999
                count += 1

        nums.sort()
        return len(nums) - count
        