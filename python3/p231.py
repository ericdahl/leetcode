class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        s = str(bin(n))[2:]
        return s[0] == "1" and "1" not in s[1:]