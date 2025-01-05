class Solution:
    def similarPairs(self, words: List[str]) -> int:

        similar_count = 0

        words = [set(w) for w in words]
        for i in range(len(words) - 1):
            for j in range(i + 1, len(words)):
                if words[i] == words[j]:
                    similar_count += 1

        return similar_count
