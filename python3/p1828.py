class Solution:

    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        
        for c in queries:
            c.append(0) # add 4th item to keep track of # of matches
            for p in points:
                if (c[0] - p[0])**2 + (c[1] - p[1])**2 <= c[2]**2:
                    c[3] += 1

        return [c[3] for c in queries]
