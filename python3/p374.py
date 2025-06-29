# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:

        min_n = 1
        max_n = n

        result = None
        while True:
            guess_n = min_n + (max_n - min_n) // 2
            result = guess(guess_n)
            if result == 0:
                return guess_n
            if result == -1:
                if max_n == min_n + 1:
                    return max_n
                max_n = guess_n
            elif result == 1:
                if max_n == min_n + 1:
                    return max_n
                min_n = guess_n