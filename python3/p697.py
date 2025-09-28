class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:

        starts = {}
        ends = defaultdict(lambda: -1)
        for i, n in enumerate(nums):
            if n not in starts:
                starts[n] = i
            ends[n] = max(ends[n], i)

        most_freq = -1
        shortest = float('inf')
        for val, freq in Counter(nums).most_common():
            if freq < most_freq:
                return shortest
            most_freq = freq
            distance = ends[val] - starts[val] + 1
            shortest = min(distance, shortest)
        return shortest
