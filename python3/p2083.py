class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        count = 0
        freq = Counter(nums)

        for prefix in nums:
            if target.startswith(prefix):
                suffix = target[len(prefix):]

                count += freq[suffix]

                if prefix == suffix:
                    count -= 1

        return count
