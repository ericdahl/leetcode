class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        start = 0
        end = 0

        for i in range(len(s)):
            sublist = s[start:end]

            if s[i] in sublist:
                start += sublist.index(s[i]) + 1

            end += 1

            if (end - start) > longest:
                longest = end - start

        return longest