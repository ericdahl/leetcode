class StockPrice:

    def __init__(self):
        self.d = {}
        self.current_time = -1
        self.max_time = -1
        self.min = 10**10
        self.max = -1

    def update(self, timestamp: int, price: int) -> None:
        self.max_time = max(self.max_time, timestamp)

        old_price = -2
        if timestamp in self.d:
            old_price = self.d[timestamp]
        self.d[timestamp] = price

        if old_price == self.min:
            self.min = min(self.d.values())
        else:
            self.min = min(self.min, price)

        if old_price == self.max:
            self.max = max(self.d.values())
        else:
            self.max = max(self.max, price)



    def current(self) -> int:
        return self.d[self.max_time]


    def maximum(self) -> int:
        return self.max

    def minimum(self) -> int:
        return self.min



# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()