class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:

        a_area = (ax2 - ax1) * (ay2 - ay1)
        b_area = (bx2 - bx1) * (by2 - by1)

        left = max(ax1, bx1)
        right = min(ax2, bx2)
        bottom = max(ay1, by1)
        top = min(ay2, by2)

        overlap = 0
        if left < right and bottom < top:
            overlap = (right - left) * (top - bottom)

        return a_area + b_area - overlap