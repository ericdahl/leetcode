class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:

        if not nums:
            return []

        ranges = []
        it = iter(nums) # avoids slice copy and no need of range index
        lower = next(it)
        last = lower

        for n in it:

            if n > last + 1:
                if lower == last:
                    ranges.append(str(lower))
                else:
                    ranges.append(f"{lower}->{last}")
                lower = n

            last = n

        if lower == nums[-1]:
            ranges.append(str(lower))
        else:
            ranges.append(f"{lower}->{nums[-1]}")

        return ranges