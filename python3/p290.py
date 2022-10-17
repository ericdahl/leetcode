class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        if len(pattern) != len(s.split(" ")):
            return False

        map_char_to_word = {}
        map_word_to_char = {}

        for c, w in zip(pattern, s.split(' ')):

            if c in map_char_to_word and map_char_to_word[c] != w:
                return False

            if w in map_word_to_char and map_word_to_char[w] != c:
                return False

            map_char_to_word[c] = w
            map_word_to_char[w] = c

        return True
