class Solution:

    @staticmethod
    def search(nums: List[int], left: int, right: int, target: int) -> int:
        middle = left + (right - left) // 2

        if middle == left:
            if nums[middle] >= target:
                return middle
            return middle + 1

        elif nums[middle] == target:
            return middle
        elif nums[middle] > target:
            return Solution.search(nums, left, middle, target)
        else:
            return Solution.search(nums, middle, right, target)



    def searchInsert(self, nums: List[int], target: int) -> int:
        return Solution.search(nums, 0, len(nums), target)
