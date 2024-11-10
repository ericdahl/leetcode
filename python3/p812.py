class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:

        def triangle_area(x1, y1, x2, y2, x3, y3):
            area = 0.5 * abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))
            return area

        max_area = 0
        for t in itertools.combinations(points, 3):
            max_area = max(max_area, triangle_area(t[0][0], t[0][1], t[1][0], t[1][1], t[2][0], t[2][1]))

        return max_area