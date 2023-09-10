class Trie:

    def __init__(self):
        self.root = {}


    def insert(self, word: str) -> None:
        current_dict = self.root
        for c in word:
            # get current_dict[c] and if not present, insert new dict and return it
            current_dict = current_dict.setdefault(c, {})

        # "." means end-of-word
        current_dict["."] = "."


    def search(self, word: str) -> bool:
        return self.startsWith(word + ".")

    def startsWith(self, prefix: str) -> bool:
        d = self.root
        for c in prefix:
            if c not in d:
                return False
            d = d[c]

        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)