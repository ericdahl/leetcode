class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:

        c = Counter(nums)

        count = 0
        for n in nums:
            count += c[n + k]
            count += c[n - k]

        return count // 2
