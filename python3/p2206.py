class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        c = Counter(nums)
        return all(map(lambda x: x % 2 == 0, c.values()))
