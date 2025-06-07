class Solution:

    def __init__(self):
        self.s = set((n * n for n in range(100000)))

    def isPerfectSquare(self, num: int) -> bool:
        return num in self.s
