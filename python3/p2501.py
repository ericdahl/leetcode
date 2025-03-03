class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:

        snums = set(nums)
        longest = -1

        for n in nums:
            l = 1
            while n * n in snums:
                n = n * n
                l += 1
                longest = max(longest, l)

        return longest