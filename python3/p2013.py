class DetectSquares:

    def __init__(self):
        self.pcounts = Counter()

    def add(self, point: List[int]) -> None:
        self.pcounts[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        px, py = point
        total = 0

        for (x, y), count in self.pcounts.items():
            if y == py:
                # skip anything which would be zero area (not a square)
                continue
            if x != px or y == py:
                continue

            d = abs(py - y)

            # left squares
            if (px - d, py) in self.pcounts and (px - d, y) in self.pcounts:
                total += count * self.pcounts[(px - d, py)] * self.pcounts[(px - d, y)]

            # right squares
            if (px + d, py) in self.pcounts and (px + d, y) in self.pcounts:
                total += count * self.pcounts[(px + d, py)] * self.pcounts[(px + d, y)]

        return total

