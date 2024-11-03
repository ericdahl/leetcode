class Solution:
    def kthCharacter(self, k: int) -> str:
        word = [0]
        while len(word) < k:
            word += [(d + 1) % 26 for d in word]

        return chr(97 + word[k - 1])