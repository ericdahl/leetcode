class MyHashMap:

    def __init__(self):
        self.buckets = [[] for _ in range(1000)]

    def _find_bucket_index(self, key) -> (int, int):
        b = self.buckets[key % 1000]

        for (i, (k, v)) in enumerate(b):
            if k == key:
                return (b, i)
        return (b, -1)



    def put(self, key: int, value: int) -> None:
        (b, bi) = self._find_bucket_index(key)
        if bi == -1:
            b.append((key, value))
        else:
            b[bi] = (key, value)


    def get(self, key: int) -> int:
        (b, bi) = self._find_bucket_index(key)

        if bi == -1:
            return -1
        return b[bi][1]



    def remove(self, key: int) -> None:
        (b, bi) = self._find_bucket_index(key)
        if bi != -1:
            b[bi] = (-1, -1)


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)