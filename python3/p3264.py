class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:

        for i in range(k):
            # not the most efficient as it has to iterate twice, but simple
            m = min(nums)
            nums[nums.index(m)] *= multiplier

        return nums