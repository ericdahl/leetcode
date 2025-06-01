class Solution:

    def __init__(self):
        self.values = set((4 ** n for n in range(16)))

    def isPowerOfFour(self, n: int) -> bool:
        return n in self.values
