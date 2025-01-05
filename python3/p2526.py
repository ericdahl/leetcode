class DataStream:

    def __init__(self, value: int, k: int):
        self.k = k
        self.value = value
        # number of most recent values that have been equal to self.value
        self.last = 0

    def consec(self, num: int) -> bool:

        if num == self.value:
            self.last += 1
        else:
            self.last = 0

        return self.last >= self.k



# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)