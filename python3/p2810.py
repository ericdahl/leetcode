class Solution:
    def finalString(self, s: str) -> str:

        a = []
        for c in s:
            if c == "i":
                a.reverse()
            else:
                a.append(c)

        return "".join(a)
