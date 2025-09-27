class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        rs = [c for c in s if c.isalpha()]
        rs.reverse()
        result = []
        for i in range(len(s)):
            if not s[i].isalpha():
                result.append(s[i])
            else:
                result.append(rs.pop(0))
        return "".join(result)
