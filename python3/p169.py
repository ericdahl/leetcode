class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c = collections.Counter(nums)
        return c.most_common(1)[0][0]