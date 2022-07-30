from collections import Counter

class Solution:

    @staticmethod
    def is_universal(word_char_counts: Counter, words2_char_counts: Counter) -> bool:
        for ch, ch_count in words2_char_counts.items():
            if word_char_counts[ch] < ch_count:
                return False
        return True


    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:

        words2_char_counts = Counter()

        for word2 in words2:
            for ch, count in Counter(word2).items():
                words2_char_counts[ch] = max(words2_char_counts[ch], count)

        return [w for w in words1 if Solution.is_universal(Counter(w), words2_char_counts)]
