class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums.sort()
        min_avg = 10**5
        l = len(nums)
        for i in range(l // 2):
            min_avg = min(min_avg, (nums[i] + nums[l - i - 1]) / 2)

        return min_avg
