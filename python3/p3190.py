class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        return len([n for n in nums if n % 3 != 0])