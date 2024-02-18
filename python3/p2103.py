class Solution:
    def countPoints(self, rings: str) -> int:
        rods = [set() for i in range(10)]
        for i in range(0, len(rings), 2):
            rods[int(rings[i + 1])].add(rings[i])

        return len([r for r in rods if len(r) == 3])
