class StockPrice:

    def __init__(self):
        self.d = {}
        self.max_time = -1
        self.min_heap = [] # (price, timestamp)
        self.max_heap = [] # (-price, timestamp)

    def update(self, timestamp: int, price: int) -> None:
        self.max_time = max(self.max_time, timestamp)
        self.d[timestamp] = price

        heapq.heappush(self.min_heap, (price, timestamp))
        heapq.heappush(self.max_heap, (-price, timestamp))

    def current(self) -> int:
        return self.d[self.max_time]

    def maximum(self) -> int:
        while self.max_heap:
            price, ts = self.max_heap[0]
            if -price == self.d[ts]: # check if this price is still valid for the time
                return -price
            heapq.heappop(self.max_heap)

    def minimum(self) -> int:
        while self.min_heap:
            price, ts = self.min_heap[0]
            if price == self.d[ts]: # check if this price is still valid for the time
                return price
            heapq.heappop(self.min_heap)



# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()