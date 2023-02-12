class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        start = -1
        end = -1

        for i, n in enumerate(nums):
            if n == target:
                if start == -1:
                    start = i

                end = i
        return [start, end]