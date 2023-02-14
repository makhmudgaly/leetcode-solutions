class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.discount = discount
        self.n = n
        self.customer = 0
        self.d = {}
        for idx in range(len(products)):
            self.d[products[idx]] = prices[idx]

    def getBill(self, product: List[int], amount: List[int]) -> float:
        self.customer += 1
        total = 0
        less = (100 - (self.discount if self.customer % self.n == 0 else 0) ) / 100
        for idx, prod in enumerate(product):
            total += (self.d[prod] * amount[idx]) * less
            
        return total

# Your Cashier object will be instantiated and called as such:
# obj = Cashier(n, discount, products, prices)
# param_1 = obj.getBill(product,amount)