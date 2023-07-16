class Solution:
    def numDifferentIntegers(self, word: str) -> int:

        s = set()

        for t in [t for t in re.split('[^0-9]', word) if t != '']:
            s.add(int(t))

        return len(s)
