class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:

        num_lines = 1
        pixels = 0

        s_list = [ ord(c) - ord('a') for c in s ]
        while s_list:
            c = s_list.pop(0)

            if pixels + widths[c] > 100:
                num_lines += 1
                pixels = widths[c]
            else:
                pixels += widths[c]

        return [num_lines, pixels]

