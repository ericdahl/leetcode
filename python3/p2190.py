class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        c = Counter([p[1] for p in pairwise(nums) if p[0] == key])
        return c.most_common(1)[0][0]
