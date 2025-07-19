class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_run = 0
        current_run = 0
        for n in nums:
            if n:
                current_run += 1
                if current_run > max_run:
                    max_run = current_run
            else:
                current_run = 0
        return max_run