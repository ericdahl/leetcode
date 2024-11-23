class Solution:
    def checkPerfectNumber(self, num: int) -> bool:

        if num == 1:
            return False


        s = 1
        max_num = num
        i = 2
        while i < max_num:
            if num % i == 0:
                s += i + num // i

            if s > num:
                return False
            max_num = num // i
            i += 1
        return s == num

