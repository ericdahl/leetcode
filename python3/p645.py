class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:

        c = Counter(nums)
        duplicated = c.most_common()[0][0]

        missing = (set(range(1, len(nums) + 1)) - set(nums)).pop()

        return [duplicated, missing]
