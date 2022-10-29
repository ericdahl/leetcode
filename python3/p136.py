class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        # O(n) space - violates O(1) requirement - trick is use xor instead
        c = collections.Counter(nums)

        return c.most_common()[-1][0]
