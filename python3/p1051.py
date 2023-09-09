class Solution:

    def heightCheckerMinified(self, heights: List[int]) -> int:
        return sum([1 for i in map(operator.sub, heights, sorted(heights)) if i != 0])

    def heightChecker(self, heights: List[int]) -> int:

        sorted_heights = sorted(heights)

        count = 0
        for i in range(len(heights)):
            if sorted_heights[i] - heights[i] != 0:
                count += 1
        return count


