class RandomizedCollection:

    def __init__(self):
        self.d = defaultdict(set)
        self.a = []

    def insert(self, val: int) -> bool:
        already_present = val in self.d and len(self.d[val]) > 0
        self.d[val].add(len(self.a))
        self.a.append(val)
        return not already_present

    def remove(self, val: int) -> bool:
        if val not in self.d or len(self.d[val]) == 0:
            return False

        freed_index = self.d[val].pop()
        last_val_old_index = len(self.a) - 1
        last_val = self.a[last_val_old_index]

        if freed_index != last_val_old_index:
            self.a[freed_index] = last_val
            self.d[last_val].remove(last_val_old_index)
            self.d[last_val].add(freed_index)

        del self.a[last_val_old_index]

        return True


    def getRandom(self) -> int:
        random_slot = randint(0, len(self.a) - 1)
        return self.a[random_slot]



# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()