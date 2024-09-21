class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:

        len_part = len(part)
        start = s.find(part)
        while start != -1:
            s = s[0:start] + s[start + len_part:]
            start = s.find(part)

        return s