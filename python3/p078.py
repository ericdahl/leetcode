class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        results = [[]]

        for n in nums:
            results.extend([r + [n] for r in results])

        return results