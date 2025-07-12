class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        parts = []
        s = s.upper().replace("-", "")

        part = []
        for c in s[::-1]:
            if len(part) == k:
                parts.insert(0, "".join(part))
                part = []
            part.insert(0, c)
        parts.insert(0, "".join(part))

        return "-".join(parts)