class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:

        word_len = len(words[0])
        total_len = word_len * len(words)
        if total_len > len(s):
            return []

        results = set()

        for w in words:
            if w not in s:
                return []

        word_count = Counter(words)
        for i in range(len(s) - total_len + 1):
            seen = []
            for j in range(i, i + total_len, word_len):
                word = s[j:j+word_len]
                seen.append(word)
            if Counter(seen) == word_count:
                results.add(i)

        return list(results)
