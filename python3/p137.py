class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        # sum a count of # of bits for each number
        bit_count = [0] * 32
        for n in nums:
            bits = bin(n)
            bits = [int(b) for b in bits[bits.find('b') + 1:].zfill(32)]

            for b_idx, b in enumerate(bits):
                bit_count[b_idx] += b

        for i, count in enumerate(bit_count):
            bit_count[i] = count % 3

        r = int("".join([str(b) for b in bit_count]), 2)
        
        if nums.count(-1 * r) == 1:
            return -1 * r
        return r

