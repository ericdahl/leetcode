class Solution:

    @staticmethod
    def is_strict_increasing(nums: List[int]) -> (bool, int):
        last = -1
        for idx, n in enumerate(nums):
            if n <= last:
                if idx + 1 < len(nums) and last > nums[idx + 1]:
                    return (False, idx - 1)

                if idx - 1 >= 0 and idx + 1 < len(nums) and nums[idx - 1] == nums[idx + 1]:
                    return (False, idx - 1)
                return (False, idx)
            last = n
        return (True, None)


    def canBeIncreasing(self, nums: List[int]) -> bool:
        
        (is_strict, idx) = Solution.is_strict_increasing(nums)

        if is_strict:
            return True
        
        del nums[idx]

        return Solution.is_strict_increasing(nums)[0]

