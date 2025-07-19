class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_run = 0
        current_run = 0
        for n in nums:
            if n == 1:
                current_run += 1
                max_run = max(max_run, current_run)
            else:
                current_run = 0
        return max_run