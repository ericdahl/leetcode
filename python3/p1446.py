class Solution:
    def maxPower(self, s: str) -> int:

        last_c = 0
        c_len = 1
        max_c_len = 0

        for c in s + ".": # add period to trigger logic at last char
            if c == last_c:
                c_len += 1
            else:
                max_c_len = max(max_c_len, c_len)
                c_len = 1

            last_c = c

        return max_c_len