class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:

        nums.sort()
        count = 0
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if abs(nums[i] - nums[j]) == k:
                    count += 1
                elif abs(nums[i] - nums[j]) > k:
                    break

        return count