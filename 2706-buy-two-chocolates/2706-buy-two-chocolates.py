class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices = sorted(prices)
        cost = prices[0] + prices[1]
        return money - cost if money >= cost else money