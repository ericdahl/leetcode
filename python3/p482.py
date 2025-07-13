class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        parts = []
        s = s.upper().replace("-", "")

        st = len(s) % k

        if st > 0:
            parts.append(s[0:st])
        s = s[st:]
        for i in range(0, len(s), k):
            parts.append(s[i:i+k])

        return "-".join(parts)