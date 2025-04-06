class Solution:

    def search(self, nums: List[int], target: int) -> int:

        # def search_rec
        if nums[0] == target:
            return 0

        left = 0
        right = len(nums) - 1
        mid = (right - left) // 2

        while left + 1 <= right:
            if target == nums[mid]:
                return mid
            if target == nums[right]:
                return right
            delta = (right - left) // 2
            if delta == 0: return -1
            if target > nums[mid]:
                left = mid
                mid += delta
            else:
                right = mid
                mid -= delta

        return -1