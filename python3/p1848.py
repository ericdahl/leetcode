class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        matches = (e[0] for e in enumerate(nums) if e[1] == target)
        
        distances = [abs(i - start) for i in matches]
        distances.sort()
        return distances[0]
