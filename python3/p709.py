class Solution:
    def toLowerCase(self, s: str) -> str:
        # return s.lower()
        offset = ord('a') - ord('A')
        chars = []
        for c in s:
            if ord(c) >= ord('A') and ord(c) <= ord('Z'):
                chars.append(chr(ord(c) + offset))
            else:
                chars.append(c)
        return "".join(chars)