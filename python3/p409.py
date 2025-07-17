class Solution:
    def longestPalindrome(self, s: str) -> int:
        counts = Counter(s)
        if len(counts) == 1:
            return len(s)

        max_len = len(s)
        has_single_letter = False
        for c, c_count in counts.items():

            if c_count %2 == 1:
                if has_single_letter:
                    max_len -= 1
                has_single_letter = True

        return max_len
