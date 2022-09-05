class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        positions = defaultdict(list)

        for index, value in enumerate(nums):
            positions[value].append(index)

        for p in [l for l in positions.values() if len(l) >= 2]:

            for i in range(len(p)):
                for j in range(i + 1, len(p)):
                    if p[j] - p[i] <= k:
                        return True
        return False