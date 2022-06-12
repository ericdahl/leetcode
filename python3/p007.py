class Solution:
    def reverse(self, x: int) -> int:
        is_negative = (x < 0)

        abs_x = abs(x)
        reverse_x = int(str(abs_x)[::-1])
        if is_negative:
            reverse_x *= -1

        if reverse_x < -2**31 or reverse_x > 2**31 -1:
            return 0

        return reverse_x