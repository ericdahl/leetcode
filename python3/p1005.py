class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:

        nums.sort()

        # swap any negatives to positives
        if nums[i:= 0] < 0:

            while k > 0 and i < len(nums) and nums[i] < 0:
                nums[i] *= -1
                k -= 1
                i += 1

        nums.sort()

        # if k is even, just swap back to original value
        if k % 2 == 1:
            nums[0] *= -1

        return sum(nums)
