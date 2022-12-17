class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_alphanumeric = [ c.lower() for c in s if c.isalpha() or c.isnumeric() ]
        return s_alphanumeric == s_alphanumeric[::-1]