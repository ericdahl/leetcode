class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.N = n
        self.DISCOUNT = discount
        self.num_customers = 0

        # could use an array given the ID range is small but dict is more natural
        self.product_prices = {}
        for (product_id, price) in zip(products, prices):
            self.product_prices[product_id] = price


    def getBill(self, product: List[int], amount: List[int]) -> float:
        self.num_customers += 1

        bill = 0
        for (product_id, quantity) in zip(product, amount):
            bill += self.product_prices[product_id] * quantity

        discount = 0
        if self.num_customers % self.N == 0:
            discount = self.DISCOUNT
        return bill * (1 - discount / 100)


# Your Cashier object will be instantiated and called as such:
# obj = Cashier(n, discount, products, prices)
# param_1 = obj.getBill(product,amount)
