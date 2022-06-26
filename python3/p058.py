class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = [ w for w in s.split(" ") if w != ""]
        return len(words[-1])