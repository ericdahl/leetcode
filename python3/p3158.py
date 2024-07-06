class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        result = 0

        for (value, count) in Counter(nums).most_common():
            if count != 2:
                break
            result ^= value
        return result