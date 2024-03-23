class OrderedStream:

    def __init__(self, n: int):
        self.l = [None] * n
        self.ptr = 0

    def insert(self, idKey: int, value: str) -> List[str]:
        self.l[idKey - 1] = value

        end_index = self.ptr
        while end_index < len(self.l) and self.l[end_index]:
            end_index += 1

        rtn = self.l[self.ptr:end_index]
        self.ptr = end_index
        return rtn



# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)
