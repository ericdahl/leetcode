class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:


        t = list(t)

        for c in s:

            if not t:
                return False

            while t and c != t[0]:
                t.pop(0)

                if not t:
                    return False

            if c == t[0]:
                t.pop(0)

        return True