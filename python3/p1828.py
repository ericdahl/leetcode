class Solution:

    @staticmethod
    def distance(x1, y1, x2, y2):
        return ((x2 - x1)**2 + (y2 - y1)**2)**0.5

    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        
        for circle in queries:
            circle.append(0) # add 4th item to keep track of # of matches
            for point in points:
                if Solution.distance(circle[0], circle[1], point[0], point[1]) <= circle[2]:
                    circle[3] += 1

        return [c[3] for c in queries]
