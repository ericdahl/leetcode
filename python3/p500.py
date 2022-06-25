class Solution:
    def findWords(self, words: List[str]) -> List[str]:

        row_words = []
        row_sets = [
            set("qwertyuiop"),
            set("asdfghjkl"),
            set("zxcvbnm"),
        ]

        for word in words:

            word_set = set(word.lower())

            for row_set in row_sets:
                if word_set.issubset(row_set):
                    row_words.append(word)
                    break

        return row_words