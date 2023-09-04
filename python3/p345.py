class Solution:
    def reverseVowels(self, s: str) -> str:

        vowels = [ c_i for c_i, c in enumerate(s) if c in "aeiouAEIOU"]

        s = list(s)
        while len(vowels) > 1:

            s[vowels[0]], s[vowels[-1]] = s[vowels[-1]], s[vowels[0]]

            vowels.pop(-1)
            vowels.pop(0)

        return "".join(s)
