class Solution:

    def makeEqual(self, words: List[str]) -> bool:


        counts = Counter()
        for word in words:
            counts.update(word)

        for c in counts:
            if counts[c] % len(words) != 0:
                return False
        return True