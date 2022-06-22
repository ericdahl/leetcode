class Solution:
    def isHappy(self, n: int) -> bool:

        seen = {}

        while n not in seen:
            seen[n] = True
            n = sum([int(i) * int(i) for i in str(n)])
            if n == 1:
                return True

        return False