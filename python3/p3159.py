class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:

        occ = [i for i, n in enumerate(nums) if n == x]

        result = [-1] * len(queries)
        for i, q in enumerate(queries):
            if q <= len(occ):
                result[i] = occ[q - 1]

        return result
