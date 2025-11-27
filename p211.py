class WordDictionary:

    def __init__(self):
        self.s = set()


    def addWord(self, word: str) -> None:
        self.s.add(word)

        for i in range(len(word)):
            self.s.add(word[:i] + '.' + word[i+1:])

        for i in range(0, len(word)):
            for j in range(i + 1, len(word)):
                self.s.add("".join(word[:i] + '.' + word[i+1:j] + '.' + word[j+1:]))


    def search(self, word: str) -> bool:
        return word in self.s



# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)