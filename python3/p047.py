class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        result = set()

        for i in permutations(nums, len(nums)):
            result.add(i)

        return result