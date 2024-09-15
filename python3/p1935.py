class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:

        count = 0
        broken = set(brokenLetters)
        for w in text.split(" "):
            if not set(w) & broken:
                count += 1
        return count