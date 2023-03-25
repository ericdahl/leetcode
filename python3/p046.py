class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        r = []

        for i in permutations(nums):
            r.append(i)

        return r