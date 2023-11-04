class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:

        s_l = list(s)
        s_l.sort(reverse=True)
        s_l[0] = "0"
        s_l.sort(reverse=True) # could be more efficient..
        s_l[-1] = "1"

        return "".join(s_l)