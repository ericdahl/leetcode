class Solution:

    @staticmethod
    def rev(n: int) -> int:
        return int(str(n)[::-1])

    def countNicePairs(self, nums: List[int]) -> int:

        rev_diffs = Counter(n - Solution.rev(n) for n in nums)

        count = 0
        for diff_count in rev_diffs.values():
            # count += sum(range(0, diff_count))
            count += diff_count * (diff_count - 1) // 2

        return count % (10**9 + 7)

