class StockSpanner:

    def __init__(self):
        # slow but apparently fast enough
        self.prices = []

    def next(self, price: int) -> int:
        self.prices.insert(0, price)

        i = 0
        for p in self.prices:
            if p <= price:
                i += 1
            else:
                break
        return i


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)