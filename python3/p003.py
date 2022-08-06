class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        start = 0
        end = 1
        longest = 0

        while end <= len(s):

            current_len = end - start
            sub = set(s[start:end])

            if len(sub) != current_len:
                start += 1
                end = start
                continue

            if current_len > longest:
                longest = current_len

            end += 1

        return longest