class Solution:
    def convertToTitle(self, columnNumber: int) -> str:

        r = []

        while columnNumber > 0:

            columnNumber -= 1
            c = chr(ord('A') + columnNumber % 26)
            r.append(c)

            columnNumber //= 26

        return ''.join(reversed(r))
