class Solution:

    @staticmethod
    def is_palindrome(s: str) -> str:
        return s == s[::-1]

    def shortestPalindrome(self, s: str) -> str:

        if self.is_palindrome(s): return s

        # start at end of string, creating reversed substrings then prepending
        # and checking, looping until entire string is prepended
        #
        # input: abcd
        #  iteration 1: dabcd (not palindrome)
        #  iteration 2: dcabcd (not palindrome)
        #  iteration 3: dcbabcd (not palindrome)
        #  iteration 4: dcbaabcd (palindrome - return)
        for i in range(1, len(s) + 1):
            new_s = s[-i:][::-1] + s
            if self.is_palindrome(new_s): return new_s