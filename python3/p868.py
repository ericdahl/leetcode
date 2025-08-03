class Solution:
    def binaryGap(self, n: int) -> int:

        max_len = 0
        curr_len = -1
        for b in str(bin(n))[2:]:
            if curr_len == -1:
                if b == '1':
                    curr_len = 0
            else:
                if b == '0':
                    curr_len += 1
                else:
                    max_len = max(max_len, curr_len + 1)
                    curr_len = 0
        return max_len