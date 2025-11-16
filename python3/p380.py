class RandomizedSet:

    def __init__(self):
        self.d = {} # dict of values -> position in array
        self.a = [] # array of values

    def insert(self, val: int) -> bool:
        if val in self.d:
            return False
        self.a.append(val)
        self.d[val] = len(self.a) - 1 # index of val
        return True


    def remove(self, val: int) -> bool:
        if not val in self.d:
            return False

        idx_of_val = self.d[val]
        last_element = self.a[-1]

        self.a[idx_of_val] = last_element
        self.d[last_element] = idx_of_val

        self.a.pop()
        del self.d[val]

        return True


    def getRandom(self) -> int:
        return self.a[random.randint(0, len(self.a) - 1)]



# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()