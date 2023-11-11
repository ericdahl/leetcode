class Solution:
    def balancedStringSplit(self, s: str) -> int:

        count = 0
        d = 0
        for c in s:
            if c == 'R': d += 1
            if c == 'L': d -= 1

            if d == 0:
                count += 1

        return count