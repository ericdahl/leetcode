class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        
        word += '0' # add final character < "a" to evaluate logic at last iteration
        start = 0
        max_len = 0
        max_start = 0
        s = set(word[0])
        for i in range(1, len(word)):
            if word[i] < word[i - 1]:
                if i - start >= max_len and len(s) == 5:
                    max_len = i - start
                    max_start = start
                start = i
                s = set(word[i])
            s.add(word[i])

        return max_len
