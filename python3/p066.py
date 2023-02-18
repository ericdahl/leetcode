class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        val = int("".join([str(d) for d in digits]))
        val += 1
        return [int(c) for c in str(val)]