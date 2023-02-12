class Solution:
        longest = 0
        start = 0
        end = 0

        for i, c in enumerate(s):
            sublist = s[start:end]

            if c in sublist:
                start += sublist.index(c) + 1

            end += 1

            if (end - start) > longest:
                longest = end - start

        return longest

