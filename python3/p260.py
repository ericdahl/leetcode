class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:

        xor_all = 0
        for n in nums:
            xor_all ^= n

        rightmost_bit = 1
        while (xor_all & rightmost_bit) == 0:
            rightmost_bit = rightmost_bit << 1

        n1, n2 = 0, 0
        for n in nums:
            if n & rightmost_bit == 0:
                n1 ^= n
            else:
                n2 ^= n
        return [n1, n2]
        
