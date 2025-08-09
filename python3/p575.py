class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        limit = len(candyType) // 2

        c = Counter(candyType)

        return min(limit, len(c))