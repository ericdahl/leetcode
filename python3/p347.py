class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        c = collections.Counter(nums)
        return [pair[0] for pair in c.most_common(k)]
