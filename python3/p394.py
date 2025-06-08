class Solution:
    def decodeString(self, s: str) -> str:

        while "]" in s:
            close_idx = s.index("]")
            open_idx = s[0:close_idx].rfind("[")

            mult_idx = open_idx - 1
            while mult_idx and s[mult_idx - 1] in "0123456789":
                mult_idx -= 1

            multiplier = int(s[mult_idx:open_idx])
            s = s[0:mult_idx] + multiplier * s[open_idx + 1:close_idx] + s[close_idx + 1:]

        return s