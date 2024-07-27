class Solution:
    def sortSentence(self, s: str) -> str:
        result = [""] * 10

        for substr in s.split(" "):
            result[int(substr[-1])] = substr[:-1]

        return " ".join(result).strip()