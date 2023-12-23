class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:

        total = 0
        for idx, i in enumerate(nums):
            # not very efficient at all but works for this
            if k == len([c for c in (str(bin(idx)))[2:] if c == '1']):
                total += i

        return total