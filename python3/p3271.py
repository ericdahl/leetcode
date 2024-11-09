class Solution:
    def stringHash(self, s: str, k: int) -> str:

        subs = []
        for i in range(0, len(s), k):
            subs += [s[i:i+k]]

        result = ""

        for sub in subs:
            s = sum([ord(c) - ord('a') for c in sub])
            hashedChar = s % 26
            result += chr(ord('a') + hashedChar)

        return result