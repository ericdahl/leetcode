class Solution:

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        candidates.sort()
        min_c = candidates[0]
        results = []

        for r in range(1, target // min_c + 1):

            # trim down candidates to subset to skip unnecessary looping
            cs = [n for n in candidates if (r - 1) * min_c + n <= target]

            for c in combinations_with_replacement(cs, r):
                if sum(c) == target:
                    results.append(c)

        return results

