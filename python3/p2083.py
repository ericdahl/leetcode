class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        count = 0
        target_len = len(target)
        nums_len = [(len(n), n) for n in nums]
        for ((a_len, a), (b_len, b)) in permutations(nums_len, 2):

            if a_len + b_len == target_len and a + b == target:
                count += 1

        return count