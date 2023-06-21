class Solution:
    def reverseBits(self, n: int) -> int:

        n_binary = bin(n)[2:]
        n_binary_str_32 = str(n_binary).zfill(32)

        return int(n_binary_str_32[::-1], 2)