class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        d = {}
        longest = 0

        for n in nums:
            if n in d:
                continue

            left = d.get(n - 1, 0)
            right = d.get(n + 1, 0)
            length = left + 1 + right

            d[n] = length
            d[n - left] = length
            d[n + right] = length

            longest = max(longest, length)

        return longest
