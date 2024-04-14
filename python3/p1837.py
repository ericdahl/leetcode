class Solution:
    def sumBase(self, n: int, k: int) -> int:
        
        digit_sum = 0
        while n > 0:
            n, rem = divmod(n, k)
            digit_sum += rem

        return digit_sum
