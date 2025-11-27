class WordDictionary:

    def __init__(self):
        self.s = set()


    def addWord(self, word: str) -> None:
        self.s.add(word)
        for i in range(0, len(word)):
            new = list(word)
            new[i] = "."
            self.s.add("".join(new))
            for j in range(i + 1, len(word)):
                new = list(word)
                new[i] = "."
                new[j] = "."
                self.s.add("".join(new))


    def search(self, word: str) -> bool:
        return word in self.s



# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)