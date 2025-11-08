class LRUCache:

    def __init__(self, capacity: int):
        # ordered dict is a linked list + hash table, so we can move things in O(1)
        self.cache = OrderedDict()
        self.capacity = capacity


    def get(self, key: int) -> int:
        if not key in self.cache:
            return -1

        # move to start - last accessed
        self.cache.move_to_end(key, last=False)
        return self.cache[key]


    def put(self, key: int, value: int) -> None:
        if len(self.cache) == self.capacity and not key in self.cache:
            self.cache.popitem()

        self.cache[key] = value
        # move to start - last accessed
        self.cache.move_to_end(key, last=False)



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)