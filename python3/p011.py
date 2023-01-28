class Solution:

    def maxArea(self, height: List[int]) -> int:

        left, right = (0, len(height) - 1)
        max_water = -1

        while left < right:
            water = min(height[left], height[right]) * (right - left)
            max_water = max(max_water, water)

            if height[left] > height[right]:
                right -= 1
            elif height[right] > height[left]:
                left += 1
            else:
                right -= 1
                left += 1

        return max_water

