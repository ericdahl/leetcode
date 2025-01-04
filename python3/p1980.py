class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        all_set = set((itertools.product("01", repeat=len(nums[0]))))
        nums_set = set(tuple(n) for n in nums)

        return ''.join(next(iter(all_set - nums_set)))
