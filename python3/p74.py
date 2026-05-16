class Solution:


    @staticmethod
    def is_in_array_bisect(nums: List[int], target: int) -> bool:
        if not nums:
            return False
        if len(nums) == 1:
            return nums[0] == target
        
        m = len(nums) // 2
        return Solution.is_in_array_bisect(nums[:m], target) or Solution.is_in_array_bisect(nums[m:], target)

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in reversed(matrix):
            if target < row[0]:
                continue

            if Solution.is_in_array_bisect(row, target):
                    return True

        return False
        
