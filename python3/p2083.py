class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        count = 0
        for (a, b) in permutations(nums, 2):
            if a + b == target:
                count += 1

        return count