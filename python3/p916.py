class Solution:


    @staticmethod
    def count_characters(word: str) -> dict[str, int]:
        char_count = collections.defaultdict(int)
        for c in word:
            char_count[c] += 1
        return char_count


    @staticmethod
    def is_universal(word: str, word_char_counts: dict[str, int], words2_char_counts: dict[str, dict[str, int]]) -> bool:
        # print("is_universal")

        for words2_char_counts in words2_char_counts:
            for ch, ch_count in words2_char_counts.items():
                if word_char_counts[ch] < ch_count:
                    # print("returning false")
                    # print(f"ch: {ch}")
                    return False
        return True


    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        universal = []

        words1_char_counts = {w : Solution.count_characters(w) for w in words1}
        words2_char_counts = [Solution.count_characters(w) for w in words2]

        # print(words1_char_counts)
        # print()
        # print(words2_char_counts)


        for word, char_counts in words1_char_counts.items():

            if Solution.is_universal(word, char_counts, words2_char_counts):
                universal.append(word)

        #         # list of dict with
        #         #   k : character for subword
        #         #   v : number of occurrences of char k in subword
        #         subword_dicts = []
        #         for subword in words2:
        #             subword_dict = collections.defaultdict(int)
        #             for c in subword:
        #                 subword_dict[c] += 1
        #             subword_dicts.append(subword_dict)


        #         for word in words1:
        #             if Solution.is_universal(word, subword_dicts):
        #                 universal.append(word)

        return universal

            